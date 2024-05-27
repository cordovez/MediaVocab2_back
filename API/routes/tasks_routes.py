from fastapi import APIRouter, HTTPException
from spacy_tasks import create_text_analysis
from dotenv import load_dotenv
from db.db import update_one_opinions_document
import os
from db.db import add_one_to_analysis_collection

load_dotenv()
BROKER = os.getenv("CELERY_BROKER_URL")
BACKEND = os.getenv("CELERY_BACKEND")
# from tasks import crawl_the_guardian_opinions

tasks_router = APIRouter()


@tasks_router.post("/analyse/{id}")
async def analyse_article(id: str):
    analysis = await create_text_analysis(id)
    response = await add_one_to_analysis_collection(analysis["article_id"], analysis)
    if not response:
        return False
    update_data = {"has_analysis": True}
    updated = await update_one_opinions_document(id, update_data)
    return updated.modified_count
