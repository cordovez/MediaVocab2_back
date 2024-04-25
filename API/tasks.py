from helpers.scrapy_subprocess import run_scrapy_subprocess
from dotenv import load_dotenv
from db.db import delete_all

load_dotenv()


async def crawl_the_guardian_opinions() -> dict[str, str]:
    try:
        await delete_all()
        run_scrapy_subprocess()

    except Exception as e:
        return {"message": str(e)}
