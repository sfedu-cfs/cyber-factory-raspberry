from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel
from pydantic.v1.typing import NoneType


class BaseNetworkInterface(BaseModel):
    deviceMacAddress: str


class BaseSingleNetworkInterface(BaseModel):
    name: str
    ipAddress: str


class SingleNetworkInterface(BaseNetworkInterface, BaseSingleNetworkInterface):
    pass


class ListNetworkInterface(BaseNetworkInterface):
    items: List[BaseSingleNetworkInterface]


class Car(BaseModel):
    name: str
    color: str


class User(BaseModel):
    id: int
    name: str
    age: Union[int, NoneType]
    town: Union[str, NoneType]
    car: Car
