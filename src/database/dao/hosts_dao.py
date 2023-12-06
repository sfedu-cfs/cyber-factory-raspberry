from src.database.connection import Session
from src.database.models.hosts import Hosts


class HostsDAO:
    def __init__(self, db: Session):
        self.db = db

    def create_host(self, host_data):
        host_entry = Hosts(**host_data)
        self.db.add(host_entry)
        self.db.commit()
        self.db.refresh(host_entry)
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
