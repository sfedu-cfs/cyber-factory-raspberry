from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.system_services import SystemServices, SystemServicesCurrent
from src.core.log_config import logger


class SystemServicesDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, system_service_data):
        try:
            system_service_entry = SystemServices(**system_service_data)
            system_service_entry.created_date = dt.now()
            self.db.add(system_service_entry)
            self.db.commit()
            self.db.refresh(system_service_entry)
        except Exception as e:
            logger.error(f"Error while creating system service: {e}")
            raise e
        return system_service_entry

    def get_system_service_by_id(self, system_service_id):
        return self.db.query(SystemServices).filter(SystemServices.id == system_service_id).first()

    def update_system_service(self, system_service_entry, updated_data):
        for key, value in updated_data.items():
            setattr(system_service_entry, key, value)
        self.db.commit()
        self.db.refresh(system_service_entry)
        return system_service_entry

    def delete_system_service(self, system_service_entry):
        self.db.delete(system_service_entry)
        self.db.commit()

    def exists(self, system_service):
        return self.db.query(SystemServices).filter(SystemServices.name == system_service.name).first() is not None


class SystemServicesCurrentDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, system_service_data):
        try:
            system_service_entry = SystemServicesCurrent(**system_service_data)
            system_service_entry.created_date = dt.now()
            self.db.add(system_service_entry)
            self.db.commit()
            self.db.refresh(system_service_entry)
        except Exception as e:
            logger.error(f"Error while creating system service: {e}")
            raise e
        return system_service_entry

    def delete_all(self):
        self.db.query(SystemServicesCurrent).delete()
        self.db.commit()

    def exists(self, system_service):
        return self.db.query(SystemServicesCurrent).filter(SystemServicesCurrent.name == system_service.name).first() is not None
