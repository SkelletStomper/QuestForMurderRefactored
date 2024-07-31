from src.combat.attack import Attack
from src.items.items import Item, Weapon, Armor

class EquipEffects:
    def __init__(self):
        self.armor = 0

        self.granted_attacks: list[Attack] = 0


class EquipSlot:
    def __init__(self) -> None:
        self._item = None

    def free(self) -> bool:
        return self._item is None

    def is_equipable(self, item: Item) -> bool:
        pass

    def equip(self, item: Item) -> None:
        if self._item is not None:
            raise RuntimeError("Cannot equip another item while there is already one equipped!")
        self._item = item

    def unequip(self) -> Item:
        item = self._item
        self._item = None
        return item

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        pass


class WeaponSlot(EquipSlot):
    def is_equipable(self, item: Item) -> bool:
        return isinstance(item, Weapon)

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        weapon: Weapon = self._item
        attack = Attack(
            dmg=weapon.damage,
            accuracy=0,
            crt=1.0,
            types=weapon.types
        )
        equip_effects.granted_attacks.append(attack)
        return equip_effects



class OffhandSlot(EquipSlot):
    pass


class ArmorSlot(EquipSlot):
    def is_equipable(self, item: Item) -> bool:
        return isinstance(item, Armor)

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        armor: Armor = self._item

        equip_effects.armor += armor.armor

        return equip_effects


class Inventory:
    def __init__(self):
        self.equip_slots = []

        self.item_capacity = 20




