from src.database.connection import session
from src.database.models.count_packet import CountPackets


class CountPacketsDAO:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db: session):
        self.db = db

    def create_count_packets(self, count_packets_data):
        count_packets_data.pop("device_id", None)

        count_packets_entry = CountPackets(**count_packets_data)
        self.db.add(count_packets_entry)
        self.db.commit()
        self.db.refresh(count_packets_entry)
        return count_packets_entry

    def get_count_packets_by_id(self, count_packets_id):
        return self.db.query(CountPackets).filter(CountPackets.id == count_packets_id).first()

    def update_count_packets(self, count_packets_entry, updated_data):
        for key, value in updated_data.items():
            setattr(count_packets_entry, key, value)
        self.db.commit()
        self.db.refresh(count_packets_entry)
        return count_packets_entry

    def delete_count_packets(self, count_packets_entry):
        self.db.delete(count_packets_entry)
        self.db.commit()


count_packets_dao = CountPacketsDAO(db=session)
