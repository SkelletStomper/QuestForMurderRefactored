from src.items.items import Item

from enum import Enum


class ArmorSlotType(Enum):
    CHEST = "CHEST"
    HEAD = "HEAD"
    HANDS = "HANDS"
    LEGS = "LEGS"
    FEET = "FEET"


class Armor(Item):
    def __init__(self, init_dict: dict):
        super().__init__(init_dict)
        self.type: ArmorSlotType = ArmorSlotType(init_dict["armor_type"])
        self.armor: int = init_dict["armor"]



