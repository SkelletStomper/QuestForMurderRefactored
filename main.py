from monster import monsterProvider

from combat import MonsterCombat, MonsterCombatant

m1 = monsterProvider["goblin1"]
m2 = monsterProvider["fat_cat"]

combat = MonsterCombat(MonsterCombatant(m1), MonsterCombatant(m2))

combat.combat()




