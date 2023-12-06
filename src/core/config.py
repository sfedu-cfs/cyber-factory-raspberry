import os

from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@dataclass
class Config:
    """
    Configuration class
    """
    base_url = os.environ.get("BASE_URL")
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    db_host = os.environ.get("DB_HOST")


config = Config()
