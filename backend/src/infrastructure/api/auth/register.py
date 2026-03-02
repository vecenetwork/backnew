import logging
from urllib.parse import quote

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr

from app.exceptions import InvalidToken
from app.services.email.email import EmailSendError
from app.services.user import UserAlreadyExistsException
from infrastructure.api.dependencies import user_service_dep
from settings.general import FRONTEND_URL

logger = logging.getLogger(__name__)

router = APIRouter(tags=["auth"])


class RequestEmailBody(BaseModel):
    email: EmailStr
    username: str
    password: str


@router.post("/register/request-email", status_code=status.HTTP_200_OK)
async def request_registration_email(
    body: RequestEmailBody,
    service: user_service_dep,
):
    """User enters email, username, password. Sends activation link. No user created yet."""
    try:
        await service.request_email_activation(body.email, body.username, body.password)
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
    - Pending registration: create user, redirect to sign-in
    - Existing user (JWT): mark email verified, redirect to sign-in
    """
    try:
        # Try pending registration first (token from email link)
        try:
            username = await user_service.activate_from_pending(token)
            return RedirectResponse(
                url=f"{FRONTEND_URL}/sign-in?activated=1&username={quote(username)}",
                status_code=status.HTTP_302_FOUND,
            )
        except InvalidToken:
            pass  # Not a pending token, try JWT flow below
        except UserAlreadyExistsException:
            raise

        # JWT flow: existing user email verification
        email = await user_service.verify_token_for_redirect(token)
        user_exists = await user_service.email_registered(email)
        if user_exists:
            await user_service.verify_user_email(token)
            return RedirectResponse(
                url=f"{FRONTEND_URL}/sign-in?verified=1",
                status_code=status.HTTP_302_FOUND,
            )
        raise InvalidToken("Invalid or expired link")
    except UserAlreadyExistsException as e:
        e.raise_http_exception()
    except InvalidToken as e:
        raise HTTPException(status_code=400, detail=e.detail)
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail="Invalid or expired link")


