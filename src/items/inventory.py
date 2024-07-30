

class EquipEffects:
    def __init__(self):
        self.armor = 0

class EquipSlot:
    def __init__(self) -> None:
        self._item = None

    def free(self) -> bool:
        return self.item is None

    def is_equipable(self, item) -> bool:
        pass

    def equip(self, item) -> None:
        if self._item is not None:
            raise RuntimeError("Cannot equip another item while there is already one equipped!")
        self._item = item

    def unequip(self):
        item = self._item
        self._item = None
        return item

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        pass

class WeaponSlot(EquipSlot):




class Inventory:
    def __init__(self):
        self.equip_slots = []

        self.item_capacity = 20




