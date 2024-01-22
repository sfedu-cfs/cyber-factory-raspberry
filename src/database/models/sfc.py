from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class SFCCurrent(Base):
    """
    Модель данных структурно-функциональных характеристик для текущей записи

    :param id: Уникальный идентификатор записи
    :param name: Название характеристики
    :param version: Версия характеристики
    :param created_date: Дата создания записи
    """
    __tablename__ = "current_structural_functional_characteristics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    version = Column(String)
    created_date = Column(DateTime)


class SFC(Base):
    """
    Модель данных структурно-функциональных характеристик для всех записей

    :param id: Уникальный идентификатор записи
    :param name: Название характеристики
    :param version: Версия характеристики
    :param created_date: Дата создания записи
    """
    __tablename__ = "structural_functional_characteristics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    version = Column(String)
    created_date = Column(DateTime)
