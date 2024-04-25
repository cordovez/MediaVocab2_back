from fastapi import APIRouter, BackgroundTasks, HTTPException, status
from tasks import crawl_the_guardian_opinions
from spacy_tasks import create_text_analysis
from dotenv import load_dotenv
from models.analysis_model import AnalysisRead, TextAnalysis
from db.db import get_one, update_one
import os
from db.db import add_one
from bson import ObjectId
import subprocess

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
    try:
        background.add_task(
            crawl_the_guardian_opinions,
        )

        return {"message": "articles successfully collected"}
    except subprocess.CalledProcessError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Scrape failed: subprocess error",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Scrape failed: {str(e)}",
        )


@tasks_router.post("/analyse/{id}")
async def analyse_article(id: str):
    analysis = await create_text_analysis(id)
    inserted = await add_one(analysis["article_id"], analysis)
    update_data = {"has_analysis": True}
    update_data = await update_one(id, update_data)
    # TO do: when analysis is made, find original article and change "has_analysis" to True, maybe add analysis id?

    if inserted:
        return update_data
    else:
        raise HTTPException(status_code=400, detail="Document already exists")
