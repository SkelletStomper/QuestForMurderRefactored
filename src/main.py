from src.data_providers import monster_provider as mp
from src.data_providers import item_provider as ip
from src.entities.npc import NPC
from src.combat.auto_combat import AutoCombat, MonsterCombatant, NPCCombatant

def main():
	m1 = mp["goblin1"]

	jane = NPC(name="Mary Jane", pronouns="3rd_she")

	inv = jane.inventory

	dagger = ip["default_dagger"]
	chest = ip["leather_chest"]
	head = ip["leather_cap"]
	legs = ip["leather_pants"]

	inv.try_equip(dagger)
	inv.try_equip(chest)
	inv.try_equip(head)
	inv.try_equip(legs)

	combat = AutoCombat(MonsterCombatant(m1), NPCCombatant(jane))
	combat.combat()


if __name__ == '__main__':
	main()

	input()
