from datetime import timedelta

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.orm.barrier_token import BarrierTokenORM
from infrastructure.api.auth.jwt_utils import create_token
from infrastructure.database import db_dependency

router = APIRouter()


@router.get("/barrier/{invitation_code}")
async def validate_invitation_code(invitation_code: str, db: db_dependency):
    query = select(BarrierTokenORM).where(BarrierTokenORM.token == invitation_code)
    result = await db.execute(query)
    token = result.scalar_one_or_none()

    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid invitation code"
        )

    data = {"invitation_code": invitation_code}
    expires = timedelta(minutes=60)
    token_str = create_token(data, expires)

    return {"access_token": token_str, "token_type": "bearer"}
