import enum

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, func, BigInteger, Enum, UniqueConstraint
from src.config.base import Base


class User(Base):
    """Таблица хранит данные о пользователе"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, index=True, unique=True)
    name = Column(String, nullable=True)
    username = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())


class Post(Base):
    """Таблица хранит посты"""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))
    text = Column(Text, nullable=False)
    file = Column(String, nullable=True)
    audio = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


class AdditionalPost(Base):
    """Таблица хранит дополнительные посты"""
    __tablename__ = 'additional_posts'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(Text, nullable=True)
    file = Column(String, nullable=True)
    file_type = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


class ReferralLink(Base):
    """Таблица хранит реферальную ссылку"""
    __tablename__ = 'referral_links'

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String, nullable=False)


class ContactMe(Base):
    """Таблица хранит данные для связи с менеджером"""

    __tablename__ = 'contact_me'

    id = Column(Integer, primary_key=True, index=True, default=1)
    text = Column(Text, nullable=False)

    __table_args__ = (
        UniqueConstraint('id'),
    )
