from pydantic import BaseModel, Field

from src.helpers.helpers import get_mac


class BaseSchema(BaseModel):
    """
    Base class for data schemas.

    Attributes:
        device_id (str): The Mac-Address of the device.
    """

    device_id: str = Field(default_factory=get_mac, alias="deviceMacAddress")
