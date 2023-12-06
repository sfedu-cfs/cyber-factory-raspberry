from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class App(Base):
    """
    Модель данных приложения

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
