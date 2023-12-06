from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class Ports(Base):
    """
    Модель данных портов

    :param id: Уникальный идентификатор записи
    :param port: Номер порта
    :param protocol: Протокол
    :param created_date: Дата создания записи
    """
    __tablename__ = "ports"

    ip_address = Column(String, ForeignKey("hosts.ip_address"), primary_key=True, index=True)
    port = Column(Integer, index=True)
    status = Column(String)
    service = Column(String)
    protocol = Column(String)
