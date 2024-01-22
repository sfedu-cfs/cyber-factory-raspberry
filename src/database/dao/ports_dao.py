from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.ports import Ports, PortsCurrent
from src.database.models.hosts import Hosts, HostsCurrent
from src.core.log_config import logger


class PortsDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, port_data, ip):
        try:
            port_entry = Ports(**port_data)
            port_entry.created_date = dt.now()
            port_entry.host_id = self.db.query(Hosts).filter(Hosts.ip_address == ip).first().id
            self.db.add(port_entry)
            self.db.commit()
            self.db.refresh(port_entry)
        except Exception as e:
            logger.error(f"Error while creating port: {e}")
            raise e
        return port_entry

    def get_port_by_ip_and_port(self, ip_address, port):
        return self.db.query(Ports).filter(Ports.ip_address == ip_address, Ports.port == port).first()

    def update_port(self, port_entry, updated_data):
        for key, value in updated_data.items():
            setattr(port_entry, key, value)
        self.db.commit()
        self.db.refresh(port_entry)
        return port_entry

    def delete_port(self, port_entry):
        self.db.delete(port_entry)
        self.db.commit()

    def exists(self, port, ip):
        return self.db.query(Ports, Hosts).join(Hosts, Ports.host_id == Hosts.id).filter(
            Hosts.ip_address == ip, Ports.port == port.port).first() is not None


class PortsCurrentDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, port_data, ip):
        try:
            port_entry = PortsCurrent(**port_data)
            port_entry.created_date = dt.now()
            port_entry.host_id = self.db.query(HostsCurrent).filter(HostsCurrent.ip_address == ip).first().id
            self.db.add(port_entry)
            self.db.commit()
            self.db.refresh(port_entry)
        except Exception as e:
            logger.error(f"Error while creating port: {e}")
            raise e
        return port_entry

    def delete_all(self):
        self.db.query(PortsCurrent).delete()
        self.db.commit()

    def exists(self, port, ip):
        return self.db.query(PortsCurrent, HostsCurrent).join(HostsCurrent, PortsCurrent.host_id == HostsCurrent.id).filter(
            HostsCurrent.ip_address == ip, PortsCurrent.port == port.port).first() is not None
