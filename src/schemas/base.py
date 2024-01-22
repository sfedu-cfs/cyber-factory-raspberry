from pydantic import BaseModel, Field

from src.core.config import config


class BaseSchema(BaseModel):
    """
    Base class for data schemas.

    Attributes:
        device_id (str): The Mac-Address of the device.
    """

    # device_id: str = Field(default=config.mac_address, alias="deviceMacAddress")
    pass
