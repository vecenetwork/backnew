"""Hashtag suggestion service using Google Gemini AI."""

import json
import logging
import os
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infrastructure.repository.hashtag import HashtagRepository

logger = logging.getLogger(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def _parse_hashtag_list_from_response(text: str) -> list[str]:
    """Extract hashtag names from Gemini response. Handles JSON, comma-separated, or line-separated."""
    text = text.strip()
    # Try JSON array first
    try:
        # Find JSON array in response (model might wrap in markdown)
        json_match = re.search(r"\[[\s\S]*?\]", text)
        if json_match:
            arr = json.loads(json_match.group())
            return [str(x).strip() for x in arr if x]
    except json.JSONDecodeError:
        pass

    # Fallback: split by comma or newline
    parts = re.split(r"[,;\n]+", text)
    return [p.strip() for p in parts if p.strip()]


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

    def _validate_and_filter(self, suggested: list[str], name_to_canonical: dict[str, str]) -> list[str]:
        """Return only hashtags that exist in DB, preserving order, deduplicated."""
        seen: set[str] = set()
        result: list[str] = []
        for s in suggested:
            key = s.strip()
            if not key:
                continue
            # Normalize: remove # if present, try case-insensitive match
            key_clean = key.lstrip("#")
            canonical = name_to_canonical.get(key_clean.lower())
            if canonical and canonical not in seen:
                seen.add(canonical)
                result.append(canonical)
        return result[:7]  # Cap at 7

    async def suggest(
        self,
        question_text: str,
        options: list[str],
        max_hashtags: int = 7,
    ) -> list[str]:
        """
        Suggest 1-7 relevant hashtags from the DB for the given question and options.
        Returns only hashtags that exist in the database.
        """
        if not GOOGLE_API_KEY:
            logger.warning("GOOGLE_API_KEY not set; hashtag suggestion disabled")
            return []

        question_text = (question_text or "").strip()
        if not question_text:
            return []

        all_names, name_to_canonical = await self._get_all_hashtag_names()
        if not all_names:
            return []

        try:
            import google.generativeai as genai

            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel("gemini-1.5-flash")

            options_str = "\n".join(f"- {o}" for o in (options or [])[:20]) if options else "(none)"
            hashtag_list_str = ", ".join(all_names[:1500])  # Limit token size

            prompt = f"""You are a hashtag selector for a social polling app. The user is writing a question with answer options.

Question: {question_text}

Answer options:
{options_str}

Available hashtags (you MUST pick ONLY from this exact list, use exact names):
{hashtag_list_str}

Task: Select 1 to {min(max_hashtags, 7)} most relevant hashtags from the list above. Avoid irrelevant ones.
Return a JSON array of hashtag names only, e.g. ["Music", "Art"]. No explanations."""

            response = model.generate_content(prompt)
            if not response or not response.text:
                return []

            suggested = _parse_hashtag_list_from_response(response.text)
            return self._validate_and_filter(suggested, name_to_canonical)

        except Exception as e:
            logger.exception("Hashtag suggestion failed: %s", e)
            return []


def build_hashtag_suggestion_service(hashtag_repo: "HashtagRepository") -> HashtagSuggestionService:
    return HashtagSuggestionService(hashtag_repo)
