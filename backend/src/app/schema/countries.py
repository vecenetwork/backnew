from pydantic import BaseModel, ConfigDict


class Country(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
