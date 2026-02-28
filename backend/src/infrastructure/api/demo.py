"""Demo endpoints: hashtags and questions from the demo pool (vece user). No auth required."""
import logging
from typing import Optional

from fastapi import APIRouter, Query

from infrastructure.api.dependencies import db_dependency
from infrastructure.repository.hashtag import build_hashtag_repository
from infrastructure.repository.questions import build_question_repository
from app.schema.questions import QuestionResponse
from app.schema.hashtags import Hashtag

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/demo", tags=["demo"])


@router.get("/hashtags", response_model=list[Hashtag])
async def get_demo_hashtags(db: db_dependency):
    """Hashtags that appear in the demo question pool (vece's questions). No auth required."""
    hashtag_repo = build_hashtag_repository(db)
    return await hashtag_repo.get_hashtags_from_demo_pool()


@router.get("/questions", response_model=list[QuestionResponse])
async def get_demo_questions(
    db: db_dependency,
    hashtag_ids: Optional[str] = Query(None, description="Comma-separated hashtag IDs to filter by"),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    """Questions from the demo pool (vece user), optionally filtered by hashtags. No auth required."""
    question_repo = build_question_repository(db)
    tag_ids = None
    if hashtag_ids:
        tag_ids = [int(x.strip()) for x in hashtag_ids.split(",") if x.strip()]
    return await question_repo.get_demo_questions(hashtag_ids=tag_ids, limit=limit, offset=offset)
