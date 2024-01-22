from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.sfc import SFC, SFCCurrent
from src.core.log_config import logger


class SFCDao:
    def __init__(self, db: Session):
        self.db = db

    def create(self, sfc_data):
        try:
            sfc_entry = SFC(**sfc_data)
            sfc_entry.created_date = dt.now()
            self.db.add(sfc_entry)
            self.db.commit()
            self.db.refresh(sfc_entry)
        except Exception as e:
            logger.error(f"Error while creating sfc: {e}")
            raise e
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

    def exists(self, sfc):
        return self.db.query(SFC).filter(SFC.name == sfc.name).first() is not None


class SFCCurrentDao:
    def __init__(self, db: Session):
        self.db = db

    def create(self, sfc_data):
        try:
            sfc_entry = SFCCurrent(**sfc_data)
            sfc_entry.created_date = dt.now()
            self.db.add(sfc_entry)
            self.db.commit()
            self.db.refresh(sfc_entry)
        except Exception as e:
            logger.error(f"Error while creating sfc: {e}")
            raise e
        return sfc_entry

    def delete_all(self):
        self.db.query(SFCCurrent).delete()
        self.db.commit()

    def exists(self, sfc):
        return self.db.query(SFCCurrent).filter(SFCCurrent.name == sfc.name).first() is not None
