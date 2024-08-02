from src.combat.attack import Attack
from src.items.items import Item

from src.items.armor import Armor, ArmorSlotType
from src.items.weapon import Weapon


class EquipEffects:
    def __init__(self):
        self.armor = 0
        self.granted_attacks: list[Attack] = []


class EquipSlot:
    def __init__(self) -> None:
        self._item = None

    def free(self) -> bool:
        return self._item is None

    def is_equipable(self, item: Item) -> bool:
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


class WeaponSlot(EquipSlot):
    def is_equipable(self, item: Item) -> bool:
        if self._item is not None:
            return False
        return isinstance(item, Weapon)

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        if self._item is None:
            return equip_effects

        weapon: Weapon = self._item
        attacks = [
            weapon.attacks["attack1"].generate_attack(),
            weapon.attacks["attack2"].generate_attack()
        ]

        equip_effects.granted_attacks += attacks
        return equip_effects


class OffhandSlot(EquipSlot):
    pass


class ArmorSlot(EquipSlot):
    def __init__(self, armor_type: ArmorSlotType):
        super().__init__()
        self.type = armor_type

    def is_equipable(self, item: Item) -> bool:
        if self._item is not None:
            return False
        return isinstance(item, Armor) and item.type == self.type

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        if self._item is None:
            return equip_effects

        armor: Armor = self._item

        equip_effects.armor += armor.armor

        return equip_effects


class Inventory:
    def __init__(self):
        self.equip_slots = [
            WeaponSlot(),
            ArmorSlot(ArmorSlotType.HEAD),
            ArmorSlot(ArmorSlotType.CHEST),
            ArmorSlot(ArmorSlotType.LEGS),
            ArmorSlot(ArmorSlotType.HANDS),
            ArmorSlot(ArmorSlotType.FEET),
        ]

        self.item_capacity = 20

    def calculate_bonus(self) -> EquipEffects:
        equip_effects = EquipEffects()
        for equip_slot in self.equip_slots:
            equip_effects = equip_slot.apply_bonus(equip_effects)

        return equip_effects

    def try_equip(self, item: Item) -> bool:
        """Try to equip the item into a fitting slot, and return success status as bool."""
        for equip_slot in self.equip_slots:
            if equip_slot.is_equipable(item):
                equip_slot.equip(item)
                return True
        return False
