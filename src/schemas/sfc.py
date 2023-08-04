from pydantic import BaseModel, Field, ValidationError
from src.helpers.helpers import get_mac


class SFC(BaseModel):
    """
    Represents a Service Function Chain (SFC) configuration.

    This class defines the structure of an SFC configuration using the Pydantic BaseModel.
    It includes properties for the device MAC address, name, and version.

    Attributes:
        deviceMacAddress (str): The MAC address of the device. It is set to the value returned by the `get_mac()` function.
        name (str): The name of the SFC.
        version (str): The version of the SFC.

    Note:
        The `get_mac()` function is imported from the `src.helpers.helpers` module.

    Example:
        sfc = SFC(name="MySFC", version="1.0")
    """

    device_id: str = Field(default_factory=get_mac, alias="deviceMacAddress")
    name: str = Field(..., description="The name of the SFC.")
    version: str = Field(..., description="The version of the SFC.")
