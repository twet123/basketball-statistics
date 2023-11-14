from fastapi import FastAPI
from .config import settings
from .api import stats

app = FastAPI(title=settings.project_name, version=settings.version)

app.include_router(stats.router, tags=["stats"])
