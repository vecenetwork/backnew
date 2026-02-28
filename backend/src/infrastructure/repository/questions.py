import logging
from typing import TYPE_CHECKING, Optional, List, Tuple, Sequence
from datetime import datetime

from sqlalchemy import select, asc, desc, and_, or_, text, update, func
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import selectinload, aliased
from sqlalchemy.sql import Select
from sqlalchemy.dialects.postgresql import Range

from app.exceptions import Missing
from app.orm.questions import QuestionORM, QuestionOptionORM, AnswerORM, QuestionHashtagLinkORM
from app.orm.user import UserORM, UserSettingsORM
from app.orm.subscriptions import SubscriptionORM
from app.schema.questions import (
    Question,
    QuestionOption,
    QuestionCreate,
    QuestionOptionCreateInternal,
    QuestionResponse,
)
from app.schema.enums import SortOrderEnum, SortByEnum, UserRoleEnum
from app.schema.user import ShowQuestionResultsEnum
from infrastructure.repository.utils import log_query

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from app.schema.user import User

logger = logging.getLogger()


class QuestionRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    def _add_base_joins(self, stmt: Select) -> Select:
        """Add common joins for question queries."""
        return stmt.options(
            selectinload(QuestionORM.author).selectinload(UserORM.country),
            selectinload(QuestionORM.author).selectinload(UserORM.settings),
            selectinload(QuestionORM.options),
            selectinload(QuestionORM.hashtags)
        )

    async def _add_hashtag_subscription_status(
        self,
        question: Question,
        current_user: "User"
    ) -> None:
        """Add subscription status to hashtags in a question."""
        hashtag_ids = [h.id for h in question.hashtags]
        if hashtag_ids:
            subscriptions = await self.db.execute(
                select(SubscriptionORM.subscribed_to_id)
                .where(
                    and_(
                        SubscriptionORM.subscriber_id == current_user.id,
                        SubscriptionORM.subscribed_to_type == "hashtag",
                        SubscriptionORM.subscribed_to_id.in_(hashtag_ids)
                    )
                )
            )
            subscribed_hashtag_ids = {row[0] for row in subscriptions.fetchall()}

            # Update is_subscribed for each hashtag
            for hashtag in question.hashtags:
                hashtag.is_subscribed = hashtag.id in subscribed_hashtag_ids

    async def _add_subscription_status(
        self,
        question: Question,
        current_user: "User"
    ) -> None:
        """Add subscription status to question author and hashtags."""
        # Add subscription status for hashtags
        await self._add_hashtag_subscription_status(question, current_user)

        # Add subscription status for author
        if question.author.id != current_user.id:  # Don't check subscription to self
            subscription = await self.db.execute(
                select(SubscriptionORM.id)
                .where(
                    and_(
                        SubscriptionORM.subscriber_id == current_user.id,
                        SubscriptionORM.subscribed_to_id == question.author.id,
                        SubscriptionORM.subscribed_to_type == "user"
                    )
                )
            )
            question.author.is_subscribed = subscription.scalar() is not None

    def _add_demography_conditions(self, current_user: "User") -> List:
        """Add demographic filtering conditions based on user profile."""
        conditions = []

        # Age matching: if question has age filter, user's age must be within range
        if current_user.birthday:
            age_condition = or_(
                QuestionORM.age.is_(None),  # No age filter
                text("CAST(EXTRACT(YEAR FROM AGE(CURRENT_DATE, :user_birthday)) AS INTEGER) <@ age").bindparams(user_birthday=current_user.birthday)
            )
            conditions.append(age_condition)

        # Gender matching: if question has gender filter, user's gender must be included
        gender_condition = or_(
            QuestionORM.gender.is_(None),  # No gender filter
            QuestionORM.gender.op('@>')([current_user.gender.value])  # User gender is in allowed list
        )
        conditions.append(gender_condition)

        # Country matching: if question has country filter, user's country must be included
        country_condition = or_(
            QuestionORM.country_id.is_(None),  # No country filter
            QuestionORM.country_id.op('@>')([current_user.country.id])  # User country is in allowed list
        )
        conditions.append(country_condition)

        return conditions

    def _add_active_filter(self, stmt: Select, is_active: Optional[bool]) -> Tuple[Select, List]:
        """Add filtering conditions for active/inactive questions."""
        conditions = []
        if is_active is True:
            conditions.append(QuestionORM.active_till > datetime.now())
        elif is_active is False:
            conditions.append(QuestionORM.active_till <= datetime.now())
        return stmt, conditions

    def _add_privacy_conditions(self, stmt: Select, current_user: "User", other_user_id: int) -> Tuple[Select, List]:
        """Add privacy-related conditions for viewing expired questions."""
        conditions = []

        # Join for user settings
        stmt = stmt.outerjoin(
            UserSettingsORM,
            QuestionORM.author_id == UserSettingsORM.user_id
        )

        # For checking if current user follows the author
        author_follower_alias = aliased(SubscriptionORM)
        stmt = stmt.outerjoin(
            author_follower_alias,
            and_(
                author_follower_alias.subscriber_id == current_user.id,
                author_follower_alias.subscribed_to_id == other_user_id,
                author_follower_alias.subscribed_to_type == "user"
            )
        )

        # For checking if author follows the current user
        author_following_alias = aliased(SubscriptionORM)
        stmt = stmt.outerjoin(
            author_following_alias,
            and_(
                author_following_alias.subscriber_id == other_user_id,
                author_following_alias.subscribed_to_id == current_user.id,
                author_following_alias.subscribed_to_type == "user"
            )
        )

        privacy_condition = or_(
            UserSettingsORM.show_question_results == ShowQuestionResultsEnum.all.value,
            and_(
                UserSettingsORM.show_question_results == ShowQuestionResultsEnum.people_i_follow.value,
                author_following_alias.id.is_not(None)
            ),
            and_(
                UserSettingsORM.show_question_results == ShowQuestionResultsEnum.people_following_me.value,
                author_follower_alias.id.is_not(None)
            ),
            and_(
                UserSettingsORM.show_question_results == ShowQuestionResultsEnum.all_connections.value,
                or_(
                    author_follower_alias.id.is_not(None),
                    author_following_alias.id.is_not(None)
                )
            )
        )

        conditions.append(privacy_condition)
        return stmt, conditions

    def _apply_sorting_and_pagination(
        self,
        stmt: Select,
        sort_by: str,
        sort_order: str,
        limit: int,
        offset: int
    ) -> Select:
        """Apply sorting and pagination to the query."""
        # Apply Sorting
        sort_column = getattr(QuestionORM, sort_by, QuestionORM.created_at)
        if sort_order == SortOrderEnum.asc.value:
            stmt = stmt.order_by(asc(sort_column))
        else:
            stmt = stmt.order_by(desc(sort_column))

        # Apply Pagination
        stmt = stmt.limit(limit).offset(offset)

        # Add DISTINCT to avoid duplicates from joins
        stmt = stmt.distinct()

        return stmt

    async def _process_questions_result(
        self,
        questions_orm: Sequence[QuestionORM],
        current_user: "User",
        stmt: Optional[Select] = None
    ) -> List[Question]:
        """Process ORM question results into validated Question models."""
        if not questions_orm:
            if stmt is not None:
                logger.warning("No questions found")
                log_query(stmt)
            return []

        questions = []
        for question_orm in questions_orm:
            validated_question = Question.model_validate(question_orm)
            validated_question.age_range = question_orm.age_range

            await self._add_subscription_status(validated_question, current_user)

            questions.append(validated_question)

        return questions

    async def create(self, question: "QuestionCreate") -> Question:
        question_options = question.options

        age_range = None
        if question.age:
            age_range = Range(question.age.start, question.age.end, bounds='[]')

        new_question = QuestionORM(
            text=question.text,
            max_options=question.max_options,
            active_till=question.active_till,
            allow_user_options=question.allow_user_options,
            gender=question.gender,
            country_id=question.country_id,
            age=age_range,
            author_id=question.author_id,
        )
        self.db.add(new_question)
        await self.db.flush()

        for option in question_options:
            option_author = question.author_id
            by_question_author = option_author == question.author_id

            new_option = QuestionOptionORM(
                question_id=new_question.id,
                text=option.text,
                position=option.position,
                author_id=option_author,
                by_question_author=by_question_author,
            )
            self.db.add(new_option)

        await self.db.commit()

        stmt = (
            select(QuestionORM)
            .where(QuestionORM.id == new_question.id)
        )
        stmt = self._add_base_joins(stmt)

        result = await self.db.execute(stmt)
        new_question = result.scalar_one()
        return Question.model_validate(new_question)

    async def get_by_id(self, question_id: int, current_user: Optional["User"] = None) -> Question:
        stmt = (
            select(QuestionORM)
            .where(QuestionORM.id == question_id)
        )
        stmt = self._add_base_joins(stmt)

        result = await self.db.execute(stmt)
        try:
            question_orm = result.scalar_one()
        except NoResultFound:
            raise Missing(f"Question with id {question_id} not found")

        validated_question = Question.model_validate(question_orm)
        validated_question.age_range = question_orm.age_range

        # Add subscription status for hashtags and author if current_user is provided
        if current_user:
            await self._add_subscription_status(validated_question, current_user)

        return validated_question

    async def get_all_paginated(
        self,
        created_by: Optional[int] = None,
        answered_by: Optional[int] = None,
        sort_by: str = SortByEnum.created_at.value,
        sort_order: str = SortOrderEnum.desc.value,
        limit: int = 20,
        offset: int = 0,
        current_user: Optional["User"] = None,
    ) -> List[Question]:
        stmt = select(QuestionORM)

        # Apply filters
        if created_by is not None:
            stmt = stmt.where(QuestionORM.author_id == created_by)
        if answered_by is not None:
            answer_subq = (
                select(AnswerORM.question_id)
                .where(AnswerORM.user_id == answered_by)
                .distinct()
                .scalar_subquery()
            )
            stmt = stmt.where(QuestionORM.id.in_(answer_subq))

        # Apply sorting
        sort_column = getattr(QuestionORM, sort_by, QuestionORM.created_at)
        if sort_order == SortOrderEnum.desc.value:
            stmt = stmt.order_by(desc(sort_column))
        else:
            stmt = stmt.order_by(asc(sort_column))

        # Apply pagination
        stmt = stmt.limit(limit).offset(offset)

        # Add joins
        stmt = self._add_base_joins(stmt)

        result = await self.db.execute(stmt)
        questions_orm = result.scalars().all()
        if not questions_orm:
            logger.warning("No questions found")
            log_query(stmt)
            return []

        questions = []
        for question_orm in questions_orm:
            validated_question = Question.model_validate(question_orm)
            validated_question.age_range = question_orm.age_range

            if current_user:
                await self._add_subscription_status(validated_question, current_user)

            questions.append(validated_question)

        return questions

    async def get_default_feed_paginated(
        self,
        current_user: "User",
        sort_by: str = SortByEnum.created_at.value,
        sort_order: str = SortOrderEnum.desc.value,
        limit: int = 20,
        offset: int = 0,
        is_answered: Optional[bool] = None,
        is_active: Optional[bool] = None,
    ) -> List[Question]:
        """Get personalized question feed based on user follows and profile matching with demography filtering."""
        stmt = select(QuestionORM)

        # Aliases for complex joins
        hashtag_subscription_alias = aliased(SubscriptionORM)
        author_subscription_alias = aliased(SubscriptionORM)
        question_hashtag_alias = aliased(QuestionHashtagLinkORM)
        user_answer_alias = aliased(AnswerORM)

        # Join for hashtag follows
        stmt = stmt.outerjoin(
            question_hashtag_alias,
            QuestionORM.id == question_hashtag_alias.question_id
        ).outerjoin(
            hashtag_subscription_alias,
            and_(
                question_hashtag_alias.hashtag_id == hashtag_subscription_alias.subscribed_to_id,
                hashtag_subscription_alias.subscribed_to_type == "hashtag",
                hashtag_subscription_alias.subscriber_id == current_user.id
            )
        )

        # Join for author follows
        stmt = stmt.outerjoin(
            author_subscription_alias,
            and_(
                QuestionORM.author_id == author_subscription_alias.subscribed_to_id,
                author_subscription_alias.subscribed_to_type == "user",
                author_subscription_alias.subscriber_id == current_user.id
            )
        )

        # Join for user answers
        stmt = stmt.outerjoin(
            user_answer_alias,
            and_(
                QuestionORM.id == user_answer_alias.question_id,
                user_answer_alias.user_id == current_user.id
            )
        )

        where_conditions = []

        # Follow condition
        follow_condition = or_(
            hashtag_subscription_alias.id.is_not(None),
            author_subscription_alias.id.is_not(None)
        )
        where_conditions.append(follow_condition)

        # Add demography conditions
        where_conditions.extend(self._add_demography_conditions(current_user))

        # Add answer filtering condition
        if is_answered is False:
            where_conditions.append(user_answer_alias.id.is_(None))

        # Add active filtering condition
        stmt, active_conditions = self._add_active_filter(stmt, is_active)
        where_conditions.extend(active_conditions)

        # Apply all conditions
        if where_conditions:
            stmt = stmt.where(and_(*where_conditions))

        # Apply sorting and pagination
        stmt = self._apply_sorting_and_pagination(stmt, sort_by, sort_order, limit, offset)

        # Add base joins
        stmt = self._add_base_joins(stmt)

        result = await self.db.execute(stmt)
        questions_orm = result.scalars().all()

        return await self._process_questions_result(questions_orm, current_user)

    async def get_me_feed_paginated(
        self,
        current_user: "User",
        sort_by: str = SortByEnum.created_at.value,
        sort_order: str = SortOrderEnum.desc.value,
        limit: int = 20,
        offset: int = 0,
        role: UserRoleEnum = UserRoleEnum.all,
    ) -> List[Question]:
        """Get user's own questions without demography filtering."""
        stmt = select(QuestionORM)
        where_conditions = []

        if role == UserRoleEnum.author:
            where_conditions.append(QuestionORM.author_id == current_user.id)
        elif role == UserRoleEnum.respondent:
            stmt = stmt.join(AnswerORM).where(AnswerORM.user_id == current_user.id)
        else:  # role == UserRoleEnum.all
            stmt = stmt.outerjoin(AnswerORM, QuestionORM.id == AnswerORM.question_id)
            where_conditions.append(
                or_(
                    QuestionORM.author_id == current_user.id,
                    and_(AnswerORM.user_id == current_user.id, AnswerORM.id.is_not(None))
                )
            )

        # Apply conditions
        if where_conditions:
            stmt = stmt.where(and_(*where_conditions))

        # Apply sorting and pagination
        stmt = self._apply_sorting_and_pagination(stmt, sort_by, sort_order, limit, offset)

        # Add base joins
        stmt = self._add_base_joins(stmt)

        result = await self.db.execute(stmt)
        questions_orm = result.scalars().all()

        return await self._process_questions_result(questions_orm, current_user, stmt)

    async def get_other_feed_paginated(
        self,
        current_user: "User",
        other_user_id: int,
        sort_by: str = SortByEnum.created_at.value,
        sort_order: str = SortOrderEnum.desc.value,
        limit: int = 20,
        offset: int = 0,
        is_active: Optional[bool] = None,
    ) -> List[Question]:
        """Get questions created by another user."""
        stmt = select(QuestionORM)
        where_conditions = []

        # Questions created by the specified user
        where_conditions.append(QuestionORM.author_id == other_user_id)

        # Add demography conditions
        where_conditions.extend(self._add_demography_conditions(current_user))

        # Handle active/inactive questions with privacy settings
        stmt, privacy_conditions = self._add_privacy_conditions(stmt, current_user, other_user_id)

        if is_active is True:
            where_conditions.append(QuestionORM.active_till > datetime.now())
        elif is_active is False:
            where_conditions.append(QuestionORM.active_till <= datetime.now())
            where_conditions.extend(privacy_conditions)
        else:  # is_active is None
            where_conditions.append(
                or_(
                    QuestionORM.active_till > datetime.now(),
                    and_(
                        QuestionORM.active_till <= datetime.now(),
                        *privacy_conditions
                    )
                )
            )

        # Apply conditions
        if where_conditions:
            stmt = stmt.where(and_(*where_conditions))

        # Apply sorting and pagination
        stmt = self._apply_sorting_and_pagination(stmt, sort_by, sort_order, limit, offset)

        # Add base joins
        stmt = self._add_base_joins(stmt)

        result = await self.db.execute(stmt)
        questions_orm = result.scalars().all()

        return await self._process_questions_result(questions_orm, current_user, stmt)

    async def update(self, question_id: int, *, commit: bool = True, **kwargs) -> None:
        """Update a question."""
        if not kwargs:
            return  # No fields to update

        stmt = (
            update(QuestionORM)
            .where(QuestionORM.id == question_id)
            .values(**kwargs)
        )
        result = await self.db.execute(stmt)
        if result.rowcount == 0:  # type: ignore[attr-defined]
            raise Missing(f"Question with id {question_id} not found or no update was made.")

        if commit:
            await self.db.commit()

    async def delete(self, question_id: int):
        async with self.db.begin():
            stmt = select(QuestionORM).where(QuestionORM.id == question_id)
            result = await self.db.execute(stmt)
            try:
                question = result.scalar_one()
            except NoResultFound:
                raise Missing(f"Question with id {question_id} not found")

            await self.db.delete(question)
        await self.db.commit()

    async def get_by_ids(self, question_ids: List[int], current_user: Optional["User"] = None) -> List[Question]:
        """Get multiple questions by their IDs."""
        if not question_ids:
            return []

        stmt = (
            select(QuestionORM)
            .where(QuestionORM.id.in_(question_ids))
        )
        stmt = self._add_base_joins(stmt)

        result = await self.db.execute(stmt)
        questions_orm = result.scalars().all()

        questions = []
        for question_orm in questions_orm:
            validated_question = Question.model_validate(question_orm)
            validated_question.age_range = question_orm.age_range

            if current_user:
                await self._add_subscription_status(validated_question, current_user)

            questions.append(validated_question)

        return questions

    async def search(
        self,
        query: str,
        limit: int,
        current_user: Optional["User"] = None
    ) -> list[QuestionResponse]:
        """Search questions by text content."""
        # Add wildcards for LIKE query and escape special characters
        search_pattern = f"%{query.replace('%', '\\%').replace('_', '\\_')}%"

        stmt = (
            select(QuestionORM)
            .where(QuestionORM.text.ilike(search_pattern))
            .limit(limit)
        )

        # Add common joins
        stmt = self._add_base_joins(stmt)

        result = await self.db.execute(stmt)
        questions_orm = result.scalars().all()

        questions = []
        for question_orm in questions_orm:
            # if current_user:
            #     await self._add_subscription_status(question_orm, current_user)
            validated_question = QuestionResponse.model_validate(question_orm)
            validated_question.age_range = question_orm.age_range
            questions.append(validated_question)

        return questions

    async def count_unanswered(self, current_user: "User") -> int:
        """Count unanswered questions in user's feed (questions from followed hashtags/users)."""
        # Aliases for complex joins
        hashtag_subscription_alias = aliased(SubscriptionORM)
        author_subscription_alias = aliased(SubscriptionORM)
        question_hashtag_alias = aliased(QuestionHashtagLinkORM)
        user_answer_alias = aliased(AnswerORM)

        stmt = select(func.count(QuestionORM.id.distinct()))

        # Join for hashtag follows
        stmt = stmt.outerjoin(
            question_hashtag_alias,
            QuestionORM.id == question_hashtag_alias.question_id
        ).outerjoin(
            hashtag_subscription_alias,
            and_(
                question_hashtag_alias.hashtag_id == hashtag_subscription_alias.subscribed_to_id,
                hashtag_subscription_alias.subscribed_to_type == "hashtag",
                hashtag_subscription_alias.subscriber_id == current_user.id
            )
        )

        # Join for author follows
        stmt = stmt.outerjoin(
            author_subscription_alias,
            and_(
                QuestionORM.author_id == author_subscription_alias.subscribed_to_id,
                author_subscription_alias.subscribed_to_type == "user",
                author_subscription_alias.subscriber_id == current_user.id
            )
        )

        # Join for user answers
        stmt = stmt.outerjoin(
            user_answer_alias,
            and_(
                QuestionORM.id == user_answer_alias.question_id,
                user_answer_alias.user_id == current_user.id
            )
        )

        where_conditions = []

        # Follow condition - must follow either hashtag or author
        follow_condition = or_(
            hashtag_subscription_alias.id.is_not(None),
            author_subscription_alias.id.is_not(None)
        )
        where_conditions.append(follow_condition)

        # Add demography conditions
        where_conditions.extend(self._add_demography_conditions(current_user))

        # Unanswered condition
        where_conditions.append(user_answer_alias.id.is_(None))

        # Active questions only
        where_conditions.append(QuestionORM.active_till > datetime.now())

        # Apply all conditions
        stmt = stmt.where(and_(*where_conditions))

        result = await self.db.execute(stmt)
        count = result.scalar()
        return count or 0


class QuestionOptionRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    async def create(self, option: "QuestionOptionCreateInternal", commit: bool = True) -> QuestionOption:
        new_option = QuestionOptionORM(
            text=option.text,
            position=option.position,
            question_id=option.question_id,
            author_id=option.author_id,
            by_question_author=option.by_question_author,
        )

        self.db.add(new_option)
        await self.db.flush()
        await self.db.refresh(new_option)
        if commit:
            await self.db.commit()

        validated_option = QuestionOption.model_validate(new_option)
        return validated_option

    async def get_by_id(self, option_id: int) -> QuestionOption:
        async with self.db.begin():
            stmt = select(QuestionOptionORM).where(QuestionOptionORM.id == option_id)
            result = await self.db.execute(stmt)
            try:
                option = result.scalar_one()
            except NoResultFound:
                raise Missing(f"Option with id {option_id} not found")

        validated_option = QuestionOption.model_validate(option)
        return validated_option

    async def get_by_ids(self, question_option_ids: list[int]) -> list[QuestionOption]:
        stmt = select(QuestionOptionORM).where(
            QuestionOptionORM.id.in_(question_option_ids)
        )
        result = await self.db.execute(stmt)
        options = result.scalars().all()

        # logger.info(options)

        found_ids = {option.id for option in options}
        missing_ids = set(question_option_ids) - found_ids

        if missing_ids:
            raise Missing(f"Options not found for IDs: {sorted(missing_ids)}")

        return [QuestionOption.model_validate(option) for option in options]

    async def get_by_question_id(self, question_id: int) -> list[QuestionOption]:
        stmt = select(QuestionOptionORM).where(
            QuestionOptionORM.question_id == question_id
        )
        result = await self.db.execute(stmt)
        options = result.scalars().all()

        return [QuestionOption.model_validate(option) for option in options]

    async def get_by_question_id_with_lock(self, question_id: int) -> list[QuestionOption]:
        stmt = select(QuestionOptionORM).where(
            QuestionOptionORM.question_id == question_id
        ).with_for_update()
        result = await self.db.execute(stmt)
        options = result.scalars().all()

        return [QuestionOption.model_validate(option) for option in options]

    async def update(self, option_id: int, *, commit: bool = True, **kwargs) -> QuestionOption | None:
        if not kwargs:
            return None

        stmt = (
            update(QuestionOptionORM)
            .where(QuestionOptionORM.id == option_id)
            .values(**kwargs)
            .returning(QuestionOptionORM)
        )
        result = await self.db.execute(stmt)
        option = result.scalar_one_or_none()
        if option is None:
            raise Missing(f"Question option with id {option_id} not found or no update was made.")

        if commit:
            await self.db.commit()

        return QuestionOption.model_validate(option)

    async def delete(self, option_id: int):
        async with self.db.begin():
            stmt = select(QuestionOptionORM).where(QuestionOptionORM.id == option_id)
            result = await self.db.execute(stmt)
            try:
                option = result.scalar_one()
            except NoResultFound:
                raise Missing(f"Question option with id {option_id} not found")

            await self.db.delete(option)
        await self.db.commit()


def build_question_repository(db: "AsyncSession") -> QuestionRepository:
    repo = QuestionRepository(db)
    return repo


def build_question_option_repository(db: "AsyncSession") -> QuestionOptionRepository:
    repo = QuestionOptionRepository(db)
    return repo
