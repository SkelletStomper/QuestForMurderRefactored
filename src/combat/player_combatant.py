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


        print("What do you want to do?")
        print("(1): Attack")
        print("(2): Inventory")
        print("(3): Flee")
        choice: str = input(">: ").to_lower()

        if choice in ["1", "(1)", "atk", "attack"]:
            pass
        elif choice in ["2", "(2)", "inv", "inventory"]:
            pass
        elif choice in ["3", "{3}", "flee", "run"]:
            return PlayerCombatChoice.FLEEING, None


# TODO
