from src.data_providers import monster_provider as mp

from src.combat.monster_combat import MonsterCombat, MonsterCombatant


def main():
	m1 = mp["dragon"]
	m2 = mp["village_guardian"]

	combat = MonsterCombat(MonsterCombatant(m1), MonsterCombatant(m2))

	combat.combat()

if __name__ == '__main__':
	main()