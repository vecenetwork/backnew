import os
from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr

from app.schema.countries import Country


def _avatar_url(user: "User") -> Optional[str]:
    """Return avatar URL: our endpoint for paths (private bucket), or original URL for legacy."""
    if not user.profile_picture:
        return None
    if user.profile_picture.startswith("http"):
        return user.profile_picture
    base = os.getenv("BASE_URL", "http://localhost:8000/api").rstrip("/")
    return f"{base}/users/{user.id}/avatar"
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
    show_country: bool = True
    show_gender: bool = True
    show_age: bool = True

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
    settings: Optional[UserSettings] = None
    description: Optional[str] = None
    profile_picture: Optional[str] = None
    social_link: Optional[str] = None
    is_verified: bool
    is_active: bool
    role: Role = Role.user
    is_subscribed: Optional[bool] = None
    similarity: Optional[Similarity] = None  # Optional similarity score with current user
    mutuality: Optional[Mutuality] = None  # Optional mutuality score with current user

    model_config = ConfigDict(from_attributes=True)


class ProfileVisibility(BaseModel):
    """Which profile fields the user allows others to see. Returned when viewing another user."""
    show_country: bool = True
    show_gender: bool = True
    show_age: bool = True


class UserResponse(BaseModel):
    id: int
    name: Optional[str] = None  # may be hidden from other users
    surname: Optional[str] = None  # may be hidden from other users
    username: str
    email: Optional[EmailStr] = None
    birthday: Optional[date] = None  # may be hidden from other users
    country: Optional[Country] = None  # hidden when show_country=False
    gender: Optional[GenderEnum] = None  # hidden when show_gender=False
    profile_visibility: Optional[ProfileVisibility] = None  # only for other users, tells what to show
    profile_picture: Optional[str] = None
    settings: Optional[UserSettings] = None
    description: Optional[str] = None
    social_link: Optional[str] = None
    is_subscribed: Optional[bool] = None
    similarity: Optional[Similarity] = None  # Optional similarity score with current user
    mutuality: Optional[Mutuality] = None  # Optional mutuality score with current user

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_user(cls, user: User):
        # Create a UserResponse from a User instance (viewing own profile)
        pv = None
        if user.settings:
            pv = ProfileVisibility(
                show_country=user.settings.show_country,
                show_gender=user.settings.show_gender,
                show_age=user.settings.show_age,
            )
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
            profile_visibility=pv,
            description=user.description,
            profile_picture=_avatar_url(user),
            social_link=user.social_link,
        )

    @classmethod
    def from_user_other(cls, user: User):
        # Create a UserResponse from a User instance when requested by other user
        if not user.settings:
            raise RuntimeError('User does not have settings')
        s = user.settings
        if s.show_name_option == ShowNameOptionEnum.name:
            name_data = {
                "name": user.name,
                "surname": user.surname,
                "username": user.username,
            }
        else:
            name_data = {
                "username": user.username,
            }

        # Apply privacy: only include country/gender/birthday if user allows
        country = user.country if s.show_country else None
        gender = user.gender if s.show_gender else None
        birthday = user.birthday if s.show_age else None

        return cls(
            id=user.id,
            email=user.email,
            birthday=birthday,
            country=country,
            gender=gender,
            settings=None,
            profile_visibility=ProfileVisibility(
                show_country=s.show_country,
                show_gender=s.show_gender,
                show_age=s.show_age,
            ),
            description=user.description,
            social_link=user.social_link,
            is_subscribed=user.is_subscribed,
            mutuality=user.mutuality,
            similarity=user.similarity,
            profile_picture=_avatar_url(user),
            **name_data,
        )


class UserSettingsUpdate(BaseModel):
    """Schema for updating user settings. All fields are optional."""

    show_name_option: Optional[ShowNameOptionEnum] = None
    show_question_results: Optional[ShowQuestionResultsEnum] = None
    allow_results_in_digests: Optional[bool] = None
    receive_digests: Optional[bool] = None
    show_country: Optional[bool] = None
    show_gender: Optional[bool] = None
    show_age: Optional[bool] = None


class UserUpdateBase(BaseModel):
    username: Optional[str] = None
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
