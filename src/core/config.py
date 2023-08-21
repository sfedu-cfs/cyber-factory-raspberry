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


config = Config()
