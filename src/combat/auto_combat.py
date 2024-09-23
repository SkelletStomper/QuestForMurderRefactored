
from src.combat.attack import Attack
from src.localization.l_string import LString

from src.combat.attack import TargetOptions, Targeting
from src.combat.combat_basics import Combatant
from src.combat.monster_combatant import MonsterCombatant
from src.combat.npc_combatant import NPCCombatant

from typing import Union
import random

import logging
logger = logging.getLogger(__name__)

AutoCombatant = Union[MonsterCombatant, NPCCombatant]


class AutoCombat:
    def __init__(self, combatants: list[AutoCombatant]) -> None:
        self.combatants = combatants

    def combat(self) -> str:


        while True:
            self.sort_after_combat_speed()

            for combatant in self.combatants:
                attacker = combatant
                for attack, amount in combatant.get_attacks():
                    possible_targets = self.get_available_targets(attacker, attack)
                    target_options: TargetOptions = attack.targets

                    if Targeting.ALL in target_options:

                        for _ in range(amount):


                    elif Targeting.RANDOM in target_options:
                        for _ in range(amount):
                            target = self.random_alive_target(possible_targets)
                            self.print_attack(attack.atk_str.wind_up, attacker, target)
                            message = target.defense(attack)
                            self.print_attack(message, attacker, target)
                            target.status_message()

                    else:  # Targeting.SINGLE assumed
                        target = self.random_alive_target(possible_targets)
                        self.print_attack(attack.atk_str.wind_up, attacker, target)
                        for _ in range(amount):
                            message = target.defense(attack)
                            self.print_attack(message, attacker, target)
                            if not target.is_alive:
                                continue
                        target.status_message()




        return "player"

    def sort_after_combat_speed(self):
        self.combatants = sorted(self.combatants, key=lambda combatant: combatant.speed)

    @staticmethod
    def random_alive_target(available_targets: list[AutoCombatant]) -> AutoCombatant:
        available_targets = [target for target in available_targets if target.is_alive]
        return random.choice(available_targets)

    def get_available_targets(self, attacker: AutoCombatant, attack: Attack) -> list[AutoCombatant]:
        target_options: TargetOptions = attack.targets
        if Targeting.SELF in target_options:
            return [attacker]

        available_targets: list[AutoCombatant] = []

        for combatant in self.combatants:
            if Targeting.EVERYONE in target_options:
                available_targets.append(combatant)
            elif Targeting.ENEMY in target_options and combatant.faction != attacker.faction:
                available_targets.append(combatant)
            elif Targeting.ALLY in target_options and combatant.faction == attacker.faction:
                available_targets.append(combatant)

        if Targeting.OTHER in target_options and attacker in available_targets:
            available_targets.remove(attacker)

        return available_targets




    def calculate_attacks(self, attacker: AutoCombatant, defender: AutoCombatant, attack: Attack, attack_count: int) -> None:
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
