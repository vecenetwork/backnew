import logging
import os

import httpx
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.exceptions import InvalidToken
from infrastructure.api.dependencies import user_service_dep

logger = logging.getLogger(__name__)

router = APIRouter(tags=["auth"])

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")


async def verify_google_token(id_token: str) -> dict:
    """Verify Google ID token via Google's tokeninfo endpoint and return user info."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(
            "https://oauth2.googleapis.com/tokeninfo",
            params={"id_token": id_token},
        )
    if resp.status_code != 200:
        raise InvalidToken("Invalid Google token")
    data = resp.json()
    if GOOGLE_CLIENT_ID and data.get("aud") != GOOGLE_CLIENT_ID:
        raise InvalidToken("Token audience mismatch")
    if data.get("email_verified") != "true":
        raise InvalidToken("Google email not verified")
    return data


class GoogleLoginBody(BaseModel):
    id_token: str


@router.post("/auth/google", status_code=status.HTTP_200_OK)
async def google_login(
    body: GoogleLoginBody,
    user_service: user_service_dep,
):
    """Login or register via Google OAuth. Returns access_token + is_new_user flag."""
    try:
        google_info = await verify_google_token(body.id_token)
    except InvalidToken as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)
    except Exception as e:
        logger.exception("Google token verification failed: %s", e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Google token verification failed")

    try:
        result = await user_service.login_with_google(google_info)
        return result
    except Exception as e:
        logger.exception("Google login failed: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Google login failed. Please try again.",
        )
