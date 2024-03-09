import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

month = datetime.now().strftime("%b").lower()
year = datetime.now().strftime("%Y")


class OpinionsSpider(CrawlSpider):
    name = "opinions"
    allowed_domains = ["theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk/commentisfree"]

    rules = Rule(LinkExtractor(allow=(r"{year}/{month}")))

    def parse(self, response):
        pass
