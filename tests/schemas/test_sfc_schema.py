import pytest
from pydantic import ValidationError

from src.helpers.helpers import get_mac
from src.schemas.sfc import SFC


def test_sfc_creation():
    """
    Test creating an SFC instance with valid attributes.
    """
    sfc = SFC(name="MySFC", version="1.0")
    assert sfc.name == "MySFC"
    assert sfc.version == "1.0"
    assert sfc.deviceMacAddress == get_mac()


def test_sfc_creation_missing_attributes():
    """
    Test creating an SFC instance with missing required attributes.
    """
    with pytest.raises(ValidationError):
        # Missing name attribute
        SFC(version="1.0")

    with pytest.raises(ValidationError):
        # Missing version attribute
        SFC(name="MySFC")


def test_sfc_creation_invalid_attributes():
    """
    Test creating an SFC instance with invalid attributes.
    """
    with pytest.raises(ValidationError):
        # Invalid data type for name attribute
        SFC(name=123, version="1.0")

    with pytest.raises(ValidationError):
        # Invalid data type for version attribute
        SFC(name="MySFC", version=1.0)
