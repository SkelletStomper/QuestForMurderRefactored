from src.combat.attack import Attack
from src.items.items import Item

from src.items.armor import Armor, ArmorSlotType
from src.items.weapon import Weapon, WeaponAttackStencil
from src.data_providers import item_provider as ip

class EquipEffects:
    def __init__(self):
        self.armor = 0
        self.granted_attacks: list[WeaponAttackStencil] = []

    def __repr__(self) -> str:
        return f"EquipEffects(armor={self.armor}, granted_attacks={self.granted_attacks})"


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
    def __init__(self, default_weapon_id: str | None = None) -> None:
        super().__init__()
        self.default_weapon_id = default_weapon_id

    def is_equipable(self, item: Item) -> bool:
        if self._item is not None:
            return False
        return isinstance(item, Weapon)

    def apply_bonus(self, equip_effects: EquipEffects) -> EquipEffects:
        weapon: Weapon = self._item
        if weapon is None:
            if self.default_weapon_id is None:
                return equip_effects
            weapon = ip[self.default_weapon_id]

        attacks = [
            weapon.attacks["attack1"],
            weapon.attacks["attack2"]
        ]

        equip_effects.granted_attacks += attacks
        return equip_effects

    def __repr__(self) -> str:
        return f"WeaponSlot(item={self._item}, default_weapon_id={self.default_weapon_id})"


class OffhandSlot(EquipSlot):

    def __repr__(self) -> str:
        return f"OffhandSlot(item={self._item})"


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

    def __repr__(self) -> str:
        return f"ArmorSlot(type={self.type}, item={self._item})"


class Inventory:
    def __init__(self):
        self.equip_slots = [
            WeaponSlot(default_weapon_id="fists"),
            ArmorSlot(ArmorSlotType.HEAD),
            ArmorSlot(ArmorSlotType.CHEST),
            ArmorSlot(ArmorSlotType.LEGS),
            ArmorSlot(ArmorSlotType.HANDS),
            ArmorSlot(ArmorSlotType.FEET),
        ]

        self.item_capacity = 20
        self.items: list[Item] = []

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

    def __repr__(self) -> str:
        return f"Inventory(item_capacity={self.item_capacity}, equip_slots={self.equip_slots}, items={self.items})"
