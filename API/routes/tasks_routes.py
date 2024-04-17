from fastapi import APIRouter
from tasks import celery_app, crawl_the_guardian_opinions
from dotenv import load_dotenv
import os
from celery.result import AsyncResult
from db.db import delete_all

load_dotenv()
BROKER = os.getenv("CELERY_BROKER_URL")
BACKEND = os.getenv("CELERY_BACKEND")
# from tasks import crawl_the_guardian_opinions

tasks_router = APIRouter()


@tasks_router.get(
    "/crawl",
)
async def crawl_and_save():
    # response = crawl_the_guardian_opinions.delay()
    # return {"task_id": response.id}
    return await crawl_the_guardian_opinions()


@tasks_router.get("/crawl-status")
def check_status(task_id: str):
    return {"to do": "get celery tasks working"}
    # complete = AsyncResult(task_id, app=celery_app).ready()
    # return {
    #     "task_id": task_id,
    #     "complete": complete,
    # }
