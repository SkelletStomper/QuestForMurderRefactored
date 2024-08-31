from src.entities.monster import Monster

import random

class MonsterPool:
    def __init__(self, monster_pool_id: str, init_dict: dict):
        self.monster_pool_id: str = monster_pool_id
        self.monsters: list[str] = init_dict["monsters"]


    def random_monster(self) -> Monster:
        from src.data_providers import monster_provider as mp
        monster_id = random.choice(self.monsters)

        return mp[monster_id]


