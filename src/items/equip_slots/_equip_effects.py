from src.items.armor import ArmorMaterial
from src.items.weapon import WeaponAttackStencil


class EquipEffects:
    def __init__(self):
        self.armor: dict[ArmorMaterial, int] = {}
        self.granted_attacks: list[WeaponAttackStencil] = []

    def __repr__(self) -> str:
        return f"EquipEffects(armor={self.armor}, granted_attacks={self.granted_attacks})"
