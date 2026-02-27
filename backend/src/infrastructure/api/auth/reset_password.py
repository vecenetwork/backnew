from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext

from app.exceptions import Missing, InvalidToken
from infrastructure.api.dependencies import user_service_dep


router = APIRouter()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class ResetRequest(BaseModel):
    email: EmailStr


@router.post("/password-reset-request")
async def password_reset_request(
    data: ResetRequest,
    background_tasks: BackgroundTasks,
    user_service: user_service_dep,
):
    try:
        user = await user_service.get_user_by_email(email=data.email)
    except Missing:
        return {
            "message": "If the email is registered, you will receive a password reset link."
        }

    background_tasks.add_task(
        user_service.verification.send_password_reset_email,
        user.email,
        user.name or user.username,
    )

    return {
        "message": "If the email is registered, you will receive a password reset link."
    }


class ResetPassword(BaseModel):
    token: str
    new_password: str


@router.post("/reset-password")
async def reset_password(
    data: ResetPassword,
    user_service: user_service_dep,
):
    try:
        await user_service.reset_password(
            token=data.token, new_password=data.new_password
        )
    except InvalidToken as e:
        raise HTTPException(status_code=400, detail=e.detail)
    except Missing:
        raise HTTPException(status_code=400, detail="User not found")

    return {"message": "Password reset successful"}
