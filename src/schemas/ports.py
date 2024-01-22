from pydantic import BaseModel, Field
from typing import List


class BaseSchema(BaseModel):
    ip_address: str = Field(None, description="The IP address of host", serialization_alias="hostIpAddress")


class BasePort(BaseModel):
    """
    Base class for a single port.
    """
    port: int = Field(None, description="The port number.")
    status: str = Field(None, description="The status of the port.")
    service: str = Field(None, description="The service running on the port.")
    protocol: str = Field(None, description="The protocol of the port.")


class SinglePort(BasePort, BaseSchema):
    """
    Class representing a single port.

    Inherits from:
        - BasePort
        - BaseSchema
    """


class ListPort(BaseSchema):
    """
    Class representing a list of ports.

    Inherits from:
        - BaseSchema

    Attributes:
        items (List[BasePort]): A list of single ports.
    """

    items: List[BasePort]
