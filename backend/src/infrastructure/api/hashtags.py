import logging

from fastapi import APIRouter, HTTPException, Query, status

from app.schema.hashtags import Hashtag, HashtagSuggestRequest, HashtagSuggestResponse

logger = logging.getLogger(__name__)
from app.exceptions import Missing
from infrastructure.api.dependencies import (
    hashtag_service_dep,
    hashtag_suggestion_service_dep,
    current_user_dep,
    token_dependency,
)

router = APIRouter(prefix="/hashtags", tags=["hashtags"])


@router.get(
    "/",
    response_model=list[Hashtag],
    description="Retrieves random hashtags (offset currently means nothing).",
)
async def get_hashtags(
    token: token_dependency,
    current_user: current_user_dep,
    hashtag_service: hashtag_service_dep,
    limit: int = Query(10, ge=1, le=100, description="Number of hashtags to return"),
    offset: int = Query(0, ge=0, description="Number of hashtags to skip"),
) -> list[Hashtag]:
    hashtags = await hashtag_service.get_hashtags(limit, offset, current_user=current_user)
    return hashtags


@router.post(
    "/classify",
    response_model=HashtagSuggestResponse,
    description="Classify question to find relevant hashtags (AI).",
)
async def suggest_hashtags(
    token: token_dependency,
    current_user: current_user_dep,
    hashtag_suggestion_service: hashtag_suggestion_service_dep,
    body: HashtagSuggestRequest,
) -> HashtagSuggestResponse:
    _ = current_user
    logger.info("[hashtag] Request: question=%r, options=%s", (body.question_text or "")[:60], body.options)
    hashtags = await hashtag_suggestion_service.suggest(
        question_text=body.question_text,
        options=body.options,
    )
    logger.info("[hashtag] Response: %d tags %s", len(hashtags), hashtags[:5])
    return HashtagSuggestResponse(hashtags=hashtags)


@router.post("/", response_model=Hashtag)
async def create_hashtag(
    token: token_dependency,
    current_user: current_user_dep,
    hashtag_service: hashtag_service_dep,
    hashtag: Hashtag,
):
    new_hashtag = await hashtag_service.create_hashtag(hashtag)
    return new_hashtag


@router.get(
    "/{hashtag_id}", response_model=Hashtag, status_code=status.HTTP_201_CREATED
)
async def get_hashtag(
    token: token_dependency,
    current_user: current_user_dep,
    hashtag_service: hashtag_service_dep,
    hashtag_id: int,
) -> Hashtag:
    try:
        hashtag = await hashtag_service.get_hashtag(hashtag_id, current_user=current_user)
    except Missing as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.detail)
    return hashtag


@router.delete("/{hashtag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hashtag(
    token: token_dependency,
    current_user: current_user_dep,
    hashtag_service: hashtag_service_dep,
    hashtag_id: int,
):
    _ = current_user
    try:
        await hashtag_service.delete_hashtag(hashtag_id)
    except Missing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

