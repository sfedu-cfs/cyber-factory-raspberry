from src.database.connection import Session
from src.database.models.system_services import SystemServices


class SystemServicesDAO:
    def __init__(self, db: Session):
        self.db = db

    def create_system_service(self, system_service_data):
        system_service_entry = SystemServices(**system_service_data)
        self.db.add(system_service_entry)
        self.db.commit()
        self.db.refresh(system_service_entry)
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
