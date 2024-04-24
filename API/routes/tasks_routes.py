from fastapi import APIRouter, BackgroundTasks, HTTPException
from tasks import crawl_the_guardian_opinions
from spacy_tasks import create_text_analysis
from dotenv import load_dotenv
from models.analysis_model import AnalysisRead, TextAnalysis
import os
from db.db import add_one
from bson import ObjectId

load_dotenv()
BROKER = os.getenv("CELERY_BROKER_URL")
BACKEND = os.getenv("CELERY_BACKEND")
# from tasks import crawl_the_guardian_opinions

tasks_router = APIRouter()


@tasks_router.get("/crawl", response_model=dict[str, str])
async def crawl_and_save(background: BackgroundTasks):
    """
    The route deletes the collection before crawling and saving the documents
    """
    background.add_task(
        crawl_the_guardian_opinions,
    )

    return {"result": "success"}


@tasks_router.post("/analyse/{id}")
async def analyse_article(id: str) -> str:
    result = await create_text_analysis(id)
    inserted = await add_one(result["article_id"], result)

    if inserted:
        return inserted
    else:
        raise HTTPException(status_code=400, detail="Document already exists")
