from datetime import datetime

from infrastructure.database import Base

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import TIMESTAMP


class BarrierTokenORM(Base):
    __tablename__ = "barrier_tokens"

    token: Mapped[str] = mapped_column(String(255), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
