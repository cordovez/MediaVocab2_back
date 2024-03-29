# from guardian.spiders.opinions import OpinionsSpider
from .guardian.spiders.opinions import OpinionsSpider
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

import logging

logging.basicConfig(level=logging.DEBUG)


def run_guardian_spider():
    settings = get_project_settings()
    settings.set("MONGO_URI", "mongodb://localhost:27017/")
    settings.set("MONGO_DATABASE", "news_articles")
    # process = CrawlerProcess(settings)
    # process.crawl("OpinionsSpider")
    # process.start()

    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner()

    d = runner.crawl(OpinionsSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

    print("+++++++++", settings.get("MONGO_URI"))
    print("+++++++++", settings.get("MONGO_DATABASE"))
    return {"message": "Crawling script process completed."}


# if __name__ == "__main__":
#     run_guardian_spider()
