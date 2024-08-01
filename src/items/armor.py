from src.items.items import Item

from enum import Enum


class ArmorSlotType(Enum):
    CHEST = "CHEST"
    HEAD = "HEAD"
    HANDS = "HANDS"
    LEGS = "LEGS"
    FEET = "FEET"


class Armor(Item):
    def __init__(self, in_dict: dict):
        super().__init__(in_dict)
        self.type: ArmorSlotType = ArmorSlotType(in_dict["type"])
        self.armor: int = in_dict["armor"]
