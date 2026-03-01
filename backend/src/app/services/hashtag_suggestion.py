"""Hashtag suggestion: send question+options to Gemini, it picks from our tags only."""

import json
import logging
import os
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infrastructure.repository.hashtag import HashtagRepository

logger = logging.getLogger(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = "gemini-1.5-flash"


def _parse_names_from_response(text: str) -> list[str]:
    """Extract tag names from response."""
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
    """Keep only tags that exist in our DB."""
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


def _keyword_fallback(
    question_text: str, options: list[str], all_names: list[str], max_hashtags: int = 7
) -> list[str]:
    """Fallback: match tags from our DB that appear in question/options. Only our tags, no inventing."""
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


class HashtagSuggestionService:
    """Sends question+options to Gemini; it picks 1-7 tags from our list. Backend does not invent."""

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
        Send full context (question + options) to Gemini. It picks 1-7 tags from our DB.
        Backend returns only what Gemini returns; no fallback, no inventing.
        """
        question_text = (question_text or "").strip()
        if not question_text:
            return []

        all_names, name_to_canonical = await self._get_all_hashtag_names()
        if not all_names:
            return []

        if not GOOGLE_API_KEY:
            logger.info("Hashtag suggest: GOOGLE_API_KEY not set")
            return _keyword_fallback(question_text, options or [], all_names, min(max_hashtags, 7))

        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=GOOGLE_API_KEY)

            options_str = "\n".join(f"- {o}" for o in (options or [])) if options else "(no options)"
            tag_list = "\n".join(all_names)

            prompt = f"""QUESTION: {question_text}

ANSWER OPTIONS:
{options_str}

Pick 1-7 tags from the list below that best describe what this question is about. Use ONLY tags from the list. Copy names exactly.

AVAILABLE TAGS (our database — pick only from here):
{tag_list}

Return a JSON array of tag names."""

            config = types.GenerateContentConfig(
                temperature=0,
                response_mime_type="application/json",
                response_schema=types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(type=types.Type.STRING),
                    min_items=0,
                    max_items=7,
                ),
            )

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=config,
            )

            if response and response.text:
                suggested = _parse_names_from_response(response.text)
                result = _filter_to_our_tags(suggested, name_to_canonical)
                if result:
                    return result
                logger.info("Hashtag suggest: Gemini returned %s, none matched our DB", suggested[:10])

        except Exception as e:
            logger.warning("Hashtag suggestion (Gemini) failed: %s", e)

        return _keyword_fallback(question_text, options or [], all_names, min(max_hashtags, 7))


def build_hashtag_suggestion_service(hashtag_repo: "HashtagRepository") -> HashtagSuggestionService:
    return HashtagSuggestionService(hashtag_repo)
