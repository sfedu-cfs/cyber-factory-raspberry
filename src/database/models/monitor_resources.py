from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class MonitorResources(Base):
    """
    Модель данных мониторинга ресурсов

    :param id: Уникальный идентификатор записи
    :param ram_usage: Использование RAM в процентах
    :param swap_usage: Использование SWAP в процентах
    :param disk_usage: Использование диска в процентах
    :param uptime: Время работы системы
    :param cpu_load: Загрузка CPU в процентах
    :param cpu_temperature: Температура CPU в градусах Цельсия
    """
    __tablename__ = "monitor_resources"

    id = Column(Integer, primary_key=True, index=True)
    ram_usage = Column(Float)
    swap_usage = Column(Float)
    disk_usage = Column(Float)
    uptime = Column(String)
    cpu_load = Column(Float)
    cpu_temperature = Column(Float)
