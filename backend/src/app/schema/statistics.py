from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator, ConfigDict

from app.schema.hashtags import Hashtag


class AgeStatistics(BaseModel):
    range: str
    count: int
    percentage: float  # Percentage of total respondents in this age range

    @field_validator("percentage", mode="before")
    @classmethod
    def default_percentage_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class GenderStatistics(BaseModel):
    gender: str
    count: int
    percentage: float  # Percentage of total respondents of this gender

    @field_validator("percentage", mode="before")
    @classmethod
    def default_percentage_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class GeoStatistics(BaseModel):
    country_id: Optional[int]
    country_name: Optional[str]
    count: int
    percentage: float  # Percentage of total respondents from this country

    @field_validator("percentage", mode="before")
    @classmethod
    def default_percentage_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class Statistics(BaseModel):
    age: Optional[list[AgeStatistics]]
    gender: Optional[list[GenderStatistics]]
    geo: Optional[list[GeoStatistics]]


class QuestionOptionStatistics(BaseModel):
    question_id: int
    option_id: int
    option_text: str
    vote_count: int
    statistics: Statistics


class OptionVotes(BaseModel):
    option_id: int
    count: int
    percentage: float  # Percentage of total votes for this option
    text: str

    @field_validator("count", mode="before")
    @classmethod
    def default_count_to_zero(cls, v):
        return 0 if v is None else v

    @field_validator("percentage", mode="before")
    @classmethod
    def default_percentage_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class QuestionVotes(BaseModel):
    question_id: int
    total_answers: int
    votes: list[OptionVotes]


class QuestionStatistics(BaseModel):
    question_id: int
    statistics: Statistics


class QuestionVotesAndStatistics(BaseModel):
    question_id: int
    total_answers: int
    votes: list[OptionVotes]
    statistics: Statistics


class MyQuestion(BaseModel):
    id: int
    text: str
    role: str
    active_till: datetime
    selected_option_ids: Optional[list[int]]
    hashtags: Optional[list[Optional[Hashtag]]]
    author_display_name: str


class UserQuestionVotes(MyQuestion):
    votes: list[OptionVotes]


class UserQuestionStatistics(MyQuestion):
    statistics: Statistics


class UserQuestionVotesAndStatistics(MyQuestion):
    votes: Optional[list[OptionVotes]]
    statistics: Optional[Statistics]


class OptimizedQuestionStats(BaseModel):
    """Optimized data model for user-specific questions with statistics, avoiding redundant question data."""
    id: int  # Question ID
    role: str
    statistics: Optional[Statistics] = None

    model_config = ConfigDict(from_attributes=True)

