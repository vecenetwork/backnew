from typing import TYPE_CHECKING, Optional, List
from datetime import date, datetime

from sqlalchemy import Integer, String, Date, Text, ForeignKey, Boolean, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schema.user import GenderEnum, Role, ShowNameOptionEnum, ShowQuestionResultsEnum
from infrastructure.database import Base

if TYPE_CHECKING:
    from app.orm.countries import CountryORM
    from app.orm.subscriptions import SubscriptionORM


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    birthday: Mapped[date] = mapped_column(Date, nullable=False)
    country_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("countries.id", ondelete="SET NULL"), nullable=False
    )
    gender: Mapped[GenderEnum] = mapped_column(
        ENUM(
            GenderEnum, name="user_gender", create_type=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now()
    )
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    profile_picture: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    social_link: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    role: Mapped[Role] = mapped_column(
        ENUM(Role, name="user_role", create_type=False, values_callable=lambda obj: [e.value for e in obj]),  # create_type=False assumes it's created in DB already
        nullable=False,
        default=Role.user,
        server_default="user",
    )
    country: Mapped["CountryORM"] = relationship(
        back_populates="users", lazy="selectin"
    )
    settings: Mapped["UserSettingsORM"] = relationship(
        uselist=False,
        cascade="all, delete",
        lazy="selectin",
    )
    following_users: Mapped[List["SubscriptionORM"]] = relationship(
        primaryjoin="and_(UserORM.id == SubscriptionORM.subscriber_id, "
        "SubscriptionORM.subscribed_to_type == 'user')",
        lazy="select",
    )
    following_hashtags: Mapped[List["SubscriptionORM"]] = relationship(
        primaryjoin="and_(UserORM.id == SubscriptionORM.subscriber_id, "
        "SubscriptionORM.subscribed_to_type == 'hashtag')",
        lazy="select",
        overlaps="following_users"
    )

    @hybrid_property
    def all_subscriptions(self) -> List["SubscriptionORM"]:
        """Return all subscriptions (both users and hashtags) in a single list."""
        return self.following_users + self.following_hashtags


class UserSettingsORM(Base):
    __tablename__ = "user_settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    show_name_option: Mapped[ShowNameOptionEnum] = mapped_column(
        ENUM(
            ShowNameOptionEnum,
            name="setting_show_name_option",
            create_type=False,
            values_callable=lambda obj: [e.value for e in obj]),  # create_type=False assumes it's created in DB already
        nullable=False,
        default=ShowNameOptionEnum.name,
        server_default="name",
    )
    show_question_results: Mapped[ShowQuestionResultsEnum] = mapped_column(
        ENUM(
            ShowQuestionResultsEnum,
            name="setting_show_question_results",
            create_type=False,
            values_callable=lambda obj: [e.value for e in obj]),  # create_type=False assumes it's created in DB already
        nullable=False,
        default=ShowQuestionResultsEnum.all,
        server_default="all",
    )
    allow_results_in_digests: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True,
    )
    receive_digests: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True,
    )
