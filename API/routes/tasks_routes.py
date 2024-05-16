from fastapi import APIRouter, HTTPException
from spacy_tasks import create_text_analysis
from dotenv import load_dotenv
from db.db import update_one
import os
from db.db import add_one

load_dotenv()
BROKER = os.getenv("CELERY_BROKER_URL")
BACKEND = os.getenv("CELERY_BACKEND")
# from tasks import crawl_the_guardian_opinions

tasks_router = APIRouter()


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
