from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

Base = declarative_base()

engine = create_engine(settings.sqlalchemy_url)

SessionLocal = sessionmaker(bind=engine)
