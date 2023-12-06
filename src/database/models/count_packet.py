from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class CountPackets(Base):
    """
    Модель данных сборщика количества пакетов

    :param id: Уникальный идентификатор записи
    :param timing: Время сбора статистики
    :param all_proto_count: Количество пакетов всех протоколов
    :param tcp_count: Количество пакетов TCP
    :param udp_count: Количество пакетов UDP
    :param http_request_count: Количество пакетов HTTP запросов
    :param http_response_count: Количество пакетов HTTP ответов
    :param icmp_count: Количество пакетов ICMP
    :param arp_count: Количество пакетов ARP
    :param modbus_01_request_count: Количество пакетов MODBUS функции 01 запросов
    :param modbus_01_response_count: Количество пакетов MODBUS функции 01 ответов
    :param modbus_02_request_count: Количество пакетов MODBUS функции 02 запросов
    :param modbus_02_response_count: Количество пакетов MODBUS функции 02 ответов
    :param modbus_03_request_count: Количество пакетов MODBUS функции 03 запросов
    :param modbus_03_response_count: Количество пакетов MODBUS функции 03 ответов
    :param modbus_04_request_count: Количество пакетов MODBUS функции 04 запросов
    :param modbus_04_response_count: Количество пакетов MODBUS функции 04 ответов
    :param modbus_05_request_count: Количество пакетов MODBUS функции 05 запросов
    :param modbus_05_response_count: Количество пакетов MODBUS функции 05 ответов
    :param modbus_06_request_count: Количество пакетов MODBUS функции 06 запросов
    :param modbus_06_response_count: Количество пакетов MODBUS функции 06 ответов
    :param modbus_15_request_count: Количество пакетов MODBUS функции 15 запросов
    :param modbus_15_response_count: Количество пакетов MODBUS функции 15 ответов
    :param modbus_16_request_count: Количество пакетов MODBUS функции 16 запросов
    :param modbus_16_response_count: Количество пакетов MODBUS функции 16 ответов
    :param created_date: Дата создания записи
    """
    __tablename__ = "count_packets"

    id = Column(Integer, primary_key=True, index=True)
    timing = Column(Integer)
    all_proto_count = Column(Integer)
    tcp_count = Column(Integer)
    udp_count = Column(Integer)
    http_request_count = Column(Integer)
    http_response_count = Column(Integer)
    icmp_count = Column(Integer)
    arp_count = Column(Integer)
    modbus_01_request_count = Column(Integer)
    modbus_01_response_count = Column(Integer)
    modbus_02_request_count = Column(Integer)
    modbus_02_response_count = Column(Integer)
    modbus_03_request_count = Column(Integer)
    modbus_03_response_count = Column(Integer)
    modbus_04_request_count = Column(Integer)
    modbus_04_response_count = Column(Integer)
    modbus_05_request_count = Column(Integer)
    modbus_05_response_count = Column(Integer)
    modbus_06_request_count = Column(Integer)
    modbus_06_response_count = Column(Integer)
    modbus_15_request_count = Column(Integer)
    modbus_15_response_count = Column(Integer)
    modbus_16_request_count = Column(Integer)
    modbus_16_response_count = Column(Integer)
    created_date = Column(DateTime)

