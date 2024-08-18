from src.items.equip_slots import EquipSlot, ArmorSlot, WeaponSlot
from src.items.armor import ArmorSlotType

from src.entities.species import Anatomy, BodyPart


def slots_from_anatomy(anatomy: Anatomy) -> list[EquipSlot]:
    slot_list = []
    slot_list += [WeaponSlot(default_weapon_id="fists") for _ in range(anatomy[BodyPart.HAND])]
    slot_list += [ArmorSlot(ArmorSlotType.HEAD) for _ in range(anatomy[BodyPart.HEAD])]
    slot_list += [ArmorSlot(ArmorSlotType.CHEST) for _ in range(anatomy[BodyPart.CHEST])]
    slot_list += [ArmorSlot(ArmorSlotType.LEGS) for _ in range(anatomy[BodyPart.LEG] // 2)]
    slot_list += [ArmorSlot(ArmorSlotType.FEET) for _ in range(anatomy[BodyPart.FOOT] // 2)]
    slot_list += [ArmorSlot(ArmorSlotType.HANDS) for _ in range(anatomy[BodyPart.HAND] // 2)]

    return slot_list




