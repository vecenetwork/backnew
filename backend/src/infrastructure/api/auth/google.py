import logging
import os

import httpx
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.exceptions import InvalidToken
from app.schema.subscriptions import SubscriptionTypeEnum
from infrastructure.api.dependencies import (
    user_service_dep,
    subscription_service_dep,
    answer_service_dep,
)
from infrastructure.api.auth.register import DemoAnswerItem, DemoDataBody

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
    demo_data: DemoDataBody | None = Field(default=None, description="Optional demo data to apply for new users")


@router.post("/auth/google", status_code=status.HTTP_200_OK)
async def google_login(
    body: GoogleLoginBody,
    user_service: user_service_dep,
    subscription_service: subscription_service_dep,
    answer_service: answer_service_dep,
):
    """Login or register via Google OAuth. Returns access_token + is_new_user flag.
    If demo_data is provided and user is new, applies hashtag subscriptions and answers."""
    try:
        google_info = await verify_google_token(body.id_token)
    except InvalidToken as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)
    except Exception as e:
        logger.exception("Google token verification failed: %s", e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Google token verification failed")

    try:
        result = await user_service.login_with_google(google_info)
    except Exception as e:
        logger.exception("Google login failed: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Google login failed. Please try again.",
        )

    # Apply demo data only for brand-new users when demo_data is provided
    if result.get("is_new_user") and body.demo_data:
        demo = body.demo_data
        # We need the User object — re-fetch using the issued token
        try:
            new_user = await user_service.get_current_user(result["access_token"])
        except Exception as e:
            logger.warning("Could not fetch new Google user for demo migration: %s", e)
            return result

        # Subscribe to hashtags
        for hashtag_id in demo.hashtag_ids:
            try:
                is_fav = hashtag_id in demo.favourite_hashtag_ids
                await subscription_service.subscribe(
                    new_user, hashtag_id, SubscriptionTypeEnum.hashtag, favourite=is_fav
                )
            except Exception as e:
                logger.warning("Demo migration (Google): failed to subscribe hashtag %s: %s", hashtag_id, e)

        # Set favourites for any that weren't set on subscribe
        for hashtag_id in demo.favourite_hashtag_ids:
            if hashtag_id not in demo.hashtag_ids:
                continue
            try:
                await subscription_service.set_favorite(
                    new_user, hashtag_id, SubscriptionTypeEnum.hashtag, True
                )
            except Exception as e:
                logger.warning("Demo migration (Google): failed to set favourite %s: %s", hashtag_id, e)

        # Create answers
        if demo.answers:
            answers_data = [
                {"question_id": a.question_id, "option_ids": a.option_ids}
                for a in demo.answers
            ]
            try:
                await answer_service.create_answers_for_demo_migration(new_user, answers_data)
            except Exception as e:
                logger.warning("Demo migration (Google): failed to create answers: %s", e)

    return result
