from src.items.items import Item
from src.entities.entity import Entity
from src.items.equip_slots.equip_effects import EquipEffects

from enum import Enum

import logging
logger = logging.getLogger(__name__)


class NoEquipReason(Enum):
    NONE = -1
    FULL = 0
    ITEM_TYPE = 1
    SLOT_TYPE = 2
    SPECIES = 3


class EquipSlot:
    def __init__(self) -> None:
        self._item = None

    def free(self) -> bool:
        return self._item is None

    def is_equipable(self, item: Item, equipped_by: Entity) -> bool:
        pass  # abstract

    def equip(self, item: Item) -> None:
        if self._item is not None:
            raise RuntimeError("Cannot equip another item while there is already one equipped!")
        self._item = item

    def unequip(self) -> Item:
        item = self._item
        self._item = None
        return item

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        pass  # abstract

    def info_short(self) -> str:
        if self._item is None:
            return "Item Slot (Nothing)"
        return f"Item Slot ({self._item.name})"

    def info_long(self) -> str:
        if self._item is None:
            return "Item Slot (Nothing)"
        return (f"Item Slot\n"
                f"Equipped: {self._item.info_long}")
