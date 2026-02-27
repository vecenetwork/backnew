from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, ConfigDict, model_validator

from app.schema.hashtags import Hashtag
from app.schema.user import UserResponse, GenderEnum
from app.schema.statistics import Statistics


class QuestionOptionBase(BaseModel):
    text: str
    position: Optional[int] = None


class QuestionOptionCreate(QuestionOptionBase):
    # author_id: Optional[int]
    pass


class QuestionOptionCreateInternal(QuestionOptionBase):
    question_id: int
    author_id: int
    by_question_author: bool


class QuestionOption(QuestionOptionBase):
    id: int
    question_id: int
    author_id: Optional[int]
    by_question_author: bool
    created_at: datetime
    count: int = 0
    percentage: float = 0.0

    model_config = ConfigDict(from_attributes=True)


class AnswerOption(BaseModel):
    answer_id: int
    option_id: int

    model_config = ConfigDict(from_attributes=True)


class AnswerCreate(BaseModel):
    options: list[int] = []
    new_options: Optional[list[str]] = None


class RangeModel(BaseModel):
    start: int
    end: int


class QuestionBase(BaseModel):
    text: str
    max_options: int
    active_till: datetime
    allow_user_options: bool
    gender: Optional[list[GenderEnum]] = None
    country_id: Optional[list[int]] = None


class QuestionCreate(QuestionBase):
    author_id: Optional[int] = None
    age: Optional[RangeModel] = None
    options: list[QuestionOptionCreate] = []
    hashtags: Optional[list[str]]

    # @field_validator("active_till", mode="before")
    # @classmethod
    # def make_naive_datetime(cls, v: datetime) -> datetime:
    #     if isinstance(v, datetime) and v.tzinfo is not None:
    #         return v.astimezone(timezone.utc).replace(tzinfo=None)
    #     return v

    @model_validator(mode="after")
    def make_datetimes_naive(self) -> "QuestionCreate":
        if self.active_till.tzinfo is not None:
            self.active_till = self.active_till.astimezone(timezone.utc).replace(
                tzinfo=None
            )
        return self


class Question(QuestionBase):
    id: int
    author: UserResponse
    age_range: Optional[RangeModel] = None  # used for reading
    options: list[QuestionOption] = []
    created_at: datetime
    total_answers: int = 0
    # answers: list[Answer] = []
    hashtags: list[Hashtag] = []
    user_selected_options: Optional[list[int]] = None  # IDs of options selected by current user (if answered)

    model_config = ConfigDict(from_attributes=True)


class QuestionResponse(QuestionBase):
    """Common response schema for all question APIs with optional statistics fields."""
    id: int
    author: UserResponse
    age_range: Optional[RangeModel] = None  # used for reading
    options: list[QuestionOption] = []
    created_at: datetime
    total_answers: int = 0
    hashtags: list[Hashtag] = []
    user_selected_options: Optional[list[int]] = None  # IDs of options selected by current user (if answered)
    
    # Optional fields for /questions/me endpoint
    role: Optional[str] = None  # "author", "respondent", or "all"
    statistics: Optional[Statistics] = None

    model_config = ConfigDict(from_attributes=True)


class AnswerOptionCreate(BaseModel):
    ids: list[int]


class QuestionUpdate(BaseModel):
    id: int


class QuestionOptionUpdate(BaseModel):
    id: int


class Answer(BaseModel):
    id: int
    user_id: int
    question: Question
    options: list[AnswerOption] = []
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AnswerResponse(BaseModel):
    id: int
    user_id: int
    question: QuestionResponse
    options: list[AnswerOption] = []
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UnansweredCountResponse(BaseModel):
    count: int