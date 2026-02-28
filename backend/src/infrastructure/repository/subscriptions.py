from typing import TYPE_CHECKING, Optional, List

from sqlalchemy import select, and_, func
from sqlalchemy.orm import selectinload

from app.exceptions import Missing, InvalidFavoriteOperation, MaxFavoritesReached
from app.orm.subscriptions import SubscriptionORM
from app.orm.user import UserORM
from app.orm.hashtags import HashtagORM
from app.schema.subscriptions import SubscriptionResponse, SubscriptionTypeEnum, UserSubscriptionsResponse, UserSubscription, HashtagSubscription

from app.schema.user import User, UserResponse
from app.schema.hashtags import Hashtag

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class SubscriptionRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    async def get_following_ids(self, user_id: int) -> List[int]:
        """Get IDs of users that the given user follows."""
        stmt = select(SubscriptionORM.subscribed_to_id).where(
            and_(
                SubscriptionORM.subscriber_id == user_id,
                SubscriptionORM.subscribed_to_type == 'user'
            )
        )
        result = await self.db.execute(stmt)
        return [row[0] for row in result]

    async def get_follower_ids(self, user_id: int) -> List[int]:
        """Get IDs of users that follow the given user."""
        stmt = select(SubscriptionORM.subscriber_id).where(
            and_(
                SubscriptionORM.subscribed_to_id == user_id,
                SubscriptionORM.subscribed_to_type == 'user'
            )
        )
        result = await self.db.execute(stmt)
        return [row[0] for row in result]

    async def get_non_connected_user_ids(self, user_id: int) -> List[int]:
        """Get IDs of users that are neither following nor followed by the given user."""
        # Get all users that are either following or being followed by the user
        connected_users = select(SubscriptionORM.subscriber_id).where(
            and_(
                SubscriptionORM.subscribed_to_id == user_id,
                SubscriptionORM.subscribed_to_type == 'user'
            )
        ).union(
            select(SubscriptionORM.subscribed_to_id).where(
                and_(
                    SubscriptionORM.subscriber_id == user_id,
                    SubscriptionORM.subscribed_to_type == 'user'
                )
            )
        )

        # Get all users except the connected ones and the user themselves
        stmt = select(UserORM.id).where(
            and_(
                UserORM.id != user_id,
                ~UserORM.id.in_(connected_users)
            )
        )
        result = await self.db.execute(stmt)
        return [row[0] for row in result]

    async def subscribe(
        self, user: "User", subscribed_to_id: int, subscription_type: SubscriptionTypeEnum, favourite: bool = False
    ) -> SubscriptionResponse:
        # TODO: add duplicate handling 409

        if favourite and subscription_type == SubscriptionTypeEnum.hashtag:
            result = await self.db.execute(
                select(func.count())
                .select_from(SubscriptionORM)
                .where(
                    SubscriptionORM.subscriber_id == user.id,
                    SubscriptionORM.subscribed_to_type == SubscriptionTypeEnum.hashtag,
                    SubscriptionORM.favourite == True,  # noqa: E712
                )
            )
            current: int = result.scalar_one()  # type: ignore[assignment]
            if current >= 8:
                raise MaxFavoritesReached(8)

        new_subscription = SubscriptionORM(
            subscriber_id=user.id,
            subscribed_to_id=subscribed_to_id,
            subscribed_to_type=subscription_type,
            favourite=favourite,
        )

        self.db.add(new_subscription)
        await self.db.commit()
        await self.db.refresh(new_subscription)
        return SubscriptionResponse.model_validate(new_subscription)

    async def unsubscribe(
        self, user: "User", subscribed_to_id: int, subscription_type: SubscriptionTypeEnum
    ):
        # TODO: it would be better to delete just by id

        result = await self.db.execute(
            select(SubscriptionORM).filter_by(
                subscriber_id=user.id,
                subscribed_to_id=subscribed_to_id,
                subscribed_to_type=subscription_type,
            )
        )
        subscription = result.scalar_one_or_none()

        if not subscription:
            raise Missing("Subscription not found")

        await self.db.delete(subscription)
        await self.db.commit()

    async def get_user_subscriptions(
        self,
        user_id: int,
        subscription_type: Optional[SubscriptionTypeEnum] = None,
    ) -> UserSubscriptionsResponse:
        """Get all subscriptions for a user.

        Args:
            user_id: The ID of the user whose subscriptions to get
            subscription_type: Optional filter for subscription type ('user' or 'hashtag')
        """
        # Base query for all subscriptions
        base_stmt = select(SubscriptionORM).where(SubscriptionORM.subscriber_id == user_id)

        # Get user subscriptions
        user_subs = []
        if subscription_type is None or subscription_type == SubscriptionTypeEnum.user:
            user_stmt = base_stmt.where(SubscriptionORM.subscribed_to_type == SubscriptionTypeEnum.user)
            user_stmt = user_stmt.outerjoin(
                UserORM,
                and_(
                    SubscriptionORM.subscribed_to_id == UserORM.id,
                    SubscriptionORM.subscribed_to_type == SubscriptionTypeEnum.user
                )
            ).options(selectinload(SubscriptionORM.subscribed_user))

            result = await self.db.execute(user_stmt)
            user_subscriptions = result.scalars().all()
            user_subs = [
                UserSubscription(
                    id=sub.id,
                    user=UserResponse.from_user_other(User.model_validate(sub.subscribed_user)),
                    favourite=sub.favourite
                )
                for sub in user_subscriptions
                if sub.subscribed_user is not None  # Skip if user was deleted
            ]

        # Get hashtag subscriptions
        hashtag_subs = []
        if subscription_type is None or subscription_type == SubscriptionTypeEnum.hashtag:
            hashtag_stmt = base_stmt.where(SubscriptionORM.subscribed_to_type == SubscriptionTypeEnum.hashtag)
            hashtag_stmt = hashtag_stmt.outerjoin(
                HashtagORM,
                and_(
                    SubscriptionORM.subscribed_to_id == HashtagORM.id,
                    SubscriptionORM.subscribed_to_type == SubscriptionTypeEnum.hashtag
                )
            ).options(selectinload(SubscriptionORM.subscribed_hashtag))

            result = await self.db.execute(hashtag_stmt)
            hashtag_subscriptions = result.scalars().all()
            hashtag_subs = [
                HashtagSubscription(
                    id=sub.id,
                    hashtag=Hashtag.model_validate(sub.subscribed_hashtag),
                    favourite=sub.favourite
                )
                for sub in hashtag_subscriptions
                if sub.subscribed_hashtag is not None  # Skip if hashtag was deleted
            ]

        return UserSubscriptionsResponse(users=user_subs, hashtags=hashtag_subs)

    async def set_favorite(
        self, user: "User", subscribed_to_id: int, subscription_type: SubscriptionTypeEnum, is_favorite: bool
    ) -> SubscriptionResponse:
        MAX_FAVORITE_HASHTAGS = 8

        result = await self.db.execute(
            select(SubscriptionORM).filter_by(
                subscriber_id=user.id,
                subscribed_to_id=subscribed_to_id,
                subscribed_to_type=subscription_type,
            )
        )
        subscription = result.scalar_one_or_none()

        if not subscription:
            raise Missing("Subscription not found")

        # Check if the operation would be redundant
        if subscription.favourite == is_favorite:
            raise InvalidFavoriteOperation(is_favorite)

        # If trying to add a favorite hashtag, check the limit
        if is_favorite and subscription_type == SubscriptionTypeEnum.hashtag:
            result = await self.db.execute(
                select(func.count())
                .select_from(SubscriptionORM)
                .where(
                    SubscriptionORM.subscriber_id == user.id,
                    SubscriptionORM.subscribed_to_type == SubscriptionTypeEnum.hashtag,
                    SubscriptionORM.favourite == True,  # noqa: E712
                )
            )
            current_favorites: int = result.scalar_one()  # type: ignore[assignment]

            if current_favorites >= MAX_FAVORITE_HASHTAGS:
                raise MaxFavoritesReached(MAX_FAVORITE_HASHTAGS)

        subscription.favourite = is_favorite
        await self.db.commit()
        await self.db.refresh(subscription)
        return SubscriptionResponse.model_validate(subscription)


def build_subscription_repository(db: "AsyncSession") -> SubscriptionRepository:
    repo = SubscriptionRepository(db)
    return repo
