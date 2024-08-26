from src.combat.combat_basics import Combatant, Attack
from src.entities.npc import NPC
from src.localization.l_string import capitalize_first

import random

import logging
logger = logging.getLogger(__name__)


class NPCCombatant(Combatant):
    def __init__(self, npc: NPC) -> None:
        self.npc = npc

    @property
    def hp(self):
        return self.npc.hp

    @hp.setter
    def hp(self, value: int):
        self.npc.hp = value

    def get_attacks(self) -> list[tuple[Attack, int]]:
        equip_effects = self.npc.inventory.calculate_bonus()
        attack_stencils = equip_effects.granted_attacks

        executed_attack = random.choice(attack_stencils)

        return [executed_attack.generate_attack()]

    def get_le(self):
        return self.npc.get_le()

    @property
    def is_alive(self) -> bool:
        return self.npc.hp > 0

    def status_message(self):
        le = self.get_le()
        print(capitalize_first(f"{le.name} has {self.npc.hp} hit points left!"))

    def get_pilot(self):
        return self.npc

    def __repr__(self) -> str:
        return f"NPCCombatant(npc={self.npc}"
