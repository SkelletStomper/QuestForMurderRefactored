
from src.combat.attack import AttackType


class Item:
    def __init__(self, in_dict: dict):
        self.name = in_dict["name"]
        self.description = in_dict["description"]
        self.weight = in_dict["weight"]

    def __repr__(self) -> str:
        return f"Item(name={self.name}, description={self.description}, weight={self.weight})"


class Offhand(Item):
    def __init__(self, in_dict: dict):
        super().__init__(in_dict)
        self.damage: int = in_dict["damage"]
        self.armor: int = in_dict["armor"]
        self.heal: int = in_dict["heal"]
        self.types: list[AttackType] = in_dict["types"]

    def __repr__(self) -> str:
        return f"OffhandItem(name={self.name}, description={self.description}, weight={self.weight})"


class Ability(Item):
    def __init__(self, in_dict):
        super().__init__(in_dict["name"])
        self.duration = in_dict["duration"]
        self.reload = in_dict["reload"]
        self.description = in_dict["description"]

    def __repr__(self) -> str:
        return f"Ability(name={self.name}, description={self.description}, weight={self.weight})"
