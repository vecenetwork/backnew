import logging
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

from app.exceptions import InvalidToken
from settings.security import SECRET_KEY

ALGORITHM = "HS256"


def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + expires_delta})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        raise InvalidToken(msg="Token expired")
    except jwt.exceptions.InvalidSignatureError:
        raise InvalidToken(msg="Token could not be validated")
    except jwt.exceptions.InvalidTokenError as e:
        logging.exception(e)
        raise InvalidToken(msg="Invalid token")


def get_username_from_token(token: str) -> str:
    """Return username from JWT access <token>"""
    payload = verify_token(token)
    if not (username := payload.get("sub")):
        raise InvalidToken(msg="Could not get username from jwt token")
    return username


def get_email_from_token(token: str) -> str:
    payload = verify_token(token)
    if not (email := payload.get("sub")):
        raise InvalidToken(msg="Could not get email from jwt token")
    return email
