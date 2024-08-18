from src.localization.l_string import LString
from src.combat.combat_basics import Combatant
from src.combat.monster_combatant import MonsterCombatant
from src.combat.npc_combatant import NPCCombatant
from src.entities.entity import Entity

from typing import Union

import logging
logger = logging.getLogger(__name__)

AutoCombatant = Union[MonsterCombatant, NPCCombatant]


class AutoCombat:
    def __init__(self, combatant1: AutoCombatant, combatant2: AutoCombatant) -> None:
        self.combatant1 = combatant1
        self.combatant2 = combatant2

    def combat(self) -> Entity:
        c1 = self.combatant1
        c2 = self.combatant2

        le1 = c1.get_le()
        le2 = c2.get_le()

        logger.info(f"Starting AutoCombat between {le1.name} and {le2.name}")

        while True:
            self.calculate_attacks(c1, c2)
            if not c2.is_alive:
                break
            print("")

            self.calculate_attacks(c2, c1)
            if not c1.is_alive:
                break
            print("")

        if c1.is_alive:
            return c1.get_pilot()
        if c2.is_alive:
            return c2.get_pilot()

    def calculate_attacks(self, attacker: AutoCombatant, defender: AutoCombatant) -> None:
        lea = attacker.get_le()
        led = defender.get_le()

        logger.info(f"Starting attack sequence with {lea.name} attacking {led.name}")
        for attack, attack_count in attacker.get_attacks():
            self.print_attack(attack.atk_str.wind_up, attacker, defender)
            for _ in range(attack_count):
                message = defender.defense(attack)
                self.print_attack(message, attacker, defender)
                if not defender.is_alive:
                    continue
        defender.status_message()

    @staticmethod
    def print_attack(message: LString, attacker: Combatant, defender: Combatant) -> None:
        atk_str = message.parse(
            attacking=attacker.get_le(),
            defending=defender.get_le()
        )
        print(atk_str)

    def __repr__(self) -> str:
        return f"AutoCombat(combatant1={self.combatant1}, combatant2={self.combatant2})"
