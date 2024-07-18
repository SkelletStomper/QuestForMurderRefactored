from enum import Enum

class AttackType(Enum):
    PHYSICAL = 'PHYSICAL'
    SLASHING = 'SLASHING'
    BASHING = 'BASHING'
    PIERCING = 'PIERCING'

    MAGICAL = 'MAGICAL'
    FIRE = 'FIRE'
    FROST = 'FROST'
    CURSE = 'CURSE'

    HOLY = 'HOLY'

    LIGHT = 'LIGHT'
    DARKNESS = 'DARKNESS'





class Attack:
    def __init__(self, dmg: int, types: list[AttackType] = None):
        if types is None:
            types = [AttackType.PHYSICAL]


        self.dmg = dmg
        self.types = types


class WeaknessSet:
    def __init__(self, str_dict: dict[str, float]):
        weaknesses = {attack_type: 1.0 for attack_type in AttackType}

        for weakness, factor in str_dict.items():
            weaknesses[AttackType(weakness)] = factor

        self.weaknesses = weaknesses

    def __getitem__(self, weakness):
        return self.weaknesses[weakness]

    def attack_factor(self, attack: Attack) -> float:
        factor = 1.0

        for attack_type in attack.types:
            factor *= self.weaknesses[attack_type]

        return factor
