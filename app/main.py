import csv

from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.orm import Session

from .settings import settings
from .api import stats
from .database import SessionLocal, engine
from .models import Performance, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    with open(settings.csv_source_file, "r", encoding="utf-8-sig") as csv_file:
        reader: csv.DictReader = csv.DictReader(csv_file)

        row: dict[str, str]
        for row in reader:
            performance = Performance(row)
            db.add(performance)

        db.commit()

    db.close()

    yield

    Base.metadata.drop_all(bind=engine)


app = FastAPI(title=settings.project_name, version=settings.version, lifespan=lifespan)

app.include_router(stats.router, tags=["stats"])
