from attack import AttackType
import json
import typing

class Flag:
    def __init__(self, in_dict: dict):

        self.description: str = in_dict["description"]
        self.weaknesses: dict[AttackType, float] = {}
        if "weaknesses" in in_dict.keys():
            for weakness, factor in in_dict["weaknesses"].items():
                self.weaknesses[AttackType(weakness)] = factor

class FlagProvider:
    def __init__(self):

        json_dict: dict[str,typing.Any] = {}
        with open("./json/flags.json", "r") as f:
          json_dict = json.load(f)

        self.flags = {flag_name :Flag(flag_data) for flag_name, flag_data in json_dict.items()}
        print(self.flags)

    def __getitem__(self, value) -> Flag:
        return self.flags[value]

flagProvider = FlagProvider()


