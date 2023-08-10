from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseSingleARP(BaseModel):
    """
    Base class for a single ARP table entry.

    Attributes:
        name (str): The name of the ARP table entry.
        ip (str): The IP address of the ARP table entry.
        mac (str): The MAC address of the ARP table entry.
    """

    name: str = Field(None, description="The name of the ARP-table entry.")
    ip: str = Field(None, description="The IP address of the ARP-table entry", alias="ipAddress")
    mac: str = Field(None, description="The MAC address of the ARP-table entry", alias="macAddress")


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
