from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseSingleApp(BaseModel):
    """
    Base class for a single app.
    """

    name: str = Field(None, description="The name of the app.")
    version: str = Field(None, description="The version of the app")
    description: str = Field(None, description="The description text of the app")


class SingleApp(BaseSingleApp, BaseSchema):
    """
    Class representing a single app.

    Inherits from:
        - BaseSingleApp
        - BaseSchema
    """


class ListApp(BaseSchema):
    """
    Class representing a list of apps.

    Inherits from:
        - BaseSchema

    Attributes:
        items (List[BaseSingleApp]): A list of single apps.
    """

    items: List[BaseSingleApp]
