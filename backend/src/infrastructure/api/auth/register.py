import logging

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, field_validator

from app.exceptions import InvalidToken
from app.schema.subscriptions import SubscriptionTypeEnum
from app.services.email.email import EmailSendError
from app.services.user import UserAlreadyExistsException
from infrastructure.api.dependencies import (
    user_service_dep,
    subscription_service_dep,
    answer_service_dep,
)

logger = logging.getLogger(__name__)

router = APIRouter(tags=["auth"])


class RequestEmailBody(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")


class RequestEmailOnlyBody(BaseModel):
    email: EmailStr


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    body: RequestEmailBody,
    service: user_service_dep,
):
    """Create user immediately. Email, username, password. No activation required."""
    try:
        await service.register_user_direct(body.email, body.username, body.password)
        return {"message": "Account created. Sign in with your username and password."}
    except UserAlreadyExistsException as e:
        e.raise_http_exception()
    except Exception as e:
        logger.exception("Registration failed: %s", e, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e) or "Registration failed",
        )


@router.post("/register/request-email", status_code=status.HTTP_200_OK)
async def request_registration_email(
    body: RequestEmailOnlyBody,
    service: user_service_dep,
):
    """User enters email. Sends 6-digit activation code."""
    try:
        await service.request_email_activation(body.email)
        return {"message": "Activation code sent. Check your email."}
    except UserAlreadyExistsException as e:
        e.raise_http_exception()
    except EmailSendError as e:
        logger.exception("Email send failed: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Email service error: {e}",
        )
    except Exception as e:
        logger.exception("Failed to send activation email: %s", e, exc_info=True)
        # Include error hint for debugging (e.g. missing table, Resend config)
        err_msg = str(e) if e else "Unknown error"
        detail = f"Failed to send activation email: {err_msg}"
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class ActivateCodeBody(BaseModel):
    code: str = Field(..., min_length=6, max_length=6, description="6-digit activation code from email")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")

    @field_validator("code", mode="before")
    @classmethod
    def normalize_code(cls, v):
        """Preserve leading zeros: frontend may send code as number (34120 → 034120)."""
        if isinstance(v, int):
            return str(v).zfill(6)
        if isinstance(v, str):
            return v.strip()
        return v


@router.post("/register/activate", status_code=status.HTTP_200_OK)
async def activate_email(
    body: ActivateCodeBody,
    service: user_service_dep,
):
    """Activate from pending (email-only signup). Creates user, returns access_token."""
    try:
        result = await service.activate_from_pending(body.code, body.password)
        return result
    except UserAlreadyExistsException as e:
        e.raise_http_exception()
    except InvalidToken as e:
        raise HTTPException(status_code=400, detail=e.detail)
    except Exception as e:
        logger.exception("Activation failed: %s", e, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Activation failed. Please try again or contact support.",
        )


class DemoAnswerItem(BaseModel):
    question_id: int
    option_ids: list[int]


class DemoDataBody(BaseModel):
    hashtag_ids: list[int] = Field(default_factory=list, description="Hashtag IDs to subscribe to")
    favourite_hashtag_ids: list[int] = Field(default_factory=list, description="Hashtag IDs to mark as favourite")
    answers: list[DemoAnswerItem] = Field(default_factory=list, description="Question answers")


class ActivateWithDemoBody(BaseModel):
    code: str = Field(..., min_length=6, max_length=6, description="6-digit activation code")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")
    demo_data: DemoDataBody = Field(default_factory=DemoDataBody)

    @field_validator("code", mode="before")
    @classmethod
    def normalize_code(cls, v):
        if isinstance(v, int):
            return str(v).zfill(6)
        if isinstance(v, str):
            return v.strip()
        return v


@router.post("/register/activate-with-demo", status_code=status.HTTP_200_OK)
async def activate_with_demo(
    body: ActivateWithDemoBody,
    user_service: user_service_dep,
    subscription_service: subscription_service_dep,
    answer_service: answer_service_dep,
):
    """Activate from pending and apply demo data (subscriptions, favourites, answers). For demo flow."""
    try:
        result, new_user = await user_service._activate_from_pending_internal(
            body.code, body.password
        )
        demo = body.demo_data

        # Subscribe to hashtags (favourites first so we can set favourite on subscribe)
        for hashtag_id in demo.hashtag_ids:
            try:
                is_fav = hashtag_id in demo.favourite_hashtag_ids
                await subscription_service.subscribe(
                    new_user, hashtag_id, SubscriptionTypeEnum.hashtag, favourite=is_fav
                )
            except Exception as e:
                logger.warning("Demo migration: failed to subscribe to hashtag %s: %s", hashtag_id, e)

        # Set favourites for any that weren't set on subscribe (e.g. already subscribed)
        for hashtag_id in demo.favourite_hashtag_ids:
            if hashtag_id not in demo.hashtag_ids:
                continue
            try:
                await subscription_service.set_favorite(
                    new_user, hashtag_id, SubscriptionTypeEnum.hashtag, True
                )
            except Exception as e:
                logger.warning("Demo migration: failed to set favourite %s: %s", hashtag_id, e)

        # Create answers
        if demo.answers:
            answers_data = [
                {"question_id": a.question_id, "option_ids": a.option_ids}
                for a in demo.answers
            ]
            await answer_service.create_answers_for_demo_migration(new_user, answers_data)

        return result
    except UserAlreadyExistsException as e:
        e.raise_http_exception()
    except InvalidToken as e:
        raise HTTPException(status_code=400, detail=e.detail)
    except Exception as e:
        logger.exception("Activation with demo failed: %s", e, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Activation failed. Please try again or contact support.",
        )


