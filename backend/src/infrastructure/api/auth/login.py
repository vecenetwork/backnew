from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.exceptions import Missing, WrongPassword
from infrastructure.api.auth.jwt_utils import create_token

from app.schema.token import Token
from infrastructure.api.dependencies import user_service_dep
from settings.security import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


class LoginForm(BaseModel):
    """
    possible usage
    form_data: Annotated[LoginForm, Depends()],
    """

    username_or_imail: str
    password: str


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: user_service_dep,
) -> Token:
    """Login user and generate an access token."""
    try:
        user = await user_service.authenticate_user(
            form_data.username, form_data.password
        )
    except (Missing, WrongPassword):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username/email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Email not verified. Please verify your email.",
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
