from typing import TYPE_CHECKING, List

from sqlalchemy import text

from app.exceptions import Missing
from app.schema import statistics as schema
from infrastructure.repository.stats import queries as queries
from infrastructure.repository.stats.queries import by_question_ids

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class StatisticsRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    async def get_statistics_by_question_id(self, question_id: int) -> schema.QuestionStatistics:
        query = text(queries.by_question.STATISTICS_BY_QUESTION_ID)
        result = await self.db.execute(query, {"question_id": question_id})
        row = result.mappings().first()
        if not row:
            raise Missing(f'No statistics found for question id {question_id}')
        return schema.QuestionStatistics.parse_obj(dict(row))

    async def get_votes_and_statistics_by_option_by_question_id(
            self, question_id: int) -> List[schema.QuestionOptionStatistics]:
        query = text(queries.by_option.STATISTICS_ALL_QUESTION_OPTIONS)
        result = await self.db.execute(query, {"question_id": question_id})
        return [schema.QuestionOptionStatistics.parse_obj(dict(row)) for row in result]

    async def get_votes_and_statistics_by_option_id(self, option_id: int) -> schema.QuestionOptionStatistics:
        query = text(queries.by_option.STATISTICS_SINGLE_QUESTION_OPTION)
        result = await self.db.execute(query, {"option_id": option_id})
        row = result.mappings().first()
        if not row:
            raise Missing(f"Missing statistics for option {option_id}")
        return schema.QuestionOptionStatistics.parse_obj(dict(row))

    async def get_statistics_for_users_questions_paginated(
            self, user_id: int, limit: int = 10, offset: int = 0) -> List[schema.UserQuestionStatistics]:
        query = text(queries.by_user.STATISTICS_BY_USER_ID_PAGINATED)
        result = await self.db.execute(query, {"user_id": user_id, "limit": limit, "offset": offset})
        return [schema.UserQuestionStatistics.parse_obj(dict(row)) for row in result]

    async def get_votes_and_statistics_for_users_questions_paginated(
            self, user_id: int, role: str = 'all', limit: int = 10, offset: int = 0
    ) -> List[schema.OptimizedQuestionStats]:
        """Optimized method that only fetches question IDs, role, votes, and statistics."""
        query = text(queries.by_user.VOTES_AND_STATISTICS_BY_USER_ID_PAGINATED)
        result = await self.db.execute(
            query, {"user_id": user_id, "limit": limit, "offset": offset, "role_filter": role})
        rows = result.mappings().all()
        return [schema.OptimizedQuestionStats.parse_obj(row) for row in rows]

    async def get_statistics_by_question_ids_for_author(
            self, user_id: int, question_ids: List[int]
    ) -> List[schema.OptimizedQuestionStats]:
        """Get statistics for specific question IDs where the user is the author."""
        if not question_ids:
            return []
            
        query = text(by_question_ids.STATISTICS_BY_QUESTION_IDS_FOR_AUTHOR)
        result = await self.db.execute(
            query, {"user_id": user_id, "question_ids": question_ids})
        rows = result.mappings().all()
        return [schema.OptimizedQuestionStats.parse_obj(row) for row in rows]


def build_statistics_repository(db: "AsyncSession") -> StatisticsRepository:
    repo = StatisticsRepository(db)
    return repo
