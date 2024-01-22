from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class CPUMonitorResource(BaseModel):
    """
    Base class for a cpu monitor resource.
    """

    cpu_load: float = Field(None,
                            description="The CPU load in percent.",
                            serialization_alias="cpuLoad")
    cpu_temperature: float = Field(0,
                                   description="The CPU temperature in degrees Celsius.",
                                   serialization_alias="cpuTemperature")


class RAMMonitorResource(BaseModel):
    """
    Base class for a ram monitor resource.
    """
    ram_usage: float = Field(None,
                             description="The RAM usage in percent.",
                             serialization_alias="ramUsage")
    swap_usage: float = Field(None,
                              description="The swap usage in percent.",
                              serialization_alias="swapUsage")


class GeneralMonitorResource(BaseModel):
    """
    Base class for a general monitor resource.
    """
    disk_usage: float = Field(None,
                              description="The disk usage in percent.",
                              serialization_alias="diskUsage")
    uptime: str = Field(None,
                        description="The uptime of the system.")


class MonitorResource(CPUMonitorResource, RAMMonitorResource, GeneralMonitorResource):
    """
    Class representing a single monitor resource.

    Inherits from:
        - BaseMonitorResource
        - BaseSchema
    """
    # system_resources: BaseMonitorResource = Field(None, description="The system monitor resource.")
