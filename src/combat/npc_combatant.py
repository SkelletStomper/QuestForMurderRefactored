from src.combat.combat_basics import Combatant, Attack
from src.entities.npc import NPC

import logging
logger = logging.getLogger(__name__)


class NPCCombatant(Combatant):
    def __init__(self, npc: NPC) -> None:
        self.npc = npc


    def get_attacks(self) -> list[Attack]:

        le = self.npc.get_le()


