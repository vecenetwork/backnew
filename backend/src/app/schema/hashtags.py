from typing import Optional

from pydantic import BaseModel, ConfigDict


class Hashtag(BaseModel):
    id: Optional[int] = None
    name: str
    is_subscribed: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)


class TagRequest(BaseModel):
    text: str


class HashtagSuggestRequest(BaseModel):
    """Request body for POST /hashtags/pick."""

    question_text: str
    options: list[str] = []


class HashtagSuggestResponse(BaseModel):
    """Response for POST /hashtags/pick."""

    hashtags: list[str]
