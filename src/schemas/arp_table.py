from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseSingleARP(BaseModel):
    """
    Base class for a single ARP table entry.

    Attributes:
        ip_address (str): The IP address of the ARP table entry.
        mac_address (str): The MAC address of the ARP table entry.
    """

    ip_address: str = Field(None, description="The IP address of the ARP-table entry", serialization_alias="ipAddress")
    mac_address: str = Field(None, description="The MAC address of the ARP-table entry", serialization_alias="macAddress")


class SingleARP(BaseSingleARP, BaseSchema):
    """
    Class representing a single ARP table entry.

    Inherits from:
        - BaseSingleARP
        - BaseSchema
    """


class ListARP(BaseSchema):
    """
    Class representing a list of ARP table entries.

    Inherits from:
        - BaseSchema

    Attributes:
        items (List[BaseSingleARP]): A list of single ARP table entries.
    """

    items: List[BaseSingleARP]
