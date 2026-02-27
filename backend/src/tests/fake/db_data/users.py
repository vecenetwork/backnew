from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import datetime, timedelta
import random
from typing import List

from app.orm.user import UserORM, UserSettingsORM

# Default test user for local dev (password: testpass123)
TESTUSER_PASSWORD_HASH = "$2b$12$pAzELgYyuJfxGI1KeU038uQzBk5KyNFeX08eBabOPL0aUkRyWIPjS"


def populate_users(db_url: str, num_users: int, countries: List[int]):
    """Populates the users and user settings tables."""

    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    fake = Faker()

    users_data = []
    settings_data = []

    # Always add default test user first (login: testuser, password: testpass123)
    if countries:
        users_data.append({
            "name": "Test",
            "surname": "User",
            "username": "testuser",
            "email": "testuser@test.com",
            "password_hash": TESTUSER_PASSWORD_HASH,
            "birthday": datetime(1990, 1, 1).date(),
            "country_id": countries[0],
            "gender": "Other",
            "is_verified": True,
            "is_active": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "description": "",
            "profile_picture": None,
            "role": "user",
        })

    for _ in range(num_users):
        birthday = fake.date_between(start_date="-80y", end_date="-18y")
        random_date = lambda: birthday + timedelta(days=random.randint(0, 365))  # noqa: E731
        user_data = {
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "password_hash": '$2b$12$epcxENsCrlhnCgdgjP6pn.Xgm4btC9p0Qz1px58rpAo8QsyRnAxVm',
            "birthday": birthday,
            "country_id": random.choice(countries),
            "gender": random.choice(["Male", "Female", "Other"]),
            "is_verified": True,
            "is_active": True,
            "created_at": random_date(),
            "updated_at": random_date(),
            "description": fake.text(),
            "profile_picture": fake.image_url(),
            "role": "user",
        }
        users_data.append(user_data)

    db.bulk_save_objects([UserORM(**user) for user in users_data])
    db.commit()

    user_ids = [user.id for user in db.query(UserORM).all()]

    for user_id in user_ids:
        settings_data.append({
            "user_id": user_id,
            "show_name_option": random.choice(["Name", "Username"]),
            "show_question_results": random.choice(['Nobody', 'People I Follow', 'People Following Me', 'All Connections', 'All']),
            "allow_results_in_digests": fake.boolean(),
            "receive_digests": fake.boolean(),
        })

    db.bulk_save_objects([UserSettingsORM(**setting) for setting in settings_data])
    db.commit()
    db.close()