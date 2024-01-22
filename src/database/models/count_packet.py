from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class CountPacketsAll(Base):
    """
    Модель данных сборщика количества всех пакетов

    :param id: Уникальный идентификатор записи
    :param created_date: Дата создания записи
    :param all_proto_count: Количество пакетов всех протоколов
    :param tcp_count: Количество пакетов TCP
    :param udp_count: Количество пакетов UDP
    :param arp_count: Количество пакетов ARP
    :param icmp_count: Количество пакетов ICMP
    :param http_count: Количество пакетов HTTP
    :param modbus_01_count: Количество пакетов MODBUS функции 01
    :param modbus_02_count: Количество пакетов MODBUS функции 02
    :param modbus_03_count: Количество пакетов MODBUS функции 03
    :param modbus_04_count: Количество пакетов MODBUS функции 04
    :param modbus_05_count: Количество пакетов MODBUS функции 05
    :param modbus_06_count: Количество пакетов MODBUS функции 06
    :param modbus_15_count: Количество пакетов MODBUS функции 15
    :param modbus_16_count: Количество пакетов MODBUS функции 16
    """
    __tablename__ = "count_packets_all"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime)
    all_proto_count = Column(Integer)
    tcp_count = Column(Integer)
    udp_count = Column(Integer)
    arp_count = Column(Integer)
    icmp_count = Column(Integer)
    http_count = Column(Integer)
    modbus_01_count = Column(Integer)
    modbus_02_count = Column(Integer)
    modbus_03_count = Column(Integer)
    modbus_04_count = Column(Integer)
    modbus_05_count = Column(Integer)
    modbus_06_count = Column(Integer)
    modbus_15_count = Column(Integer)
    modbus_16_count = Column(Integer)


class CountPacketsInput(Base):
    """
    Модель данных сборщика количества входящих пакетов

    :param id: Уникальный идентификатор записи
    :param created_date: Дата создания записи
    :param all_proto_count: Количество пакетов всех протоколов
    :param tcp_count: Количество пакетов TCP
    :param udp_count: Количество пакетов UDP
    :param arp_count: Количество пакетов ARP
    :param icmp_count: Количество пакетов ICMP
    :param http_count: Количество пакетов HTTP
    :param modbus_01_count: Количество пакетов MODBUS функции 01
    :param modbus_02_count: Количество пакетов MODBUS функции 02
    :param modbus_03_count: Количество пакетов MODBUS функции 03
    :param modbus_04_count: Количество пакетов MODBUS функции 04
    :param modbus_05_count: Количество пакетов MODBUS функции 05
    :param modbus_06_count: Количество пакетов MODBUS функции 06
    :param modbus_15_count: Количество пакетов MODBUS функции 15
    :param modbus_16_count: Количество пакетов MODBUS функции 16
    """
    __tablename__ = "count_packets_input"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime)
    all_proto_count = Column(Integer)
    tcp_count = Column(Integer)
    udp_count = Column(Integer)
    arp_count = Column(Integer)
    icmp_count = Column(Integer)
    http_count = Column(Integer)
    modbus_01_count = Column(Integer)
    modbus_02_count = Column(Integer)
    modbus_03_count = Column(Integer)
    modbus_04_count = Column(Integer)
    modbus_05_count = Column(Integer)
    modbus_06_count = Column(Integer)
    modbus_15_count = Column(Integer)
    modbus_16_count = Column(Integer)


class CountPacketsOutput(Base):
    """
    Модель данных сборщика количества исходящих пакетов

    :param id: Уникальный идентификатор записи
    :param created_date: Дата создания записи
    :param all_proto_count: Количество пакетов всех протоколов
    :param tcp_count: Количество пакетов TCP
    :param udp_count: Количество пакетов UDP
    :param arp_count: Количество пакетов ARP
    :param icmp_count: Количество пакетов ICMP
    :param http_count: Количество пакетов HTTP
    :param modbus_01_count: Количество пакетов MODBUS функции 01
    :param modbus_02_count: Количество пакетов MODBUS функции 02
    :param modbus_03_count: Количество пакетов MODBUS функции 03
    :param modbus_04_count: Количество пакетов MODBUS функции 04
    :param modbus_05_count: Количество пакетов MODBUS функции 05
    :param modbus_06_count: Количество пакетов MODBUS функции 06
    :param modbus_15_count: Количество пакетов MODBUS функции 15
    :param modbus_16_count: Количество пакетов MODBUS функции 16
    """
    __tablename__ = "count_packets_output"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime)
    all_proto_count = Column(Integer)
    tcp_count = Column(Integer)
    udp_count = Column(Integer)
    arp_count = Column(Integer)
    icmp_count = Column(Integer)
    http_count = Column(Integer)
    modbus_01_count = Column(Integer)
    modbus_02_count = Column(Integer)
    modbus_03_count = Column(Integer)
    modbus_04_count = Column(Integer)
    modbus_05_count = Column(Integer)
    modbus_06_count = Column(Integer)
    modbus_15_count = Column(Integer)
    modbus_16_count = Column(Integer)
