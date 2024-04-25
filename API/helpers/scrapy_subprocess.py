import os
import subprocess


def run_scrapy_subprocess():
    os.chdir("scrapers/guardian")
    result = subprocess.run(
        ["scrapy", "crawl", "opinions"], capture_output=True, text=True
    )
    if result.returncode == 0:
        print("articles have been scraped")
        return {"message": "articles have been scraped"}
    else:
        print("failure")
        return {"message": "error", "output": result.stderr}
