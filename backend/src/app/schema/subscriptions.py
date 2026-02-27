from enum import Enum

from pydantic import BaseModel, Field

from app.schema.user import UserResponse
from app.schema.hashtags import Hashtag


class SubscriptionTypeEnum(str, Enum):
    """Type of subscription."""
    user = "user"
    hashtag = "hashtag"


class SubscriptionBase(BaseModel):
    subscribed_to_id: int = Field(
        ..., description="ID of the user or hashtag being subscribed to"
    )
    subscribed_to_type: SubscriptionTypeEnum = Field(
        ..., description="Type of subscription ('user' or 'hashtag')"
    )
    favourite: bool = Field(False, description="Favourite flag")


class SubscriptionCreate(SubscriptionBase):
    pass  # Uses the same fields as SubscriptionBase


class SubscriptionResponse(SubscriptionBase):
    id: int
    subscriber_id: int

    class Config:
        from_attributes = True


class UserSubscription(BaseModel):
    id: int
    user: UserResponse
    favourite: bool

    class Config:
        from_attributes = True


class HashtagSubscription(BaseModel):
    id: int
    hashtag: Hashtag
    favourite: bool

    class Config:
        from_attributes = True


class UserSubscriptionsResponse(BaseModel):
    users: list[UserSubscription] = []
    hashtags: list[HashtagSubscription] = []


class SubscribersResponse(BaseModel):
    subscribers: list[int]  # List of user IDs who follow the entity
