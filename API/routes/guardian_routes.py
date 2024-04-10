from fastapi import APIRouter
from models.opinion_model import OpinionRead
from db.db import get_all, get_one, add_one

from scrapers.guardian.run_spider import run_guardian_spider


guardian_router = APIRouter()


@guardian_router.get("/crawl", response_model=dict[str, str])
async def crawl_and_save():
    return run_guardian_spider()


@guardian_router.get("/", response_model=list[OpinionRead])
async def get_guardian_opinions():
    return await get_all()


@guardian_router.get("/{id}", response_model=OpinionRead)
async def get_guardian_opinion(article_id: str):
    """
    use "65f010b6b15eb75edca25a51" to test
    """
    return await get_one(article_id)
