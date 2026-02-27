from pydantic import BaseModel, field_validator
from typing import Optional


class Mutuality(BaseModel):
    mutuality: Optional[float] = 0
    my_total: int = 0
    other_total: int = 0
    common_total: int = 0

    @field_validator("mutuality", mode="before")
    @classmethod
    def default_mutuality_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class Similarity(BaseModel):
    avg_similarity: Optional[float] = 0
    common_total: int = 0

    @field_validator("avg_similarity", mode="before")
    @classmethod
    def default_similarity_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class MutualityAndSimilarity(BaseModel):
    mutuality: Optional[float] = 0
    avg_similarity: Optional[float] = 0
    my_total: int = 0
    other_total: int = 0
    common_total: int = 0

    @field_validator("mutuality", "avg_similarity", mode="before")
    @classmethod
    def default_scores_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class HashtagMutuality(BaseModel):
    hashtag_id: int
    hashtag_name: str
    my_total: int = 0
    other_total: int = 0
    common_total: int = 0
    mutuality: Optional[float] = 0

    @field_validator("mutuality", mode="before")
    @classmethod
    def default_mutuality_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class HashtagSimilarity(BaseModel):
    hashtag_id: int
    hashtag_name: str
    avg_similarity: Optional[float] = 0
    common_total: int = 0

    @field_validator("avg_similarity", mode="before")
    @classmethod
    def default_similarity_to_zero(cls, v):
        return 0.0 if v is None else float(v)


class HashtagMutualityAndSimilarity(BaseModel):
    hashtag_id: int
    hashtag_name: str
    my_total: int = 0
    other_total: int = 0
    common_total: int = 0
    mutuality: Optional[float] = 0
    avg_similarity: Optional[float] = 0

    @field_validator("mutuality", "avg_similarity", mode="before")
    @classmethod
    def default_scores_to_zero(cls, v):
        return 0.0 if v is None else float(v)
