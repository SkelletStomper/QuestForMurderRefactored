from random import sample

from data_providers import monster_provider as mp
from src.entities.monster import Monster
from src.combat.auto_combat import AutoCombat
from src.combat.monster_combatant import MonsterCombatant


class MonsterTournament:
    class Bracket:
        def __init__(self, c1, c2):
            self.c1 = c1
            self.c2 = c2

        def resolve(self) -> Monster:
            if isinstance(self.c1, MonsterTournament.Bracket):
                self.c1 = self.c1.resolve()

            if isinstance(self.c2, MonsterTournament.Bracket):
                self.c2 = self.c2.resolve()

            m1 = MonsterCombatant(self.c1)
            m2 = MonsterCombatant(self.c2)

            winner = AutoCombat(m1, m2)
            return winner






    def __init__(self, rounds=3):

        monster_count = 2**rounds
        all_monsters = mp.all_ids()

        fighting_monsters = sample(all_monsters, monster_count)





