from src.data_providers import monster_provider as mp

from src.combat.auto_combat import AutoCombat, MonsterCombatant


def main():
	m1 = mp["dragon"]
	m2 = mp["village_guardian"]

	combat = AutoCombat(MonsterCombatant(m1), MonsterCombatant(m2))

	combat.combat()


if __name__ == '__main__':
	main()
