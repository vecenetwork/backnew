"""Hashtag suggestion: Gemini picks 1-7 tags from our DB list. No fallback."""

import json
import logging
import os
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infrastructure.repository.hashtag import HashtagRepository

logger = logging.getLogger(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# Best model: 2.5 Flash (price-performance). Fallback to 1.5 Flash if 404.
MODELS = ["gemini-2.5-flash", "gemini-1.5-flash"]


def _parse_names_from_response(text: str) -> list[str]:
    """Extract tag names from Gemini response."""
    text = text.strip()
    try:
        json_match = re.search(r"\[[\s\S]*?\]", text)
        if json_match:
            arr = json.loads(json_match.group())
            return [str(x).strip().strip('"') for x in arr if x]
    except json.JSONDecodeError:
        pass
    parts = re.split(r"[,;\n]+", text)
    return [p.strip().strip('"') for p in parts if p.strip()]


def _filter_to_our_tags(suggested: list[str], name_to_canonical: dict[str, str]) -> list[str]:
    """Keep only tags that exist in our DB, return in canonical form."""
    result: list[str] = []
    seen: set[str] = set()
    for s in suggested:
        key = s.strip().lstrip("#").strip('"')
        if not key:
            continue
        canonical = name_to_canonical.get(key.lower())
        if canonical and canonical not in seen:
            seen.add(canonical)
            result.append(canonical)
        if len(result) >= 7:
            break
    return result[:7]


class HashtagSuggestionService:
    """Gemini picks 1-7 tags from our DB. Returns exact names for question creation."""

    def __init__(self, hashtag_repo: "HashtagRepository"):
        self.hashtag_repo = hashtag_repo
        self._all_names_cache: list[str] | None = None
        self._name_to_canonical: dict[str, str] | None = None

    async def _get_all_hashtag_names(self) -> tuple[list[str], dict[str, str]]:
        if self._all_names_cache is not None:
            return self._all_names_cache, self._name_to_canonical or {}

        names = await self.hashtag_repo.get_all_names()
        self._all_names_cache = names
        self._name_to_canonical = {n.lower(): n for n in names}
        return names, self._name_to_canonical

    async def suggest(
        self,
        question_text: str,
        options: list[str],
        max_hashtags: int = 7,
    ) -> list[str]:
        """
        Send question + options to Gemini with full tag list. Gemini returns 1-7
        exact tag names from our DB. Backend returns them as-is for question creation.
        """
        question_text = (question_text or "").strip()
        if not question_text:
            return []

        all_names, name_to_canonical = await self._get_all_hashtag_names()
        if not all_names:
            return []

        if not GOOGLE_API_KEY:
            logger.warning("[hashtag] GOOGLE_API_KEY not set")
            return []

        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=GOOGLE_API_KEY)
            options_str = "\n".join(f"- {o}" for o in (options or [])) if options else "(no options)"
            tag_list = "\n".join(all_names)

            prompt = f"""You are a tag classifier. You know ALL our tags. Pick 1-7 most relevant for the content.

Question: "{question_text}"
Options:
{options_str}

Our tags (use EXACT names only):
{tag_list}

Return a JSON array of tag names, e.g. ["Football", "Sports"]. Use only names from the list above."""

            config = types.GenerateContentConfig(
                temperature=0.1,
                response_mime_type="application/json",
                response_schema=types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(type=types.Type.STRING),
                    min_items=0,
                    max_items=min(max_hashtags, 7),
                ),
            )

            last_error: Exception | None = None
            for model in MODELS:
                try:
                    response = client.models.generate_content(
                        model=model,
                        contents=prompt,
                        config=config,
                    )
                    raw_text = response.text if response else None
                    if response and raw_text:
                        suggested = _parse_names_from_response(raw_text)
                        result = _filter_to_our_tags(suggested, name_to_canonical)
                        if result:
                            return result
                except Exception as e:
                    last_error = e
                    err_str = str(e)
                    if "404" in err_str or "NOT_FOUND" in err_str:
                        logger.info("[hashtag] Model %s not available, trying next", model)
                        continue
                    raise

            if last_error:
                raise last_error

        except Exception as e:
            logger.warning("[hashtag] Gemini failed: %s", e)

        return []


def build_hashtag_suggestion_service(hashtag_repo: "HashtagRepository") -> HashtagSuggestionService:
    return HashtagSuggestionService(hashtag_repo)
