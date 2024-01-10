from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User
from database_config import get_db


async def create_user(db: AsyncSession, data: dict):
    """Function to create a user"""
    db_user = User(name=data['name'], username=data['username'])
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user