from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class SystemServices(Base):
    """
    Модель данных системных сервисов

    :param id: Уникальный идентификатор записи
    :param name: Название сервиса
    :param status: Статус сервиса
    :param created_date: Дата создания записи
    """
    __tablename__ = "system_services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    status = Column(String)
    created_date = Column(DateTime)