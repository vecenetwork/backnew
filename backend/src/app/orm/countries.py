from typing import TYPE_CHECKING

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database import Base

if TYPE_CHECKING:
    from .user import UserORM  # Import for type checking


class CountryORM(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str | None] = mapped_column(String(2))
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(200))
    iso3: Mapped[str | None] = mapped_column(String(3))
    number: Mapped[str | None] = mapped_column(String(3))
    continent_code: Mapped[str | None] = mapped_column(String(2))
    display_order: Mapped[int | None] = mapped_column(Integer)

    users: Mapped[list["UserORM"]] = relationship("UserORM", back_populates="country")
