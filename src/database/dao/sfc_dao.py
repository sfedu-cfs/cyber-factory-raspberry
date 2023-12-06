from src.database.connection import Session
from src.database.models.sfc import SFC


class SFCDao:
    def __init__(self, db: Session):
        self.db = db

    def create_sfc(self, sfc_data):
        sfc_entry = SFC(**sfc_data)
        self.db.add(sfc_entry)
        self.db.commit()
        self.db.refresh(sfc_entry)
        return sfc_entry

    def get_sfc_by_id(self, sfc_id):
        return self.db.query(SFC).filter(SFC.id == sfc_id).first()

    def update_sfc(self, sfc_entry, updated_data):
        for key, value in updated_data.items():
            setattr(sfc_entry, key, value)
        self.db.commit()
        self.db.refresh(sfc_entry)
        return sfc_entry

    def delete_sfc(self, sfc_entry):
        self.db.delete(sfc_entry)
        self.db.commit()
