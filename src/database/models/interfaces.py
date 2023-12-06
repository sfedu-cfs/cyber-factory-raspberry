from sqlalchemy import Column, Integer, String, DateTime

from src.database.connection import Base


class NetworkInterfaces(Base):
    __tablename__ = "network_interfaces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip_address = Column(String)
    created_date = Column(DateTime)
