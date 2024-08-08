
from src.localization.l_string import LString
from src.base.types import AttackType

import logging
logger = logging.getLogger(__name__)


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
