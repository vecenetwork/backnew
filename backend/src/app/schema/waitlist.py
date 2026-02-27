from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr

from app.schema.user import GenderEnum


class WaitlistData(BaseModel):
    country: str
    gender: GenderEnum
    birthday: date
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)