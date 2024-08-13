from src.combat.combat_basics import attack_dodged
from src.combat.auto_combat import AutoCombat, AutoCombatant
from src.combat.player_combatant import PlayerCombatant, PlayerCombatChoice
from src.entities.npc import Entity

import logging
logger = logging.getLogger(__name__)


class PlayerCombat(AutoCombat):
    def __init__(self, player: PlayerCombatant, opponent: AutoCombatant) -> None:
        self.player = player
        self.opponent = opponent

    def combat(self) -> Entity:
        pl = self.player
        op = self.opponent

        le_pl = pl.get_le()
        le_op = op.get_le()

        logger.info(f"Starting PlayerCombat between {le_pl.name} and {le_op.name}")

        while True:
            do, extra = pl.turn()

            if do == PlayerCombatChoice.INT_ACTION:
                logger.info("Turn was spent without attacking")
            elif do == PlayerCombatChoice.ATTACKING:
                for attack in extra:
                    self.print_attack(attack.atk_str.wind_up, pl, op)
                    message = op.defense(attack)
                    self.print_attack(message, pl, op)
                    if not op.is_alive:
                        continue
                op.status_message()

            elif do == PlayerCombatChoice.FLEEING:
                return op.get_pilot()

            if not op.is_alive:
                break
            print("")

            self.calculate_attacks(op, pl)
            if not pl.is_alive:
                break
            print("")

        if pl.is_alive:
            return pl.get_pilot()
        if op.is_alive:
            return op.get_pilot()

# TODO
