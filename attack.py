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
