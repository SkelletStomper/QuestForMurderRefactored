from src.base.flag import Flag

import logging
logger = logging.getLogger(__name__)


class FlagProvider:
    def __init__(self, all_flag_data):
        logger.info("Start parsing flag data")
        self.flags = {flag_name: Flag(flag_name, flag_data) for flag_name, flag_data in all_flag_data.items()}
        logger.info("Finished parsing flag data")
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

    def __repr__(self) -> str:
        return "FlagProvider"
