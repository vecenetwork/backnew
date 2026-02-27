from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
    Index,
    UniqueConstraint,
    CheckConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database import Base

if TYPE_CHECKING:
    from app.orm.user import UserORM
    from app.orm.hashtags import HashtagORM


class SubscriptionORM(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    subscriber_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    subscribed_to_id: Mapped[int] = mapped_column(
        Integer, nullable=False, index=True
    )  # Could be a user or hashtag
    subscribed_to_type: Mapped[str] = mapped_column(
        String(10), nullable=False
    )  # 'user' or 'hashtag'
    favourite: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

    # Relationships
    subscribed_user: Mapped[Optional["UserORM"]] = relationship(
        "UserORM",
        foreign_keys=[subscribed_to_id],
        primaryjoin="and_(SubscriptionORM.subscribed_to_id == UserORM.id, "
                   "SubscriptionORM.subscribed_to_type == 'user')",
        lazy="selectin",
        viewonly=True
    )

    subscribed_hashtag: Mapped[Optional["HashtagORM"]] = relationship(
        "HashtagORM",
        foreign_keys=[subscribed_to_id],
        primaryjoin="and_(SubscriptionORM.subscribed_to_id == HashtagORM.id, "
                   "SubscriptionORM.subscribed_to_type == 'hashtag')",
        lazy="selectin",
        viewonly=True
    )

    __table_args__ = (
        UniqueConstraint(
            "subscriber_id",
            "subscribed_to_id",
            "subscribed_to_type",
            name="unique_subscription",
        ),
        CheckConstraint(
            "subscribed_to_type IN ('user', 'hashtag')", name="check_subscribed_to_type"
        ),
        Index("idx_subscriber_id", "subscriber_id"),
        Index("idx_subscribed_to_id", "subscribed_to_id"),
        Index("idx_subscriber_type", "subscriber_id", "subscribed_to_type"),
        Index("idx_subscribed_to_type", "subscribed_to_id", "subscribed_to_type"),
    )
