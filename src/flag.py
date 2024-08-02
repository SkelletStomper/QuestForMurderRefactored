from src.combat.attack import WeaknessSet
from src.util.read_data import read_json_data
from copy import copy


class Flag:
    def __init__(self, name: str, init_dict: dict):

        self.name = name
        self.value = None
        self.value_type = None
        if "default_value" in init_dict:
            self.value = init_dict["default_value"]
            self.value_type = type(self.value)

        self.description: str = init_dict["description"]

        raw_weaknesses = {}
        if "weaknesses" in init_dict.keys():
            raw_weaknesses = init_dict["weaknesses"]
        self.weaknesses = WeaknessSet(raw_weaknesses)

    def get_copy(self, value=None) -> "Flag":
        flag_copy = copy(self)
        if value is not None:
            flag_copy.value = value

        return flag_copy

    def __eq__(self, value: str) -> bool:
        return self.name == value


class FlagProvider:
    def __init__(self):
        json_dict = read_json_data("flags.json")
        self.flags = {flag_name: Flag(flag_name, flag_data) for flag_name, flag_data in json_dict.items()}
        print(self.flags)

    def __getitem__(self, value) -> Flag:
        return self.flags[value]

    def __call__(self, flag_str: str) -> Flag:
        flag_name = flag_str
        value = None
        if "$" in flag_str:
            flag_name, value = flag_str.split("$")
            value = self[flag_name].value_type(value)

        return self[flag_name].get_copy(value)


flag_provider = FlagProvider()
