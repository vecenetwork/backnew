from typing import TYPE_CHECKING, List

from app.schema import similarity as schema

if TYPE_CHECKING:
    from infrastructure.repository.similarity.repo import SimilarityRepository


class SimilarityService:
    def __init__(self, stats_repo: "SimilarityRepository"):
        self.stats_repo = stats_repo

    async def get_mutuality(self, my_id: int, other_id: int) -> schema.Mutuality:
        results = await self.stats_repo.get_mutuality(my_id, other_id)
        return results

    async def get_similarity(self, my_id: int, other_id: int) -> schema.Similarity:
        results = await self.stats_repo.get_similarity(my_id, other_id)
        return results

    async def get_mutuality_and_similarity(self, my_id: int, other_id: int) -> schema.MutualityAndSimilarity:
        results = await self.stats_repo.get_mutuality_and_similarity(my_id, other_id)
        return results

    async def get_mutuality_by_hashtag(self, my_id: int, other_id: int, limit: int) -> List[schema.HashtagMutuality]:
        results = await self.stats_repo.get_mutuality_by_hashtag(my_id, other_id, limit)
        return results

    async def get_similarity_by_hashtag(self, my_id: int, other_id: int, limit: int) -> List[schema.HashtagSimilarity]:
        results = await self.stats_repo.get_similarity_by_hashtag(my_id, other_id, limit)
        return results

    async def get_mutuality_and_similarity_by_hashtag(
            self, my_id: int, other_id: int, limit: int) -> List[schema.HashtagMutualityAndSimilarity]:
        results = await self.stats_repo.get_mutuality_and_similarity_by_hashtag(my_id, other_id, limit)
        return results


def build_similarity_service(repo: "SimilarityRepository") -> SimilarityService:
    similarity_service = SimilarityService(repo)
    return similarity_service
