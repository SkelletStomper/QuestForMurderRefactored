from src.items.items import Item
from src.base.types import AttackType
from src.combat.attack import Attack, ConditionalAttackText
from src.localization.l_string import LString


class WeaponAttackStencil:
    def __init__(self, in_dict: dict) -> None:
        self.name: str = in_dict["name"]
        self.description: str = in_dict["description"]
        self.text: ConditionalAttackText = ConditionalAttackText(in_dict["text"])

        self.dmg: int = in_dict["dmg"]
        self.acc: int = in_dict["acc"]
        self.crt: float = in_dict["crt"]
        self.types: list[AttackType] = [AttackType(attack_type) for attack_type in in_dict["types"]]

    def generate_attack(self) -> Attack:
        """Generate an attack from this stencil."""
        return Attack(
            dmg=self.dmg,
            acc=self.acc,
            crt=self.crt,
            types=self.types,
            atk_str=self.text,
        )

    def __repr__(self) -> str:
        return f"WeaponAttackStencil(name={self.name}, description={self.description}, text={self.text}, dmg={self.dmg}, " \
               f"acc={self.acc}, crt={self.crt}, types={self.types})"


class Weapon(Item):
    def __init__(self, item_id,  in_dict: dict):
        super().__init__(item_id, in_dict)
        self.attacks = {atk_id: WeaponAttackStencil(atk_data) for atk_id, atk_data in in_dict["attacks"].items()}

    def __repr__(self) -> str:
        return f"Weapon(id={self.id}, name={self.name}, description={self.description}, weight={self.weight}, attacks={self.attacks})"
