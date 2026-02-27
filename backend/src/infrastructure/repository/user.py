import logging
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import select, update, and_, exists
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import Select

from app.exceptions import Missing
from app.orm.user import UserORM, UserSettingsORM
from app.orm.subscriptions import SubscriptionORM

from app.schema.user import User, UserCreate, UserUpdateInternal

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class UserRepository:
    """Handles database operations related to User."""

    def __init__(self, db: "AsyncSession"):
        self.db = db

    def _add_subscription_status(self, stmt: Select, current_user_id: int) -> Select:
        """Add subscription status to a user query."""
        exists_stmt = (
            exists(SubscriptionORM)
            .where(
                and_(
                    SubscriptionORM.subscriber_id == current_user_id,
                    SubscriptionORM.subscribed_to_id == UserORM.id,
                    SubscriptionORM.subscribed_to_type == "user"
                )
            )
            .correlate(UserORM)
        )
        return stmt.add_columns(exists_stmt.label("is_subscribed"))

    async def user_exists_by_username_or_email(self, username: str, email: str) -> bool:
        async with self.db.begin():
            stmt = select(UserORM).where(
                (UserORM.username == username) | (UserORM.email == email)
            )
            result = await self.db.execute(stmt)
            user = result.scalars().first()
        return user is not None

    async def get_by_username_or_email(self, username: str, email: str) -> User:
        async with self.db.begin():
            stmt = (
                select(UserORM)
                .where((UserORM.username == username) | (UserORM.email == email))
                .options(
                    selectinload(UserORM.settings),
                    selectinload(UserORM.country))
            )
            result = await self.db.execute(stmt)
            user = result.scalar_one_or_none()

        if not user:
            raise Missing("User not found")

        return User.model_validate(user)

    async def get_by_username(self, username: str, current_user_id: Optional[int] = None) -> User:
        """Get a user by username with optional subscription status."""
        stmt = (
            select(UserORM)
            .where(UserORM.username == username)
            .options(
                selectinload(UserORM.settings),
                selectinload(UserORM.country)
            )
        )

        if current_user_id:
            stmt = self._add_subscription_status(stmt, current_user_id)
            result = await self.db.execute(stmt)
            row = result.first()
            if not row:
                raise Missing(f"User with username {username} not found")
            user_orm, is_subscribed = row
            user = User.model_validate(user_orm)
            user.is_subscribed = is_subscribed
            return user
        else:
            result = await self.db.execute(stmt)
            user_orm = result.scalar_one_or_none()
            if not user_orm:
                raise Missing(f"User with username {username} not found")
            return User.model_validate(user_orm)

    async def get_by_email(self, email: str) -> User:
        async with self.db.begin():
            stmt = (
                select(UserORM)
                .options(
                    selectinload(UserORM.settings),
                    selectinload(UserORM.country))
                .where(UserORM.email == email)
            )
            result = await self.db.execute(stmt)
            user = result.scalar_one_or_none()

        if not user:
            raise Missing(f"User with email {email} not found")

        return User.model_validate(user)

    async def create_user(self, user_data: UserCreate, hashed_password: str) -> User:
        """Creates a new user and their default settings."""
        # async with self.db.begin():  # Ensures atomic transaction
        new_user = UserORM(
            name=user_data.name or "",
            surname=user_data.surname or "",
            username=user_data.username,
            email=user_data.email,
            password_hash=hashed_password,  # Store hashed password
            birthday=user_data.birthday,
            country_id=user_data.country_id,
            gender=user_data.gender.value,
            is_verified=False,
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        self.db.add(new_user)
        await (
            self.db.flush()
        )  # Ensures new_user.id is available before inserting settings

        # Create default user settings
        default_settings = UserSettingsORM(
            user_id=new_user.id,
            show_name_option="Name",
            show_question_results="Nobody",
            allow_results_in_digests=False,
            receive_digests=False,
        )
        self.db.add(default_settings)

        await self.db.commit()
        await self.db.refresh(new_user)
        logger.info(new_user)
        validated_user = User.model_validate(new_user)
        return validated_user

    async def create_user_simple(
        self, user_data: UserCreate, hashed_password: str, is_verified: bool = False
    ) -> User:
        """Creates user with simplified registration (email, username, password)."""
        new_user = UserORM(
            name=user_data.name or "",
            surname=user_data.surname or "",
            username=user_data.username,
            email=user_data.email,
            password_hash=hashed_password,
            birthday=user_data.birthday,
            country_id=user_data.country_id,
            gender=user_data.gender.value,
            is_verified=is_verified,
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.db.add(new_user)
        await self.db.flush()
        default_settings = UserSettingsORM(
            user_id=new_user.id,
            show_name_option="Name",
            show_question_results="Nobody",
            allow_results_in_digests=False,
            receive_digests=False,
        )
        self.db.add(default_settings)
        await self.db.commit()
        await self.db.refresh(new_user)
        return User.model_validate(new_user)

    async def update_user(self, user_id: int, update_data: UserUpdateInternal) -> User:
        """
        Update a user and their settings with only the provided fields.
        """
        # TODO: set updated_at
        update_dict = update_data.model_dump(exclude_unset=True, exclude_none=True)

        # Split user fields & settings fields
        user_fields = {k: v for k, v in update_dict.items() if k != "settings"}
        settings_fields = update_dict.get("settings", {})

        if not user_fields and not settings_fields:
            raise ValueError("No valid fields provided for update")

        # Update user fields if any
        if user_fields:
            stmt = (
                update(UserORM)
                .where(UserORM.id == user_id)
                .values(**user_fields)
                .returning(UserORM)
            )
            result = await self.db.execute(stmt)
            updated_user = result.scalar_one_or_none()

            if not updated_user:
                raise Missing("User not found")

        # Update settings if any
        if settings_fields:
            stmt_settings = (
                update(UserSettingsORM)
                .where(UserSettingsORM.user_id == user_id)
                .values(**settings_fields)
            )
            await self.db.execute(stmt_settings)

        await self.db.commit()

        # Fetch the updated user with settings
        stmt_updated_user = (
            select(UserORM)
            .where(UserORM.id == user_id)
            .options(
                selectinload(UserORM.settings),
                selectinload(UserORM.country))
        )
        result = await self.db.execute(stmt_updated_user)
        updated_user = result.scalar_one_or_none()

        if not updated_user:
            # TODO: looks like 500 err case
            raise Missing("User not found after update")

        return User.model_validate(updated_user)

    async def verify_user_email(self, email: str) -> User:
        """
        Verify a user by setting `is_verified = True`.
        """
        # Fetch user by email
        stmt = select(UserORM).where(UserORM.email == email)
        result = await self.db.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            raise Missing(f"User with email {email} does not exist")

        # Update the user
        user.is_verified = True
        await self.db.commit()
        await self.db.refresh(user)  # Refresh to get updated data

        return User.model_validate(user)

    async def get_user_by_id(self, user_id: int, current_user_id: Optional[int] = None) -> User:
        """Get a user by ID with optional subscription status."""
        stmt = (
            select(UserORM)
            .where(UserORM.id == user_id)
            .options(
                selectinload(UserORM.settings),
                selectinload(UserORM.country)
            )
        )

        if current_user_id and current_user_id != user_id:  # Don't check subscription to self
            stmt = self._add_subscription_status(stmt, current_user_id)
            result = await self.db.execute(stmt)
            row = result.first()
            if not row:
                raise Missing(f"User with id {user_id} not found")
            user_orm, is_subscribed = row
            user = User.model_validate(user_orm)
            user.is_subscribed = is_subscribed
            return user
        else:
            result = await self.db.execute(stmt)
            user_orm = result.scalar_one_or_none()
            if not user_orm:
                raise Missing(f"User with id {user_id} not found")
            return User.model_validate(user_orm)

    async def get_all_users_paginated(
        self,
        limit: int,
        offset: int,
        current_user_id: Optional[int] = None
    ) -> list[User]:
        """Get paginated users with optional subscription status."""
        stmt = (
            select(UserORM)
            .options(
                selectinload(UserORM.settings),
                selectinload(UserORM.country)
            )
            .limit(limit)
            .offset(offset)
        )

        if current_user_id:
            stmt = self._add_subscription_status(stmt, current_user_id)
            result = await self.db.execute(stmt)
            rows = result.all()
            users = []
            for row in rows:
                user_orm, is_subscribed = row
                user = User.model_validate(user_orm)
                user.is_subscribed = is_subscribed
                users.append(user)
            return users
        else:
            result = await self.db.execute(stmt)
            user_orms = result.scalars().all()
            return [User.model_validate(user_orm) for user_orm in user_orms]

    async def get_users_by_ids(
        self,
        user_ids: list[int],
        current_user_id: Optional[int] = None
    ) -> list[User]:
        """Get multiple users by their IDs with optional subscription status."""
        if not user_ids:
            return []

        stmt = (
            select(UserORM)
            .where(UserORM.id.in_(user_ids))
            .options(
                selectinload(UserORM.settings),
                selectinload(UserORM.country)
            )
        )

        if current_user_id:
            stmt = self._add_subscription_status(stmt, current_user_id)
            result = await self.db.execute(stmt)
            rows = result.all()
            users = []
            for row in rows:
                user_orm, is_subscribed = row
                user = User.model_validate(user_orm)
                user.is_subscribed = is_subscribed
                users.append(user)
            return users
        else:
            result = await self.db.execute(stmt)
            user_orms = result.scalars().all()
            return [User.model_validate(user_orm) for user_orm in user_orms]

    async def delete_user(self, user_id: int) -> None:
        """Delete a user, raise exception if not found."""
        async with self.db.begin():
            stmt = select(UserORM).where(UserORM.id == user_id)
            result = await self.db.execute(stmt)
            user = result.scalars().first()
            if not user:
                raise Missing("User not found")

            await self.db.delete(user)
        await self.db.commit()

    async def search(
        self,
        query: str,
        limit: int,
        current_user_id: Optional[int] = None
    ) -> list[User]:
        """Search users by username or name."""
        # Add wildcards for LIKE query and escape special characters
        search_pattern = f"%{query.replace('%', '\\%').replace('_', '\\_')}%"

        stmt = (
            select(UserORM)
            .where(
                (UserORM.username.ilike(search_pattern)) |
                (UserORM.name.ilike(search_pattern)) |
                (UserORM.surname.ilike(search_pattern))
            )
            .options(
                selectinload(UserORM.settings),
                selectinload(UserORM.country)
            )
            .limit(limit)
        )

        if current_user_id:
            stmt = self._add_subscription_status(stmt, current_user_id)
            result = await self.db.execute(stmt)
            rows = result.all()
            users = []
            for row in rows:
                user_orm, is_subscribed = row
                user = User.model_validate(user_orm)
                user.is_subscribed = is_subscribed
                users.append(user)
            return users
        else:
            result = await self.db.execute(stmt)
            user_orms = result.scalars().all()
            return [User.model_validate(user_orm) for user_orm in user_orms]


def build_user_repository(db: "AsyncSession") -> UserRepository:
    user_repo = UserRepository(db)
    return user_repo
