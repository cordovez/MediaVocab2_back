import os
import subprocess
from dotenv import load_dotenv
from celery import Celery
from db.db import delete_all

load_dotenv()
BROKER = os.getenv("CELERY_BROKER_URL")
BACKEND = os.getenv("CELERY_BACKEND")

celery_app = Celery("tasks", broker=BROKER, backend=BACKEND)

print("CELERY_BROKER_URL:", BROKER)
print("CELERY_BACKEND:", BACKEND)


@celery_app.task
async def crawl_the_guardian_opinions() -> dict[str, str]:
    try:
        deleted = await delete_all()
        if deleted:
            os.chdir("API/scrapers/guardian")
            result = subprocess.run(
                ["scrapy", "crawl", "opinions"], capture_output=True, text=True
            )
            if result.returncode == 0:
                return {"message": "sucess"}
            else:
                return {"message": "error", "output": result.stderr}
    except Exception as e:
        return {"message": "error", "exception": str(e)}
