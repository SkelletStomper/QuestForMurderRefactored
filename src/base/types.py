from enum import Enum
from math import isclose

import logging
logger = logging.getLogger(__name__)


class Attack:
    pass


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

        weakness_strings = [f"{attackType.value}: {value}"
                            for attackType, value in self.weaknesses.items()
                            if not isclose(value, 1.0)]
        return f"WeaknessSet({', '.join(weakness_strings)})"

