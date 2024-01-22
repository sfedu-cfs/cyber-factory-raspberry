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
    db_user = os.environ.get("PGUSER")
    db_password = os.environ.get("PGPASSWORD")
    db_host = os.environ.get("PGHOST")
    network_interface = os.environ.get("NET_IFACE")
    mac_address = os.environ.get("MAC_ADDRESS")
    ip_address = os.environ.get("IP_ADDRESS")
    default_gateway = os.environ.get("DEFAULT_GATEWAY")


config = Config()
