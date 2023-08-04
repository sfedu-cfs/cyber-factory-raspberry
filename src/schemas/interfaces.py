from pydantic import BaseModel
from typing import List

from src.helpers.helpers import get_mac


class BaseNetworkInterface(BaseModel):
    deviceMacAddress: str = get_mac()


class BaseSingleNetworkInterface(BaseModel):
    name: str
    ipAddress: str


class SingleNetworkInterface(BaseSingleNetworkInterface, BaseNetworkInterface):
    pass


class ListNetworkInterface(BaseNetworkInterface):
    items: List[BaseSingleNetworkInterface]
