from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseSingleNetworkInterface(BaseModel):
    """
    Base class for a single network interface.
    """

    name: str = Field(None, description="The name of the interface.")
    ip: str = Field(None, description="The IP address of the interface", alias="ipAddress")


class SingleNetworkInterface(BaseSingleNetworkInterface, BaseSchema):
    """
    Class representing a single network interface.

    Inherits from:
        - BaseSingleNetworkInterface
        - BaseSchema
    """


class ListNetworkInterface(BaseSchema):
    """
    Class representing a list of network interfaces.

    Inherits from:
        - BaseSchema

    Attributes:
        items (List[BaseSingleNetworkInterface]): A list of single network interfaces.
    """

    items: List[BaseSingleNetworkInterface]
