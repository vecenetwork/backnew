from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from infrastructure.database import db

if TYPE_CHECKING:
    from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: "FastAPI"):
    await db.check_connection()
    yield
    await db.dispose()
