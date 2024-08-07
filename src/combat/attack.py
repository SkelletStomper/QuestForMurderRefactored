from enum import Enum

from src.localization.l_string import LString

import logging
logger = logging.getLogger(__name__)


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


class WeaknessSet:
    """
    Describes Weaknesses to or Strength against any of the Attack Types.
    For each Attack type, a float factor is defined with a default of 1.0.
    """

    def __init__(self, str_dict: dict[str, float]) -> None:
        weaknesses = {attack_type: 1.0 for attack_type in AttackType}

        for weakness, factor in str_dict.items():
            if isinstance(factor, int):
                factor = float(factor)
            if not isinstance(factor, float):
                logger.error(f"Tried to initialize weakness {weakness} with factor {factor} of type {type(factor)}")
                raise TypeError("Weakness factor must be float or int")

            weaknesses[AttackType(weakness)] = factor

        logger.debug(f"Initialized WeaknessSet from {str_dict} to {weaknesses}")

        self.weaknesses = weaknesses

    def __getitem__(self, weakness: AttackType | str) -> float:
        if isinstance(weakness, str):
            weakness = AttackType(weakness)
        return self.weaknesses[weakness]

    def attack_factor(self, attack: "Attack") -> float:
        """Calculates the damage factor of an Attack for this WeaknessSet.
        Iterates through all types of the attack and multiplies all weakness factors with themselves, returning the final weakness factor."""
        factor = 1.0

        for attack_type in attack.types:
            factor *= self.weaknesses[attack_type]

        logging.debug(f"Calculated factor {factor} for attack with types {attack.types} with WeaknessSet {self.weaknesses}")
        return factor

    def __repr__(self) -> str:
        return f"WeaknessSet({self.weaknesses})"


class Attack:
    """
    An Attempted Attack. To apply effects, a target needs to call the defense-method with this as a parameter.
    """

    def __init__(self,
                 dmg: int,
                 acc: int = 0,
                 crt: float = 1.0,
                 types: list[AttackType] = None,
                 atk_str: LString | None = None
                 ) -> None:

        if types is None:
            logger.debug("Default-Initializing Attack Types with [AttackType.PHYSICAL]")
            types = [AttackType.PHYSICAL]

        self.dmg = dmg
        self.crt = crt
        self.acc = acc
        self.types = types

        if atk_str is None:
            atk_str = LString("Unspecified attack landed.")
            logger.debug(f"Default-Initializing Attack LString as '{atk_str}'")
        self.atk_str = atk_str

    def __repr__(self) -> str:
        return f"Attack(dmg={self.dmg}, acc={self.acc}, crt={self.crt}, types={self.types}, atk_str={self.atk_str})"
