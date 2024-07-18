from attack import WeaknessSet
import json


class Flag:
    def __init__(self, in_dict: dict):

        self.description: str = in_dict["description"]

        raw_weaknesses = {}
        if "weaknesses" in in_dict.values():
            raw_weaknesses = in_dict["weaknesses"]
        self.weaknesses = WeaknessSet(raw_weaknesses)

class FlagProvider:
    def __init__(self):


        with open("./json/flags.json", "r") as f:
          json_dict = json.load(f)

        self.flags = {flag_name :Flag(flag_data) for flag_name, flag_data in json_dict.items()}
        print(self.flags)

    def __getitem__(self, value) -> Flag:
        return self.flags[value]

flagProvider = FlagProvider()


