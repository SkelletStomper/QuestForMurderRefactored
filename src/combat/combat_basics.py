from src.combat.attack import Attack, AttackType
from src.localization.localized_entity import LocalizedEntity
from src.localization.l_string import LString, capitalize_first
from src.entities.entity import Entity

import logging
logger = logging.getLogger(__name__)


def dodge_dice_roll(accuracy: int, dodge: int) -> bool:
    from src.util.dice import d
    dice_dodge = d(8)
    if dice_dodge == 1:
        logger.debug("Attack hit on critical dodge blunder")
        return False
    if dice_dodge == 8:
        logger.debug("Attack missed on critical dodge success")
        return True

    dice_accuracy = d(6)

    total_accuracy = accuracy + dice_accuracy
    total_dodge = dodge + dice_dodge - 1
    result = total_accuracy < total_dodge

    logger.debug(f"Attack dodged: {result} (({accuracy} + {dice_accuracy} = {total_accuracy}) accuracy "
                 f"vs. ({dodge} + {dice_dodge} = {total_dodge}) dodge)")

    return result


class Combatant:
    def get_attacks(self) -> list[Attack]:
        # Abstract Method
        pass

    def defense(self, attack: Attack, attempt_dodge: bool = True) -> LString | None:
        """Let the combatant defend against the Attack, giving it chance to dodge and applying damage if it.
        Returns an LString signifying the result of the attack."""

        entity = self.get_pilot()
        le = self.get_le()
        if attempt_dodge and self.attack_dodged(attack):
            return attack.atk_str.on_dodge

        dmg_factor = entity.calculate_dmg_factor(attack)
        dmg = round(attack.dmg * dmg_factor)
        effective_armor = entity.calculate_effective_armor(attack)
        dmg -= effective_armor

        logger.debug(f"Received Damage Before Crit: round({attack.dmg}*{dmg_factor})- {effective_armor} = {dmg}")

        if dmg > 0:
            logger.debug(f"Crit-Adjusted damage: round({dmg}*{attack.crt}) = {dmg * attack.crt}")
            dmg = round(dmg*attack.crt)

            if AttackType.HEALING not in attack.types:
                self.damage(dmg)
                logger.debug(f"HP of {le.name} reduced by {dmg}, from {self.hp+dmg} to {self.hp}")
            else:
                self.heal(dmg)
                logger.debug(f"HP of {le.name} increased by {dmg}, from {self.hp+dmg} to {self.hp}")

            print(capitalize_first("{le.name} got hit for {dmg} damage!"))
            if self.hp > 0:
                return attack.atk_str.on_hit
            else:
                return attack.atk_str.on_kill
        else:
            logger.debug(f"Damage <= 0, no damage taken by {le.name}")
            return attack.atk_str.on_armor_save

    def attack_dodged(self, attack: Attack) -> bool:
        le = self.get_le()
        accuracy = attack.acc
        dodge = self.get_pilot().dodge

        if dodge_dice_roll(accuracy, dodge):
            logger.debug(f"Attack was dodged by {le.name}")
            return True
        return False

    def heal(self, amount: int):
        self.hp = min(self.hp + amount, self.get_pilot().hp_max)

    def damage(self, amount: int):

        self.hp -= amount

    def is_alive(self) -> bool:
        # Abstract Method
        pass

    def get_le(self) -> LocalizedEntity:
        pass  # abstract

    def get_pilot(self) -> Entity:
        pass  # abstract

    @property
    def hp(self):
        pass  # abstract

    @hp.setter
    def hp(self, value):
        pass  # abstract
