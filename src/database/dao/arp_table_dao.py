from src.database.connection import Session
from src.database.models.arp_table import ArpTable


class ArpTableDAO:
    def __init__(self, db: Session):
        self.db = db

    def create_arp_entry(self, arp_data):
        arp_entry = ArpTable(**arp_data.dict())
        self.db.add(arp_entry)
        self.db.commit()
        self.db.refresh(arp_entry)
        return arp_entry

    def get_arp_entry_by_id(self, arp_id):
        return self.db.query(ArpTable).filter(ArpTable.id == arp_id).first()

    def get_arp_entry_by_mac_address(self, mac_address):
        return self.db.query(ArpTable).filter(ArpTable.mac_address == mac_address).first()

    def update_arp_entry(self, arp_entry, updated_data):
        for key, value in updated_data.items():
            setattr(arp_entry, key, value)
        self.db.commit()
        self.db.refresh(arp_entry)
        return arp_entry

    def delete_arp_entry(self, arp_entry):
        self.db.delete(arp_entry)
        self.db.commit()
