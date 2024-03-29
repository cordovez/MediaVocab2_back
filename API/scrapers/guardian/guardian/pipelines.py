from itemadapter import ItemAdapter
import pymongo
import logging
import sys
from .items import GuardianItem

logging.basicConfig(level=logging.DEBUG)
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class MongoPipeline:
    collection_name = "the_guardian_opinions"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        if not self.mongodb_uri:
            sys.exit("You need to provide a Connection String")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        logging.debug("Attempting to insert to Mongo.")

        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        logging.debug("Data added to MongoDB")
        return item

    # def process_item(self, item, spider):
    #     data = dict(GuardianItem(item))
    #     self.db[self.collection].insert_one(data)
    #     logging.debug("Data added to MongoDB")
    #     return item
