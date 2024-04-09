# To do: use a CrawlerProcess as specified by Scrapy

import subprocess
import os


def run_guardian_spider():
    os.chdir("scrapers/guardian")

    # Run the scrapy crawl command in the terminal
    result = subprocess.run(
        ["scrapy", "crawl", "opinions"], capture_output=True, text=True
    )

    # Check if the command was successful
    if result.returncode == 0:
        # If successful, return the captured output
        return {
            "message": "Crawling script process completed.",
            "output": result.stdout,
        }
    else:
        # If not successful, return an error message
        return {"error": "Error running scrapy crawl command.", "output": result}
