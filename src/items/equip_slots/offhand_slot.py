from src.items.equip_slots.equip_slot import EquipSlot


class OffhandSlot(EquipSlot):

    def __repr__(self) -> str:
        item_print = None
        if self._item is not None:
            item_print = self._item.id
        return f"OffhandSlot(item={item_print})"
