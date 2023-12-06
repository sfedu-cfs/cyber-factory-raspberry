from src.database.connection import Session
from src.database.models.interfaces import NetworkInterfaces


class NetworkInterfacesDAO:
    def __init__(self, db: Session):
        self.db = db

    def create_network_interface(self, network_interface_data):
        network_interface_entry = NetworkInterfaces(**network_interface_data)
        self.db.add(network_interface_entry)
        self.db.commit()
        self.db.refresh(network_interface_entry)
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
