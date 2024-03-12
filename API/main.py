from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.db import init_db
import uvicorn

from routes.guardian_routes import guardian_router
from models.opinion_model import OpinionRead
from db.db import get_all


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(guardian_router, tags=["The Guardian"])


def main():
    uvicorn.run(reload=True, app="main:app")


if __name__ == "__main__":
    main()
