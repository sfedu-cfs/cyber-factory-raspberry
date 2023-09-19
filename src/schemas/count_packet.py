from datetime import time, datetime as dt

from pydantic import BaseModel, Field

from src.schemas.base import BaseSchema


class BaseCountPacket(BaseModel):
    """
    Base class for a count packet.
    """

    all_proto_count: int = Field(0, description="The number of packets.", serialization_alias="allProtoCount")
    timing: int = Field(..., description="Time interval for which packets were collected in seconds")
    last_update: time = Field(default=dt.now().time(), description="The time of the last packet update.", exclude=True)


class EthernetLayer(BaseModel):
    """
    Base class for an ethernet layer.
    """

    arp_count: int = Field(0, description="The number of arp packets.", serialization_alias="arpCount")


class TransportLayer(BaseModel):
    """
    Base class for a transport layer.
    """

    tcp_count: int = Field(0, description="The number of tcp packets.", serialization_alias="tcpCount")
    udp_count: int = Field(0, description="The number of udp packets.", serialization_alias="udpCount")
    icmp_count: int = Field(0, description="The number of icmp packets.", serialization_alias="icmpCount")


class PresentationLayer(BaseModel):
    """
    Base class for a presentation layer
    """

    http_request_count: int = Field(0, description="The number of http request packets.",
                                    serialization_alias="httpRequestCount")
    http_response_count: int = Field(0, description="The number of http response packets.",
                                     serialization_alias="httpResponseCount")


class ModbusLayer(BaseModel):
    """
    Base class for a modbus layer
    """

    modbus_01_request_count: int = Field(0, description="The number of modbus 01 function request packets.",
                                         serialization_alias="modbus01RequestCount")
    modbus_01_response_count: int = Field(0, description="The number of modbus 01 function response packets.",
                                          serialization_alias="modbus01ResponseCount")
    modbus_02_request_count: int = Field(0, description="The number of modbus 02 function request packets.",
                                         serialization_alias="modbus02RequestCount")
    modbus_02_response_count: int = Field(0, description="The number of modbus 02 function response packets.",
                                          serialization_alias="modbus02ResponseCount")
    modbus_03_request_count: int = Field(0, description="The number of modbus 03 function request packets.",
                                         serialization_alias="modbus03RequestCount")
    modbus_03_response_count: int = Field(0, description="The number of modbus 03 function response packets.",
                                          serialization_alias="modbus03ResponseCount")
    modbus_04_request_count: int = Field(0, description="The number of modbus 04 function request packets.",
                                         serialization_alias="modbus04RequestCount")
    modbus_04_response_count: int = Field(0, description="The number of modbus 04 function response packets.",
                                          serialization_alias="modbus04ResponseCount")
    modbus_05_request_count: int = Field(0, description="The number of modbus 05 function request packets.",
                                         serialization_alias="modbus05RequestCount")
    modbus_05_response_count: int = Field(0, description="The number of modbus 05 function response packets.",
                                          serialization_alias="modbus05ResponseCount")
    modbus_06_request_count: int = Field(0, description="The number of modbus 06 function request packets.",
                                         serialization_alias="modbus06RequestCount")
    modbus_06_response_count: int = Field(0, description="The number of modbus 06 function response packets.",
                                          serialization_alias="modbus06ResponseCount")
    modbus_15_request_count: int = Field(0, description="The number of modbus 15 function request packets.",
                                         serialization_alias="modbus15RequestCount")
    modbus_15_response_count: int = Field(0, description="The number of modbus 15 function response packets.",
                                          serialization_alias="modbus15ResponseCount")
    modbus_16_request_count: int = Field(0, description="The number of modbus 16 function request packets.",
                                         serialization_alias="modbus16RequestCount")
    modbus_16_response_count: int = Field(0, description="The number of modbus 16 function response packets.",
                                          serialization_alias="modbus16ResponseCount")


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
