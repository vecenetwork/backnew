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
    """Fallback: strictly match tags from our DB that appear in question/options."""
    combined = f"{question_text} {' '.join(options or [])}".lower()
    # Extract words with length >= 3 to avoid matching 'is', 'in', 'at'
    words = set(re.findall(r"\b[a-z0-9]{3,}\b", combined))
    
    if not words:
        return []

    matched = []
    seen = set()
    
    for name in all_names:
        name_lower = name.lower()
        
        # 1. Check if the full tag name appears as a substring in the text
        # e.g. "World Cup" tag in "will argentina win the world cup"
        if name_lower in combined:
            if name not in seen:
                seen.add(name)
                matched.append(name)
            continue
            
        # 2. Check if any significant word from the text matches the tag exactly
        # e.g. "Sports" tag matches "sports" word
        if name_lower in words:
             if name not in seen:
                seen.add(name)
                matched.append(name)

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
            logger.info("[hashtag] GOOGLE_API_KEY not set, using keyword fallback")
            return _keyword_fallback(question_text, options or [], all_names, min(max_hashtags, 7))

        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=GOOGLE_API_KEY)
            options_str = "\n".join(f"- {o}" for o in (options or [])) if options else "(no options)"
            tag_list = "\n".join(all_names)

            prompt = f"""You are a classification assistant.
Your task is to label the user's input (Question + Options) with 1 to 7 tags from the provided "Allowed Tags" list.

Input:
Question: "{question_text}"
Options: {options_str}

Allowed Tags:
{tag_list}

Instructions:
1. **Analyze Meaning:** Understand the core topic of the question. It might be in **English, Spanish, or any other language**.
2. **Cross-Language Matching:** If the text is in Spanish (or another language), understand the *meaning* and find the corresponding *English* tags in the list.
   - *Example:* "Quién ganará el mundial?" -> match with "Football", "Sports".
3. **Select Tags:** Pick the most relevant tags from the "Allowed Tags" list.
   - Prioritize specific tags over broad ones, but include both if relevant.
   - If exact keywords don't match, use semantic relevance.
4. **Constraints:**
   - Return ONLY a JSON array of strings (e.g. ["Tag1", "Tag2"]).
   - Use **EXACT** names from the list. Do not invent new tags.
"""

            logger.info("[hashtag] Calling Gemini: question=%r, options_count=%d, tags_count=%d",
                        question_text[:80], len(options or []), len(all_names))

            config = types.GenerateContentConfig(
                temperature=0.1,
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

            raw_text = response.text if response else None
            logger.info("[hashtag] Gemini raw response: %r", raw_text[:200] if raw_text else None)

            if response and raw_text:
                suggested = _parse_names_from_response(raw_text)
                result = _filter_to_our_tags(suggested, name_to_canonical)
                logger.info("[hashtag] Gemini suggested=%s, filtered=%s", suggested[:10], result)
                if result:
                    return result
                logger.info("[hashtag] None of Gemini's tags matched our DB")

        except Exception as e:
            logger.warning("[hashtag] Gemini failed: %s", e, exc_info=True)

        return _keyword_fallback(question_text, options or [], all_names, min(max_hashtags, 7))


def build_hashtag_suggestion_service(hashtag_repo: "HashtagRepository") -> HashtagSuggestionService:
    return HashtagSuggestionService(hashtag_repo)
