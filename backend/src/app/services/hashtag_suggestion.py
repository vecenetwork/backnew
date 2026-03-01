"""Hashtag suggestion service using Google Gemini AI (new google-genai SDK)."""

import json
import logging
import os
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infrastructure.repository.hashtag import HashtagRepository

logger = logging.getLogger(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

SYSTEM_INSTRUCTION = """You are a hashtag selector. Your ONLY task: choose 1 to 7 tag NUMBERS from the numbered list provided.
Rules:
- Return ONLY a JSON array of integers (the numbers, not names). Example: [1, 5, 12]
- Never invent numbers. Use only numbers from the list.
- Pick the most relevant tags for the question and answer options."""


def _parse_indices_from_response(text: str) -> list[int]:
    """Extract list of indices from Gemini response. Expects JSON array of integers."""
    text = text.strip()
    try:
        json_match = re.search(r"\[[\s\S]*?\]", text)
        if json_match:
            arr = json.loads(json_match.group())
            return [int(x) for x in arr if isinstance(x, (int, float)) and x == int(x)]
    except (json.JSONDecodeError, ValueError, TypeError):
        pass
    return []


class HashtagSuggestionService:
    """Suggests relevant hashtags for a question using Gemini."""

    def __init__(self, hashtag_repo: "HashtagRepository"):
        self.hashtag_repo = hashtag_repo
        self._all_names_cache: list[str] | None = None
        self._name_to_canonical: dict[str, str] | None = None

    async def _get_all_hashtag_names(self) -> tuple[list[str], dict[str, str]]:
        """Get all hashtag names and a case-insensitive lookup map."""
        if self._all_names_cache is not None:
            return self._all_names_cache, self._name_to_canonical or {}

        names = await self.hashtag_repo.get_all_names()
        self._all_names_cache = names
        self._name_to_canonical = {n.lower(): n for n in names}
        return names, self._name_to_canonical

    def _keyword_fallback(
        self, question_text: str, options: list[str], all_names: list[str], max_hashtags: int = 7
    ) -> list[str]:
        """Fallback: match hashtags whose names appear in question/options, or vice versa."""
        combined = f"{question_text} {' '.join(options or [])}".lower()
        words = re.findall(r"[a-z0-9]+", combined)
        words = [w for w in words if len(w) >= 3]
        if not combined.strip():
            return []
        matched = []
        seen = set()
        for name in all_names:
            name_lower = name.lower()
            if name_lower in combined:
                if name not in seen:
                    seen.add(name)
                    matched.append(name)
            else:
                for w in words:
                    if w in name_lower or name_lower in w:
                        if name not in seen:
                            seen.add(name)
                            matched.append(name)
                        break
            if len(matched) >= max_hashtags:
                break
        return matched[:max_hashtags]

    async def suggest(
        self,
        question_text: str,
        options: list[str],
        max_hashtags: int = 7,
    ) -> list[str]:
        """
        Suggest 1-7 relevant hashtags from the DB for the given question and options.
        Uses Gemini when available; falls back to keyword matching otherwise.
        """
        question_text = (question_text or "").strip()
        if not question_text:
            return []

        all_names, name_to_canonical = await self._get_all_hashtag_names()
        if not all_names:
            return []

        result: list[str] = []

        if GOOGLE_API_KEY:
            try:
                from google import genai
                from google.genai import types

                client = genai.Client(api_key=GOOGLE_API_KEY)
                # Numbered list: model returns indices, we map to names (reliable)
                tag_limit = min(800, len(all_names))  # Keep prompt manageable
                numbered_list = "\n".join(f"{i}. {name}" for i, name in enumerate(all_names[:tag_limit], 1))

                options_str = "\n".join(f"- {o}" for o in (options or [])[:20]) if options else "(none)"

                prompt = f"""TAGS (choose 1-7 by number):
{numbered_list}

QUESTION:
{question_text}

ANSWER OPTIONS:
{options_str}

Return JSON array of numbers. Example: [1, 5, 12]"""

                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.2,
                    ),
                )
                if response and response.text:
                    indices = _parse_indices_from_response(response.text)
                    for idx in indices:
                        if 1 <= idx <= len(all_names):
                            name = all_names[idx - 1]
                            if name not in result:
                                result.append(name)
                        if len(result) >= 7:
                            break
                    result = result[:7]
            except Exception as e:
                logger.warning("Hashtag suggestion (Gemini) failed: %s", e)

        # Keyword fallback when Gemini returns empty or is not configured
        if not result:
            result = self._keyword_fallback(
                question_text, options or [], all_names, min(max_hashtags, 7)
            )

        return result


def build_hashtag_suggestion_service(hashtag_repo: "HashtagRepository") -> HashtagSuggestionService:
    return HashtagSuggestionService(hashtag_repo)
