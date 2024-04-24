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
    # custom_settings = {"FEEDS": {"opinions_crawled.json": {"format": "json"}}}
    rules = (
        Rule(LinkExtractor(allow=(r"uk/commentisfree/",), deny=(r"-cartoon",))),
        Rule(
            LinkExtractor(allow=(rf"{year}/{month}/",)),
            callback="parse_opinion",
        ),
    )

    def parse_opinion(self, response):
        """headline = response.css("h1::text").get()
        'Germany’s reputation for decisive leadership is in tatters when Europe needs it most'
        author = response.css("div.dcr-0 a[rel='author']::text").get()
        'Simon Tisdall'
        teaser= response.css("div.dcr-1kpcv08::text").get()
        response.css(".dcr-1qp23oo p::text").get()
        'Olaf Scholz’s endless dithering over Ukraine is playing into Putin’s hands'
        published = response.css("div.dcr-1kpcv08 span::text").get()
        'Sat 9 Mar 2024 20.07 CET'
        joined_text = ''.join(response.css("div.dcr-1g5o3j6 p:not(footer) *::text").getall())
        canonical_url = response.css('link[rel="canonical"]::attr(href)').get()
        """
        guardian_article = ItemLoader(item=GuardianItem(), response=response)

        guardian_article.add_css("headline", "h1")
        guardian_article.add_css("author", " a[rel='author']")
        guardian_article.add_css("teaser", ".dcr-1qp23oo p")
        guardian_article.add_css("published", "span.dcr-u0h1qy")
        guardian_article.add_css("content", "div.dcr-1g5o3j6 p ")
        guardian_article.add_css("url", "link[rel='canonical']::attr(href)")

        return guardian_article.load_item()
