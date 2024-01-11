from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from src.config.base import Base
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency




