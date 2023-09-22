from pydantic import BaseModel, Field


class RegDevice(BaseModel):
    name: str = Field(None, description="The name of device.")
    ip: str = Field(None, description="The ip address of device",
                    serialization_alias="ipAddress")
    mac: str = Field(None, description="The ip address of device",
                     serialization_alias="macAddress")
    net_iface: str = Field(None, description="The primary network interface of device",
                           serialization_alias="networkInterface")
    cfs_id: int = Field(None, description="The Cyber Physical System ID",
                        serialization_alias="cyberPhysicalSystemId")
