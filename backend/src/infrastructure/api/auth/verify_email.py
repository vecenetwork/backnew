from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from app.exceptions import InvalidToken, Missing
from infrastructure.api.dependencies import user_service_dep

router = APIRouter()


class VerifyEmailResponse(BaseModel):
    message: str
    email: str


@router.get("/verify-email", response_model=VerifyEmailResponse)
async def verify_email(
    token: str,
    user_service: user_service_dep,
):
    try:
        email = await user_service.verify_user_email(token)
    except InvalidToken as e:
        raise HTTPException(status_code=400, detail=e.detail)
    except Missing:
        raise HTTPException(status_code=400, detail="User not found")

    return VerifyEmailResponse(message="Email verified successfully!", email=email)
