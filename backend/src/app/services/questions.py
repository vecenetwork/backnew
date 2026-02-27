import logging
from typing import List, TYPE_CHECKING

from app.exceptions import ConfigurationError, ApiException
from app.schema.questions import (
    Question,
    QuestionCreate,
    QuestionOption,
    QuestionOptionCreate,
    QuestionOptionCreateInternal,
    QuestionOptionUpdate,
    QuestionResponse,
    QuestionUpdate,
)
from app.schema.statistics import QuestionStatistics, QuestionOptionStatistics
from app.schema.user import UserResponse, ShowNameOptionEnum
from app.schema.enums import SortOrderEnum, SortByEnum, UserRoleEnum, FeedTypeEnum

if TYPE_CHECKING:
    from app.schema.user import User
    from app.services.statistics import StatisticsService
    from infrastructure.repository.hashtag import QuestionHashtagLinkRepository
    from infrastructure.repository.questions import (
        QuestionRepository,
        QuestionOptionRepository,
    )
    from infrastructure.repository.answers import AnswerRepository

logger = logging.getLogger()


class CustomOptionsNotAllowedError(ApiException):
    status_code = 400


class OptionMismatchError(ApiException):
    status_code = 400


class QuestionService:
    def __init__(
        self,
        statistics_service: "StatisticsService",
        question_repo: "QuestionRepository",
        option_repo: "QuestionOptionRepository",
        hashtag_link_repo: "QuestionHashtagLinkRepository",
        answer_repo: "AnswerRepository",
    ):
        self.statistics_service = statistics_service
        self.question_repo = question_repo
        self.option_repo = option_repo
        self.hashtag_link_repo = hashtag_link_repo
        self.answer_repo = answer_repo

    def _apply_author_privacy(self, question: "Question", current_user: "User") -> "Question":
        # TODO: move to some other place
        # If it's the user's own question, keep the author as is
        if question.author.id == current_user.id:
            return question
        
        if not question.author.settings:
            # If no settings, return as is (fallback)
            return question
        
        filtered_author_dict = question.author.model_dump()
        if question.author.settings.show_name_option == ShowNameOptionEnum.name:
            pass
        else:
            filtered_author_dict['name'] = None
            filtered_author_dict['surname'] = None
        
        filtered_author_dict['birthday'] = None
        filtered_author_dict['email'] = None
        filtered_author_dict['settings'] = None

        # Create new question with filtered author
        question_dict = question.model_dump()
        question_dict['author'] = UserResponse.model_validate(filtered_author_dict)
        
        return Question.model_validate(question_dict)

    def _question_to_response(self, question: "Question") -> "QuestionResponse":
        """Convert Question to QuestionResponse with null statistics fields."""
        return QuestionResponse(
            # Base question fields
            text=question.text,
            max_options=question.max_options,
            active_till=question.active_till,
            allow_user_options=question.allow_user_options,
            gender=question.gender,
            country_id=question.country_id,
            id=question.id,
            author=question.author,
            age_range=question.age_range,
            options=question.options,
            created_at=question.created_at,
            hashtags=question.hashtags,
            user_selected_options=question.user_selected_options,
            total_answers=question.total_answers,
            # Statistics fields are None for regular questions
            role=None,
            statistics=None,
        )

    # === Questions ===

    async def create_question(
        self, question: "QuestionCreate", user: "User"
    ) -> "QuestionResponse":
        if question.author_id is None:
            question.author_id = user.id
        new_question = await self.question_repo.create(question)
        
        # Handle hashtags if provided
        if question.hashtags:
            await self.hashtag_link_repo.bulk_create(question.hashtags, new_question.id)
            # Reload the question with hashtags
            new_question = await self.question_repo.get_by_id(new_question.id)
        
        # For created questions, no need to apply privacy since it's the user's own question
        # No need to check for selected options since it's a new question
        return self._question_to_response(new_question)

    async def get_question(self, question_id: int, current_user: "User") -> "QuestionResponse":
        question = await self.question_repo.get_by_id(question_id, current_user=current_user)
        privacy_filtered_question = self._apply_author_privacy(question, current_user)
        
        # Get user's selected options if they answered this question
        user_answers = await self.answer_repo.get_user_answers_for_questions(current_user.id, [question_id])
        privacy_filtered_question.user_selected_options = user_answers.get(question_id)
        
        # Convert to QuestionResponse
        return self._question_to_response(privacy_filtered_question)

    async def get_my_questions(
        self,
        user: "User",
        created_by: int | None = None,
        answered_by: int | None = None,
        sort_by: str = SortByEnum.created_at.value,
        sort_order: str = SortOrderEnum.desc.value,
        limit: int = 50,
        offset: int = 0,
    ) -> List["QuestionResponse"]:
        questions = await self.question_repo.get_all_paginated(
            created_by, answered_by, sort_by, sort_order, limit, offset, current_user=user
        )
        
        # Apply privacy filtering
        privacy_filtered_questions = [self._apply_author_privacy(q, user) for q in questions]
        
        # Get user's answers for these questions to populate selected options
        question_ids = [q.id for q in privacy_filtered_questions]
        user_answers = await self.answer_repo.get_user_answers_for_questions(user.id, question_ids)
        
        # Populate user_selected_options for each question
        for question in privacy_filtered_questions:
            question.user_selected_options = user_answers.get(question.id)
            
        # Convert to QuestionResponse
        return [self._question_to_response(q) for q in privacy_filtered_questions]

    async def get_stats_for_question(self, user: "User", question_id: int) -> "QuestionStatistics":
        _ = user
        stats = await self.statistics_service.get_statistics_by_question_id(question_id)
        return stats

    async def update_question(
        self, question_id: int, data: "QuestionUpdate", user: "User"
    ) -> "Question":
        question = await self.question_repo.get_by_id(question_id)
        if question.author.id != user.id:
            # Or some other permission check
            raise PermissionError("User cannot update this question")
        
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return question  # No fields to update
            
        await self.question_repo.update(question_id, **update_data)
        return await self.question_repo.get_by_id(question_id)

    async def delete_question(self, question_id: int):
        await self.question_repo.delete(question_id)

    # === Options ===

    async def create_option(
        self, question_id: int, option: "QuestionOptionCreate", user: "User", commit: bool = True
    ) -> "QuestionOption":
        question = await self.question_repo.get_by_id(question_id)
        question = self._apply_author_privacy(question, user)

        current_options_positions = [opt.position for opt in question.options]
        if option.position in current_options_positions:
            raise ConfigurationError(
                f"Option with position {option.position} already exists ({current_options_positions})"
            )

        if not question.allow_user_options and question.author.id != user.id:
            raise CustomOptionsNotAllowedError(
                "Author restricted adding custom options"
            )

        # author = option.author_id or user.id
        author_id = user.id
        by_question_author = author_id == question.author.id

        option_internal = QuestionOptionCreateInternal(
            question_id=question_id,
            text=option.text,
            position=option.position,
            author_id=author_id,
            by_question_author=by_question_author,
        )
        return await self.option_repo.create(option_internal, commit=commit)

    async def get_options(self, question_id: int) -> list["QuestionOption"]:
        # Note: This doesn't need current_user since options only return author_id, not full author data
        return await self.option_repo.get_by_question_id(question_id)

    async def get_stats_for_option(self, user: "User", option_id: int) -> "QuestionOptionStatistics":
        _ = user
        stats = await self.statistics_service.get_votes_and_statistics_by_option_id(option_id)
        return stats

    async def get_option(self, question_id: int, option_id: int) -> "QuestionOption":
        option = await self.option_repo.get_by_id(option_id)
        if option.question_id != question_id:
            raise OptionMismatchError("Option doesn't belong to this question")
        return option

    async def update_option(
        self, question_id: int, option_id: int, data: "QuestionOptionUpdate", user: "User"
    ) -> "QuestionOption":
        option = await self.get_option(question_id, option_id)
        question = await self.question_repo.get_by_id(question_id)

        # Allow only author of question or author of option to update it
        if option.author_id != user.id and question.author.id != user.id:
            raise PermissionError("User cannot update this option")
            
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return option  # No fields to update
            
        updated_option = await self.option_repo.update(option_id, **update_data)
        if updated_option is None:
            # This shouldn't happen since we checked existence above, but handle it just in case
            return await self.option_repo.get_by_id(option_id)
        return updated_option

    async def delete_option(self, question_id: int, option_id: int):
        # TODO: should we check that option belong to a question?
        await self.get_option(question_id, option_id)
        await self.option_repo.delete(option_id)

    async def get_question_feed(
        self,
        user: "User",
        sort_by: str = SortByEnum.created_at.value,
        sort_order: str = SortOrderEnum.desc.value,
        limit: int = 50,
        offset: int = 0,
        is_answered: bool | None = None,
        is_active: bool | None = None,
        feed_type: "FeedTypeEnum" = FeedTypeEnum.default,
        role: "UserRoleEnum" = UserRoleEnum.all,
        other_user_id: int | None = None,
    ) -> List["QuestionResponse"]:
        """Get personalized question feed based on user's follows and profile matching."""
        stats_map: dict = {}
        if feed_type == FeedTypeEnum.default:
            questions = await self.question_repo.get_default_feed_paginated(
                user, sort_by, sort_order, limit, offset, is_answered, is_active
            )

        elif feed_type == FeedTypeEnum.me:
            questions = await self.question_repo.get_me_feed_paginated(
                user, sort_by, sort_order, limit, offset, role
            )
            # For me feed, collect statistics for all questions where user is author
            author_question_ids = [q.id for q in questions if q.author.id == user.id]
            stats_map = {}
            if author_question_ids:
                stats_data = await self.statistics_service.get_statistics_by_question_ids_for_author(
                    user.id, author_question_ids
                )
                stats_map = {stats.id: stats for stats in stats_data}
        elif feed_type == FeedTypeEnum.other:
            if not other_user_id:
                raise ConfigurationError(msg="User ID is required for other feed type")
            questions = await self.question_repo.get_other_feed_paginated(
                user, other_user_id, sort_by, sort_order, limit, offset, is_active
            )
        else:
            raise ConfigurationError(msg="Invalid feed type")

        # Apply privacy filtering
        privacy_filtered_questions = [self._apply_author_privacy(q, user) for q in questions]
        
        # Get user's answers for these questions to populate selected options
        question_ids = [q.id for q in privacy_filtered_questions]
        user_answers = await self.answer_repo.get_user_answers_for_questions(user.id, question_ids)
        
        # Populate user_selected_options for each question
        for question in privacy_filtered_questions:
            question.user_selected_options = user_answers.get(question.id)
        
        response_questions = []
        for question in privacy_filtered_questions:
            # Get statistics if user is the author
            stats = stats_map.get(question.id) if question.author.id == user.id else None
            
            response_q = QuestionResponse(
                id=question.id,
                text=question.text,
                max_options=question.max_options,
                active_till=question.active_till,
                allow_user_options=question.allow_user_options,
                gender=question.gender,
                country_id=question.country_id,
                author=question.author,
                age_range=question.age_range,
                options=question.options,
                created_at=question.created_at,
                hashtags=question.hashtags,
                user_selected_options=question.user_selected_options,
                total_answers=question.total_answers,
                # role=stats.role if stats else None,
                role=None,
                statistics=stats.statistics if stats else None,
            )
            response_questions.append(response_q)
        
        return response_questions

    async def count_unanswered(self, user: "User") -> int:
        """Count unanswered questions in user's feed."""
        return await self.question_repo.count_unanswered(user)


def build_question_service(
    statistics_service: "StatisticsService",
    question_repo: "QuestionRepository",
    option_repo: "QuestionOptionRepository",
    hashtag_link_repo: "QuestionHashtagLinkRepository",
    answer_repo: "AnswerRepository",
) -> QuestionService:
    service = QuestionService(
        statistics_service, question_repo, option_repo, hashtag_link_repo, answer_repo
    )
    return service
