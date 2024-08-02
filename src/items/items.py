from enum import Enum

from src.combat.attack import AttackType, Attack


class Item:
    def __init__(self, in_dict: dict):
        self.name = in_dict["name"]
        self.description = in_dict["description"]
        self.weight = in_dict["weight"]


class Offhand(Item):
    def __init__(self, in_dict: dict):
        super().__init__(in_dict)
        self.damage: int = in_dict["damage"]
        self.armor: int = in_dict["armor"]
        self.heal: int = in_dict["heal"]
        self.types: list[AttackType] = in_dict["types"]


class Ability(Item):
    def __init__(self, in_dict):
        super().__init__(in_dict["name"])
        self.duration = in_dict["duration"]
        self.reload = in_dict["reload"]
        self.description = in_dict["description"]





