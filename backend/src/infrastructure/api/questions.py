"""
POST /questions
GET /questions
GET /questions/{question_id}
PUT /questions/{question_id}
DELETE /questions/{question_id}

POST /questions/{question_id}/options
GET /questions/{question_id}/options
GET /questions/{question_id}/options/{option_id}
PUT /questions/{question_id}/options/{option_id}
DELETE /questions/{question_id}/options/{option_id}

POST /questions/{question_id}/answers
GET /questions/{question_id}/answers
GET /questions/{question_id}/answers/{answer_id}
DELETE /questions/{question_id}/answers/{option_id}

POST /answers/{answer_id}/options
"""

from fastapi import APIRouter, HTTPException, Query, status

from app.exceptions import ApiException, Missing
from app.schema.questions import (
    Question,
    QuestionOption,
    QuestionResponse,
    QuestionCreate,
    QuestionUpdate,
    QuestionOptionCreate,
    QuestionOptionUpdate,
    Answer,
    AnswerCreate,
    AnswerOptionCreate,
    AnswerResponse,
    UnansweredCountResponse,
)
from app.services.questions import OptionMismatchError
from app.schema.statistics import QuestionStatistics, QuestionOptionStatistics
from app.schema.user import Role
from app.schema.enums import FeedTypeEnum, SortOrderEnum, SortByEnum, UserRoleEnum
from infrastructure.api.dependencies import (
    token_dependency,
    current_user_dep,
    question_service_dep,
    answer_service_dep,
)

router = APIRouter(tags=["questions"])

# ==== Questions ====


@router.post(
    "/questions",
    description="Do not add gender, country_id, age_range in request if the question does not have filters",
    status_code=status.HTTP_201_CREATED,
    response_model=QuestionResponse
)
async def create_question(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    question: QuestionCreate,
):
    try:
        new_question = await question_service.create_question(question, current_user)
    except ApiException as exc:
        exc.raise_http_exception()

    return new_question


@router.get(
    "/questions",
    response_model=list[QuestionResponse],
    summary="Retrieve a list of questions with optional filtering and sorting.",
    description="""Retrieves a list of questions. Supports filtering by questions created or answered 
    by the authenticated user. Allows sorting by different fields and in ascending or descending order.""",
)
async def get_all_questions(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    created_by: str | None = Query(
        None,
        description="Filter questions created by 'me' (the current user) or a specific user ID",
    ),
    answered_by: str | None = Query(
        None,
        description="Filter questions answered by 'me' (the current user) or a specific user ID",
    ),
    sort_by: SortByEnum = Query(
        SortByEnum.created_at,
        description="Field to sort the questions by.",
    ),
    sort_order: SortOrderEnum = Query(
        SortOrderEnum.desc,
        description="Sorting order.",
    ),
    limit: int = Query(10, ge=1, le=100, description="Number of questions to return"),
    offset: int = Query(0, ge=0, description="Number of questions to skip"),
):
    # permissions check
    if created_by:
        if created_by == "me":
            created_by_id = current_user.id
        else:
            if current_user.role != Role.admin:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="")
            else:
                created_by_id = int(created_by)
    else:
        created_by_id = None

    if answered_by:
        if answered_by == "me":
            answered_by_id = current_user.id
        else:
            if current_user.role != Role.admin:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="")
            else:
                answered_by_id = int(answered_by)
    else:
        answered_by_id = None

    try:
        questions = await question_service.get_my_questions(
            current_user, created_by_id, answered_by_id, sort_by.value, sort_order.value, limit, offset
        )
    except ApiException as exc:
        exc.raise_http_exception()

    return questions


@router.get(
    "/feed",
    response_model=list[QuestionResponse],
    summary="Retrieve a personalized question feed.",
    description="""Retrieves a personalized list of questions based on the type of feed requested.""",
)
async def get_feed(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    feed_type: FeedTypeEnum = Query(
        FeedTypeEnum.default,
        description="Type of feed to retrieve.",
    ),
    sort_by: SortByEnum = Query(
        SortByEnum.created_at,
        description="Field to sort the questions by.",
    ),
    sort_order: SortOrderEnum = Query(
        SortOrderEnum.desc,
        description="Sorting order.",
    ),
    limit: int = Query(10, ge=1, le=100, description="Number of questions to return"),
    offset: int = Query(0, ge=0, description="Number of questions to skip"),
    # Fields for 'me' feed
    stats: bool = Query(
        True,
        description="Include statistics in response (for 'me' feed)",
    ),
    role: UserRoleEnum = Query(
        UserRoleEnum.all,
        description="User's role: author / respondent or both (all) (for 'me' feed)",
    ),
    # Fields for 'default' feed
    is_answered: bool = Query(
        False,
        description="Filter questions by answered status (for 'default' feed only). If false, filter out questions already answered by user.",
    ),
    is_active: bool = Query(
        True,
        description="Filter questions by active status (for 'default' feed only). If true, filter out inactive questions (where active_till has passed).",
    ),
    # Fields for 'other' feed
    other_user_id: int | None = Query(
        None,
        description="User ID to fetch questions from (required for 'other' feed type)",
    ),
):
    try:
        questions = await question_service.get_question_feed(
            current_user,
            sort_by.value,
            sort_order.value,
            limit,
            offset,
            is_answered,
            is_active,
            feed_type,
            role,
            other_user_id,
        )
    except ApiException as exc:
        exc.raise_http_exception()

    return questions


@router.get("/questions/{question_id}", response_model=QuestionResponse)
async def get_question(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    question_id: int,
):
    try:
        question = await question_service.get_question(question_id, current_user)
    except ApiException as exc:
        exc.raise_http_exception()

    return question


@router.put(
    "/questions/{question_id}",
    response_model=Question,
    status_code=status.HTTP_200_OK,
)
async def update_question(
    question_id: int,
    question_data: QuestionUpdate,
    question_service: question_service_dep,
    current_user: current_user_dep,
):
    try:
        updated_question = await question_service.update_question(
            question_id, question_data, current_user
        )
        return updated_question
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
    except Missing as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/questions/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_question(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    question_id: int,
):
    try:
        await question_service.delete_question(question_id)
    except ApiException as exc:
        exc.raise_http_exception()


# === Question stats ===


@router.get(
    "/questions/unanswered/count",
    response_model=UnansweredCountResponse,
    summary="Get count of unanswered questions",
    description="Returns the number of unanswered questions in the user's feed (active questions from followed hashtags and users that the user hasn't answered yet).",
)
async def get_unanswered_count(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
):
    try:
        count = await question_service.count_unanswered(current_user)
    except ApiException as exc:
        exc.raise_http_exception()

    return UnansweredCountResponse(count=count)


@router.get("/questions/{question_id}/stats", response_model=QuestionStatistics)
async def get_question_stats(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    question_id: int,
):
    try:
        stats = await question_service.get_stats_for_question(current_user, question_id)
    except ApiException as exc:
        exc.raise_http_exception()

    return stats

# ==== Options ====


@router.post(
    "/questions/{question_id}/options",
    status_code=status.HTTP_201_CREATED,
    response_model=QuestionOption,
)
async def create_option(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    question_id: int,
    option: QuestionOptionCreate,
):
    try:
        question_option = await question_service.create_option(
            question_id, option, current_user
        )
    except ApiException as exc:
        exc.raise_http_exception()

    return question_option


@router.get("/questions/{question_id}/options", response_model=list[QuestionOption])
async def get_question_options(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    question_id: int,
):
    # TODO: may be add pagination here
    try:
        question_options = await question_service.get_options(question_id)
    except ApiException as exc:
        exc.raise_http_exception()
    return question_options


@router.get(
    "/questions/{question_id}/options/{option_id}", response_model=QuestionOption
)
async def get_option(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    question_id: int,
    option_id: int,
):
    try:
        question_option = await question_service.get_option(question_id, option_id)
    except ApiException as exc:
        exc.raise_http_exception()

    return question_option


@router.put(
    "/questions/{question_id}/options/{option_id}",
    response_model=QuestionOption,
    status_code=status.HTTP_200_OK,
)
async def update_option(
    question_id: int,
    option_id: int,
    option_data: QuestionOptionUpdate,
    question_service: question_service_dep,
    current_user: current_user_dep,
):
    try:
        updated_option = await question_service.update_option(
            question_id, option_id, option_data, current_user
        )
        return updated_option
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
    except (Missing, OptionMismatchError) as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete(
    "/questions/{question_id}/options/{option_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_option(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    question_id: int,
    option_id: int,
):
    try:
        await question_service.delete_option(question_id, option_id)
    except ApiException as exc:
        exc.raise_http_exception()


# === Question Option Stats ===

@router.get(
    "/options/{option_id}/stats", response_model=QuestionOptionStatistics
)
async def get_option_stats(
    token: token_dependency,
    current_user: current_user_dep,
    question_service: question_service_dep,
    option_id: int,
):
    try:
        stats = await question_service.get_stats_for_option(current_user, option_id)
    except ApiException as exc:
        exc.raise_http_exception()
    return stats


# ==== Answers ====


@router.post(
    "/questions/{question_id}/answers",
    status_code=status.HTTP_201_CREATED,
    response_model=AnswerResponse,
    description="Create an answer for a question. Can include both existing option IDs and new option objects if the question allows user options.",
)
async def create_answer(
    token: token_dependency,
    current_user: current_user_dep,
    answer_service: answer_service_dep,
    question_id: int,
    answer: AnswerCreate,
):
    try:
        new_answer = await answer_service.create_answer(question_id, answer, current_user)
    except ApiException as exc:
        exc.raise_http_exception()
    return new_answer


@router.get("/questions/{question_id}/answers", response_model=list[AnswerResponse])
async def get_answers(
    token: token_dependency,
    current_user: current_user_dep,
    answer_service: answer_service_dep,
    question_id: int,
):
    try:
        answers = await answer_service.get_answers_by_question_id_paginated(
            question_id, current_user
        )
    except ApiException as exc:
        exc.raise_http_exception()
    return answers


@router.get("/questions/{question_id}/answers/{answer_id}", response_model=AnswerResponse)
async def get_answer(
    token: token_dependency,
    current_user: current_user_dep,
    answer_service: answer_service_dep,
    question_id: int,
    answer_id: int,
):
    try:
        answer = await answer_service.get_answer_by_id(question_id, answer_id, current_user)
    except ApiException as exc:
        exc.raise_http_exception()
    return answer


@router.delete(
    "/questions/{question_id}/answers/{answer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_answer(
    token: token_dependency,
    current_user: current_user_dep,
    answer_service: answer_service_dep,
    question_id: int,
    answer_id: int,
):
    try:
        await answer_service.delete_answer(question_id, answer_id, current_user)
    except ApiException as exc:
        exc.raise_http_exception()


# ==== Answer Options ====


@router.post(
    "/answers/{answer_id}/options",
    status_code=status.HTTP_201_CREATED,
    response_model=Answer,
)
async def submit_answer_options(
    token: token_dependency,
    current_user: current_user_dep,
    answer_service: answer_service_dep,
    answer_id: int,
    payload: "AnswerOptionCreate",
):
    try:
        await answer_service.add_answer_options(answer_id, payload.ids, current_user)
    except ApiException as exc:
        exc.raise_http_exception()
