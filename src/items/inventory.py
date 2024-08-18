from src.items.items import Item
from src.items.armor import ArmorSlotType

from src.items.equip_slots import EquipSlot,slots_from_anatomy,EquipEffects, NoEquipReason

from src.entities.entity import Entity

import logging
logger = logging.getLogger(__name__)


class Inventory:
    def __init__(self, owner: Entity, slots: list[EquipSlot]|None = None):
        self.owner = owner
        if slots is None:
            self.equip_slots = slots_from_anatomy(owner.species.anatomy)
        else:
            self.slots = slots

        self.item_capacity = 20
        self.items: list[Item] = []


    def calculate_bonus(self) -> EquipEffects:
        equip_effects = EquipEffects()
        for equip_slot in self.equip_slots:
            equip_effects = equip_slot.apply_bonus(equip_effects)

        return equip_effects

    def is_equipable(self, item):
        for equip_slot in self.equip_slots:
            if equip_slot.is_equipable(item, self.owner):
                return True
        return False

    def _try_equip(self, item: Item) -> bool:
        """Try to equip the item into a fitting slot, and return success status as bool.
        Will directly try to equip an item without taking it from the inventory."""
        for equip_slot in self.equip_slots:
            no_equip_reason = equip_slot.is_equipable(item, self.owner)  # type: ignore
            if no_equip_reason == NoEquipReason.NONE:
                equip_slot.equip(item)
                return True
            elif no_equip_reason == NoEquipReason.FULL:
                self.add(equip_slot.unequip())
                equip_slot.equip(item)
                return True
        return False

    def try_equip(self, index: int) -> bool:
        item = self[index]
        success = self._try_equip(item)
        if success:
            self.remove(index)

            return True
        return False

    def add(self, item: Item) -> None | Item:
        if len(self.items) < self.item_capacity:
            self.items.append(item)
            return None
        else:
            return item

    def remove(self, index: int) -> Item:
        if not self.valid_index(index):
            raise IndexError(f"Tried to remove item from nonexistent index {index}")
        item = self[index]
        self.items.remove(item)
        return item

    def valid_index(self, index: int) -> bool:
        return 0 <= index < len(self.items)

    def item_count(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int) -> Item:
        return self.items[index]

    def __repr__(self) -> str:
        return f"Inventory(item_capacity={self.item_capacity}, equip_slots={self.equip_slots}, items={self.items})"
