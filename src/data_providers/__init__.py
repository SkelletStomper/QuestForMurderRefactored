from src.util.read_data import get_all_filenames, read_json_data

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




def load_pronouns():
    from src.data_providers._pronoun_provider import PronounProvider
    _pronoun_data = filter_json_type(_all_data, "pronouns")
    new_pronoun_provider = PronounProvider(_pronoun_data)
    logger.info(new_pronoun_provider)
    return new_pronoun_provider


def load_flags():
    from src.data_providers._flag_provider import FlagProvider
    _flag_data = filter_json_type(_all_data, "flag")
    new_flag_provider = FlagProvider(_flag_data)
    logger.info(new_flag_provider)
    return new_flag_provider


def load_armats():
    from src.data_providers._armor_material_provider import ArmorMaterialProvider
    _armat_data = filter_json_type(_all_data, "armor_material")
    new_armat_provider = ArmorMaterialProvider(_armat_data)
    logger.info(new_armat_provider)
    return new_armat_provider


def load_species():
    from src.data_providers._species_provider import SpeciesProvider
    _species_data = filter_json_type(_all_data, "species")
    new_species_provider = SpeciesProvider(_species_data)
    logger.info(new_species_provider)
    return new_species_provider


def load_items():
    from src.data_providers._item_provider import ItemProvider
    _item_data = filter_json_type(_all_data, "item")
    new_item_provider = ItemProvider(_item_data)
    logger.info(new_item_provider)
    return new_item_provider


def load_monsters():
    from src.data_providers._monster_provider import MonsterProvider
    _monster_data = filter_json_type(_all_data, "monster")
    new_monster_provider = MonsterProvider(_monster_data)
    logger.info(new_monster_provider)
    return new_monster_provider


def load_dialogue():
    from src.data_providers._dialogue_provider import DialogueProvider
    _dialogue_data = filter_json_type(_all_data, "dialogue")
    new_dialogue_provider = DialogueProvider(_dialogue_data)
    logger.info(new_dialogue_provider)
    return new_dialogue_provider


quest_provider = load_quests()

pronoun_provider = load_pronouns()

flag_provider = load_flags()

armat_provider = load_armats()

species_provider = load_species()

item_provider = load_items()

monster_provider = load_monsters()

dialogue_provider = load_dialogue()


