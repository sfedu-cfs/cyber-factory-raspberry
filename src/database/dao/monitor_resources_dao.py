from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.monitor_resources import MonitorResources
from src.core.log_config import logger


class MonitorResourcesDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, monitor_resource_data):
        try:
            monitor_resource_entry = MonitorResources(**monitor_resource_data)
            monitor_resource_entry.created_date = dt.now()
            self.db.add(monitor_resource_entry)
            self.db.commit()
            self.db.refresh(monitor_resource_entry)
        except Exception as e:
            logger.error(f"Error while creating monitor resource: {e}")
            raise e
        return monitor_resource_entry

    def get_monitor_resource_by_id(self, monitor_resource_id):
        return self.db.query(MonitorResources).filter(MonitorResources.id == monitor_resource_id).first()

    def update_monitor_resource(self, monitor_resource_entry, updated_data):
        for key, value in updated_data.items():
            setattr(monitor_resource_entry, key, value)
        self.db.commit()
        self.db.refresh(monitor_resource_entry)
        return monitor_resource_entry

    def delete_monitor_resource(self, monitor_resource_entry):
        self.db.delete(monitor_resource_entry)
        self.db.commit()
