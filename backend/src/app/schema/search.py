from enum import Enum

from pydantic import BaseModel

from app.schema.hashtags import Hashtag
from app.schema.questions import QuestionResponse
from app.schema.user import UserResponse


class SearchType(str, Enum):
    all = "all"
    hashtags = "hashtags"
    users = "users"
    questions = "questions"


class SearchResults(BaseModel):
    hashtags: list[Hashtag] = []
    users: list[UserResponse] = []
    questions: list[QuestionResponse] = []
