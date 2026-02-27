from typing import TYPE_CHECKING, Optional

from app.schema.hashtags import Hashtag
from app.schema.user import User

if TYPE_CHECKING:
    from infrastructure.repository.hashtag import HashtagRepository


class HashtagService:
    def __init__(self, repo: "HashtagRepository"):
        self.repo = repo

    async def get_hashtags(self, limit: int, offset: int, current_user: Optional[User] = None) -> list[Hashtag]:
        # TODO: tmp return random hashtags
        # return await self.repo.get_all_paginated(limit=limit, offset=offset)
        _ = offset
        return await self.repo.get_random_hashtags(limit=limit, current_user=current_user)

    async def get_all_hashtags_as_str(self) -> list[str]:
        # TODO: replace big limit with unlimited call
        hashtags = await self.repo.get_all_paginated(limit=1000, offset=0)
        return [hashtag.name for hashtag in hashtags]

    async def get_hashtag(self, hashtag_id: int, current_user: Optional[User] = None) -> Hashtag:
        return await self.repo.get_by_id(hashtag_id, current_user=current_user)

    async def create_hashtag(self, hashtag: Hashtag) -> Hashtag:
        return await self.repo.create(hashtag)

    async def update_hashtag(self, hashtag: Hashtag) -> Hashtag:
        return await self.repo.update(hashtag)

    async def delete_hashtag(self, hashtag_id: int):
        await self.repo.delete(hashtag_id)


def build_hashtag_service(repo: "HashtagRepository") -> HashtagService:
    service = HashtagService(repo)
    return service
