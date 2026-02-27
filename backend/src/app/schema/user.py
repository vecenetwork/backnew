from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr

from app.schema.countries import Country
from app.schema.similarity import Similarity, Mutuality


class Role(str, Enum):
    user = "user"
    admin = "admin"
    # moderator
    # paid user


class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class ShowNameOptionEnum(str, Enum):
    name = "Name"
    username = "Username"


class ShowQuestionResultsEnum(str, Enum):
    nobody = "Nobody"
    people_i_follow = "People I Follow"
    people_following_me = "People Following Me"
    all_connections = "All Connections"
    all = "All"


class UserSettings(BaseModel):
    # TODO: check default values
    show_name_option: ShowNameOptionEnum = ShowNameOptionEnum.name
    show_question_results: ShowQuestionResultsEnum = ShowQuestionResultsEnum.all_connections
    allow_results_in_digests: bool = True
    receive_digests: bool = True

    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    id: int
    name: str
    surname: str
    username: str
    email: EmailStr
    password_hash: str
    birthday: date
    country: Country
    gender: GenderEnum
    settings: UserSettings | None = None
    description: str | None = None
    profile_picture: str | None = None
    social_link: str | None = None
    is_verified: bool
    is_active: bool
    role: Role = Role.user
    is_subscribed: bool | None = None
    similarity: Similarity | None = None  # Optional similarity score with current user
    mutuality: Mutuality | None = None  # Optional mutuality score with current user

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id: int
    name: str | None = None  # may be hidden from other users
    surname: str | None = None  # may be hidden from other users
    username: str
    email: EmailStr | None = None
    birthday: date | None = None  # may be hidden from other users
    country: Country
    gender: GenderEnum
    profile_picture: str | None = None
    settings: UserSettings | None = None
    description: str | None = None
    social_link: str | None = None
    is_subscribed: bool | None = None
    similarity: Similarity | None = None  # Optional similarity score with current user
    mutuality: Mutuality | None = None  # Optional mutuality score with current user

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_user(cls, user: User):
        # Create a UserResponse from a User instance
        return cls(
            id=user.id,
            name=user.name,
            surname=user.surname,
            username=user.username,
            email=user.email,
            birthday=user.birthday,
            country=user.country,
            gender=user.gender,
            settings=user.settings,
            description=user.description,
            profile_picture=user.profile_picture,
            social_link=user.social_link,
        )

    @classmethod
    def from_user_other(cls, user: User):
        # Create a UserResponse from a User instance when requested by other user
        if not user.settings:
            raise RuntimeError('User does not have settings')
        if user.settings.show_name_option == ShowNameOptionEnum.name:
            name_data = {
                "name": user.name,
                "surname": user.surname,
                "username": user.username,
            }
        else:
            name_data = {
                "username": user.username,
            }

        return cls(
            id=user.id,
            email=user.email,
            birthday=None,
            country=user.country,
            gender=user.gender,
            settings=None,
            description=user.description,
            social_link=user.social_link,
            is_subscribed=user.is_subscribed,
            mutuality=user.mutuality,
            similarity=user.similarity,
            profile_picture=user.profile_picture,
            **name_data,
        )


class UserSettingsUpdate(BaseModel):
    """Schema for updating user settings. All fields are optional."""

    show_name_option: Optional[ShowNameOptionEnum] = None
    show_question_results: Optional[ShowQuestionResultsEnum] = None
    allow_results_in_digests: Optional[bool] = None
    receive_digests: Optional[bool] = None


class UserUpdateBase(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    birthday: Optional[date] = None
    country_id: Optional[int] = None
    gender: Optional[GenderEnum] = None
    description: Optional[str] = None
    profile_picture: Optional[str] = None
    social_link: Optional[str] = None
    settings: Optional[UserSettingsUpdate] = None


class UserUpdateInternal(UserUpdateBase):
    password_hash: Optional[str] = None


class UserUpdate(UserUpdateBase):
    old_password: Optional[str] = None
    new_password: Optional[str] = None


class UserCreate(BaseModel):
    """Registration: required — country_id, gender, birthday, email, username, password. Optional — name, surname."""

    name: Optional[str] = None
    surname: Optional[str] = None
    username: str
    email: EmailStr
    password: str
    birthday: date
    country_id: int
    gender: GenderEnum


class TimeRangeEnum(str, Enum):
    last_year = "last_year"
    last_day = "last_day"
    last_week = "last_week"
    last_month = "last_month"


class ConnectionFilterEnum(str, Enum):
    followings = "followings"
    followers = "followers"
    non_connected = "non_connected"


class SimilaritySortEnum(str, Enum):
    mutuality = "mutuality"
    similarity = "similarity"


class SimilarUserResponse(BaseModel):
    """Response model for similar users endpoint that includes similarity scores"""
    user: UserResponse
    similarity: Optional[Similarity] = None
    mutuality: Optional[Mutuality] = None

    model_config = ConfigDict(from_attributes=True)
