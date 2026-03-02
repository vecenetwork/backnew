import logging
from typing import TYPE_CHECKING, Annotated

from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer

from app.exceptions import Missing, InvalidToken
from app.services.answers import build_answer_service
from app.services.email.email import build_email_service
from app.services.email.verification import build_verification_service
from app.services.hashtags import build_hashtag_service
from app.services.hashtag_suggestion import build_hashtag_suggestion_service
from app.services.questions import build_question_service
from app.services.similarity import build_similarity_service
from app.services.statistics import build_statistics_service
from app.services.subscription import build_subscription_service
from app.services.user import build_user_service
from app.services.waitlist import build_waitlist_service
from app.services.search import build_search_service
from infrastructure.database import db_dependency
from infrastructure.repository.answers import (
    build_answer_repository,
    build_answer_option_repository,
)
from infrastructure.repository.hashtag import build_hashtag_repository, build_question_hashtag_repository
from infrastructure.repository.questions import (
    build_question_repository,
    build_question_option_repository,
)
from infrastructure.repository.similarity.repo import build_similarity_repository
from infrastructure.repository.stats.repo import build_statistics_repository
from infrastructure.repository.subscriptions import build_subscription_repository
from infrastructure.repository.user import build_user_repository
from infrastructure.repository.user_settings import build_user_settings_repository
from infrastructure.repository.pending_registration import build_pending_registration_repository
from infrastructure.repository.waitlist import build_waitlist_repository

if TYPE_CHECKING:
    from app.schema.user import User
    from app.services.answers import AnswerService
    from app.services.questions import QuestionService
    from app.services.user import UserService
    from app.services.statistics import StatisticsService
    from app.services.subscription import SubscriptionService
    from app.services.hashtags import HashtagService
    from app.services.hashtag_suggestion import HashtagSuggestionService
    from app.services.similarity import SimilarityService
    from app.services.waitlist import WaitlistService
    from app.services.search import SearchService

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
token_dependency = Annotated[str, Depends(oauth2_scheme)]


def get_app(request: Request) -> "FastAPI":
    return request.app


app_dep = Annotated["FastAPI", Depends(get_app)]


def get_user_service(db: db_dependency) -> "UserService":
    user_repo = build_user_repository(db)
    user_settings_repo = build_user_settings_repository(db)
    pending_repo = build_pending_registration_repository(db)
    email_service = build_email_service()
    verification_service = build_verification_service(email_service)
    subscription_repo = build_subscription_repository(db)
    similarity_repo = build_similarity_repository(db, subscription_repo)
    return build_user_service(
        user_repo, user_settings_repo, verification_service, similarity_repo, subscription_repo, pending_repo
    )


user_service_dep = Annotated["UserService", Depends(get_user_service)]


async def current_user(
    token: token_dependency,
    user_service: user_service_dep,
) -> "User":
    try:
        user = await user_service.get_current_user(token)
        return user
    except Missing as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.detail)
    except InvalidToken as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=exc.detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


current_user_dep = Annotated["User", Depends(current_user)]


def get_subscription_service(db: db_dependency) -> "SubscriptionService":
    subscription_repo = build_subscription_repository(db)
    subscription_service = build_subscription_service(subscription_repo)
    return subscription_service


subscription_service_dep = Annotated[
    "SubscriptionService", Depends(get_subscription_service)
]


def get_hashtag_service(db: db_dependency) -> "HashtagService":
    hashtag_repo = build_hashtag_repository(db)
    hashtag_service = build_hashtag_service(hashtag_repo)
    return hashtag_service


hashtag_service_dep = Annotated["HashtagService", Depends(get_hashtag_service)]


def get_hashtag_suggestion_service(db: db_dependency) -> "HashtagSuggestionService":
    hashtag_repo = build_hashtag_repository(db)
    return build_hashtag_suggestion_service(hashtag_repo)


hashtag_suggestion_service_dep = Annotated[
    "HashtagSuggestionService", Depends(get_hashtag_suggestion_service)
]


def get_statistics_service(db: db_dependency) -> "StatisticsService":
    statistics_repo = build_statistics_repository(db)
    statistics_service = build_statistics_service(statistics_repo)
    return statistics_service


statistics_service_dep = Annotated["StatisticsService", Depends(get_statistics_service)]


def get_question_service(
    db: db_dependency,
    statistics_service: statistics_service_dep,
) -> "QuestionService":
    question_repo = build_question_repository(db)
    question_option_repo = build_question_option_repository(db)
    hashtag_link_repo = build_question_hashtag_repository(db)
    answer_repo = build_answer_repository(db)
    service = build_question_service(
        statistics_service, question_repo, question_option_repo, hashtag_link_repo, answer_repo
    )
    return service


question_service_dep = Annotated["QuestionService", Depends(get_question_service)]


def get_answer_service(
    db: db_dependency, question_service: question_service_dep
) -> "AnswerService":
    # TODO: replace question service build with deop
    question_repo = build_question_repository(db)
    question_option_repo = build_question_option_repository(db)
    answer_repo = build_answer_repository(db)
    answer_option_repo = build_answer_option_repository(db)
    service = build_answer_service(
        answer_repo=answer_repo,
        answer_option_repo=answer_option_repo,
        question_option_repo=question_option_repo,
        question_service=question_service,
        question_repo=question_repo,
    )
    return service


answer_service_dep = Annotated["AnswerService", Depends(get_answer_service)]


def get_similarity_service(
    db: db_dependency,
) -> "SimilarityService":
    # TODO: replace question service build with deop
    subscription_repo = build_subscription_repository(db)
    repo = build_similarity_repository(db, subscription_repo)
    service = build_similarity_service(
        repo=repo,
    )
    return service


similarity_service_dep = Annotated["SimilarityService", Depends(get_similarity_service)]


def get_waitlist_service(
    db: db_dependency,
) -> "WaitlistService":
    # TODO: replace question service build with deop
    repo = build_waitlist_repository(db)
    email_service = build_email_service()
    service = build_waitlist_service(
        repo=repo,
        email_service=email_service,
    )
    return service


waitlist_service_dep = Annotated["WaitlistService", Depends(get_waitlist_service)]


async def get_search_service(
    db: db_dependency,
) -> 'SearchService':
    hashtag_repo = build_hashtag_repository(db)
    question_repo = build_question_repository(db)
    user_repo = build_user_repository(db)
    return build_search_service(
        hashtag_repo=hashtag_repo,
        question_repo=question_repo,
        user_repo=user_repo,
    )

search_service_dep = Annotated['SearchService', Depends(get_search_service)]
