from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseHost(BaseModel):
    """
    Base class for a single host.
    """

    ip_address: str = Field(None, description="The IP address of the host.", serialization_alias="ipAddress")
    mac_address: str = Field(None, description="The MAC address of the host.", serialization_alias="macAddress")


class SingleHost(BaseHost, BaseSchema):
    """
    Class representing a single host.

    Inherits from:
        - BaseHost
        - BaseSchema
    """


class ListHost(BaseSchema):
    """
    Class representing a list of hosts.

    Inherits from:
        - BaseSchema

    Attributes:
        items (List[BaseHost]): A list of single hosts.
    """

    items: List[BaseHost]
