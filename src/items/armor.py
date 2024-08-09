from src.items.items import Item
from src.base.types import WeaknessSet

from enum import Enum


class ArmorSlotType(Enum):
    ANY = "ANY"
    CHEST = "CHEST"
    HEAD = "HEAD"
    HANDS = "HANDS"
    LEGS = "LEGS"
    FEET = "FEET"


class ArmorMaterial:
    def __init__(self, armat_id, in_dict: dict) -> None:
        self.id = armat_id
        self.efficiency = WeaknessSet(in_dict["armor_efficiency"])

    def __repr__(self):
        return f"ArmorMaterial(id={self.id}, efficiency={self.efficiency})"


class Armor(Item):
    def __init__(self, item_id, init_dict: dict) -> None:
        super().__init__(item_id, init_dict)
        self.type: ArmorSlotType = ArmorSlotType(init_dict["armor_type"])
        self.armor: int = init_dict["armor"]

    def __repr__(self) -> str:
        return f"Armor(id={self.id}, name={self.name}, description={self.description}, weight={self.weight}, " \
               f"type={self.type}, armor={self.armor})"

