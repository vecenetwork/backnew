import logging
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import text

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


@dataclass
class PendingRegistration:
    id: int
    email: str
    username: str
    password_hash: str
    token: str
    created_at: datetime
    expires_at: datetime


class PendingRegistrationRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    async def create(
        self, email: str, username: str, password_hash: str, token: str, expires_at: datetime
    ) -> PendingRegistration:
        stmt = text("""
            INSERT INTO pending_registrations (email, username, password_hash, token, expires_at)
            VALUES (:email, :username, :password_hash, :token, :expires_at)
            RETURNING id, email, username, password_hash, token, created_at, expires_at
        """)
        result = await self.db.execute(
            stmt,
            {
                "email": email,
                "username": username,
                "password_hash": password_hash,
                "token": token,
                "expires_at": expires_at,
            },
        )
        row = result.fetchone()
        await self.db.commit()
        return PendingRegistration(
            id=row[0],
            email=row[1],
            username=row[2],
            password_hash=row[3],
            token=row[4],
            created_at=row[5],
            expires_at=row[6],
        )

    async def get_by_token(self, token: str) -> PendingRegistration | None:
        stmt = text("""
            SELECT id, email, username, password_hash, token, created_at, expires_at
            FROM pending_registrations
            WHERE token = :token AND expires_at > NOW()
        """)
        result = await self.db.execute(stmt, {"token": token})
        row = result.fetchone()
        if not row:
            return None
        return PendingRegistration(
            id=row[0],
            email=row[1],
            username=row[2],
            password_hash=row[3],
            token=row[4],
            created_at=row[5],
            expires_at=row[6],
        )

    async def delete_by_token(self, token: str) -> None:
        await self.db.execute(
            text("DELETE FROM pending_registrations WHERE token = :token"),
            {"token": token},
        )
        await self.db.commit()


def build_pending_registration_repository(db: "AsyncSession") -> PendingRegistrationRepository:
    return PendingRegistrationRepository(db)
