from src.base.types import WeaknessSet

from copy import copy


class Flag:
    """
    Entities can have flags to signify special properties.
    By checking if an entity has a flag, it is possible to check this condition later in the code, and allows for special effects.
    Flags are gotten from and instantiated in the Flag Provider.
    Some Flags come with a WeaknessSet and/or a value.
    """
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

    def __repr__(self) -> str:
        return f"Flag(name={self.name}, value={self.value}, value_type={self.value_type}, description={self.description}, " \
               f"weaknesses= {self.weaknesses})"
