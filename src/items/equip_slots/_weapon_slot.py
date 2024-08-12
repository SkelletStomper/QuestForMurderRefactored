from src.items.equip_slots._equip_slot import EquipSlot, EquipEffects, Entity

from src.items.weapon import Weapon

from src.data_providers import item_provider as ip

import logging
logger = logging.getLogger(__name__)


class WeaponSlot(EquipSlot):
    def __init__(self, default_weapon_id: str | None = None) -> None:
        super().__init__()
        self.default_weapon_id = default_weapon_id

    def is_equipable(self, item: Weapon, equipped_by: Entity) -> bool:
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

    def info_short(self) -> str:
        if self._item is None:
            return "Weapon Slot (Nothing)"
        return f"Weapon Slot ({self._item.name})"

    def info_long(self) -> str:
        if self._item is None:
            return "Weapon Slot (Nothing)"
        return (f"Weapon Slot\n"
                f"Equipped: {self._item.info_long()}")

    def __repr__(self) -> str:
        item_print = None
        if self._item is not None:
            item_print = self._item.id
        return f"WeaponSlot(item={item_print})"
