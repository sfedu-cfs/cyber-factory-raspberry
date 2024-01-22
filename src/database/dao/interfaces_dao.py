from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.interfaces import NetworkInterfaces, NetworkInterfacesCurrent
from src.core.log_config import logger


class NetworkInterfacesDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, network_interface_data):
        try:
            network_interface_entry = NetworkInterfaces(**network_interface_data)
            network_interface_entry.created_date = dt.now()
            self.db.add(network_interface_entry)
            self.db.commit()
            self.db.refresh(network_interface_entry)
        except Exception as e:
            logger.error(f"Error while creating network interface: {e}")
            raise e
        return network_interface_entry

    def get_network_interface_by_id(self, network_interface_id):
        return self.db.query(NetworkInterfaces).filter(NetworkInterfaces.id == network_interface_id).first()

    def update_network_interface(self, network_interface_entry, updated_data):
        for key, value in updated_data.items():
            setattr(network_interface_entry, key, value)
        self.db.commit()
        self.db.refresh(network_interface_entry)
        return network_interface_entry

    def delete_network_interface(self, network_interface_entry):
        self.db.delete(network_interface_entry)
        self.db.commit()

    def exists(self, network_interface):
        return self.db.query(NetworkInterfaces).filter(NetworkInterfaces.name == network_interface.name).first() is not None


class NetworkInterfacesCurrentDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, network_interface_data):
        try:
            network_interface_entry = NetworkInterfacesCurrent(**network_interface_data)
            network_interface_entry.created_date = dt.now()
            self.db.add(network_interface_entry)
            self.db.commit()
            self.db.refresh(network_interface_entry)
        except Exception as e:
            logger.error(f"Error while creating network interface: {e}")
            raise e
        return network_interface_entry

    def delete_all(self):
        self.db.query(NetworkInterfacesCurrent).delete()
        self.db.commit()

    def exists(self, network_interface):
        return self.db.query(NetworkInterfacesCurrent).filter(NetworkInterfacesCurrent.name == network_interface.name).first() is not None