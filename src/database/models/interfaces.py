from sqlalchemy import Column, Integer, String, DateTime

from src.database.connection import Base


class NetworkInterfacesCurrent(Base):
    """
    Модель данных сетевых интерфейсов для текущей записи

    :param id: Уникальный идентификатор записи
    :param name: Название сетевого интерфейса
    :param ip_address: IP адрес сетевого интерфейса
    :param created_date: Дата создания записи
    """
    __tablename__ = "current_network_interfaces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip_address = Column(String)
    created_date = Column(DateTime)


class NetworkInterfaces(Base):
    """
    Модель данных сетевых интерфейсов для всех записей

    :param id: Уникальный идентификатор записи
    :param name: Название сетевого интерфейса
    :param ip_address: IP адрес сетевого интерфейса
    :param created_date: Дата создания записи
    """
    __tablename__ = "network_interfaces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip_address = Column(String)
    created_date = Column(DateTime)
