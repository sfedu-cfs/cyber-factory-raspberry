from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseMonitorResource(BaseModel):
    """
    Base class for a monitor resource.
    """

    cpu_load: float = Field(None, description="The CPU load in percent.")
    cpu_usage: float = Field(None, description="The CPU usage in percent.")
    cpu_avg_load: float = Field(None, description="The average CPU load in percent.")
    cpu_temperature: float = Field(None, description="The CPU temperature in degrees Celsius.")
    ram_usage: float = Field(None, description="The RAM usage in percent.")
    swap_usage: float = Field(None, description="The swap usage in percent.")
    disk_usage: float = Field(None, description="The disk usage in percent.")
    uptime: str = Field(None, description="The uptime of the system.")


class MonitorResource(BaseMonitorResource, BaseSchema):
    """
    Class representing a single monitor resource.

    Inherits from:
        - BaseMonitorResource
        - BaseSchema
    """
