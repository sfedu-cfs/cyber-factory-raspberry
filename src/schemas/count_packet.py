from pydantic import BaseModel, Field

from src.schemas.base import BaseSchema


class BaseCountPacket(BaseModel):
    """
    Base class for a count packet.
    """

    all_proto_count: int = Field(0, description="The number of packets.")
    timing: int = Field(..., description="Time interval for which packets were collected in seconds")


class EthernetLayer(BaseModel):
    """
    Base class for a ethernet layer.
    """

    arp_count: int = Field(None, description="The number of arp packets.")


class TransportLayer(BaseModel):
    """
    Base class for a transport layer.
    """

    tcp_count: int = Field(None, description="The number of tcp packets.")
    udp_count: int = Field(None, description="The number of udp packets.")
    icmp_count: int = Field(None, description="The number of icmp packets.")


class PresentationLayer(BaseModel):
    """
    Base class for a presentation layer
    """

    http_request_count: int = Field(None, description="The number of http request packets.")
    http_response_count: int = Field(None, description="The number of http response packets.")


class ModbusLayer(BaseModel):
    """
    Base class for a modbus layer
    """

    modbus_01_request_count: int = Field(None, description="The number of modbus 01 function request packets.")
    modbus_01_response_count: int = Field(None, description="The number of modbus 01 function response packets.")
    modbus_02_request_count: int = Field(None, description="The number of modbus 02 function request packets.")
    modbus_02_response_count: int = Field(None, description="The number of modbus 02 function response packets.")
    modbus_03_request_count: int = Field(None, description="The number of modbus 03 function request packets.")
    modbus_03_response_count: int = Field(None, description="The number of modbus 03 function response packets.")
    modbus_04_request_count: int = Field(None, description="The number of modbus 04 function request packets.")
    modbus_04_response_count: int = Field(None, description="The number of modbus 04 function response packets.")
    modbus_05_request_count: int = Field(None, description="The number of modbus 05 function request packets.")
    modbus_05_response_count: int = Field(None, description="The number of modbus 05 function response packets.")
    modbus_06_request_count: int = Field(None, description="The number of modbus 06 function request packets.")
    modbus_06_response_count: int = Field(None, description="The number of modbus 06 function response packets.")
    modbus_15_request_count: int = Field(None, description="The number of modbus 15 function request packets.")
    modbus_15_response_count: int = Field(None, description="The number of modbus 15 function response packets.")
    modbus_16_request_count: int = Field(None, description="The number of modbus 16 function request packets.")
    modbus_16_response_count: int = Field(None, description="The number of modbus 16 function response packets.")


class CountPacket(ModbusLayer, PresentationLayer, TransportLayer, EthernetLayer, BaseCountPacket, BaseSchema):
    """
    Class representing a count packet.

    Inherits from:
        - ModbusLayer
        - PresentationLayer
        - TransportLayer
        - EthernetLayer
        - BaseCountPacket
        - BaseSchema
    """


c_p = CountPacket(timing=5)
