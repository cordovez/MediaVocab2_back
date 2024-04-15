import os
import subprocess
from dotenv import load_dotenv
from celery import Celery
from scrapers.guardian.run_spider import run_guardian_spider
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapers.guardian.guardian.spiders.opinions import OpinionsSpider

load_dotenv()
BROKER = os.getenv("CELERY_BROKER_URL")
BACKEND = os.getenv("CELERY_BACKEND")

celery_app = Celery("tasks", broker=BROKER, backend=BACKEND)

print("CELERY_BROKER_URL:", BROKER)
print("CELERY_BACKEND:", BACKEND)


@celery_app.task
def sample_add(a: int, b: int) -> int:
    return a + b


@celery_app.task
def crawl_the_guardian_opinions() -> dict[str, str]:
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner()

    d = runner.crawl(OpinionsSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
