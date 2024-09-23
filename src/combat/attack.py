
from src.localization.l_string import LString
from src.base.types import AttackType

from enum import Enum

import logging
logger = logging.getLogger(__name__)


class ConditionalAttackText:
    """
    Contains different LStrings for an attack, depending on the Attack outcome.
    """
    default_wind_up = LString("{atk.name} prepares an attack on {def.name}.")
    default_on_hit = LString("{atk.name} hit{atk.s} {def.name} with the attack.")
    default_on_kill = LString("{atk.name} hit{atk.s} {def.name} with the attack, and {def.name} drops dead!")
    default_on_dodge = LString("{def.name} dodge{def.s} {atk.owns} attack!")
    default_on_armor_save = LString("{def.owns} armor fully negates the attack!")

    def __init__(self, in_dict: dict[str, str]) -> None:
        self.wind_up = LString(in_dict["wind_up"])
        if self.wind_up == "":
            self.wind_up = self.default_wind_up

        self.on_hit = LString(in_dict["on_hit"])
        if self.on_hit == "":
            self.on_hit = self.default_on_hit

        self.on_kill = LString(in_dict["on_kill"])
        if self.on_kill == "":
            if self.on_hit == self.default_on_hit:  # If custom hit message exists, use that instead of default kill
                self.on_kill = self.default_on_kill
            else:
                self.on_kill = self.on_hit

        self.on_dodge = LString(in_dict["on_dodge"])
        if self.on_dodge == "":
            self.on_dodge = self.default_on_dodge

        self.on_armor_save = LString(in_dict["on_armor_save"])
        if self.on_armor_save == "":
            self.on_armor_save = self.default_on_armor_save

        self.dict = in_dict


default_text = ConditionalAttackText({
    "wind_up": "",
    "on_hit": "",
    "on_kill": "",
    "on_dodge": "",
    "on_armor_save": ""
})

class Targeting(Enum):
    ALL = 'ALL'
    SINGLE = 'SINGLE'

    ALLY = 'ALLY'
    ENEMY = 'ENEMY'
    EVERYONE = 'EVERYONE'
    SELF = 'SELF'
    OTHER = 'OTHER'

class TargetOptions:
    def __init__(self, option_strings: list[str]) -> None:
        self.options: list[Targeting] = [Targeting(option_string) for option_string in option_strings]


    def __contains__(self, targeting: Targeting) -> bool:
        return targeting in self.options



class Attack:
    """
    An Attempted Attack. To apply effects, a target needs to call the defense-method with this as a parameter.
    """

    def __init__(self,
                 dmg: int,
                 acc: int = 0,
                 crt: float = 1.0,
                 types: list[AttackType] = None,
                 atk_str: ConditionalAttackText = default_text,
                 targets: TargetOptions = None,
                 ) -> None:

        if types is None:
            logger.debug("Default-Initializing Attack Types with [AttackType.PHYSICAL]")
            types = [AttackType.PHYSICAL]

        self.dmg = dmg
        self.crt = crt
        self.acc = acc
        self.types = types

        self.atk_str = atk_str

        self.targets = targets if targets is not None else ["ENEMY", "SINGLE"]

    def __repr__(self) -> str:
        return f"Attack(dmg={self.dmg}, acc={self.acc}, crt={self.crt}, types={self.types}, atk_str={self.atk_str})"
