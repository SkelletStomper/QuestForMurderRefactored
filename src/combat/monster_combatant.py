from src.combat.combat_basics import Combatant, attack_dodged
from src.combat.attack import Attack
from src.entities.monster import Monster, MonsterAttackStencil

import random

import logging
logger = logging.getLogger(__name__)


class MonsterCombatant(Combatant):
    def __init__(self, monster: Monster) -> None:
        self.monster = monster
        self.hp = self.monster.hp_max

    def get_attacks(self) -> list[Attack]:
        """
        Receive a list of Attacks from the Monster that can be used by a different combatant to defend against.
        Randomly picks one of the monsters "attack"-attacks, and multiplies it in case of a multi-attack.
        """
        le = self.monster.get_le()
        print(f"{le.name} attacks!".capitalize())

        attack_dict: {MonsterAttackStencil, int} = \
            {attack: attack.weight for atk_id, attack
             in self.monster.attacks.items()
             if atk_id.startswith("attack")}

        logger.debug(f"Choosing Attack for {le.name} out of the following attacks: {attack_dict}")

        attack_stencil: MonsterAttackStencil = random.choices(list(attack_dict.keys()), list(attack_dict.values()))[0]

        attacks = attack_stencil.generate_attacks()
        logger.debug(f"Chose following attacks for {le.name}: {attacks}")
        return attacks

    def defense(self, attack: Attack) -> bool:
        """Let the monster defend against the Attack, giving it chance to dodge and applying damage if it.
        Returns true if the attack does damage, false if not."""

        le = self.monster.get_le()
        accuracy = attack.acc
        dodge = self.monster.dodge

        if attack_dodged(accuracy, dodge):
            logger.debug(f"Attack was dodged by {le.name}")
            print(f"{le.name} dodged the attack!".capitalize())
            return False

        dmg_factor = self.monster.calculate_dmg_factor(attack)
        dmg = round(attack.dmg*dmg_factor)
        dmg -= self.monster.armor

        logger.debug(f"Received Damage Before Crit: round({attack.dmg}*{dmg_factor})- {self.monster.armor} = {dmg}")

        if dmg > 0:
            logger.debug(f"Crit-Adjusted damage: round({dmg}*{attack.crt}) = {dmg * attack.crt}")
            dmg = round(dmg*attack.crt)

            self.hp -= dmg
            logger.debug(f"HP of {le.name} reduced by {dmg}, from {self.hp+dmg} to {self.hp}")

            print(f"{le.name} got hit for {dmg} damage!".capitalize())
            return True
        else:
            logger.debug(f"Damage <= 0, no damage taken by {le.name}")
            print(f"The hit doesn't penetrate {le.owns} armor!")
            return False

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def status_message(self):
        le = self.monster.get_le()
        print(f"{le.name} has {self.hp} hit points left!".capitalize())

    def __repr__(self) -> str:
        return f"MonsterCombatant(hp= {self.hp}, monster: {self.monster}"
