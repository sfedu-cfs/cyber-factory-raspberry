from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.arp_table import ArpTable, ArpTableCurrent
from src.core.log_config import logger


class ArpTableDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, arp_data):
        try:
            arp_entry = ArpTable(**arp_data)
            arp_entry.created_date = dt.now()
            self.db.add(arp_entry)
            self.db.commit()
            self.db.refresh(arp_entry)
        except Exception as e:
            logger.error(f"Error while creating arp entry: {e}")
            raise e
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

    def exists(self, arp_entry):
        return self.db.query(ArpTable).filter(ArpTable.mac_address == arp_entry.mac_address).first() is not None


class ArpTableCurrentDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, arp_data):
        try:
            arp_entry = ArpTableCurrent(**arp_data)
            arp_entry.created_date = dt.now()
            self.db.add(arp_entry)
            self.db.commit()
            self.db.refresh(arp_entry)
        except Exception as e:
            logger.error(f"Error while creating arp entry: {e}")
            raise e
        return arp_entry

    def delete_all(self):
        self.db.query(ArpTableCurrent).delete()
        self.db.commit()

    def exists(self, arp_entry):
        return self.db.query(ArpTableCurrent).filter(ArpTableCurrent.mac_address == arp_entry.mac_address).first() is not None