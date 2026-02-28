import logging
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import psycopg2
from infrastructure.database import db
from settings import pg as pg_settings

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = logging.getLogger(__name__)

# Миграции, которые нужно применить при старте (idempotent)
_STARTUP_MIGRATIONS = [
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS social_link VARCHAR(255)",
]


def _run_startup_migrations():
    host = pg_settings.POSTGRES_HOST
    port = int(pg_settings.POSTGRES_PORT or 5432)
    if host and "pooler" in host:
        port = 5432  # session mode для DDL
    if not all([host, pg_settings.POSTGRES_USER, pg_settings.POSTGRES_PASSWORD, pg_settings.POSTGRES_DB]):
        return
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=pg_settings.POSTGRES_USER,
            password=pg_settings.POSTGRES_PASSWORD,
            dbname=pg_settings.POSTGRES_DB,
        )
        conn.autocommit = True
        try:
            with conn.cursor() as cur:
                for sql in _STARTUP_MIGRATIONS:
                    cur.execute(sql)
            logger.info("Startup migrations applied")
        finally:
            conn.close()
    except Exception as e:
        logger.warning("Startup migrations skipped: %s", e)


@asynccontextmanager
async def lifespan(app: "FastAPI"):
    _run_startup_migrations()
    try:
        await db.check_connection()
    except Exception as e:
        logger.exception("Database connection failed on startup: %s", e)
        raise
    yield
    await db.dispose()
