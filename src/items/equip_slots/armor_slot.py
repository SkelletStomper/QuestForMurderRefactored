from src.items.equip_slots.equip_slot import EquipSlot, EquipEffects, Entity
from src.items.armor import Armor, ArmorSlotType

import logging
logger = logging.getLogger(__name__)


class ArmorSlot(EquipSlot):
    def __init__(self, armor_type: ArmorSlotType):
        super().__init__()
        self.type = armor_type

    def is_equipable(self, item: Armor, equipped_by: Entity) -> bool:
        if self._item is not None:
            logger.info(f"Item {item.id} is not equipable because Item {self._item.id} is already equipped")
            return False

        if not isinstance(item, Armor):
            logger.debug(f"Item {item.id} is not equipable because it is {type(item)}, not an Armor")
            return False

        if item.type != self.type:
            logger.debug(f"Armor {item.id} is not equipable because of it's type {item.type}, "
                         f"which is not {self.type}")
            return False

        equipper_species = equipped_by.species
        must_be_species = item.made_for
        if not equipper_species.is_subspecies(must_be_species.id):
            logger.debug(f"Armor {item.id} is not equipable because it is made for {must_be_species.id}, which  "
                         f"the equipper {equipped_by.name} with species {equipper_species.id} is not a subspecies of.")
            return False
        logger.debug(f"Armor {item.id} is equipable into the ArmorSlot")
        return True

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        if self._item is None:
            return equip_effects

        armor: Armor = self._item
        for armat, value in armor.armor.items():
            if armat not in equip_effects.armor:
                equip_effects.armor[armat] = 0
            equip_effects.armor[armat] += value

        return equip_effects

    def info_short(self) -> str:
        if self._item is None:
            return f"Armor Slot-({self.type.value.lower()}) (Nothing)"
        return f"Armor Slot({self.type.value.lower()}) ({self._item.name})"

    def info_long(self) -> str:
        if self._item is None:
            return f"Armor Slot({self.type.value.lower()}) (Nothing)"
        return (f"Armor Slot({self.type.value.lower()})\n"
                f"Equipped: {self._item.info_long()}")

    def __repr__(self) -> str:
        item_print = None
        if self._item is not None:
            item_print = self._item.id
        return f"ArmorSlot(type={self.type}, item={item_print})"
