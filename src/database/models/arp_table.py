from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class ArpTable(Base):
    """
    Модель данных ARP таблицы

    :param id: Уникальный идентификатор записи
    :param ip_address: IP адрес
    :param mac_address: MAC адрес
    :param created_date: Дата создания записи
    """
    __tablename__ = "arp_table"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String)
    mac_address = Column(String, unique=True, index=True)
    created_date = Column(DateTime)
