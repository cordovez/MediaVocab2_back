from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
from contextlib import asynccontextmanager
from db.db import init_db
import uvicorn
from db.db import get_all
from models.opinion_model import Opinion, OpinionRead


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/", response_model=list[OpinionRead])
async def read_root():
    return await get_all()


def main():
    uvicorn.run(reload=True, app="main:app")


if __name__ == "__main__":
    main()
