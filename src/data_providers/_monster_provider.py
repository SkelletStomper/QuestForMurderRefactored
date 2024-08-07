from src.entities.monster import Monster

import logging
logger = logging.getLogger(__name__)


class MonsterProvider:
    def __init__(self, all_monster_data: dict[str, dict]):
        logger.info("Start parsing monster data")
        self.monsters = \
            {monster_name: Monster(monster_data) for monster_name, monster_data in all_monster_data.items()}
        logger.info("Finished parsing monster data")

    def __getitem__(self, value: str) -> Monster:
        return self.monsters[value]

    def __repr__(self) -> str:
        return "MonsterProvider"
