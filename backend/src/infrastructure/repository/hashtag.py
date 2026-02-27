from typing import TYPE_CHECKING, Optional

from sqlalchemy import func, select, and_
from sqlalchemy.sql import Select

from app.exceptions import Missing
from app.orm.hashtags import HashtagORM
from app.orm.questions import QuestionHashtagLinkORM
from app.orm.subscriptions import SubscriptionORM
from app.schema.hashtags import Hashtag
from app.schema.user import User


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class HashtagRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    def _add_subscription_status(self, stmt: Select, current_user: User) -> Select:
        """Add subscription status to a query for the current user."""
        return stmt.outerjoin(
            SubscriptionORM,
            and_(
                SubscriptionORM.subscribed_to_id == HashtagORM.id,
                SubscriptionORM.subscribed_to_type == "hashtag",
                SubscriptionORM.subscriber_id == current_user.id
            )
        ).add_columns(SubscriptionORM.id.isnot(None).label("is_subscribed"))

    async def _execute_hashtag_query(
        self,
        stmt: Select,
        current_user: Optional[User] = None
    ) -> list[Hashtag]:
        """Execute a hashtag query and process the results."""
        if current_user:
            stmt = self._add_subscription_status(stmt, current_user)

        if self.db.in_transaction():
            result = await self.db.execute(stmt)
        else:
            async with self.db.begin():
                result = await self.db.execute(stmt)

        if current_user:
            rows = result.all()
            hashtags = []
            for hashtag_orm, is_subscribed in rows:
                hashtag = Hashtag.model_validate(hashtag_orm)
                hashtag.is_subscribed = is_subscribed
                hashtags.append(hashtag)
        else:
            hashtags_orm = result.scalars().all()
            hashtags = [Hashtag.model_validate(hashtag) for hashtag in hashtags_orm]
        return hashtags

    async def create(self, hashtag: Hashtag) -> Hashtag:
        raise NotImplementedError("Not implemented yet")

    async def get_by_id(self, hashtag_id: int, current_user: Optional[User] = None) -> Hashtag:
        """Get a hashtag by ID with optional subscription status."""
        stmt = select(HashtagORM).where(HashtagORM.id == hashtag_id)
        hashtags = await self._execute_hashtag_query(stmt, current_user)
        if not hashtags:
            raise Missing("Hashtag not found")
        return hashtags[0]

    async def get_all_paginated(self, limit: int, offset: int, current_user: Optional[User] = None) -> list[Hashtag]:
        """Retrieve paginated hashtags with optional subscription status."""
        stmt = select(HashtagORM).limit(limit).offset(offset)
        return await self._execute_hashtag_query(stmt, current_user)

    async def get_all_names(self) -> list[str]:
        """Retrieve all hashtag names (for AI suggestion)."""
        stmt = select(HashtagORM.name).order_by(HashtagORM.name)
        if self.db.in_transaction():
            result = await self.db.execute(stmt)
        else:
            async with self.db.begin():
                result = await self.db.execute(stmt)
        return [row[0] for row in result.all()]

    async def get_random_hashtags(self, limit: int, current_user: Optional[User] = None) -> list[Hashtag]:
        """Retrieve random hashtags with optional subscription status."""
        stmt = select(HashtagORM).order_by(func.random()).limit(limit)
        return await self._execute_hashtag_query(stmt, current_user)

    async def search(self, query: str, limit: int, current_user: Optional[User] = None) -> list[Hashtag]:
        """Search hashtags by name."""
        # Add wildcards for LIKE query and escape special characters
        escaped = query.replace("%", r"\%").replace("_", r"\_")
        search_pattern = f"%{escaped}%"

        stmt = (
            select(HashtagORM)
            .where(HashtagORM.name.ilike(search_pattern))
            .limit(limit)
        )

        return await self._execute_hashtag_query(stmt, current_user)

    async def delete(self, hashtag_id: int):
        """Delete a hashtag, raise exception if not found."""
        async with self.db.begin():
            stmt = select(HashtagORM).where(HashtagORM.id == hashtag_id)
            result = await self.db.execute(stmt)
            user = result.scalars().first()
            if not user:
                raise Missing("Hashtag not found")

            await self.db.delete(user)
        await self.db.commit()

    async def update(self, hashtag: Hashtag) -> Hashtag:
        raise NotImplementedError("Not implemented yet")


def build_hashtag_repository(db: "AsyncSession") -> HashtagRepository:
    repo = HashtagRepository(db)
    return repo


class QuestionHashtagLinkRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    async def create(self, hashtag_id: int, question_id: int):
        link = QuestionHashtagLinkORM(
            question_id=question_id,
            hashtag_id=hashtag_id,
        )
        self.db.add(link)
        await self.db.commit()

    async def bulk_create(self, hashtag_names: list[str], question_id: int):
        # Step 1: Query all hashtags by name
        result = await self.db.execute(
            select(HashtagORM).where(HashtagORM.name.in_(hashtag_names))
        )
        hashtags = result.scalars().all()

        found_names = {hashtag.name for hashtag in hashtags}
        missing = set(hashtag_names) - found_names
        if missing:
            raise Missing(f"Hashtags not found: {', '.join(missing)}")

        # Step 2: Create links using hashtag IDs
        links = [
            QuestionHashtagLinkORM(
                question_id=question_id,
                hashtag_id=hashtag.id,
            )
            for hashtag in hashtags
        ]
        self.db.add_all(links)
        await self.db.commit()

    async def bulk_create_by_id(self, hashtag_ids: list[int], question_id: int):
        links = [
            QuestionHashtagLinkORM(
                question_id=question_id,
                hashtag_id=hashtag_id,
            )
            for hashtag_id in hashtag_ids
        ]
        self.db.add_all(links)
        await self.db.commit()


def build_question_hashtag_repository(db: "AsyncSession") -> QuestionHashtagLinkRepository:
    repo = QuestionHashtagLinkRepository(db)
    return repo
