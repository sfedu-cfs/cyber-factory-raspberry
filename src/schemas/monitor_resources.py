from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class CPUMonitorResource(BaseModel):
    """
    Base class for a cpu monitor resource.
    """

    cpu_load: float = Field(None, description="The CPU load in percent.")
    cpu_usage: float = Field(None, description="The CPU usage in percent.")
    cpu_avg_load: float = Field(None, description="The average CPU load in percent.")
    cpu_temperature: float = Field(None, description="The CPU temperature in degrees Celsius.")


class RAMMonitorResource(BaseModel):
    """
    Base class for a ram monitor resource.
    """
    ram_usage: float = Field(None, description="The RAM usage in percent.")
    swap_usage: float = Field(None, description="The swap usage in percent.")


class GeneralMonitorResource(BaseModel):
    """
    Base class for a general monitor resource.
    """
    disk_usage: float = Field(None, description="The disk usage in percent.")
    uptime: str = Field(None, description="The uptime of the system.")


class BaseMonitorResource(BaseModel):
    """
    Base class for a single monitor resource.
    """
    cpu: CPUMonitorResource = Field(None, description="The CPU monitor resource.")
    ram: RAMMonitorResource = Field(None, description="The RAM monitor resource.")
    general: GeneralMonitorResource = Field(None, description="The general monitor resource.")


class MonitorResource(BaseSchema):
    """
    Class representing a single monitor resource.

    Inherits from:
        - BaseMonitorResource
        - BaseSchema
    """
    system_resources: BaseMonitorResource = Field(None, description="The system monitor resource.")
