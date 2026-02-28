import logging
from urllib.parse import quote

from datetime import date
from typing import Optional

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr

from app.exceptions import InvalidToken
from app.schema.user import UserResponse, GenderEnum
from app.services.user import UserAlreadyExistsException
from infrastructure.api.dependencies import user_service_dep
from settings.general import FRONTEND_URL

logger = logging.getLogger(__name__)

router = APIRouter(tags=["auth"])


class RequestEmailBody(BaseModel):
    email: EmailStr


class RegisterCompleteBody(BaseModel):
    email: EmailStr
    username: str
    password: str
    verification_token: str
    # Optional: country, birthday, gender — if not sent, defaults are used
    country_id: Optional[int] = None
    birthday: Optional[date] = None
    gender: Optional[GenderEnum] = None
    name: Optional[str] = None
    surname: Optional[str] = None


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
):
    """Step 2: After email activation, user submits username, password, and optionally country, birthday, gender."""
    try:
        new_user = await service.complete_registration(
            email=body.email,
            username=body.username,
            password=body.password,
            verification_token=body.verification_token,
            country_id=body.country_id,
            birthday=body.birthday,
            gender=body.gender,
            name=body.name,
            surname=body.surname,
        )
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
