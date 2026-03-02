import logging

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

from app.exceptions import InvalidToken
from app.services.email.email import EmailSendError
from app.services.user import UserAlreadyExistsException
from infrastructure.api.dependencies import user_service_dep

logger = logging.getLogger(__name__)

router = APIRouter(tags=["auth"])


class RequestEmailBody(BaseModel):
    email: EmailStr
    username: str
    password: str


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
    body: RequestEmailBody,
    service: user_service_dep,
):
    """Legacy: User enters email, username, password. Sends activation link."""
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
        logger.exception("Failed to send activation email: %s", e, exc_info=True)
        # Include error hint for debugging (e.g. missing table, Resend config)
        err_msg = str(e) if e else "Unknown error"
        detail = f"Failed to send activation email: {err_msg}"
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class ActivateTokenBody(BaseModel):
    token: str


@router.post("/register/activate", status_code=status.HTTP_200_OK)
async def activate_email(
    body: ActivateTokenBody,
    service: user_service_dep,
):
    """Activate from pending registration. Returns username. Called by frontend when user lands with ?token= in URL."""
    try:
        username = await service.activate_from_pending(body.token)
        return {"username": username}
    except UserAlreadyExistsException as e:
        e.raise_http_exception()
    except InvalidToken as e:
        raise HTTPException(status_code=400, detail=e.detail)


