from src.items.items import Item
from src.combat.attack import Attack, AttackType
from src.localization.l_string import LString


class AttackStencil:
    def __init__(self, in_dict: dict) -> None:
        self.name = in_dict["name"]
        self.description = in_dict["description"]
        self.text = LString(in_dict["text"])

        self.dmg = in_dict["dmg"]
        self.acc = in_dict["acc"]
        self.crt = in_dict["crt"]
        self.types = [AttackType(attack_type) for attack_type in in_dict["types"]]

    def generate_attack(self) -> Attack:
        return Attack(
            dmg=self.dmg,
            acc=self.acc,
            crt=self.crt,
            types=self.types,
            atk_str=self.text,
        )


class Weapon(Item):
    def __init__(self, in_dict: dict):
        super().__init__(in_dict)
        self.attacks = {atk_id: AttackStencil(atk_data) for atk_id, atk_data in in_dict["attacks"].items()}
