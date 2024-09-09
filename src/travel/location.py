from src.effects import apply_effects


class Location:
    class Interactive:
        def __init__(self, interactive_id: str, in_dict: dict):
            self.interactive_id = interactive_id
            self.name: str = in_dict['name']
            self.description: str = in_dict['description']
            self.conditions: list[str] = in_dict['conditions']
            self.effects: list[str] = in_dict['effects']

        def is_availaible(self) -> bool:
            return True

        def apply_effects(self):
            apply_effects(self.effects)


    def __init__(self, location_id: str, in_dict: dict):
        from src.data_providers import monster_pool_provider as mpp
        from src.entities.monster_pool import MonsterPool

        self.location_id = location_id
        self.name: str = in_dict['name']
        self.description: str = in_dict['description']
        self.monster_pool: MonsterPool = mpp[in_dict['monster_pool']]

        self.interactions: list[Location.Interactive] = [
            Location.Interactive(interactive_id, interactive_data)
            for interactive_id, interactive_data in in_dict["interactions"].items()
        ]

        self.exits: list[Location.Interactive] = [
            Location.Interactive(exit_id, exit_data) for exit_id, exit_data in in_dict["exits"].items()
        ]

    def get_monster_id(self):
        return self.monster_pool.random_monster_id()


    def __repr__(self):
        return (f"Location(id={self.location_id}, name={self.name}, description={self.description}, "
                f"{len(self.interactions)} interactions, {len(self.exits)})")
