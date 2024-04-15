from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.db import init_db
import uvicorn
import logging
import os
from dotenv import load_dotenv
from routes.guardian_routes import guardian_router
from routes.celery_routes import celery_router

load_dotenv()
DB = os.getenv("MONGO_URI")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(guardian_router, tags=["The Guardian"])
app.include_router(celery_router, prefix="/tasks", tags=["Tasks"])


def main():
    uvicorn.run(reload=True, app="main:app")


if __name__ == "__main__":
    print("Connection: ", DB)
    main()
