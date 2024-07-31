from enum import Enum

from src.combat.attack import AttackType, Attack


class Item:
    def __init__(self, in_dict: dict):
        self.name = in_dict["name"]
        self.description = in_dict["description"]
        self.weight = in_dict["weight"]


class AttackStencil:
    def __init__(self, in_dict: dict) -> None:
        self.name = in_dict["name"]
        self.description = in_dict["description"]
        self.text = in_dict["text"]

        self.dmg = in_dict["dmg"]
        self.acc = in_dict["acc"]
        self.crt = in_dict["crt"]
        self.types = [AttackType(attack_type) for attack_type in in_dict["types"]]

    def generate_attack(self) -> Attack:
        return Attack(
            dmg=self.dmg,
            acc=self.acc,
            crt=self.crt,
            types=self.types
        )


class Weapon(Item):
    def __init__(self, in_dict: dict):
        super().__init__(in_dict)
        self.attacks = {atk_id: AttackStencil(atk_data) for atk_id, atk_data in in_dict["attacks"].keys()}


class Offhand(Item):
    def __init__(self, in_dict: dict):
        super().__init__(in_dict)
        self.damage: int = in_dict["damage"]
        self.armor: int = in_dict["armor"]
        self.heal: int = in_dict["heal"]
        self.types: list[AttackType] = in_dict["types"]



class ArmorType(Enum):
    CHEST = "CHEST"
    HEAD = "HEAD"
    HANDS = "HANDS"
    LEGS = "LEGS"
    FEET = "FEET"


class Armor(Item):
    def __init__(self, in_dict: dict):
        super().__init__(in_dict)
        self.type: ArmorType = ArmorType(["type"])
        self.armor: int = in_dict["armor"]


class Ability(Item):
    def __init__(self, in_dict):
        super().__init__(in_dict["name"])
        self.duration = in_dict["duration"]
        self.reload = in_dict["reload"]
        self.description = in_dict["description"]
