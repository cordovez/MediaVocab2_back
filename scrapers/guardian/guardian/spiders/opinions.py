import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime
from ..items import GuardianItem
from scrapy.loader import ItemLoader


month = datetime.now().strftime("%b").lower()
year = datetime.now().strftime("%Y")


class OpinionsSpider(CrawlSpider):
    name = "opinions"
    allowed_domains = ["theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk/commentisfree/"]

    rules = (
        Rule(LinkExtractor(allow=(rf"uk/commentisfree/",), deny=(r"-cartoon",))),
        Rule(
            LinkExtractor(allow=(rf"{year}/{month}/",)),
            callback="parse_opinion",
        ),
    )

    def parse_opinion(self, response):
        """headline = response.css("h1::text").get()
        'Germany’s reputation for decisive leadership is in tatters when Europe needs it most'
        author = response.css("div.dcr-0 a::text").get()
        'Simon Tisdall'
        teaser= response.css("div.dcr-1kpcv08::text").get()
        response.css(".dcr-1qp23oo p::text").get()
        'Olaf Scholz’s endless dithering over Ukraine is playing into Putin’s hands'
        published = response.css("div.dcr-1kpcv08 span::text").get()
        'Sat 9 Mar 2024 20.07 CET'
        content= text_combined = ''.join(response.css("#maincontent p::text, #maincontent span::text").getall())
        """
        guardian_article = ItemLoader(opinion=GuardianItem(), response=response)
        guardian_article.add_css("headline", "h1fd")
        guardian_article.add_css("author", ".dcr-0 a")
        guardian_article.add_css("teaser", ".dcr-1qp23oo p")
        guardian_article.add_css("published", ".dcr-1kpcv08 span")
        guardian_article.add_css("content", "#maincontent p, #maincontent span ")
        return guardian_article.load_item()
