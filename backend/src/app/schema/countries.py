from pydantic import BaseModel, ConfigDict, computed_field


class Country(BaseModel):
    id: int
    name: str

    @computed_field
    @property
    def value(self) -> int:
        return self.id

    model_config = ConfigDict(from_attributes=True)
