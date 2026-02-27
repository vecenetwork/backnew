from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.exceptions import Missing
from app.orm.user import UserSettingsORM, UserORM
from app.schema.user import UserSettings, UserSettingsUpdate


class UserSettingsRepository:
    """Handles database operations related to UserSettings."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_settings_by_user_id(self, user_id: int) -> UserSettings:
        """Retrieve a user's settings, raise if not found."""
        stmt = select(UserSettingsORM).where(UserSettingsORM.user_id == user_id)
        result = await self.db.execute(stmt)
        settings = result.scalars().first()
        if not settings:
            raise Missing("User settings not found")
        return UserSettings.model_validate(settings)

    async def create_settings(
        self, user_id: int, settings_data: UserSettings
    ) -> UserSettings:
        """Create settings for a user, raise if settings already exist."""
        # Ensure user exists
        stmt = select(UserORM).where(UserORM.id == user_id)
        result = await self.db.execute(stmt)
        user = result.scalars().first()
        if not user:
            raise Missing("User not found")

        # Check if settings already exist
        stmt_settings = select(UserSettingsORM).where(
            UserSettingsORM.user_id == user_id
        )
        result = await self.db.execute(stmt_settings)
        existing_settings = result.scalars().first()
        if existing_settings:
            raise Missing("User settings already exist")

        new_settings = UserSettingsORM(user_id=user_id, **settings_data.dict())
        self.db.add(new_settings)
        await self.db.flush()
        await self.db.commit()
        return UserSettings.model_validate(new_settings)

    async def update_settings(
        self, user_id: int, settings_data: UserSettingsUpdate
    ) -> UserSettings:
        """Update user settings, raise if not found."""
        stmt = select(UserSettingsORM).where(UserSettingsORM.user_id == user_id)
        result = await self.db.execute(stmt)
        settings = result.scalars().first()
        if not settings:
            raise Missing("User settings not found")

        for field, value in settings_data.dict(exclude_unset=True).items():
            setattr(settings, field, value)
        await self.db.flush()
        await self.db.commit()
        return UserSettings.model_validate(settings)

    async def delete_settings(self, user_id: int) -> None:
        """Delete user settings, raise if not found."""
        stmt = select(UserSettingsORM).where(UserSettingsORM.user_id == user_id)
        result = await self.db.execute(stmt)
        settings = result.scalars().first()
        if not settings:
            raise Missing("User settings not found")

        await self.db.delete(settings)
        await self.db.commit()


def build_user_settings_repository(db: "AsyncSession") -> UserSettingsRepository:
    repo = UserSettingsRepository(db)
    return repo
