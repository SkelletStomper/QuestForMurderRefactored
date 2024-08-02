
from src.data_providers._flag_provider import FlagProvider, Flag


def test_flag_provider():
    read_data = {"test_flag": {"description": "A test flag"}}

    provider = FlagProvider(read_data)
    assert "test_flag" in provider.flags
    flag = provider["test_flag"]
    assert isinstance(flag, Flag)
    assert flag.description == "A test flag"


def test_flag_provider_with_default_value():
    read_data = {"test_flag": {"description": "A test flag", "default_value": 10}}
    provider = FlagProvider(read_data)
    flag = provider("test_flag")
    assert flag.value == 10
    assert flag.value_type == int

    flag_with_value = provider("test_flag$20")
    assert flag_with_value.value == 20
    assert flag_with_value.value_type == int

