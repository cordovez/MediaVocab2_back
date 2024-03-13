import motor.motor_asyncio
from dotenv import load_dotenv
import os
import asyncio
import json
from pprint import pprint
from bson import ObjectId
from models.opinion_model import Opinion
from fastapi import HTTPException

load_dotenv()

DB_URL = os.getenv("DATABASE")


async def init_db():
    return motor.motor_asyncio.AsyncIOMotorClient(DB_URL)


client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
news_articles = client.news_articles
guardian = news_articles.the_guardian_opinions

with open("the_guardian_opinions.json", "r") as file:
    data = json.load(file)


async def get_all():
    try:
        cursor = guardian.find()
        documents = []
        for document in await cursor.to_list(length=100):
            document["_id"] = str(document["_id"])
            documents.append(document)
        return documents
    except Exception as e:
        print(f"An error occurred in get_all: {e}")

        return []


async def get_one(item_id: str):

    if document := await guardian.find_one({"_id": ObjectId(item_id)}):
        document["_id"] = str(document["_id"])
        return document
    else:
        raise HTTPException(status_code=404, detail="Opinion not found")


async def add_one(item):
    result = await guardian.insert_one(item)
    print("result %s" % repr(result.inserted_id))
    return result


async def add_many(items: list):
    try:
        result = await guardian.insert_many(items)

        return {
            "message": f"articles successfully added {len(result.inserted_ids)} items to the database"
        }
    except Exception as e:
        print(f"An error occurred in add_many: {e}")
        return {"error message": e}


# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_one("65f010b6b15eb75edca25a53"))
