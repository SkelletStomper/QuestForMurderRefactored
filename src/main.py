from src.data_providers import monster_provider as mp
from src.data_providers import item_provider as ip
from src.entities.npc import NPC
from src.combat.auto_combat import MonsterCombatant
from src.combat.player_combat import PlayerCombatant, PlayerCombat


def main():

	m1 = mp["snake1"]

	jane = NPC(name="Mary Sue", pronouns="3rd_she", hp_max=30)

	inv = jane.inventory

	dagger = ip["default_dagger"]
	tome = ip["default_pyro_tome"]
	mace = ip["default_mace"]
	chest = ip["leather_chest"]
	head = ip["leather_cap"]
	legs = ip["leather_pants"]

	inv.add(dagger)
	inv.add(tome)
	inv.add(mace)
	inv.add(chest)
	inv.add(head)
	inv.add(legs)

	# InventoryDialogue(inv).dialogue()

	combat = PlayerCombat(PlayerCombatant(jane), MonsterCombatant(m1))
	combat.combat()


if __name__ == '__main__':
	main()
	print("Combat Finished")
