from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.core.config import config

# Создание подключения к базе данных
engine = create_engine(f"postgresql://{config.db_user}:{config.db_password}@{config.db_host}:5432/cyber-factory")

# Создание сессии для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Определение базовой модели данных с использованием SQLAlchemy
Base = declarative_base()
