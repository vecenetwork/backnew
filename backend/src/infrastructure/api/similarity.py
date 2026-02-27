from fastapi import APIRouter, status

from app.exceptions import ApiException
from app.schema import similarity as schema
from infrastructure.api.dependencies import current_user_dep, token_dependency, similarity_service_dep

router = APIRouter(tags=["similarity"])


@router.get(
    "/mutuality/{other_id}",
    response_model=schema.Mutuality,
    summary="Get mutuality between current user and another user",
    status_code=status.HTTP_200_OK
)
async def get_mutuality(
    token: token_dependency,
    current_user: current_user_dep,
    service: similarity_service_dep,
    other_id: int
):
    try:
        result = await service.get_mutuality(current_user.id, other_id)
        return result
    except ApiException as exc:
        exc.raise_http_exception()


@router.get(
    "/similarity/{other_id}",
    response_model=schema.Similarity,
    summary="Get similarity between current user and another user",
    status_code=status.HTTP_200_OK
)
async def get_similarity(
    token: token_dependency,
    current_user: current_user_dep,
    service: similarity_service_dep,
    other_id: int
):
    try:
        result = await service.get_similarity(current_user.id, other_id)
        return result
    except ApiException as exc:
        exc.raise_http_exception()


@router.get(
    "/mutuality-and-similarity/{other_id}",
    response_model=schema.MutualityAndSimilarity,
    summary="Get both mutuality and similarity between current user and another user",
    status_code=status.HTTP_200_OK
)
async def get_mutuality_and_similarity(
    token: token_dependency,
    current_user: current_user_dep,
    service: similarity_service_dep,
    other_id: int
):
    try:
        result = await service.get_mutuality_and_similarity(current_user.id, other_id)
        return result
    except ApiException as exc:
        exc.raise_http_exception()


@router.get(
    "/mutuality-by-hashtag/{other_id}",
    response_model=list[schema.HashtagMutuality],
    summary="Get mutuality by hashtag for current user and another user",
    status_code=status.HTTP_200_OK
)
async def get_mutuality_by_hashtag(
    token: token_dependency,
    current_user: current_user_dep,
    service: similarity_service_dep,
    other_id: int,
    limit: int = 8,
):
    try:
        result = await service.get_mutuality_by_hashtag(current_user.id, other_id, limit)
        return result
    except ApiException as exc:
        exc.raise_http_exception()


@router.get(
    "/similarity-by-hashtag/{other_id}",
    response_model=list[schema.HashtagSimilarity],
    summary="Get similarity by hashtag for current user and another user",
    status_code=status.HTTP_200_OK
)
async def get_similarity_by_hashtag(
    token: token_dependency,
    current_user: current_user_dep,
    service: similarity_service_dep,
    other_id: int,
    limit: int = 8,
):
    try:
        result = await service.get_similarity_by_hashtag(current_user.id, other_id, limit)
        return result
    except ApiException as exc:
        exc.raise_http_exception()


@router.get(
    "/mutuality-and-similarity-by-hashtag/{other_id}",
    response_model=list[schema.HashtagMutualityAndSimilarity],
    summary="Get mutuality and similarity by hashtag for current user and another user",
    status_code=status.HTTP_200_OK
)
async def get_mutuality_and_similarity_by_hashtag(
    token: token_dependency,
    current_user: current_user_dep,
    service: similarity_service_dep,
    other_id: int,
    limit: int = 8,
):
    try:
        result = await service.get_mutuality_and_similarity_by_hashtag(current_user.id, other_id, limit)
        return result
    except ApiException as exc:
        exc.raise_http_exception()
