from src.data_providers import monster_provider as mp

from src.combat.combat import MonsterCombat, MonsterCombatant


m1 = mp["dragon"]
m2 = mp["village_guardian"]

combat = MonsterCombat(MonsterCombatant(m1), MonsterCombatant(m2))

combat.combat()




