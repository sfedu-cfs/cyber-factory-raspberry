from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class HostsCurrent(Base):
    """
    Модель данных хостов для текущей записи

    :param id: Уникальный идентификатор записи
    :param ip_address: IP адрес
    :param mac_address: MAC адрес
    :param created_date: Дата создания записи
    """
    __tablename__ = "current_hosts"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, unique=True, index=True)
    mac_address = Column(String, unique=True, index=True)
    created_date = Column(DateTime)


class Hosts(Base):
    """
    Модель данных хостов для всех записей

    :param id: Уникальный идентификатор записи
    :param ip_address: IP адрес
    :param mac_address: MAC адрес
    :param created_date: Дата создания записи
    """
    __tablename__ = "hosts"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, unique=True, index=True)
    mac_address = Column(String, unique=True, index=True)
    created_date = Column(DateTime)
