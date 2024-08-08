from src.combat.attack import Attack

import logging
logger = logging.getLogger(__name__)


def attack_dodged(accuracy: int, dodge: int) -> bool:
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

    logger.debug(f"Attack dodged: {result} (({accuracy} + {dice_accuracy} = {total_accuracy}) accuracy vs. ({dodge} + {dice_dodge} = {total_dodge}) dodge)")

    return result


class Combatant:
    def get_attacks(self) -> list[Attack]:
        # Abstract Method
        pass

    def defense(self, attack: Attack) -> None:
        # Abstract Method
        pass

    def is_alive(self) -> bool:
        # Abstract Method
        pass
