import motor.motor_asyncio
from dotenv import load_dotenv
import os
from bson import ObjectId
from fastapi import HTTPException
import logging

logging.basicConfig(level=logging.DEBUG)
load_dotenv()

URI = os.getenv("MONGO_URI")
DB = os.getenv("MONGO_DATABASE")
# URI = os.getenv("DATABASE")


async def init_db():
    return motor.motor_asyncio.AsyncIOMotorClient(URI)


logging.debug(f"Attempting to establish connection to the database {URI}")

client = motor.motor_asyncio.AsyncIOMotorClient(URI)
news_organization = client[DB]
collection = news_organization.opinions

logging.debug("Connection to the database established successfully.")


async def get_all() -> list:

    try:
        cursor = collection.find()
        documents = []
        for document in await cursor.to_list(length=100):
            document["_id"] = str(document["_id"])
            documents.append(document)
        return documents

    except Exception as e:
        print(f"An error occurred in get_all: {e}")
        return []


async def get_one(item_id: str) -> dict:

    if document := await collection.find_one({"_id": ObjectId(item_id)}):
        document["_id"] = str(document["_id"])
        return document
    else:
        raise HTTPException(status_code=404, detail="Opinion not found")


async def delete_all() -> bool:

    await collection.delete_many({})
    count = await collection.count_documents({})
    if count == 0:
        return True


# used for running in the terminal as __main__
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_one("65f010b6b15eb75edca25a53"))
