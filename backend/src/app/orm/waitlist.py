from datetime import date, datetime
from sqlalchemy import String, Date, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from app.schema.user import GenderEnum
from infrastructure.database import Base


class WaitlistORM(Base):
    __tablename__ = "waitlist"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[GenderEnum] = mapped_column(
        ENUM(
            GenderEnum, name="user_gender", create_type=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    birthday: Mapped[date] = mapped_column(Date, nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
