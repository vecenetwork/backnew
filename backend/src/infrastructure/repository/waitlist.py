from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from app.exceptions import Missing
from app.orm.waitlist import WaitlistORM
from app.schema.waitlist import WaitlistData

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class WaitlistRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    async def create(self, data: WaitlistData) -> WaitlistData:
        """Add a user to the waitlist"""
        new_entry = WaitlistORM(**data.dict())
        async with self.db.begin():
            self.db.add(new_entry)
        await self.db.flush()
        await self.db.refresh(new_entry)
        return WaitlistData.model_validate(new_entry)

    async def get_by_email(self, email: str) -> WaitlistData:
        """Get a waitlist entry by email"""
        async with self.db.begin():
            stmt = select(WaitlistORM).where(WaitlistORM.email == email)
            result = await self.db.execute(stmt)
            try:
                entry = result.scalar_one()
            except NoResultFound:
                raise Missing(f"No waitlist entry found for email: {email}")
        return WaitlistData.model_validate(entry)

    async def list_all(self, limit: int = 100, offset: int = 0) -> list[WaitlistData]:
        """List all waitlist entries, paginated"""
        async with self.db.begin():
            stmt = select(WaitlistORM).limit(limit).offset(offset)
            result = await self.db.execute(stmt)
            entries = result.scalars().all()
        return [WaitlistData.model_validate(entry) for entry in entries]

    async def delete_by_email(self, email: str):
        """Delete a waitlist entry by email"""
        async with self.db.begin():
            stmt = select(WaitlistORM).where(WaitlistORM.email == email)
            result = await self.db.execute(stmt)
            try:
                entry = result.scalar_one()
            except NoResultFound:
                raise Missing(f"No waitlist entry found for email: {email}")
            await self.db.delete(entry)
        await self.db.commit()


def build_waitlist_repository(db: "AsyncSession") -> WaitlistRepository:
    return WaitlistRepository(db)
