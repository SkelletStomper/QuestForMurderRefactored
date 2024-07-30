from src.combat.attack import AttackType


class Item:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight


class Weapon(Item):
    def __init__(self, in_dict):
        super().__init__(in_dict["name"], in_dict["weight"])
        self.damage: int = in_dict["damage"]
        self.types: list[AttackType] = in_dict["types"]
        self.attribute = in_dict["attribute"]


class Offhand(Item):
    def __init__(self, in_dict):
        super().__init__(in_dict["name"], in_dict["weight"])
        self.damage = in_dict["damage"]
        self.armor = in_dict["armor"]
        self.heal = in_dict["heal"]
        self.types: list[AttackType] = in_dict["types"]
        self.attribute = in_dict["attribute"]


class Armor(Item):
    def __init__(self, in_dict):
        super().__init__(in_dict["name"], in_dict["weight"])
        self.armor = in_dict["armor"]


class Ability(Item):
    def __init__(self, in_dict):
        super().__init__(in_dict["name"])
        self.duration = in_dict["duration"]
        self.reload = in_dict["reload"]
        self.description = in_dict["description"]
