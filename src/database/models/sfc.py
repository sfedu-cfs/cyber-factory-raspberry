from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from src.database.connection import Base


class SFC(Base):
    __tablename__ = "structural_functional_characteristics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    version = Column(String)
    created_date = Column(DateTime)
