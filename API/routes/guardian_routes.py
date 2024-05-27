from fastapi import APIRouter
from models.opinion_model import OpinionRead
from models.analysis_model import AnalysisRead
from db.db import get_all, get_one, get_one_analysis, get_count


guardian_router = APIRouter()


@guardian_router.get(
    "/",
)
async def get_root() -> str:
    """
    returns all documents.

    Some documents may have missing 'published' or 'teaser'
    """
    return {"message": "MediaVocabulary API"}


@guardian_router.get("/articles", response_model=list[OpinionRead])
async def get_guardian_opinions(limit: int = 5, skip: int = 0):
    """
    returns all documents.

    Some documents may have missing 'published' or 'teaser'
    """
    return await get_all(limit, skip)


@guardian_router.get("/count")
async def get_document_count():
    return await get_count()


@guardian_router.get("/article/{id}", response_model=OpinionRead)
async def get_guardian_opinion(id: str):
    """
    returns a single document
    """

    return await get_one(id)


@guardian_router.get("/analysis/{article_id}", response_model=AnalysisRead)
async def get_opinion_analysis(article_id: str):
    return await get_one_analysis(article_id)
