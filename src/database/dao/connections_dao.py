from datetime import datetime as dt

from src.database.connection import Session
from src.database.models.connections import Connections, ConnectionsCurrent
from src.core.log_config import logger


class ConnectionsDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, connection_data):
        try:
            connection = Connections(**connection_data)
            connection.created_date = dt.now()
            self.db.add(connection)
            self.db.commit()
            self.db.refresh(connection)
        except Exception as e:
            logger.error(f"Error while creating connection: {e}")
            raise e
        return connection

    def get_connection_by_id(self, connection_id):
        return self.db.query(Connections).filter(Connections.id == connection_id).first()

    def update_connection(self, connection, updated_data):
        for key, value in updated_data.items():
            setattr(connection, key, value)
        self.db.commit()
        self.db.refresh(connection)
        return connection

    def delete_connection(self, connection):
        self.db.delete(connection)
        self.db.commit()

    def exists(self, connection):
        return self.db.query(Connections).filter(Connections.service_name == connection.service_name).first() is not None


class ConnectionsCurrentDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, connection_data):
        try:
            connection = ConnectionsCurrent(**connection_data)
            connection.created_date = dt.now()
            self.db.add(connection)
            self.db.commit()
            self.db.refresh(connection)
        except Exception as e:
            logger.error(f"Error while creating connection: {e}")
            raise e
        return connection

    def get_connection_by_id(self, connection_id):
        return self.db.query(ConnectionsCurrent).filter(ConnectionsCurrent.id == connection_id).first()

    def update_connection(self, connection, updated_data):
        for key, value in updated_data.items():
            setattr(connection, key, value)
        self.db.commit()
        self.db.refresh(connection)
        return connection

    def delete_connection(self, connection):
        self.db.delete(connection)
        self.db.commit()

    def exists(self, connection):
        return self.db.query(ConnectionsCurrent).filter(ConnectionsCurrent.service_name == connection.service_name).first() is not None

    def delete_all(self):
        self.db.query(ConnectionsCurrent).delete()
        self.db.commit()
