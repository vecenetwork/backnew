from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, and_
from sqlalchemy.orm import Mapped, mapped_column, relationship, foreign

from app.orm.questions import QuestionHashtagLinkORM
from app.orm.subscriptions import SubscriptionORM
from infrastructure.database import Base

if TYPE_CHECKING:
    from app.orm.questions import QuestionORM


class HashtagORM(Base):
    __tablename__ = "hashtags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    # Hashtags followed by users
    followers: Mapped[list["SubscriptionORM"]] = relationship(
        "SubscriptionORM",
        primaryjoin=and_(
            id == foreign(SubscriptionORM.subscribed_to_id),
            SubscriptionORM.subscribed_to_type == "hashtag",
        ),
        lazy="selectin",
    )

    questions: Mapped[list["QuestionORM"]] = relationship(
        secondary=QuestionHashtagLinkORM.__table__,
        back_populates="hashtags"
    )
