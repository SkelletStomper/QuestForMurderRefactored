from src.util.read_data import get_all_filenames, read_json_data

from src.data_providers._pronoun_provider import PronounProvider
from src.data_providers._flag_provider import FlagProvider
from src.data_providers._item_provider import ItemProvider
from src.data_providers._monster_provider import MonsterProvider


def filter_json_type(all_data, json_type):
    right_data = {}

    for _key, _value in all_data.items():
        if isinstance(_value, str):
            raise ValueError(f"{_key}: {_value} does not have a dict as value!")
        if _value["json_type"].startswith(json_type):
            right_data[_key] = _value

    return right_data


_filenames = get_all_filenames()

_all_data: dict[str, dict] = {}

print(_filenames)


for filename in _filenames:
    this_data = read_json_data(filename)

    for key, value in this_data.items():
        if key in _all_data:
            raise KeyError(f"duplicate key {key} in data")
        _all_data[key] = value

print(_all_data)

_pronoun_data = filter_json_type(_all_data, "pronouns")
pronoun_provider = PronounProvider(_pronoun_data)


_flag_data = filter_json_type(_all_data, "flag")
flag_provider = FlagProvider(_flag_data)

_monster_data = filter_json_type(_all_data, "monster")
monster_provider = MonsterProvider(_monster_data)

_item_data = filter_json_type(_all_data, "item")
item_provider = ItemProvider(_item_data)

print(_pronoun_data)
print(_flag_data)
print(_monster_data)
print(_item_data)

