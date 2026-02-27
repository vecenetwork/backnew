from typing import TYPE_CHECKING

from sqlalchemy import select, delete, insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import selectinload

from app.exceptions import Missing
from app.orm.questions import AnswerORM, AnswerOptionORM
from app.schema.questions import AnswerOption, Answer

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AnswerRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    async def create(
        self, question_id: int, user_id: int, options: list[int] | None = None, *, commit: bool = True
    ) -> Answer:
        """Create a new answer for a question by a user"""
        new_answer = AnswerORM(
            question_id=question_id,
            user_id=user_id,
        )
        self.db.add(new_answer)
        await self.db.flush()  # Ensures `obj.id` is populated

        if options:
            values = [
                {"answer_id": new_answer.id, "option_id": option_id}
                for option_id in options
            ]
            stmt = insert(AnswerOptionORM).values(values)
            await self.db.execute(stmt)
            await self.db.refresh(new_answer)

        # Load the full question data
        await self.db.refresh(new_answer, ["question"])
        
        if commit:
            await self.db.commit()
            
        return Answer.model_validate(new_answer)

    async def get_by_id(self, answer_id: int) -> Answer:
        """Get a single answer by ID"""
        stmt = (
            select(AnswerORM)
            .where(AnswerORM.id == answer_id)
            .options(selectinload(AnswerORM.question))
        )
        result = await self.db.execute(stmt)
        try:
            answer = result.scalar_one()
        except NoResultFound:
            raise Missing(f"Answer not found with id={answer_id}")
            
        return Answer.model_validate(answer)

    async def get_by_user_and_question(self, user_id: int, question_id: int) -> Answer:
        """Check if a user has already answered a specific question"""
        stmt = (
            select(AnswerORM)
            .where(
                (AnswerORM.question_id == question_id) & (AnswerORM.user_id == user_id)
            )
            .options(selectinload(AnswerORM.question))
        )
        result = await self.db.execute(stmt)
        answer = result.scalars().first()
        if not answer:
            raise Missing("Answer not found")
            
        return Answer.model_validate(answer)

    async def get_by_question_id_paginated(
        self, question_id: int, limit: int, offset: int
    ) -> list[Answer]:
        """Get all answers for a question"""
        stmt = (
            select(AnswerORM)
            .where(AnswerORM.question_id == question_id)
            .options(selectinload(AnswerORM.question))
            .limit(limit)
            .offset(offset)
        )
        result = await self.db.execute(stmt)
        answers = result.scalars().all()
            
        return [Answer.model_validate(answer) for answer in answers]

    async def get_user_answers_for_questions(
        self, user_id: int, question_ids: list[int]
    ) -> dict[int, list[int]]:
        """Get user's selected option IDs for multiple questions.
        Returns dict mapping question_id -> list of selected option_ids"""
        if not question_ids:
            return {}

        stmt = (
            select(AnswerORM)
            .where(
                (AnswerORM.user_id == user_id) &
                (AnswerORM.question_id.in_(question_ids))
            )
        )
        result = await self.db.execute(stmt)
        answers = result.scalars().all()

        # Create mapping of question_id -> list of selected option_ids
        question_to_options = {}
        for answer in answers:
            option_ids = [opt.option_id for opt in answer.options]
            question_to_options[answer.question_id] = option_ids

        return question_to_options

    async def delete(self, answer_id: int, *, commit: bool = True):
        stmt = select(AnswerORM).where(AnswerORM.id == answer_id)
        result = await self.db.execute(stmt)
        try:
            question = result.scalar_one()
        except NoResultFound:
            raise Missing(f"Answer with id {answer_id} not found")

        await self.db.delete(question)
        if commit:
            await self.db.commit()


class AnswerOptionRepository:
    def __init__(self, db: "AsyncSession"):
        self.db = db

    async def bulk_create(self, answer_id: int, option_ids: list[int], *, commit: bool = True):
        """Assign multiple options to an answer"""
        if not option_ids:
            return

        values = [
            {"answer_id": answer_id, "option_id": option_id} for option_id in option_ids
        ]
        stmt = insert(AnswerOptionORM).values(values)
        await self.db.execute(stmt)
        if commit:
            await self.db.commit()

    async def get_by_ids(self, answer_option_ids: list[int]) -> list[AnswerOption]:
        stmt = select(AnswerOptionORM).where(
            AnswerOptionORM.option_id.in_(answer_option_ids)
        )
        result = await self.db.execute(stmt)
        options = result.scalars().all()

        found_ids = {option.option_id for option in options}
        missing_ids = set(answer_option_ids) - found_ids

        if missing_ids:
            raise Missing(f"Options not found for IDs: {sorted(missing_ids)}")

        return [AnswerOption.model_validate(option) for option in options]

    async def get_by_answer_id(self, answer_id: int) -> list[AnswerOption]:
        """Retrieve all selected options for a given answer"""
        stmt = select(AnswerOptionORM).where(AnswerOptionORM.answer_id == answer_id)
        result = await self.db.execute(stmt)
        options = result.scalars().all()
        if not options:
            raise Missing(f"Options not found for answer {answer_id}")
        return [AnswerOption.model_validate(option) for option in options]

    async def delete_by_answer_id(self, answer_id: int, *, commit: bool = True):
        """Remove all options for a given answer (if editing is allowed)"""
        stmt = delete(AnswerOptionORM).where(AnswerOptionORM.answer_id == answer_id)
        await self.db.execute(stmt)
        if commit:
            await self.db.commit()


def build_answer_repository(db: "AsyncSession") -> AnswerRepository:
    repo = AnswerRepository(db)
    return repo


def build_answer_option_repository(db: "AsyncSession") -> AnswerOptionRepository:
    repo = AnswerOptionRepository(db)
    return repo
