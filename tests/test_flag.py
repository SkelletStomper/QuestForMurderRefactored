import pytest
from unittest.mock import patch, mock_open
from src.flag import Flag, FlagProvider
from src.combat.attack import WeaknessSet


# Test data for Flag class
@pytest.fixture
def flag_data():
    return {
        "name": "test_flag",
        "default_value": 10,
        "description": "A test flag",
        "weaknesses": {"PHYSICAL": "1.0"}
    }


def test_flag_initialization(flag_data):
    flag = Flag(flag_data["name"], flag_data)
    assert flag.name == flag_data["name"]
    assert flag.value == flag_data["default_value"]
    assert flag.value_type == int
    assert flag.description == flag_data["description"]
    assert isinstance(flag.weaknesses, WeaknessSet)



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
    assert flag == flag_data["name"]
    assert flag != "another_flag"


@patch("src.flag.open", new_callable=mock_open, read_data='{"test_flag": {"description": "A test flag"}}')
def test_flag_provider(mock_file):
    provider = FlagProvider()
    assert "test_flag" in provider.flags
    flag = provider["test_flag"]
    assert isinstance(flag, Flag)
    assert flag.description == "A test flag"


@patch("src.flag.open", new_callable=mock_open, read_data='{"test_flag": {"description": "A test flag", "default_value": 10}}')
def test_flag_provider_with_default_value(mock_file):
    provider = FlagProvider()
    flag = provider("test_flag")
    assert flag.value_type == 10
    assert flag.value == int

    flag_with_value = provider("test_flag$20")
    assert flag_with_value.value == 20
    assert flag_with_value.value_type == int


# Mocking WeaknessSet and checking the interactions
@patch("src.flag.WeaknessSet", autospec=True)
def test_flag_with_mocked_weaknesses(MockWeaknessSet, flag_data):
    MockWeaknessSet.return_value = MockWeaknessSet
    flag = Flag("test_flag", flag_data)
    assert isinstance(flag.weaknesses, MockWeaknessSet)


# Mocking the file read error
@patch("src.flag.open", new_callable=mock_open)
def test_flag_provider_file_read_error(mock_file):
    mock_file.side_effect = IOError("File not found")
    with pytest.raises(OSError):
        FlagProvider()

