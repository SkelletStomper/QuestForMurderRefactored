from src.items.items import Item
from src.base.types import WeaknessSet, AttackType

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
        self.name = in_dict["name"]
        self.description = in_dict["description"]
        self._efficiencies = WeaknessSet(in_dict["armor_efficiency"])

    def effective_factor(self, type_list: list[AttackType]):
        return self._efficiencies.attack_factor(type_list)

    def __repr__(self):
        return f"ArmorMaterial(id={self.id}, efficiency={self._efficiencies})"


class Armor(Item):
    def __init__(self, item_id, init_dict: dict) -> None:
        from src.data_providers import armat_provider as amp
        from src.data_providers import species_provider as sp

        super().__init__(item_id, init_dict)
        self.type: ArmorSlotType = ArmorSlotType(init_dict["armor_type"])
        self.made_for = sp[init_dict["made_for"]]
        armats: dict[str, int] = init_dict["armor"]
        self.armor: dict[ArmorMaterial, int] = \
            {amp[armat]: value for armat, value in armats.items()}

    def __repr__(self) -> str:
        return f"Armor(id={self.id}, name={self.name}, description={self.description}, weight={self.weight}, " \
               f"type={self.type}, made_for={self.made_for.id}, armor={self.armor})"

    def info_short(self) -> str:
        return f"{self.name} (Armor - {self.type.value.lower()})"

    def info_long(self) -> str:
        armor_strings = [f"{armat.name}: {value}" for armat, value in self.armor.items()]
        armor_string = ", ".join(armor_strings)
        return (f"{self.name}"
                f"\"{self.description}\""
                f"Provides the following armor Points:"
                f"{armor_string}")
