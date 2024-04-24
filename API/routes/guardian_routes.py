from fastapi import APIRouter
from models.opinion_model import OpinionRead
from models.analysis_model import AnalysisRead
from db.db import get_all, get_one, get_one_analysis


guardian_router = APIRouter()


@guardian_router.get("/", response_model=list[OpinionRead])
async def get_guardian_opinions():
    """
    returns all documents.

    Some documents may have missing 'published' or 'teaser'
    """
    return await get_all()


@guardian_router.get("/{id}", response_model=OpinionRead)
async def get_guardian_opinion(article_id: str):
    """
    returns a single document
    """

    return await get_one(article_id)


@guardian_router.get("/analysis/{article_id}", response_model=AnalysisRead)
async def get_opinion_analysis(article_id: str):
    return await get_one_analysis(article_id)
