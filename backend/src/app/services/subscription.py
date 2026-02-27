import logging
from typing import TYPE_CHECKING

from app.schema.subscriptions import (
    SubscriptionTypeEnum,
    UserSubscriptionsResponse,
    SubscriptionResponse,
)

if TYPE_CHECKING:
    from app.schema.user import User
    from infrastructure.repository.subscriptions import SubscriptionRepository

logger = logging.getLogger(__name__)


class SubscriptionService:
    def __init__(self, repo: "SubscriptionRepository"):
        self.repo = repo

    async def subscribe(
        self, current_user: "User", subscribed_to_id: int, subscription_type: SubscriptionTypeEnum
    ) -> SubscriptionResponse:
        logger.info(f"Subscribing to subscription type {subscription_type}")
        new_subscription = await self.repo.subscribe(
            current_user, subscribed_to_id, subscription_type
        )
        logger.info(f"Created subscription {new_subscription}")
        return new_subscription

    async def unsubscribe(
        self, current_user: "User", subscribed_to_id: int, subscription_type: SubscriptionTypeEnum
    ):
        await self.repo.unsubscribe(current_user, subscribed_to_id, subscription_type)

    async def get_user_subscriptions(
        self,
        user_id: int,
        subscription_type: SubscriptionTypeEnum | None = None,
    ) -> UserSubscriptionsResponse:
        return await self.repo.get_user_subscriptions(
            user_id=user_id,
            subscription_type=subscription_type,
        )

    async def set_favorite(
        self, current_user: "User", subscribed_to_id: int, subscription_type: SubscriptionTypeEnum, is_favorite: bool
    ) -> SubscriptionResponse:
        logger.info(f"Setting favorite status to {is_favorite} for {subscription_type} subscription {subscribed_to_id}")
        updated_subscription = await self.repo.set_favorite(
            current_user, subscribed_to_id, subscription_type, is_favorite
        )
        logger.info(f"Updated subscription {updated_subscription}")
        return updated_subscription


def build_subscription_service(repo: "SubscriptionRepository") -> SubscriptionService:
    service = SubscriptionService(repo)
    return service
