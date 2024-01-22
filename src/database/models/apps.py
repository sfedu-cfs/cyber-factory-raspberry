from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class AppCurrent(Base):
    """
    Модель данных приложения для текущей записи

    :param id: Уникальный идентификатор записи
    :param name: Название приложения
    :param version: Версия приложения
    :param description: Описание приложения
    :param created_date: Дата создания записи
    """
    __tablename__ = "current_applications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    version = Column(String)
    description = Column(String)
    created_date = Column(DateTime)


class App(Base):
    """
    Модель данных приложения для всех записей

    :param id: Уникальный идентификатор записи
    :param name: Название приложения
    :param version: Версия приложения
    :param description: Описание приложения
    :param created_date: Дата создания записи
    """
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    version = Column(String)
    description = Column(String)
    created_date = Column(DateTime)
