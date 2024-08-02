from src.flag import Flag

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