from fastapi import APIRouter
from tasks import celery_app, crawl_the_guardian_opinions
from dotenv import load_dotenv
import os
from celery.result import AsyncResult

load_dotenv()
BROKER = os.getenv("CELERY_BROKER_URL")
BACKEND = os.getenv("CELERY_BACKEND")
# from tasks import crawl_the_guardian_opinions

celery_router = APIRouter()


# @celery_router.get("/add", response_model=dict[str, str])
# async def crawl_and_save(x: int, y: int):
#     return {"task_id": sample_add.delay(x, y).id}
# result = crawl_the_guardian_opinions.delay()
# return {"task_id": result}


@celery_router.get("/crawl", response_model=dict[str, str])
async def crawl_and_save():
    # result = crawl_the_guardian_opinions.delay().id
    # return {"task_id": result}
    result = crawl_the_guardian_opinions()
    # result = crawl_the_guardian_opinions.delay().result
    return result


@celery_router.get("/crawl-status")
def check_status(task_id: str):
    result = celery_app.AsyncResult(task_id).ready()
    return {"task_id": task_id, "result": result}
