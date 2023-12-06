from src.database.connection import Session
from src.database.models.ports import Ports


class PortsDAO:
    def __init__(self, db: Session):
        self.db = db

    def create_port(self, port_data):
        port_entry = Ports(**port_data)
        self.db.add(port_entry)
        self.db.commit()
        self.db.refresh(port_entry)
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
