from src.util.read_data import get_all_filenames, read_json_data

from src.data_providers._pronoun_provider import PronounProvider
from src.data_providers._flag_provider import FlagProvider
from src.data_providers._item_provider import ItemProvider
from src.data_providers._monster_provider import MonsterProvider
from src.data_providers._armor_material_provider import ArmorMaterialProvider
from src.data_providers._species_provider import SpeciesProvider

import logging
logger = logging.getLogger(__name__)



def filter_json_type(all_data, json_type):
    right_data = {}

    for _key, _value in all_data.items():
        if isinstance(_value, str):
            raise ValueError(f"{_key}: {_value} does not have a dict as value!")
        if _value["json_type"].startswith(json_type):
            right_data[_key] = _value

    return right_data


_filenames = get_all_filenames()
logger.debug(f"Got all filenames: {_filenames}")
_all_data: dict[str, dict] = {}


for filename in _filenames:
    this_data = read_json_data(filename)

    for key, value in this_data.items():
        if key in _all_data:
            logger.error(f"duplicate key {key} in data")
            raise KeyError(f"duplicate key {key} in data")
        _all_data[key] = value


_pronoun_data = filter_json_type(_all_data, "pronouns")
pronoun_provider = PronounProvider(_pronoun_data)
logger.info(pronoun_provider)

_flag_data = filter_json_type(_all_data, "flag")
flag_provider = FlagProvider(_flag_data)
logger.info(flag_provider)


_item_data = filter_json_type(_all_data, "item")
item_provider = ItemProvider(_item_data)
logger.info(item_provider)

_armat_data = filter_json_type(_all_data, "armor_material")
armat_provider = ArmorMaterialProvider(_armat_data)
logger.info(armat_provider)

_species_data = filter_json_type(_all_data, "species")
species_provider = SpeciesProvider(_species_data)
logger.info(species_provider)

_monster_data = filter_json_type(_all_data, "monster")
monster_provider = MonsterProvider(_monster_data)
logger.info(monster_provider)


