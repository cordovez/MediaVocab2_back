import motor.motor_asyncio
from dotenv import load_dotenv
import os
from bson import ObjectId
from fastapi import HTTPException
import logging
from models.analysis_model import TextAnalysis

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
opinions_collection = news_organization.opinions
analysis_collection = news_organization.analysis

logging.debug("Connection to the database established successfully.")


async def get_all() -> list:

    try:
        cursor = opinions_collection.find()
        documents = []
        for document in await cursor.to_list(length=100):
            document["_id"] = str(document["_id"])
            documents.append(document)
        return documents

    except Exception as e:
        print(f"An error occurred in get_all: {e}")
        return []


async def get_one(item_id: str) -> dict:

    if document := await opinions_collection.find_one({"_id": ObjectId(item_id)}):
        document["_id"] = str(document["_id"])
        return document
    else:
        raise HTTPException(status_code=404, detail="Opinion not found")


async def get_one_analysis(item_id: str) -> dict:

    if document := await analysis_collection.find_one({"article_id": item_id}):
        document["_id"] = str(document["_id"])
        return document
    else:
        raise HTTPException(status_code=404, detail="Analysis not found")


async def delete_all() -> None:
    await opinions_collection.delete_many({})
    await analysis_collection.delete_many({})


async def update_one(item_id: str, dict_data: dict) -> dict:
    result = await opinions_collection.update_one(
        {"_id": ObjectId(item_id)}, {"$set": dict_data}
    )
    print("modified items:", result.modified_count)
    if result.modified_count == 0:
        print({"message": "update failed"})
        return {"message": "update failed"}
    new_value = await opinions_collection.find_one({"_id": ObjectId(item_id)})
    print({"has_analysis": new_value.get("has_analysis")})
    return {"has_analysis": new_value.get("has_analysis")}


async def add_one(article_id: str, data: dict) -> str:
    try:
        document_found = await analysis_collection.find_one({"article_id": article_id})
        if document_found:
            print("Document already exists")
            return None

        # Ensure the data is converted to a dictionary
        if isinstance(data, TextAnalysis):
            document = data.model_dump
        else:
            document = data

        result = await analysis_collection.insert_one(document)
        print(f"Inserted document ID: {result.inserted_id}")

        return f"Inserted document ID: {result.inserted_id}"

    except Exception as e:
        print(f"An error occurred: {e}")
        return e
