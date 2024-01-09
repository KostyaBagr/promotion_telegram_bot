from sqlalchemy import Column, Integer, String, DateTime, Boolean,Text,  func
from src.config.base import Base


class User(Base):
    """Таблица хранит данные о пользователе"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    username = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())


class Post(Base):
    """Таблица хранит посты"""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    file = Column(String, nullable=True)
    audio = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


class ReferralLink(Base):
    """Таблица хранит реферальную ссылку"""
    __tablename__ = 'referral_links'

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String, nullable=False)



