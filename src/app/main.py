from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.adapters.object_model import UserModel
from app.api.routers import api_router
from app.api.system import router as system_router
from app.core.config import settings
from app.core.db.mongodb import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db([UserModel])
    app.include_router(api_router, prefix=settings.app.api_prefix)
    app.include_router(system_router)
    yield

app = FastAPI(lifespan=lifespan)
