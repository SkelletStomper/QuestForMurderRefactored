from src.data_providers import monster_provider as mp
from src.combat.auto_combat import MonsterCombatant
from src.combat.player_combat import PlayerCombatant, PlayerCombat

from src.dialogue import DialogueContext

from src.state.gamestate import global_state as gs

import logging
logging.basicConfig(level=logging.WARNING)


def main():
	gs.game_loop()


if __name__ == '__main__':
	main()
	print("Combat Finished")
