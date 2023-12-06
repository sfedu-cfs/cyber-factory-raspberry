from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseSingleConnection(BaseModel):
    """
    Base class for a single connection.
    """

    protocol: str = Field(None, description="The protocol of the connection")
    src_ip_address: str = Field(None, description="The source ip address of the connection")
    src_port: int = Field(None, description="The source port of the connection")
    dst_ip_address: str = Field(None, description="The destination ip address of the connection")
    dst_port: int = Field(None, description="The destination port of the connection")
    state: str = Field(None, description="The state of the connection")
    service_name: str = Field(None, description="The name of the service")


class SingleConnection(BaseSingleConnection, BaseSchema):
    """
    Class representing a single connection.

    Inherits from:
        - BaseSingleConnection
        - BaseSchema
    """


class ListConnection(BaseSchema):
    """
    Class representing a list of connections.

    Inherits from:
        - BaseSchema

    Attributes:
        items (List[BaseSingleConnection]): A list of single connections.
    """

    items: List[BaseSingleConnection]
