from src.data_providers import monster_provider as mp

from src.entities.npc import NPC
from src.combat.auto_combat import AutoCombat, MonsterCombatant, NPCCombatant


def main():
	m1 = mp["goblin1"]
	m2 = mp["village_guardian"]

	jane = NPC()


	combat = AutoCombat(MonsterCombatant(m1), NPCCombatant(jane))

	combat.combat()


if __name__ == '__main__':
	main()
