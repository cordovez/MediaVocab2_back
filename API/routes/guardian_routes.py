from fastapi import APIRouter
from models.opinion_model import OpinionRead
from db.db import get_all, get_one, add_one
from scrapy.crawler import CrawlerProcess

from scrapers.guardian.guardian.spiders.opinions import OpinionsSpider
from scrapy.utils.project import get_project_settings
from scrapers.guardian.run_spider import run_guardian_spider

# from subprocess import Popen, PIPE
# from pathlib import Path

guardian_router = APIRouter()


@guardian_router.get("/crawl")
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


@guardian_router.post("/add", response_model=OpinionRead)
async def add_item_manually(item: dict):
    return await add_one(item)
