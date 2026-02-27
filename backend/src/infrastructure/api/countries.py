from fastapi import APIRouter

from sqlalchemy import select

from app.orm.countries import CountryORM
from app.schema.countries import Country
from infrastructure.database import db_dependency

router = APIRouter(prefix="/countries", tags=["countries"])


@router.get("/", response_model=list[Country])
async def get_countries(db: db_dependency) -> list[Country]:
    stmt = select(CountryORM)
    async with db.begin():
        result = await db.execute(stmt)
    countries = result.scalars().all()
    return [Country.model_validate(country) for country in countries]
