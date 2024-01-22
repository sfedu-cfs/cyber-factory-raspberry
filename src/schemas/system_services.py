from datetime import date

from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseSingleSystemService(BaseModel):
    """
    Base class for a single system service.

    Attributes:
        name (str): The name of the system service.
        status (str): The status of the system service.
    """

    name: str = Field(None, description="The name of the system service.")
    status: str = Field(None, description="The status of the system service.")
    created_date: date = Field(None, description="The date the system service was created.")


class SingleSystemService(BaseSingleSystemService, BaseSchema):
    """
    Class representing a single system service.

    Inherits from:
        - BaseSingleSystemService
        - BaseSchema
    """


class ListSystemService(BaseSchema):
    """
    Class representing a list of system services.

    Inherits from:
        - BaseSchema

    Attributes:
        items (List[BaseSingleSystemService]): A list of single system services.
    """

    items: List[BaseSingleSystemService]
