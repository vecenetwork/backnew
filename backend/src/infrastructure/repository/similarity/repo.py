from datetime import datetime
from typing import TYPE_CHECKING, TypeVar, Type, Optional, List, Tuple, NamedTuple
from sqlalchemy import text
from pydantic import BaseModel

from app.exceptions import Missing
from app.schema import similarity as schema
from app.schema.user import SimilaritySortEnum
from . import queries

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from infrastructure.repository.subscriptions import SubscriptionRepository

T = TypeVar("T", bound=BaseModel)


class UserScores(NamedTuple):
    mutuality: Optional[float] = 0
    similarity: Optional[float] = 0


class SimilarityRepository:
    def __init__(self, db: "AsyncSession", subscription_repo: "SubscriptionRepository"):
        self.db = db
        self.subscription_repo = subscription_repo

    async def _execute_single_query(self, query: str, params: dict, schema_type: Type[T]) -> T:
        """Execute a single query and return one result."""
        result = await self.db.execute(text(query), params)
        row = result.mappings().first()
        if not row:
            raise Missing(f"Could not calculate {schema_type.__name__.lower()}")
        return schema_type.parse_obj(dict(row))

    async def _execute_multiple_query(self, query: str, params: dict, schema_type: Type[T]) -> list[T]:
        """Execute a query and return multiple results."""
        result = await self.db.execute(text(query), params)
        rows = result.mappings().all()
        if not rows:
            raise Missing(f"Could not calculate {schema_type.__name__.lower()}")
        return [schema_type.parse_obj(dict(row)) for row in rows]

    async def get_mutuality(
            self, my_id: int, other_id: int, start_date: Optional[datetime] = None,
    ) -> schema.Mutuality:
        return await self._execute_single_query(
            query=queries.all.MUTUALITY,
            params={"my_id": my_id, "other_id": other_id, "start_date": start_date},
            schema_type=schema.Mutuality
        )

    async def get_similarity(
            self, my_id: int, other_id: int, start_date: Optional[datetime] = None,
    ) -> schema.Similarity:
        return await self._execute_single_query(
            query=queries.all.SIMILARITY,
            params={"my_id": my_id, "other_id": other_id, "start_date": start_date},
            schema_type=schema.Similarity
        )

    async def get_mutuality_and_similarity(
            self, my_id: int, other_id: int, start_date: Optional[datetime] = None,
    ) -> schema.MutualityAndSimilarity:
        return await self._execute_single_query(
            query=queries.all.MUTUALITY_AND_SIMILARITY,
            params={"my_id": my_id, "other_id": other_id, "start_date": start_date},
            schema_type=schema.MutualityAndSimilarity
        )

    async def get_mutuality_by_hashtag(self, my_id: int, other_id: int, limit: int) -> list[schema.HashtagMutuality]:
        return await self._execute_multiple_query(
            query=queries.by_hashtag.MUTUALITY,
            params={"my_id": my_id, "other_id": other_id, "limit": limit},
            schema_type=schema.HashtagMutuality
        )

    async def get_similarity_by_hashtag(self, my_id: int, other_id: int, limit: int) -> list[schema.HashtagSimilarity]:
        return await self._execute_multiple_query(
            query=queries.by_hashtag.SIMILARITY,
            params={"my_id": my_id, "other_id": other_id, "limit": limit},
            schema_type=schema.HashtagSimilarity
        )

    async def get_mutuality_and_similarity_by_hashtag(
            self, my_id: int, other_id: int, limit: int
    ) -> list[schema.HashtagMutualityAndSimilarity]:
        return await self._execute_multiple_query(
            query=queries.by_hashtag.MUTUALITY_AND_SIMILARITY,
            params={"my_id": my_id, "other_id": other_id, "limit": limit},
            schema_type=schema.HashtagMutualityAndSimilarity
        )

    async def _get_similarity_scores(
        self,
        current_user_id: int,
        other_user_id: int,
        start_date: Optional[datetime] = None,
    ) -> Optional[UserScores]:
        result = await self.get_mutuality_and_similarity(
            current_user_id,
            other_user_id,
            start_date=start_date
        )
        return UserScores(
            mutuality=result.mutuality,
            similarity=result.avg_similarity
        )

    async def get_top_scores(
        self,
        current_user_id: int,
        target_users: List[int],  # Changed to List[int] - we only need IDs
        sort_by: SimilaritySortEnum,
        start_date: Optional[datetime] = None,
        limit: int = 10,
        offset: int = 0,
    ) -> List[Tuple[int, UserScores]]:  # Changed to return Tuple[int, UserScores]
        # Calculate scores for each user
        scores_list = []
        for user_id in target_users:
            if user_id == current_user_id:
                continue
            scores = await self._get_similarity_scores(
                current_user_id,
                user_id,
                start_date
            )
            if scores is not None:
                scores_list.append((user_id, scores))

        # Sort by the requested score type
        scores_list.sort(
            key=lambda x: (
                x[1].mutuality if sort_by == SimilaritySortEnum.mutuality else x[1].similarity
            ) or 0.0,
            reverse=True
        )

        return scores_list[offset:offset + limit]


def build_similarity_repository(db: "AsyncSession", subscription_repo: "SubscriptionRepository") -> SimilarityRepository:
    return SimilarityRepository(db, subscription_repo)
