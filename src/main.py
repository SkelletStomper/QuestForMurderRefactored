from src.data_providers import monster_provider as mp

from src.combat.combat import MonsterCombat, MonsterCombatant

m1 = mp["goblin1"]
m2 = mp["fat_cat"]

combat = MonsterCombat(MonsterCombatant(m1), MonsterCombatant(m2))

combat.combat()




