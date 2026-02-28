import logging
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from infrastructure.database import db

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: "FastAPI"):
    try:
        await db.check_connection()
    except Exception as e:
        logger.exception("Database connection failed on startup: %s", e)
        raise
    yield
    await db.dispose()
