from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.hosts import Hosts, HostsCurrent
from src.core.log_config import logger


class HostsDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, host_data):
        try:
            host_entry = Hosts(**host_data)
            host_entry.created_date = dt.now()
            self.db.add(host_entry)
            self.db.commit()
            self.db.refresh(host_entry)
        except Exception as e:
            logger.error(f"Error while creating host: {e}")
            raise e
        return host_entry

    def get_host_by_id(self, host_id):
        return self.db.query(Hosts).filter(Hosts.id == host_id).first()

    def update_host(self, host_entry, updated_data):
        for key, value in updated_data.items():
            setattr(host_entry, key, value)
        self.db.commit()
        self.db.refresh(host_entry)
        return host_entry

    def delete_host(self, host_entry):
        self.db.delete(host_entry)
        self.db.commit()

    def exists(self, host):
        return self.db.query(Hosts).filter(Hosts.ip_address == host.ip_address).first() is not None


class HostsCurrentDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, host_data):
        try:
            host_entry = HostsCurrent(**host_data)
            host_entry.created_date = dt.now()
            self.db.add(host_entry)
            self.db.commit()
            self.db.refresh(host_entry)
        except Exception as e:
            logger.error(f"Error while creating host: {e}")
            raise e
        return host_entry

    def delete_all(self):
        self.db.query(HostsCurrent).delete()
        self.db.commit()

    def exists(self, host):
        return self.db.query(HostsCurrent).filter(HostsCurrent.ip_address == host.ip_address).first() is not None
