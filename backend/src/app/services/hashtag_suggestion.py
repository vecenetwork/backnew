"""Hashtag suggestion service using Google Gemini AI (new google-genai SDK)."""

import hashlib
import json
import logging
import os
import re
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from infrastructure.repository.hashtag import HashtagRepository

logger = logging.getLogger(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = "gemini-1.5-flash"
CACHE_TTL = "86400s"  # 24 hours

SYSTEM_INSTRUCTION = """You are a hashtag selector. Choose 1 to 7 tags from the list provided.
Rules: Return ONLY a JSON array of tag names. Copy names EXACTLY as written in the list. Do not invent or modify names.
Example: ["Sports", "Music"]"""


def _parse_names_from_response(text: str) -> list[str]:
    """Extract tag names from Gemini response. Handles JSON array, comma-separated, or line-separated."""
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


def _validate_and_map_to_canonical(
    suggested: list[str], name_to_canonical: dict[str, str], all_names: list[str]
) -> list[str]:
    """Map suggested names to canonical DB names. Exact match first, then fuzzy (Sport→Sports)."""
    result: list[str] = []
    seen: set[str] = set()
    for s in suggested:
        key = s.strip().lstrip("#").strip('"')
        if not key:
            continue
        key_lower = key.lower()
        canonical = name_to_canonical.get(key_lower)
        if not canonical and len(key_lower) >= 3:
            canonical = next(
                (n for n in all_names if n.lower().startswith(key_lower) or key_lower.startswith(n.lower())),
                None,
            )
        if canonical and canonical not in seen:
            seen.add(canonical)
            result.append(canonical)
        if len(result) >= 7:
            break
    return result[:7]


class HashtagSuggestionService:
    """Suggests relevant hashtags for a question using Gemini."""

    def __init__(self, hashtag_repo: "HashtagRepository"):
        self.hashtag_repo = hashtag_repo
        self._all_names_cache: list[str] | None = None
        self._name_to_canonical: dict[str, str] | None = None
        self._gemini_cache_name: str | None = None
        self._gemini_cache_tags_hash: str | None = None

    async def _get_or_create_gemini_cache(self, all_names: list[str]) -> Optional[str]:
        """Create or reuse Gemini context cache with full tag list. Returns cache name or None."""
        if not GOOGLE_API_KEY:
            return None
        tags_hash = hashlib.sha256("|".join(sorted(all_names)).encode()).hexdigest()
        if self._gemini_cache_name and self._gemini_cache_tags_hash == tags_hash:
            return self._gemini_cache_name
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=GOOGLE_API_KEY)
            tag_list = "\n".join(sorted(all_names))
            cached_content = (
                f"TAGS (pick 1-7, copy names exactly):\n{tag_list}\n\n"
                "Use ONLY these tags. Return JSON array of tag names."
            )
            cache = client.caches.create(
                model=MODEL,
                config=types.CreateCachedContentConfig(
                    display_name="vece-hashtags",
                    system_instruction=SYSTEM_INSTRUCTION,
                    contents=[types.Content(parts=[types.Part(text=cached_content)])],
                    ttl=CACHE_TTL,
                ),
            )
            self._gemini_cache_name = cache.name
            self._gemini_cache_tags_hash = tags_hash
            logger.info("Gemini hashtag cache created: %s", cache.name)
            return cache.name
        except Exception as e:
            logger.warning("Gemini cache create failed: %s", e)
            self._gemini_cache_name = None
            self._gemini_cache_tags_hash = None
            return None

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
                cache_name = await self._get_or_create_gemini_cache(all_names)

                options_str = "\n".join(f"- {o}" for o in (options or [])[:20]) if options else "(none)"
                prompt = f"""QUESTION: {question_text}
OPTIONS: {options_str}

Return JSON array of tag names. Example: ["Sports", "Music"]"""

                if cache_name:
                    config = types.GenerateContentConfig(
                        cached_content=cache_name,
                        temperature=0.3,
                    )
                else:
                    tag_list = "\n".join(all_names[:400])
                    prompt = f"""TAGS (pick 1-7, copy names exactly):
{tag_list}

{prompt}"""
                    config = types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.3,
                    )

                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt,
                    config=config,
                )
                if response and response.text:
                    suggested = _parse_names_from_response(response.text)
                    result = _validate_and_map_to_canonical(suggested, name_to_canonical, all_names)
            except Exception as e:
                logger.warning("Hashtag suggestion (Gemini) failed: %s", e)
                if "cached" in str(e).lower() or "cache" in str(e).lower():
                    self._gemini_cache_name = None
                    self._gemini_cache_tags_hash = None

        # Keyword fallback when Gemini returns empty or is not configured
        if not result:
            result = self._keyword_fallback(
                question_text, options or [], all_names, min(max_hashtags, 7)
            )

        return result


def build_hashtag_suggestion_service(hashtag_repo: "HashtagRepository") -> HashtagSuggestionService:
    return HashtagSuggestionService(hashtag_repo)
