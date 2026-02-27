import logging
from typing import TYPE_CHECKING
from datetime import datetime, timezone

from app.exceptions import Unauthorized, Missing, ApiException
from app.orm.questions import QuestionORM
from app.schema.questions import Answer, AnswerCreate, QuestionOptionCreate, AnswerResponse, Question, QuestionResponse
from app.schema.user import User, Role

if TYPE_CHECKING:
    from app.services.questions import QuestionService
    from infrastructure.repository.answers import (
        AnswerRepository,
        AnswerOptionRepository,
    )
    from infrastructure.repository.questions import (
        QuestionOptionRepository,
        QuestionRepository,
    )

default_logger = logging.getLogger()


class AlreadyAnsweredError(ApiException):
    status_code = 409


class TooManyOptionsError(ApiException):
    status_code = 400


class OptionMismatchError(ApiException):
    status_code = 400


class DemographicMismatchError(ApiException):
    status_code = 403
    message = "User does not match question's demographic filters"


class QuestionExpiredError(ApiException):
    status_code = 403
    message = "Question is no longer active"


class AnswerService:
    def __init__(
        self,
        answer_repo: "AnswerRepository",
        answer_option_repo: "AnswerOptionRepository",
        question_option_repo: "QuestionOptionRepository",
        question_service: "QuestionService",
        question_repo: "QuestionRepository",
    ):
        self.answer_repo = answer_repo
        self.answer_option_repo = answer_option_repo
        self.question_option_repo = question_option_repo
        self.question_service = question_service
        self.question_repo = question_repo

    def _validate_user_demographics(self, user: User, question: Question | QuestionResponse):
        # Check gender filter
        if question.gender and user.gender not in question.gender:
            raise DemographicMismatchError("User's gender does not match question's filter")

        # Check country filter
        if question.country_id and user.country.id not in question.country_id:
            raise DemographicMismatchError("User's country does not match question's filter")

        # Check age filter
        if question.age_range:
            today = datetime.now().date()
            age = today.year - user.birthday.year - ((today.month, today.day) < (user.birthday.month, user.birthday.day))
            
            if (question.age_range.start is not None and age < question.age_range.start) or \
               (question.age_range.end is not None and age > question.age_range.end):
                raise DemographicMismatchError("User's age does not match question's filter")

    def _validate_question_active(self, question: Question | QuestionResponse):
        """Check if the question is still active based on active_till date"""
        if not question.active_till:
            default_logger.warning(f"Question {question.id} has no active_till date")
            return
            
        if question.active_till.tzinfo is None:
            # If active_till is naive, assume it's in UTC
            active_till = question.active_till.replace(tzinfo=timezone.utc)
        else:
            active_till = question.active_till
            
        now = datetime.now(timezone.utc)
        if active_till < now:
            raise QuestionExpiredError("This question has expired and is no longer accepting answers")

    def _to_response(self, answer: Answer) -> AnswerResponse:
        """Convert Answer to AnswerResponse"""
        question_response = self.question_service._question_to_response(answer.question)
        return AnswerResponse(
            id=answer.id,
            user_id=answer.user_id,
            question=question_response,
            options=answer.options,
            created_at=answer.created_at
        )

    async def create_answer(
        self, question_id: int, answer: "AnswerCreate", user: "User"
    ) -> "AnswerResponse":
        async with self.question_repo.db.begin_nested() as nested:
            try:
                await self.answer_repo.get_by_user_and_question(user.id, question_id)
            except Missing:
                pass
            else:
                raise AlreadyAnsweredError("Question already answered by user")

            question = await self.question_service.get_question(question_id, user)
            
            self._validate_question_active(question)
            
            self._validate_user_demographics(user, question)
            
            # Handle new options creation if question allows user options
            new_option_ids = []
            new_option_creates = []
            if answer.new_options:
                for text in answer.new_options:
                    new_option_creates.append(QuestionOptionCreate(text=text))
            if new_option_creates:
                if not question.allow_user_options:
                    raise TooManyOptionsError("Question does not allow user-created options")
                
                # Get existing option positions to check for conflicts
                existing_positions = {opt.position for opt in question.options}
                # Assign positions to new options if missing
                for new_option in new_option_creates:
                    if new_option.position is None:
                        # Assign the lowest available non-conflicting position starting from 1
                        pos = 1
                        while pos in existing_positions:
                            pos += 1
                        new_option.position = pos
                    if new_option.position in existing_positions:
                        raise TooManyOptionsError(f"Position conflict: {new_option.position}")
                    existing_positions.add(new_option.position)
                
                # Create new options and collect their IDs
                for new_option in new_option_creates:
                    created_option = await self.question_service.create_option(
                        question_id, new_option, user, commit=False
                    )
                    new_option_ids.append(created_option.id)
            
            # Combine existing and new option IDs
            all_option_ids = answer.options + new_option_ids
            
            # Ensure at least one option is selected
            if not all_option_ids:
                raise TooManyOptionsError("At least one option must be selected")
            
            if len(all_option_ids) > question.max_options:
                raise TooManyOptionsError(f"Too many options, max = {question.max_options}")

            # validate existing options belong to the same question
            if answer.options:
                options = await self.question_option_repo.get_by_ids(answer.options)
                for opt in options:
                    if opt.question_id != question.id:
                        raise OptionMismatchError(f"Wrong option: {opt.id}")

            new_answer = await self.answer_repo.create(
                question_id=question_id, user_id=user.id, options=all_option_ids, commit=False
            )
            await self.question_repo.update(
                question_id, total_answers=QuestionORM.total_answers + 1, commit=False
            )
            
            # Lock and fetch all options for the question to prevent race conditions.
            all_options = await self.question_option_repo.get_by_question_id_with_lock(question_id)
            selected_option_ids = set(all_option_ids)

            # Calculate the total number of selections for the question.
            # This is the sum of previous selections plus the new selections from the current answer.
            total_selections = sum(o.count for o in all_options) + len(selected_option_ids)

            # Update each option's count and percentage
            for option in all_options:
                new_count = option.count
                if option.id in selected_option_ids:
                    new_count += 1
                
                new_percentage = (new_count * 100.0 / total_selections) if total_selections > 0 else 0

                await self.question_option_repo.update(
                    option.id,
                    count=new_count,
                    percentage=new_percentage,
                    commit=False
                )

            # Get updated question with new stats and convert to response
            answer_response = self._to_response(new_answer)
            updated_question = await self.question_service.get_question(question_id, user)
            answer_response.question = updated_question

            await nested.commit()
            await self.question_repo.db.commit()
            
            return answer_response

    async def get_answer_by_id(
        self, question_id: int, answer_id: int, user: "User"
    ) -> AnswerResponse:
        answer = await self.answer_repo.get_by_id(answer_id)
        if answer.user_id != user.id:
            question = await self.question_service.get_question(question_id, user)
            if question.author.id != user.id or user.role != Role.admin:
                raise Unauthorized("Only author of question /answer can see the answer")
        return self._to_response(answer)

    async def get_answers_by_question_id_paginated(
        self, question_id, user: "User", limit: int = 50, offset: int = 0
    ) -> list[AnswerResponse]:
        question = await self.question_service.get_question(question_id, user)
        if question.author.id != user.id and user.role != Role.admin:
            raise Unauthorized("Only author can see all answers")

        answers = await self.answer_repo.get_by_question_id_paginated(
            question_id, limit=limit, offset=offset
        )
        return [self._to_response(answer) for answer in answers]

    async def delete_answer(self, question_id: int, answer_id: int, user: "User"):
        answer = await self.answer_repo.get_by_id(answer_id)
        if answer.question.id != question_id:
            raise ValueError(f"Wrong question_id: {answer}")
        if answer.user_id != user.id:
            question = await self.question_service.get_question(question_id, user)
            if question.author.id != user.id or user.role != Role.admin:
                raise Unauthorized("Only the question author or admin can delete answers")

        await self.answer_repo.delete(answer_id)

    async def add_answer_options(
        self, answer_id: int, option_ids: list[int], user: "User"
    ):
        answer = await self.answer_repo.get_by_id(answer_id)
        if answer.user_id != user.id and user.role != Role.admin:
            raise Unauthorized("Can not add options to other user's answer")
        question = await self.question_service.get_question(answer.question.id, user)

        if len(option_ids) > question.max_options:
            raise TooManyOptionsError('Maximum number of options exceeded')

        # validate options belong to the same question
        options = await self.question_option_repo.get_by_ids(option_ids)
        for opt in options:
            if opt.question_id != question.id:
                raise OptionMismatchError(f"Wrong option: {opt}")

        # create answer_option entries
        await self.answer_option_repo.bulk_create(
            answer_id=answer.id, option_ids=option_ids
        )


def build_answer_service(
    answer_repo: "AnswerRepository",
    answer_option_repo: "AnswerOptionRepository",
    question_option_repo: "QuestionOptionRepository",
    question_service: "QuestionService",
    question_repo: "QuestionRepository",
) -> AnswerService:
    answer_service = AnswerService(
        answer_repo,
        answer_option_repo,
        question_option_repo,
        question_service,
        question_repo,
    )
    return answer_service
