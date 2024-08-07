from src.combat.attack import Attack
from src.combat.monster_combatant import MonsterCombatant
from src.combat.npc_combatant import NPCCombatant

from typing import Union

import logging
logger = logging.getLogger(__name__)

AutoCombatant = Union[MonsterCombatant, NPCCombatant]


class AutoCombat:
    def __init__(self, combatant1: AutoCombatant, combatant2: AutoCombatant) -> None:
        self.combatant1 = combatant1
        self.combatant2 = combatant2

    def combat(self) -> None:
        c1 = self.combatant1
        c2 = self.combatant2

        le1 = c1.get_le()
        le2 = c2.get_le()

        logger.info(f"Starting MonsterCombat between {le1.name} and {le2.name}")

        while c1.is_alive and c2.is_alive:
            self.calculate_attacks(c1, c2)
            print("")

            self.calculate_attacks(c2, c1)
            print("")

    def calculate_attacks(self, attacker: AutoCombatant, defender: AutoCombatant) -> None:
        lea = attacker.get_le()
        led = defender.get_le()

        logger.info(f"Starting attack sequence with {lea.name} attacking {led.name}")
        for attack in attacker.get_attacks():
            if defender.defense(attack):
                self.print_attack(attack, attacker, defender)
            if not defender.is_alive:
                continue
        defender.status_message()

    @staticmethod
    def print_attack(attack: Attack, attacker: MonsterCombatant, defender: MonsterCombatant) -> None:
        atk_str = attack.atk_str.parse(
            attacking=attacker.monster.get_le(),
            defending=defender.monster.get_le()
        )
        print(atk_str)

    def __repr__(self) -> str:
        return f"MonsterCombat(combatant1={self.combatant1}, combatant2={self.combatant2})"

