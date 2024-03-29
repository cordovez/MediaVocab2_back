# from guardian.spiders.opinions import OpinionsSpider
from .guardian.spiders.opinions import OpinionsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def run_guardian_spider():
    settings = get_project_settings()
    # settings.set("MONGO_URI", "mongodb://localhost:27017/")
    # settings.set("MONGO_DATABASE", "news_articles")
    process = CrawlerProcess(settings)
    process.crawl(OpinionsSpider)
    process.start()

    return {"message": "Crawling script process completed."}


# if __name__ == "__main__":
#     run_guardian_spider()
