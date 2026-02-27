from fastapi import APIRouter, Query, status

from app.schema.user import (
    UserResponse, UserUpdate, UserSettings, UserSettingsUpdate, SimilaritySortEnum, ConnectionFilterEnum,
    TimeRangeEnum
)
from app.exceptions import ApiException
from infrastructure.api.dependencies import (
    user_service_dep,
    current_user_dep,
    token_dependency,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
async def read_users_me(
    token: token_dependency, user: current_user_dep
) -> UserResponse:
    return UserResponse.from_user(user)


@router.get("/", response_model=list[UserResponse])
async def get_users(
    user_service: user_service_dep,
    token: token_dependency,
    limit: int = Query(10, ge=1, le=100, description="Number of users to return"),
    offset: int = Query(0, ge=0, description="Number of users to skip"),
) -> list[UserResponse]:
    try:
        users = await user_service.get_users(limit, offset, token)
    except ApiException as exc:
        exc.raise_http_exception()
    return users


@router.get("/similar", response_model=list[UserResponse])
async def get_similar_users(
    token: token_dependency,
    user_service: user_service_dep,
    current_user: current_user_dep,
    sort_by: SimilaritySortEnum = Query(..., description="Sort by mutuality or similarity"),
    connection_filter: ConnectionFilterEnum = Query(..., description="Filter by connection status"),
    time_range: TimeRangeEnum = Query(TimeRangeEnum.last_year, description="Time range for calculating similarity"),
    limit: int = Query(10, ge=1, le=100, description="Number of users to return"),
    offset: int = Query(0, ge=0, description="Number of users to skip"),
) -> list[UserResponse]:
    """Get a list of users similar to the current user based on various criteria.

    The similarity can be calculated based on:
    - mutuality: ratio of common answered questions
    - similarity: how similar the answers are

    Users can be filtered by connection status (followings/followers/non-connected)

    The time range for calculating similarity can be:
    - last_year (default)
    - last_day
    - last_week
    - last_month
    """
    _ = token
    try:
        users = await user_service.get_similar_users(
            current_user=current_user,
            sort_by=sort_by,
            connection_filter=connection_filter,
            time_range=time_range,
            limit=limit,
            offset=offset,
        )
    except ApiException as exc:
        exc.raise_http_exception()
    return users


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int, token: token_dependency, user_service: user_service_dep, current_user: current_user_dep
) -> UserResponse:
    try:
        user = await user_service.get_user_by_id(user_id, current_user)
    except ApiException as exc:
        exc.raise_http_exception()
    return user


# TODO: move from register
# @router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# async def create_user(user_data: UserCreate, user_service: user_service_dep) -> UserResponse:
#     return await user_service.create_user(user_data)


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    token: token_dependency,
    user_service: user_service_dep,
    current_user: current_user_dep,
) -> UserResponse:
    try:
        user = await user_service.update_user(user_id, user_data, current_user)
    except ApiException as exc:
        exc.raise_http_exception()
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    token: token_dependency,
    user_service: user_service_dep,
    current_user: current_user_dep,
):
    try:
        await user_service.delete_user(user_id, current_user)
    except ApiException as exc:
        exc.raise_http_exception()


@router.get("/{user_id}/settings", response_model=UserSettings)
async def get_user_settings(
    user_id: int,
    token: token_dependency,
    user_service: user_service_dep,
    current_user: current_user_dep,
):
    """Get settings for a specific user."""
    try:
        return await user_service.get_settings(user_id, current_user)
    except ApiException as exc:
        exc.raise_http_exception()


@router.post(
    "/{user_id}/settings",
    response_model=UserSettings,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_settings(
    user_id: int,
    settings_data: UserSettings,
    token: token_dependency,
    user_service: user_service_dep,
    current_user: current_user_dep,
):
    """Create settings for a specific user."""
    # TODO: check if authorization is actually needed here
    try:
        return await user_service.create_settings(user_id, settings_data, current_user)
    except ApiException as exc:
        exc.raise_http_exception()


@router.put("/{user_id}/settings", response_model=UserSettings)
async def update_user_settings(
    user_id: int,
    settings_data: UserSettingsUpdate,
    token: token_dependency,
    user_service: user_service_dep,
    current_user: current_user_dep,
):
    """Update settings for a specific user."""
    try:
        return await user_service.update_settings(user_id, settings_data, current_user)
    except ApiException as exc:
        exc.raise_http_exception()


@router.delete("/{user_id}/settings", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_settings(
    user_id: int,
    token: token_dependency,
    user_service: user_service_dep,
    current_user: current_user_dep,
):
    """Delete settings for a specific user."""
    try:
        await user_service.delete_settings(user_id, current_user)
    except ApiException as exc:
        exc.raise_http_exception()
