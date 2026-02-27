from fastapi import APIRouter, Query

from app.schema.search import SearchResults, SearchType
from infrastructure.api.dependencies import (
    search_service_dep,
    current_user_dep,
    token_dependency,
)

router = APIRouter(prefix="/search", tags=["search"])


@router.get(
    "/",
    response_model=SearchResults,
    summary="Search across different entities",
    description="""
    Performs a case-insensitive search across different entity types (hashtags, questions, users).
    The search looks for partial matches in entity names/titles and returns paginated results.

    For hashtags:
    - Searches in hashtag names
    - Returns subscription status if user is authenticated

    For questions:
    - Searches in question text
    - Returns full question details including options and hashtags

    For users:
    - Searches in usernames, names, and surnames
    - Returns subscription status if user is authenticated
    """,
)
async def search(
    token: token_dependency,
    current_user: current_user_dep,
    search_service: search_service_dep,
    query: str = Query(
        ...,
        min_length=2,
        description="Search query string. Case-insensitive, supports partial matches.",
    ),
    type: SearchType = Query(
        SearchType.all,
        description="Type of entities to search for. Use 'all' to search across all types.",
    ),
    limit: int = Query(
        5,
        ge=1,
        le=100,
        description="Maximum number of results to return per category.",
    ),
) -> SearchResults:
    return await search_service.search(query, type, limit, current_user)
