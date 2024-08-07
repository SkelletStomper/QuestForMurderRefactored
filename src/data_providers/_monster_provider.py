from src.entities.monster import Monster


class MonsterProvider:
    def __init__(self, all_monster_data: dict[str, dict]):
        self.monsters = \
            {monster_name: Monster(monster_data) for monster_name, monster_data in all_monster_data.items()}

    def __getitem__(self, value: str) -> Monster:
        return self.monsters[value]

    def __repr__(self) -> str:
        return "MonsterProvider"
