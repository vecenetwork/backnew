from typing import Optional, TYPE_CHECKING

from app.schema.search import SearchResults, SearchType
from app.schema.user import User, UserResponse

if TYPE_CHECKING:
    from infrastructure.repository.hashtag import HashtagRepository
    from infrastructure.repository.questions import QuestionRepository
    from infrastructure.repository.user import UserRepository


class SearchService:
    def __init__(
        self,
        hashtag_repo: 'HashtagRepository',
        question_repo: 'QuestionRepository',
        user_repo: 'UserRepository',
    ):
        self.hashtag_repo = hashtag_repo
        self.question_repo = question_repo
        self.user_repo = user_repo

    async def search(
        self,
        query: str,
        search_type: SearchType = SearchType.all,
        limit: int = 5,
        current_user: Optional[User] = None
    ) -> SearchResults:
        """
        Search across different entities based on search type.
        Returns up to `limit` results for each category.
        """
        hashtags = []
        questions = []
        users: list['UserResponse'] = []

        # Execute searches based on type
        if search_type in (SearchType.all, SearchType.hashtags):
            hashtags = await self.hashtag_repo.search(query, limit, current_user)

        if search_type in (SearchType.all, SearchType.questions):
            questions = await self.question_repo.search(query, limit, current_user)

        if search_type in (SearchType.all, SearchType.users):
            current_user_id = current_user.id if current_user else None
            found_users = await self.user_repo.search(query, limit, current_user_id)
            users = [UserResponse.from_user_other(user) for user in found_users]

        return SearchResults(
            hashtags=hashtags,
            users=users,
            questions=questions
        )


def build_search_service(
    hashtag_repo: 'HashtagRepository',
    question_repo: 'QuestionRepository',
    user_repo: 'UserRepository',
) -> SearchService:
    return SearchService(
        hashtag_repo=hashtag_repo,
        question_repo=question_repo,
        user_repo=user_repo,
    )
