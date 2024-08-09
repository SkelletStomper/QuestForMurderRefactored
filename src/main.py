from src.data_providers import monster_provider as mp, species_provider as sp

from src.entities.npc import NPC
from src.combat.auto_combat import AutoCombat, MonsterCombatant, NPCCombatant

def main():
	m1 = mp["goblin1"]

	jane = NPC(name="Mary Jane", pronouns="3rd_she")

	combat = AutoCombat(MonsterCombatant(m1), NPCCombatant(jane))
	combat.combat()


if __name__ == '__main__':
	main()

	input()
