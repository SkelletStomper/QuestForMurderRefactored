from src.combat.combat_basics import Combatant, Attack
from src.entities.npc import NPC
from src.combat.combat_basics import attack_dodged
from src.localization.l_string import capitalize_first, LString

import random

import logging
logger = logging.getLogger(__name__)


class NPCCombatant(Combatant):
    def __init__(self, npc: NPC) -> None:
        self.npc = npc

    def get_attacks(self) -> list[Attack]:
        equip_effects = self.npc.inventory.calculate_bonus()
        attack_stencils = equip_effects.granted_attacks

        executed_attack = random.choice(attack_stencils)

        return [executed_attack.generate_attack()]

    def defense(self, attack: Attack) -> LString:
        """Let the NPC defend against the Attack, giving it chance to dodge and applying damage if it.
        Returns true if the attack does damage, false if not."""

        le = self.npc.get_le()
        accuracy = attack.acc
        dodge = self.npc.dodge

        equip_effects = self.npc.inventory.calculate_bonus()

        if attack_dodged(accuracy, dodge):
            logger.debug(f"Attack was dodged by {le.name}")
            return attack.atk_str.on_dodge

        armor = self.npc.armor + equip_effects.armor

        dmg_factor = self.npc.calculate_dmg_factor(attack)
        dmg = round(attack.dmg*dmg_factor)
        dmg -= armor

        logger.debug(f"Received Damage Before Crit: round({attack.dmg}*{dmg_factor})- {armor} = {dmg}")

        if dmg > 0:
            logger.debug(f"Crit-Adjusted damage: round({dmg}*{attack.crt}) = {dmg * attack.crt}")
            dmg = round(dmg*attack.crt)

            self.npc.hp -= dmg
            logger.debug(f"HP of {le.name} reduced by {dmg}, from {self.npc.hp+dmg} to {self.npc.hp}")

            print(capitalize_first(f"{le.name} got hit for {dmg} damage!"))
            if self.npc.hp > 0:
                return attack.atk_str.on_hit
            else:
                return attack.atk_str.on_kill
        else:
            logger.debug(f"Damage <= 0, no damage taken by {le.name}")
            return attack.atk_str.on_armor_save

    def get_le(self):
        return self.npc.get_le()

    @property
    def is_alive(self) -> bool:
        return self.npc.hp > 0

    def status_message(self):
        le = self.npc.get_le()
        print(capitalize_first(f"{le.name} has {self.npc.hp} hit points left!"))

    def __repr__(self) -> str:
        return f"NPCCombatant(npc={self.npc}"

