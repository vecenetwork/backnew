import logging
from typing import Annotated, AsyncGenerator, Optional

from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from settings import pg
from settings import sql_alchemy

logger = logging.getLogger(__name__)


def _get_database_url() -> str:
    """Build DATABASE_URL and validate required env vars."""
    required = {
        "POSTGRES_USER": pg.POSTGRES_USER,
        "POSTGRES_PASSWORD": pg.POSTGRES_PASSWORD,
        "POSTGRES_HOST": pg.POSTGRES_HOST,
        "POSTGRES_PORT": pg.POSTGRES_PORT,
        "POSTGRES_DB": pg.POSTGRES_DB,
    }
    missing = [k for k, v in required.items() if not v]
    if missing:
        raise RuntimeError(
            f"Missing required env vars in Railway Variables: {', '.join(missing)}. "
            "Add them in Railway → backnew → Variables."
        )
    return f"postgresql+asyncpg://{pg.POSTGRES_USER}:{pg.POSTGRES_PASSWORD}@{pg.POSTGRES_HOST}:{pg.POSTGRES_PORT}/{pg.POSTGRES_DB}"


class Base(DeclarativeBase):
    pass


class Database:
    DATABASE_URL = _get_database_url()

    def __init__(self, database_url: Optional[str] = None):
        self.engine = create_async_engine(
            database_url or self.DATABASE_URL,
            pool_size=30,
            max_overflow=10,
            pool_recycle=3600,
            future=True,
            echo=sql_alchemy.SQLALCHEMY_ECHO,
        )
        self.async_session_maker = async_sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )
        self._connection_repr: str = (
            f"{pg.POSTGRES_USER}@{pg.POSTGRES_HOST}:{pg.POSTGRES_PORT}/{pg.POSTGRES_DB}"
        )

    async def check_connection(self):
        try:
            async with self.engine.connect() as connection:
                result = await connection.execute(text("SELECT 1"))
                if result.scalar() == 1:
                    logger.info(
                        f"Database connection successful {self._connection_repr}"
                    )
                else:
                    logger.error(
                        f"Database connection check failed  {self._connection_repr}."
                    )
        except Exception as e:
            logger.error(f"Database connection error  {self._connection_repr}: {e}")
            raise

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session_maker() as session:
            yield session

    async def dispose(self):
        await self.engine.dispose()
        logger.info("Database connection closed")


db = Database()
db_dependency = Annotated[AsyncSession, Depends(db.get_session)]
