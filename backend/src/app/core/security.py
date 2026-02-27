import logging

from passlib.context import CryptContext
from passlib.exc import UnknownHashError

logger = logging.getLogger()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except UnknownHashError as e:
        logger.exception(e)
        return False
