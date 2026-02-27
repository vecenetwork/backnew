from typing import TYPE_CHECKING, List

from app.schema import statistics as schema

if TYPE_CHECKING:
    from infrastructure.repository.stats.repo import StatisticsRepository


class StatisticsService:
    def __init__(self, stats_repo: "StatisticsRepository"):
        self.stats_repo = stats_repo

    async def get_statistics_by_question_id(self, question_id: int) -> schema.QuestionStatistics:
        results = await self.stats_repo.get_statistics_by_question_id(question_id)
        return results

    async def get_votes_and_statistics_by_option_by_question_id(
            self, question_id: int) -> List[schema.QuestionOptionStatistics]:
        results = await self.stats_repo.get_votes_and_statistics_by_option_by_question_id(question_id)
        return results

    async def get_votes_and_statistics_by_option_id(self, option_id: int) -> schema.QuestionOptionStatistics:
        results = await self.stats_repo.get_votes_and_statistics_by_option_id(option_id)
        return results

    async def get_statistics_for_users_questions_paginated(
        self, user_id: int, limit: int = 10, offset: int = 0
    ) -> List[schema.UserQuestionStatistics]:
        results = await self.stats_repo.get_statistics_for_users_questions_paginated(user_id, limit, offset)
        return results

    async def get_votes_and_statistics_for_users_questions_paginated(
        self, user_id: int, role: str = 'all', limit: int = 10, offset: int = 0
    ) -> List[schema.OptimizedQuestionStats]:
        """Get minimal statistics data (IDs, role, votes, statistics) without redundant question fields."""
        results = await self.stats_repo.get_votes_and_statistics_for_users_questions_paginated(
            user_id, role, limit, offset)
        return results

    async def get_statistics_by_question_ids_for_author(
        self, user_id: int, question_ids: List[int]
    ) -> List[schema.OptimizedQuestionStats]:
        """Get statistics for specific question IDs where the user is the author."""
        results = await self.stats_repo.get_statistics_by_question_ids_for_author(
            user_id, question_ids)
        return results


def build_statistics_service(stats_repo: "StatisticsRepository") -> StatisticsService:
    stats_service = StatisticsService(stats_repo)
    return stats_service
