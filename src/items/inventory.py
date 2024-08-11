from src.items.items import Item

from src.items.armor import Armor, ArmorSlotType
from src.items.weapon import Weapon, WeaponAttackStencil
from src.items.armor import ArmorMaterial
from src.entities.entity import Entity

from src.data_providers import item_provider as ip

import logging
logger = logging.getLogger(__name__)


class EquipEffects:
    def __init__(self):
        self.armor: dict[ArmorMaterial, int] = {}
        self.granted_attacks: list[WeaponAttackStencil] = []

    def __repr__(self) -> str:
        return f"EquipEffects(armor={self.armor}, granted_attacks={self.granted_attacks})"


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


class WeaponSlot(EquipSlot):
    def __init__(self, default_weapon_id: str | None = None) -> None:
        super().__init__()
        self.default_weapon_id = default_weapon_id

    def is_equipable(self, item: Item, equipped_by: Entity) -> bool:
        if self._item is not None:
            logger.debug(f"Item {item.id} is not equipable because Item {self._item.id} is already equipped")
            return False
        if not isinstance(item, Weapon):
            logger.debug(f"Item {item.id} is not equipable because Item it is {type(item)}, not a Weapon")
            return False

        logger.debug(f"Item {item.id} is equipable into the WeaponSlot")
        return True

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
        item_print = None
        if self._item is not None:
            item_print = self._item.id
        return f"WeaponSlot(item={item_print})"


class OffhandSlot(EquipSlot):

    def __repr__(self) -> str:
        item_print = None
        if self._item is not None:
            item_print = self._item.id
        return f"OffhandSlot(item={item_print})"


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

    def __repr__(self) -> str:
        item_print = None
        if self._item is not None:
            item_print = self._item.id
        return f"ArmorSlot(type={self.type}, item={item_print})"


class Inventory:
    def __init__(self, owner: Entity):
        self.owner = owner
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

    def _try_equip(self, item: Item) -> bool:
        """Try to equip the item into a fitting slot, and return success status as bool."""
        for equip_slot in self.equip_slots:
            if equip_slot.is_equipable(item, self.owner):
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
        return index < len(self.items)

    def __getitem__(self, index: int) -> Item:
        return self.items[index]

    def __repr__(self) -> str:
        return f"Inventory(item_capacity={self.item_capacity}, equip_slots={self.equip_slots}, items={self.items})"
