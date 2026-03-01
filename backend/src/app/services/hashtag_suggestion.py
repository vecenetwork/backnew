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

    def _validate_and_filter(
        self, suggested: list[str], name_to_canonical: dict[str, str], all_names: list[str]
    ) -> list[str]:
        """Return only hashtags that exist in DB. Exact match first, then fuzzy (e.g. Sport→Sports)."""
        seen: set[str] = set()
        result: list[str] = []

        for s in suggested:
            key = s.strip().lstrip("#")
            if not key:
                continue
            key_lower = key.lower()
            canonical = name_to_canonical.get(key_lower)
            if not canonical and len(key_lower) >= 3:
                # Fuzzy: "Sport" → "Sports" when model returns slight variant (prefix match only)
                canonical = next(
                    (
                        n
                        for n in all_names
                        if n.lower().startswith(key_lower) or key_lower.startswith(n.lower())
                    ),
                    None,
                )
            if canonical and canonical not in seen:
                seen.add(canonical)
                result.append(canonical)
            if len(result) >= 7:
                break
        return result[:7]

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
                import google.generativeai as genai

                genai.configure(api_key=GOOGLE_API_KEY)
                model = genai.GenerativeModel("gemini-1.5-flash")

                options_str = "\n".join(f"- {o}" for o in (options or [])[:20]) if options else "(none)"
                hashtag_list_str = ", ".join(all_names[:1500])  # Limit token size

                prompt = f"""You are a hashtag selector. Choose 1 to 7 hashtags from our list. Do NOT invent tags.

OUR HASHTAG LIST (choose ONLY from here, copy names exactly):
{hashtag_list_str}

QUESTION:
{question_text}

ANSWER OPTIONS:
{options_str}

RULES:
1. Read the question and answer options.
2. Select 1 to 7 most relevant hashtags from OUR HASHTAG LIST above.
3. Use EXACT names from the list (e.g. "Sports" not "Sport").
4. Return ONLY a JSON array. Example: ["Sports", "Entertainment"]"""

                response = model.generate_content(prompt)
                if response and response.text:
                    suggested = _parse_hashtag_list_from_response(response.text)
                    result = self._validate_and_filter(suggested, name_to_canonical, all_names)
            except Exception as e:
                logger.warning("Hashtag suggestion (Gemini) failed: %s", e)

        # Keyword fallback only when Gemini is not configured
        if not result and not GOOGLE_API_KEY:
            result = self._keyword_fallback(
                question_text, options or [], all_names, min(max_hashtags, 7)
            )

        return result


def build_hashtag_suggestion_service(hashtag_repo: "HashtagRepository") -> HashtagSuggestionService:
    return HashtagSuggestionService(hashtag_repo)
