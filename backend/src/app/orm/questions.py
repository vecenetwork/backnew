from __future__ import annotations
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import (
    Integer,
    Text,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    ARRAY,
)
from sqlalchemy.dialects.postgresql import INT4RANGE
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schema.questions import RangeModel
from infrastructure.database import Base

if TYPE_CHECKING:
    from app.orm.hashtags import HashtagORM
    from app.orm.user import UserORM


class QuestionHashtagLinkORM(Base):
    __tablename__ = "question_hashtag_links"
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"), primary_key=True)
    hashtag_id: Mapped[int] = mapped_column(ForeignKey("hashtags.id", ondelete="CASCADE"), primary_key=True)


class QuestionORM(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    text: Mapped[str] = mapped_column(Text, nullable=False)
    max_options: Mapped[int] = mapped_column(nullable=False)
    active_till: Mapped[datetime]
    allow_user_options: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    total_answers: Mapped[int] = mapped_column(default=0, server_default="0", nullable=False)

    gender: Mapped[Optional[list[str]]] = mapped_column(ARRAY(Text))
    country_id: Mapped[Optional[list[int]]] = mapped_column(ARRAY(Integer))
    age: Mapped[Optional[RangeModel]] = mapped_column(INT4RANGE)

    # Relationships
    author: Mapped["UserORM"] = relationship(lazy="selectin")
    options: Mapped[list[QuestionOptionORM]] = relationship(
        back_populates="question", cascade="all, delete-orphan", lazy="selectin"
    )
    hashtags: Mapped[list["HashtagORM"]] = relationship(
        secondary=QuestionHashtagLinkORM.__table__,  # use the table from the orm class
        secondaryjoin="QuestionHashtagLinkORM.hashtag_id == HashtagORM.id",
        primaryjoin="QuestionORM.id == QuestionHashtagLinkORM.question_id",
        back_populates="questions",
        lazy="selectin"
    )
    answers: Mapped[list[AnswerORM]] = relationship(
        back_populates="question", cascade="all, delete-orphan", lazy="select"
    )

    __table_args__ = (
        CheckConstraint("max_options > 0", name="check_max_options_positive"),
    )

    @property
    def age_range(self) -> Optional["RangeModel"]:
        if self.age:
            return RangeModel(start=self.age.lower,  # type: ignore[attr-defined]
                            end=self.age.upper)  # type: ignore[attr-defined]
        return None


class QuestionOptionORM(Base):
    __tablename__ = "question_options"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id", ondelete="CASCADE")
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    position: Mapped[int] = mapped_column(nullable=False)
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    by_question_author: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    count: Mapped[int] = mapped_column(default=0, server_default="0", nullable=False)
    percentage: Mapped[float] = mapped_column(default=0.0, server_default="0.0", nullable=False)

    # Relationships
    question: Mapped[QuestionORM] = relationship(back_populates="options")
    answer_options: Mapped[List[AnswerOptionORM]] = relationship(
        back_populates="option", cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("question_id", "position", name="uq_question_position"),
    )


class AnswerORM(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    # Relationships
    question: Mapped[QuestionORM] = relationship(back_populates="answers")
    options: Mapped[List[AnswerOptionORM]] = relationship(
        back_populates="answer", cascade="all, delete-orphan", lazy="selectin"
    )

    __table_args__ = (
        UniqueConstraint("question_id", "user_id", name="uq_question_user"),
    )


class AnswerOptionORM(Base):
    __tablename__ = "answer_options"

    answer_id: Mapped[int] = mapped_column(
        ForeignKey("answers.id", ondelete="CASCADE"), primary_key=True
    )
    option_id: Mapped[int] = mapped_column(
        ForeignKey("question_options.id", ondelete="CASCADE"), primary_key=True
    )

    # Relationships
    answer: Mapped[AnswerORM] = relationship(back_populates="options")
    option: Mapped[QuestionOptionORM] = relationship(back_populates="answer_options")
