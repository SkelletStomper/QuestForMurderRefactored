from src.combat.combat_basics import Combatant
from src.combat.attack import Attack
from src.entities.monster import Monster, MonsterAttackStencil
from src.localization.l_string import LString
import random

import logging
logger = logging.getLogger(__name__)


class MonsterCombatant(Combatant):
    def __init__(self, monster: Monster) -> None:
        self.monster = monster
        self._hp = self.monster.hp_max

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value: int):
        self._hp = value

    def get_attacks(self) -> list[tuple[Attack, int]]:
        """
        Receive a list of Attacks from the Monster that can be used by a different combatant to defend against.
        Randomly picks one of the monsters "attack"-attacks, and multiplies it in case of a multi-attack.
        """
        le = self.monster.get_le()

        attack_dict: {MonsterAttackStencil, int} = \
            {attack: attack.weight for atk_id, attack
             in self.monster.attacks.items()
             if atk_id.startswith("attack")}

        logger.debug(f"Choosing Attack for {le.name} out of the following attacks: {attack_dict}")

        attack_stencil: MonsterAttackStencil = random.choices(list(attack_dict.keys()), list(attack_dict.values()))[0]

        attacks = attack_stencil.generate_attacks()
        logger.debug(f"Chose following attacks for {le.name}: {attacks}")
        return attacks

    def get_le(self):
        return self.monster.get_le()

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def status_message(self) -> None:
        le = self.get_le()
        print(f"{le.name} has {self.hp} hit points left!".capitalize())

    def get_pilot(self) -> Monster:
        return self.monster

    def __repr__(self) -> str:
        return f"MonsterCombatant(hp={self.hp}, monster={self.monster.name})"
