from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.apps import App, AppCurrent
from src.core.log_config import logger


class AppDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, app_data):
        try:
            app = App(**app_data)
            app.created_date = dt.now()
            self.db.add(app)
            self.db.commit()
            self.db.refresh(app)
        except Exception as e:
            logger.error(f"Error while creating app: {e}")
            raise e
        return app

    def get_app_by_id(self, app_id):
        return self.db.query(App).filter(App.id == app_id).first()

    def get_app_by_name(self, app_name):
        return self.db.query(App).filter(App.name == app_name).first()

    def update_app(self, app, updated_data):
        for key, value in updated_data.items():
            setattr(app, key, value)
        self.db.commit()
        self.db.refresh(app)
        return app

    def delete_app(self, app):
        self.db.delete(app)
        self.db.commit()

    def exists(self, app):
        return self.db.query(App).filter(App.name == app.name).first() is not None


class AppCurrentDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, app_data):
        try:
            app = AppCurrent(**app_data)
            app.created_date = dt.now()
            self.db.add(app)
            self.db.commit()
            self.db.refresh(app)
        except Exception as e:
            logger.error(f"Error while creating app: {e}")
            raise e
        return app

    def delete_all(self):
        self.db.query(AppCurrent).delete()
        self.db.commit()

    def exists(self, app):
        return self.db.query(AppCurrent).filter(AppCurrent.name == app.name).first() is not None
