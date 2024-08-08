from src.combat.combat_basics import Combatant

from src.entities.npc import NPC

from enum import Enum
from typing import Any
import logging
logger = logging.getLogger(__name__)


class PlayerCombatChoice(Enum):
    ATTACKING = "ATTACK"
    FLEEING = "FLEEING"
    INT_ACTION = "INT_ACTION"


class PlayerCombatant(Combatant):
    def __init__(self, npc: NPC):
        self.npc = npc


    def turn(self) -> tuple[PlayerCombatChoice, Any]:
        print()



