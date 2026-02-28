import logging
from urllib.parse import quote

from datetime import date
from typing import Optional

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr

from app.exceptions import InvalidToken
from app.schema.user import UserResponse, GenderEnum
from app.schema.subscriptions import SubscriptionTypeEnum
from app.services.email.email import EmailSendError
from app.services.user import UserAlreadyExistsException
from infrastructure.api.dependencies import (
    user_service_dep,
    subscription_service_dep,
    answer_service_dep,
)
from settings.general import FRONTEND_URL

logger = logging.getLogger(__name__)

router = APIRouter(tags=["auth"])


class RequestEmailBody(BaseModel):
    email: EmailStr


class DemoAnswerItem(BaseModel):
    question_id: int
    option_ids: list[int] = []


class DemoData(BaseModel):
    hashtag_ids: list[int] = []
    favourite_hashtag_ids: list[int] = []  # Subset of hashtag_ids to mark as favourite
    answers: list[DemoAnswerItem] = []


class RegisterCompleteBody(BaseModel):
    email: EmailStr
    password: str
    verification_token: str
    country_id: int
    birthday: date
    gender: GenderEnum
    name: Optional[str] = None
    surname: Optional[str] = None
    demo_data: Optional[DemoData] = None


@router.post("/register/request-email", status_code=status.HTTP_200_OK)
async def request_registration_email(
    body: RequestEmailBody,
    service: user_service_dep,
):
    """Step 1: User enters email. Sends activation link. No user created yet."""
    try:
        await service.request_email_activation(body.email)
        return {"message": "Activation email sent. Check your inbox."}
    except UserAlreadyExistsException as e:
        e.raise_http_exception()
    except EmailSendError as e:
        logger.exception("Email send failed: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Email service error: {e}",
        )
    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send activation email",
        )


@router.get("/verify-email")
async def verify_email_redirect(
    token: str,
    user_service: user_service_dep,
):
    """
    Validates token and either:
    - If user exists: marks email verified, redirects to frontend
    - If no user (registration flow): redirects to sign-up with email and token
    """
    try:
        email = await user_service.verify_token_for_redirect(token)
        user_exists = await user_service.email_registered(email)
        if user_exists:
            await user_service.verify_user_email(token)
            # Redirect to sign-in
            return RedirectResponse(
                url=f"{FRONTEND_URL}/sign-in?verified=1",
                status_code=status.HTTP_302_FOUND,
            )
        # Registration flow: redirect to sign-up with email and token
        return RedirectResponse(
            url=f"{FRONTEND_URL}/sign-up?email={quote(email)}&token={quote(token)}",
            status_code=status.HTTP_302_FOUND,
        )
    except InvalidToken as e:
        raise HTTPException(status_code=400, detail=e.detail)
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail="Invalid or expired link")


@router.post("/register/complete", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def complete_registration(
    body: RegisterCompleteBody,
    service: user_service_dep,
    subscription_service: subscription_service_dep,
    answer_service: answer_service_dep,
):
    """Step 2: After email activation, user submits password, country, birthday, gender. Username is auto-generated.
    Optional demo_data migrates demo hashtags and answers into the new account."""
    try:
        new_user = await service.complete_registration(
            email=body.email,
            password=body.password,
            verification_token=body.verification_token,
            country_id=body.country_id,
            birthday=body.birthday,
            gender=body.gender,
            name=body.name,
            surname=body.surname,
        )
        if body.demo_data:
            favourite_ids = set(body.demo_data.favourite_hashtag_ids or [])
            for hashtag_id in set(body.demo_data.hashtag_ids):
                try:
                    await subscription_service.subscribe(
                        new_user, hashtag_id, SubscriptionTypeEnum.hashtag,
                        favourite=hashtag_id in favourite_ids,
                    )
                except Exception as e:
                    logger.warning("Demo migration: failed to subscribe to hashtag %s: %s", hashtag_id, e)
            if body.demo_data.answers:
                try:
                    await answer_service.create_answers_for_demo_migration(
                        new_user,
                        [{"question_id": a.question_id, "option_ids": a.option_ids} for a in body.demo_data.answers],
                    )
                except Exception as e:
                    logger.exception("Demo migration: failed to migrate answers: %s", e)
        return UserResponse.from_user(new_user)
    except UserAlreadyExistsException as e:
        e.raise_http_exception()
    except InvalidToken as e:
        raise HTTPException(status_code=400, detail=e.detail)
    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed",
        )
