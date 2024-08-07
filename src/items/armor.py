from src.items.items import Item

from enum import Enum


class ArmorSlotType(Enum):
    ANY = "ANY"
    CHEST = "CHEST"
    HEAD = "HEAD"
    HANDS = "HANDS"
    LEGS = "LEGS"
    FEET = "FEET"


class Armor(Item):
    def __init__(self, init_dict: dict) -> None:
        super().__init__(init_dict)
        self.type: ArmorSlotType = ArmorSlotType(init_dict["armor_type"])
        self.armor: int = init_dict["armor"]

    def __repr__(self) -> str:
        return f"Armor(name={self.name}, description={self.description}, weight={self.weight}, " \
               f"type={self.type}, armor={self.armor})"

