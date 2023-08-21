from pydantic import BaseModel, Field
from typing import List

from src.schemas.base import BaseSchema


class BaseSingleSFC(BaseModel):
    """
    Base model representing a single Service Function Component (SFC).

    Attributes:
        name (str): The name of the SFC.
        version (str): The version of the SFC.
    """

    name: str = Field(None, description="The name of the SFC.")
    version: str = Field(None, description="The version of the SFC.")


class SingleSFC(BaseSingleSFC, BaseSchema):
    """
    Model representing a single Service Function Component (SFC) with device ID.

    Inherits from:
        - BaseSingleSFC
        - BaseSchema
    """


class ListSFC(BaseSchema):
    """
    Model representing a list of Service Function Components (SFCs) with device ID.

    Inherits from:
        - BaseSchema

    Attributes:
        items (List[BaseSingleSFC]): A list of BaseSingleSFC instances representing the SFCs.
    """

    items: List[BaseSingleSFC]
