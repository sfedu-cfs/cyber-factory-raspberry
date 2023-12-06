from src.database.connection import Session
from src.database.models.apps import App


class AppDAO:
    def __init__(self, db: Session):
        self.db = db

    def create_app(self, app_data):
        app = App(**app_data.dict())
        self.db.add(app)
        self.db.commit()
        self.db.refresh(app)
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
