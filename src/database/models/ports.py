from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class PortsCurrent(Base):
    """
    Модель данных портов для текущей записи

    :param id: Уникальный идентификатор записи
    :param host_id: Уникальный идентификатор хоста
    :param port: Номер порта
    :param status: Статус порта
    :param service: Сервис, использующий порт
    :param protocol: Протокол
    :param created_date: Дата создания записи
    """
    __tablename__ = "current_ports"
    id = Column(Integer, primary_key=True, index=True)
    host_id = Column(String, ForeignKey("current_hosts.id"), index=True)
    port = Column(Integer, index=True)
    status = Column(String)
    service = Column(String)
    protocol = Column(String)
    created_date = Column(DateTime)


class Ports(Base):
    """
    Модель данных портов для всех записей

    :param id: Уникальный идентификатор записи
    :param host_id: Уникальный идентификатор хоста
    :param port: Номер порта
    :param status: Статус порта
    :param service: Сервис, использующий порт
    :param protocol: Протокол
    :param created_date: Дата создания записи
    """
    __tablename__ = "ports"
    id = Column(Integer, primary_key=True, index=True)
    host_id = Column(String, ForeignKey("hosts.id"), index=True)
    port = Column(Integer, index=True)
    status = Column(String)
    service = Column(String)
    protocol = Column(String)
    created_date = Column(DateTime)
