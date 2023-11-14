from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .config import settings

Base = declarative_base()

engine = create_engine(
    settings.sqlalchemy_url,
    poolclass=StaticPool,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)
