from src.items.items import Item
from src.base.types import AttackType
from src.combat.attack import Attack, ConditionalAttackText


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

    def info(self) -> str:
        type_list = [attack_type.value for attack_type in self.types]
        type_string = ", ".join(type_list)

        return (f"Attack: {self.name}\n"
                f"\"{self.description}\"\n"
                f"Damage: {self.dmg}\n"
                f"Accuracy: {self.acc}\n"
                f"Critical modifier: {self.crt}\n"
                f"Types: {type_string}")

    def __repr__(self) -> str:
        return f"WeaponAttackStencil(name={self.name}, description={self.description}, text={self.text}, dmg={self.dmg}, " \
               f"acc={self.acc}, crt={self.crt}, types={self.types})"


class Weapon(Item):
    def __init__(self, item_id,  in_dict: dict):
        super().__init__(item_id, in_dict)
        self.attacks = {atk_id: WeaponAttackStencil(atk_data) for atk_id, atk_data in in_dict["attacks"].items()}

    def info_short(self) -> str:
        return f"{self.name} (Weapon)"

    def info_long(self) -> str:
        attack_list = [attack.info() for attack in self.attacks.values()]
        attack_string = "\n\n".join(attack_list)

        return (f"{self.name}\n"
                f"\"{self.description}\"\n"
                f"Weight: {self.weight}\n"
                f"Grants the following Attacks:\n"
                f"{attack_string}")

    def __repr__(self) -> str:
        return f"Weapon(id={self.id}, name={self.name}, description={self.description}, weight={self.weight}, attacks={self.attacks})"
