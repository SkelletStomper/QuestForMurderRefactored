from src.entities.monster_pool import MonsterPool

import logging
logger = logging.getLogger(__name__)


class MonsterPoolProvider:
    def __init__(self, all_pronoun_data: dict[str, dict]):
        logger.info("Start parsing MonsterPool data")
        self.monster_pools: dict[str, MonsterPool] = \
            {monster_pool_id: MonsterPool(monster_pool_id, monster_pool_data)
             for monster_pool_id, monster_pool_data in all_pronoun_data.items()}
        logger.info("Finished parsing MonsterPool data")

    def __getitem__(self, item: str) -> MonsterPool:
        return self.monster_pools[item]

    def all_ids(self) -> list[str]:
        return list(self.monster_pools.keys())

    def __repr__(self) -> str:
        return f"MonsterPoolProvider({self.monster_pools}) MonsterPools )"
