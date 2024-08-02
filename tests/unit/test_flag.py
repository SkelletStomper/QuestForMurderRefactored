import pytest
from unittest.mock import patch, mock_open
from math import isclose

from src.flag import Flag, FlagProvider
from src.combat.attack import WeaknessSet


# Test data for Flag class
@pytest.fixture
def flag_data() -> dict:
    return {
        "name": "test_flag",
        "default_value": 10,
        "description": "A test flag",
    }


def test_flag_initialization(flag_data):
    flag = Flag(flag_data["name"], flag_data)
    assert flag.name == flag_data["name"]
    assert flag.value == flag_data["default_value"]
    assert flag.value_type == int
    assert flag.description == flag_data["description"]


def test_flag_initialization_weaknesses(flag_data):
    flag_data["weaknesses"] = {"PHYSICAL": 0.5}
    flag = Flag(flag_data["name"], flag_data)

    assert isinstance(flag.weaknesses, WeaknessSet)
    assert isclose(flag.weaknesses["PHYSICAL"], 0.5)
    assert isclose(flag.weaknesses["MAGICAL"], 1.0)


def test_flag_get_copy(flag_data):
    flag = Flag("test_flag", flag_data)
    flag_copy = flag.get_copy()
    assert flag_copy.name == flag_data["name"]
    assert flag_copy.value == flag_data["default_value"]
    assert flag_copy.value_type == int
    assert flag_copy.description == flag_data["description"]

    # Test with modified value
    flag_copy = flag.get_copy(value=20)
    assert flag_copy.value == 20


def test_flag_equality(flag_data):
    flag = Flag(flag_data["name"], flag_data)
    assert flag == flag_data["name"]  # type: ignore
    assert flag != "another_flag"


@patch("src.util.read_data.open", new_callable=mock_open, read_data='{"test_flag": {"description": "A test flag"}}')
def test_flag_provider(mock_file):
    provider = FlagProvider()
    assert "test_flag" in provider.flags
    flag = provider["test_flag"]
    assert isinstance(flag, Flag)
    assert flag.description == "A test flag"


@patch("src.util.read_data.open", new_callable=mock_open,
       read_data='{"test_flag": {"description": "A test flag", "default_value": 10}}')
def test_flag_provider_with_default_value(mock_file):
    provider = FlagProvider()
    flag = provider("test_flag")
    assert flag.value == 10
    assert flag.value_type == int

    flag_with_value = provider("test_flag$20")
    assert flag_with_value.value == 20
    assert flag_with_value.value_type == int

