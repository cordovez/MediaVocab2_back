import os
import subprocess
from dotenv import load_dotenv
from db.db import delete_all

load_dotenv()


async def crawl_the_guardian_opinions() -> dict[str, str]:
    """
    Summary:
    Asynchronously crawls The Guardian opinions and handles success or error cases.

    Explanation:
    This function attempts to delete all, changes directory, and runs a subprocess to crawl opinions using Scrapy.
    If successful, it returns a success message; otherwise, it returns an error message with output details.

    Returns:
    dict[str, str]: A dictionary containing a message key with success or error message and optional output details.

    Raises:
    Exception: If any error occurs during the process.
    """
    try:
        deleted = await delete_all()
        if deleted:
            os.chdir("API/scrapers/guardian")
            result = subprocess.run(
                ["scrapy", "crawl", "opinions"], capture_output=True, text=True
            )
            if result.returncode == 0:
                print("success")
                return {"message": "success"}
            else:
                print("failure")
                return {"message": "error", "output": result.stderr}
    except Exception as e:
        return {"message": "error", "exception": str(e)}
