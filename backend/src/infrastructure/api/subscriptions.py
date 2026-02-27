import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Path, status

from app.exceptions import ApiException
from app.schema.subscriptions import (
    UserSubscriptionsResponse,
    SubscriptionTypeEnum,
    SubscriptionResponse,
)
from infrastructure.api.dependencies import (
    token_dependency,
    current_user_dep,
    subscription_service_dep,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


@router.post(
    "/{subscribed_to_type}/{subscribed_to_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=SubscriptionResponse,
)
async def subscribe_to_user_or_hashtag(
    token: token_dependency,
    current_user: current_user_dep,
    subscription_service: subscription_service_dep,
    subscribed_to_type: SubscriptionTypeEnum = Path(
        ..., description="Type of subscription ('user' or 'hashtag')"
    ),
    subscribed_to_id: int = Path(
        ..., description="ID of the user or hashtag being subscribed to"
    ),
):
    """Subscribe to another user or hashtag."""
    if subscribed_to_type == SubscriptionTypeEnum.user:
        if current_user.id == subscribed_to_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot subscribe to yourself.",
            )

    try:
        new_sub = await subscription_service.subscribe(
            current_user, subscribed_to_id, subscribed_to_type
        )
    except ApiException as exc:
        exc.raise_http_exception()

    return new_sub


@router.delete(
    "/{subscribed_to_type}/{subscribed_to_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def unsubscribe_from_user_or_hashtag(
    token: token_dependency,
    current_user: current_user_dep,
    subscription_service: subscription_service_dep,
    subscribed_to_type: SubscriptionTypeEnum = Path(
        ..., description="Type of subscription ('user' or 'hashtag')"
    ),
    subscribed_to_id: int = Path(
        ..., description="ID of the user or hashtag being subscribed to"
    ),
):
    """Unsubscribe from a user or hashtag."""
    try:
        await subscription_service.unsubscribe(
            current_user, subscribed_to_id, subscribed_to_type
        )
    except ApiException as exc:
        exc.raise_http_exception()


@router.delete("/{subscription_id}", status_code=status.HTTP_204_NO_CONTENT)
async def unsubscribe_by_id(
    token: token_dependency,
    current_user: current_user_dep,
    subscription_service: subscription_service_dep,
    subscription_id: int = Path(
        ..., description="ID of the user or hashtag being subscribed to"
    ),
):
    """Unsubscribe from a user or hashtag by subscription_id."""
    raise NotImplementedError("Not implemented yet")
    # await subscription_service.unsubscribe_by_id(current_user, subscription_id)


@router.post(
    "/{subscribed_to_type}/{subscribed_to_id}/favorite",
    status_code=status.HTTP_200_OK,
    response_model=SubscriptionResponse,
    description="Mark a subscription as favorite",
)
async def mark_as_favorite(
    token: token_dependency,
    current_user: current_user_dep,
    subscription_service: subscription_service_dep,
    subscribed_to_type: SubscriptionTypeEnum = Path(
        ..., description="Type of subscription ('user' or 'hashtag')"
    ),
    subscribed_to_id: int = Path(
        ..., description="ID of the user or hashtag being marked as favorite"
    ),
):
    """Mark a subscription as favorite."""
    try:
        updated_sub = await subscription_service.set_favorite(
            current_user, subscribed_to_id, subscribed_to_type, True
        )
    except ApiException as exc:
        exc.raise_http_exception()

    return updated_sub


@router.delete(
    "/{subscribed_to_type}/{subscribed_to_id}/favorite",
    status_code=status.HTTP_200_OK,
    response_model=SubscriptionResponse,
    description="Remove favorite status from a subscription",
)
async def remove_favorite(
    token: token_dependency,
    current_user: current_user_dep,
    subscription_service: subscription_service_dep,
    subscribed_to_type: SubscriptionTypeEnum = Path(
        ..., description="Type of subscription ('user' or 'hashtag')"
    ),
    subscribed_to_id: int = Path(
        ..., description="ID of the user or hashtag being unmarked as favorite"
    ),
):
    """Remove favorite status from a subscription."""
    try:
        updated_sub = await subscription_service.set_favorite(
            current_user, subscribed_to_id, subscribed_to_type, False
        )
    except ApiException as exc:
        exc.raise_http_exception()

    return updated_sub


@router.get(
    "/me",
    response_model=UserSubscriptionsResponse,
    summary="Get current user's subscriptions",
    description="Get all subscriptions for the current user. Can be filtered by type (user/hashtag)."
)
async def get_my_subscriptions(
    token: token_dependency,
    current_user: current_user_dep,
    subscription_service: subscription_service_dep,
    subscription_type: Optional[SubscriptionTypeEnum] = None,
) -> UserSubscriptionsResponse:
    """Get all subscriptions for the current user."""
    return await subscription_service.get_user_subscriptions(
        user_id=current_user.id,
        subscription_type=subscription_type,
    )
