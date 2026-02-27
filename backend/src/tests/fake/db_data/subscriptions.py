from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from datetime import datetime

from app.orm.subscriptions import SubscriptionORM


def populate_subscriptions(db_url: str, user_ids: list, hashtag_ids: list):
    """Populates the subscriptions table with user and hashtag subscriptions."""

    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    subscriptions_data = []

    for user_id in user_ids:
        # Hashtag subscriptions
        subscribed_hashtags = random.sample(hashtag_ids, 50)
        favorite_hashtags = random.sample(subscribed_hashtags, 10)

        for hashtag_id in subscribed_hashtags:
            subscriptions_data.append({
                "subscriber_id": user_id,
                "subscribed_to_id": hashtag_id,
                "subscribed_to_type": "hashtag",
                "favourite": hashtag_id in favorite_hashtags,
                "created_at": datetime.utcnow()
            })

        # User subscriptions
        other_users = [u_id for u_id in user_ids if u_id != user_id]
        subscribed_users = random.sample(other_users, min(20, len(other_users))) # prevent error if there are less than 20 users.

        for subscribed_user_id in subscribed_users:
            subscriptions_data.append({
                "subscriber_id": user_id,
                "subscribed_to_id": subscribed_user_id,
                "subscribed_to_type": "user",
                "favourite": False,
                "created_at": datetime.utcnow()
            })

    db.bulk_save_objects([SubscriptionORM(**sub) for sub in subscriptions_data])
    db.commit()
    db.close()

