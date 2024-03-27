from fastapi import APIRouter
from models.opinion_model import OpinionRead
from db.db import get_all, get_one

# from subprocess import Popen, PIPE
# from pathlib import Path

# guardian_router = APIRouter()

# @guardian_router.get("/crawl")
# async def crawl_and_save():
#     # Specify the path to your Scrapy project directory
#     scrapy_project_path = Path("/path/to/your/scrapy/project")

#     # Specify the path to the spider script
#     spider_script = scrapy_project_path / "run_spider.py"

#     # Run the spider script using subprocess
#     process = Popen(["python", str(spider_script)], cwd=scrapy_project_path, stdout=PIPE, stderr=PIPE)
#     stdout, stderr = process.communicate()

#     # Check if the process was successful
#     if process.returncode == 0:
#         return {"message": "Crawling process completed successfully"}
#     else:
#         return {"message": f"Error occurred during crawling process: {stderr.decode('utf-8')}"}

guardian_router = APIRouter()


@guardian_router.get("/", response_model=list[OpinionRead])
async def get_guardian_opinions():
    return await get_all()


@guardian_router.get("/{id}", response_model=OpinionRead)
async def get_guardian_opinion(article_id: str):
    """
    use "65f010b6b15eb75edca25a51" to test
    """
    return await get_one(article_id)
