from sqlalchemy import Column, Integer, String, DateTime

from src.database.connection import Base


class ConnectionsCurrent(Base):
    """
    Модель данных мониторинга ресурсов для текущей записи

    :param id: Уникальный идентификатор записи
    :param created_date: Дата создания записи
    :param protocol: Протокол соединения
    :param src_ip_address: IP адрес источника
    :param src_port: Порт источника
    :param dst_ip_address: IP адрес назначения
    :param dst_port: Порт назначения
    :param state: Состояние соединения
    :param service_name: Название сервиса
    """
    __tablename__ = "current_connections"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime)
    protocol = Column(String)
    src_ip_address = Column(String)
    src_port = Column(Integer)
    dst_ip_address = Column(String)
    dst_port = Column(Integer)
    state = Column(String)
    service_name = Column(String)


class Connections(Base):
    """
    Модель данных мониторинга ресурсов для всех записей

    :param id: Уникальный идентификатор записи
    :param created_date: Дата создания записи
    :param protocol: Протокол соединения
    :param src_ip_address: IP адрес источника
    :param src_port: Порт источника
    :param dst_ip_address: IP адрес назначения
    :param dst_port: Порт назначения
    :param state: Состояние соединения
    :param service_name: Название сервиса
    """
    __tablename__ = "connections"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime)
    protocol = Column(String)
    src_ip_address = Column(String)
    src_port = Column(Integer)
    dst_ip_address = Column(String)
    dst_port = Column(Integer)
    state = Column(String)
    service_name = Column(String)
