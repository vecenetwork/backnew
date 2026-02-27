import logging

from sqlalchemy.dialects import postgresql

default_logger = logging.getLogger()


def log_query(stmt, logger: logging.Logger | None = None):
    logger = logger or default_logger
    try:
        compiled = stmt.compile(dialect=postgresql.dialect())
        logger.info(f"DEBUG SQL QUERY: {compiled}")
        logger.info(f"DEBUG SQL PARAMS: {compiled.params}")
    except Exception as e:
        logger.warning(f"Failed to log query: {e}")
