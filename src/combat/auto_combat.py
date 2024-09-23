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
    def __init__(self, combatants: list[AutoCombatant]) -> None:
        self.combatants = combatants

    def combat(self) -> Entity:



        while True:
            for combatant in self.combatants:
                combatant.get_attacks()

    def sort_after_combat_speed(self):
        self.combatants = sorted(self.combatants, key=lambda combatant: combatant.speed)

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
        return f"AutoCombat(combatants: {", ".join([combatant.__repr__() for combatant in self.combatants])})"
