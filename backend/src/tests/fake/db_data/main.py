"""
docker exec -it vece-backend-1 bash -c "source .venv/bin/activate && python3 -c 'from tests.fake.db_data.main import populate_database; populate_database(50)'"
"""

import logging

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.orm.countries import CountryORM
from app.orm.hashtags import HashtagORM
from app.orm.user import UserORM
from tests.fake.db_data.questions import populate_questions_answers
from tests.fake.db_data.subscriptions import populate_subscriptions
from tests.fake.db_data.users import populate_users, TESTUSER_PASSWORD_HASH

from settings import pg

logger = logging.getLogger()


def ensure_testuser():
    """Creates default test user (testuser / testpass123) if not present. Safe to run multiple times."""
    from datetime import datetime
    from app.orm.user import UserORM, UserSettingsORM
    from app.schema.user import ShowNameOptionEnum, ShowQuestionResultsEnum, GenderEnum, Role

    db_url = f"postgresql://{pg.POSTGRES_USER}:{pg.POSTGRES_PASSWORD}@{pg.POSTGRES_HOST}:{pg.POSTGRES_PORT}/{pg.POSTGRES_DB}"
    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    if db.query(UserORM).filter(UserORM.username == "testuser").first():
        logger.info("testuser already exists")
        db.close()
        return

    country = db.query(CountryORM).first()
    if not country:
        logger.warning("No countries in DB; run migrations and seed countries first.")
        db.close()
        return

    user = UserORM(
        name="Test",
        surname="User",
        username="testuser",
        email="testuser@test.com",
        password_hash=TESTUSER_PASSWORD_HASH,
        birthday=datetime(1990, 1, 1).date(),
        country_id=country.id,
        gender=GenderEnum.other,
        is_verified=True,
        is_active=True,
        description=None,
        profile_picture=None,
        role=Role.user,
    )
    db.add(user)
    db.flush()
    settings = UserSettingsORM(
        user_id=user.id,
        show_name_option=ShowNameOptionEnum.name,
        show_question_results=ShowQuestionResultsEnum.all,
        allow_results_in_digests=True,
        receive_digests=False,
    )
    db.add(settings)
    db.commit()
    logger.info("Created testuser (password: testpass123)")
    db.close()


def ensure_vece_user():
    """Creates or updates VECE user (username: vece, password: testpass123). Sets is_verified=True, is_active=True."""
    from datetime import datetime
    from app.orm.user import UserORM, UserSettingsORM
    from app.schema.user import ShowNameOptionEnum, ShowQuestionResultsEnum, GenderEnum, Role

    db_url = f"postgresql://{pg.POSTGRES_USER}:{pg.POSTGRES_PASSWORD}@{pg.POSTGRES_HOST}:{pg.POSTGRES_PORT}/{pg.POSTGRES_DB}"
    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    country = db.query(CountryORM).first()
    if not country:
        logger.warning("No countries in DB; run migrations and seed countries first.")
        db.close()
        return

    existing = db.query(UserORM).filter(UserORM.username == "vece").first()
    if existing:
        existing.is_verified = True
        existing.is_active = True
        db.commit()
        logger.info("Updated vece user (is_verified=True, is_active=True)")
        db.close()
        return

    user = UserORM(
        name="VECE",
        surname="Official",
        username="vece",
        email="vece@vece.ai",
        password_hash=TESTUSER_PASSWORD_HASH,
        birthday=datetime(1990, 1, 1).date(),
        country_id=country.id,
        gender=GenderEnum.other,
        is_verified=True,
        is_active=True,
        description=None,
        profile_picture=None,
        role=Role.user,
    )
    db.add(user)
    db.flush()
    settings = UserSettingsORM(
        user_id=user.id,
        show_name_option=ShowNameOptionEnum.name,
        show_question_results=ShowQuestionResultsEnum.all,
        allow_results_in_digests=True,
        receive_digests=False,
    )
    db.add(settings)
    db.commit()
    logger.info("Created vece user (username: vece, password: testpass123)")
    db.close()


def populate_database(num_users: int):
    """Populates the database with users, subscriptions, questions, and answers."""

    db_url = f"postgresql://{pg.POSTGRES_USER}:{pg.POSTGRES_PASSWORD}@{pg.POSTGRES_HOST}:{pg.POSTGRES_PORT}/{pg.POSTGRES_DB}"
    logger.info("started populating database")
    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    db.execute(text("INSERT INTO barrier_tokens VALUES ('vecetest')"))
    db.commit()

    # Get existing country and hashtag ids
    country_ids = [country.id for country in db.query(CountryORM).all()]
    hashtag_ids = [hashtag.id for hashtag in db.query(HashtagORM).all()]

    db.close()

    # 1. Populate users and user settings
    populate_users(db_url, num_users, country_ids)
    logger.info("Added_users")

    # Recreate session to get fresh user ids
    db = SessionLocal()
    user_ids = [user.id for user in db.query(UserORM).all()]
    db.close()

    # 2. Populate subscriptions
    populate_subscriptions(db_url, user_ids, hashtag_ids)
    logger.info("Added subscriptions")

    # 3. Populate questions and answers
    populate_questions_answers(db_url, user_ids, hashtag_ids)
    logger.info("Added questions and answers")

    logger.info("Database population complete.")
