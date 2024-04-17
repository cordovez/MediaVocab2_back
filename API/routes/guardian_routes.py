from fastapi import APIRouter
from models.opinion_model import OpinionRead
from db.db import get_all, get_one


guardian_router = APIRouter()


@guardian_router.get("/", response_model=list[OpinionRead])
async def get_guardian_opinions():
    """
    returns all documents. \n
    Some documents may have missing 'published' or 'teaser'
    """
    return await get_all()


@guardian_router.get("/{id}", response_model=OpinionRead)
async def get_guardian_opinion(article_id: str):
    """
    returns a single document
    """
    return await get_one(article_id)
