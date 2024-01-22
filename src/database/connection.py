import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.log_config import logger

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
database_url = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(root_path, 'cyber_factory.db')}")

engine = create_engine(database_url)
logger.info(f"Database created at: {database_url}")

Session = sessionmaker(bind=engine)
Base = declarative_base()
