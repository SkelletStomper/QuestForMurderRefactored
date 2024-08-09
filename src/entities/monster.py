from src.entities.entity import Entity
from src.base.types import WeaknessSet, AttackType
from src.combat.attack import Attack, ConditionalAttackText
from src.localization.localized_entity import LocalizedEntity
from src.localization.l_string import LString


class MonsterAttackStencil:
    def __init__(self, in_dict: dict) -> None:
        self.name = in_dict["name"]

        self.text = ConditionalAttackText(in_dict["text"])

        self.dmg = in_dict["dmg"]
        self.acc = in_dict["acc"]
        self.crt = in_dict["crt"]
        self.types = [AttackType(attack_type) for attack_type in in_dict["types"]]
        self.weight = in_dict["weight"]

        if "multi" in in_dict.keys():
            self.multi = in_dict["multi"]
        else:
            self.multi = 1

    def generate_attacks(self) -> [Attack]:
        """
        Return a list of Attacks fitted after the Attack Stencil.
        """
        return [Attack(
            dmg=self.dmg,
            acc=self.acc,
            crt=self.crt,
            types=self.types,
            atk_str=self.text,
        )]*self.multi

    def __repr__(self) -> str:
        return f"MonsterAttackStencil(name={self.name}, text={self.text}, dmg={self.dmg}, acc={self.acc}, " \
               f"crt={self.crt}, types={self.types}, weight={self.weight})"


class Monster(Entity):
    def __init__(self, in_dict: dict):
        super().__init__(
            name=in_dict["name"],
            title=in_dict["title"],
            pronouns=in_dict["pronouns"],
            hp_max=in_dict["hp_max"],
            dodge=in_dict["dodge"],
            accuracy=0,
            armor=in_dict["armor"],
            flags=in_dict["flags"],
        )

        self.info: str = in_dict["information"]
        self.death_messages: list[str] = in_dict["death_messages"]

        self.attacks: dict[str, MonsterAttackStencil] = \
            {attack_name: MonsterAttackStencil(attack_data)
             for attack_name, attack_data
             in in_dict["attacks"].items()}

        self.weaknesses = WeaknessSet(in_dict["weaknesses"])

    def calculate_dmg_factor(self, attack: Attack) -> float:
        """
        Calculate the damage factor of a given attack against this monster.
        Takes into perspective the own WeaknessSet as well as the weaknesses of all Flags.
        """
        dmg_factor = super().calculate_dmg_factor(attack)

        dmg_factor *= self.weaknesses.attack_factor(attack)

        return dmg_factor

    def get_le(self) -> LocalizedEntity:
        """
        Get a Localized Entity describing the monster grammatically.
        """
        plural = False
        if "plural" in self.flags:
            plural = True

        return LocalizedEntity(
            name=self.name,
            title=self.title,
            plural=plural,
            pronouns=self.pronouns,
            flags=self.flags,
        )

    def __repr__(self) -> str:
        return f"Monster(name={self.name}, title={self.title}, pronouns={self.pronouns}, info={self.info}, " \
               f"death_messages={self.death_messages}, hp_max={self.hp_max}, dodge={self.dodge}, armor={self.armor}, " \
               f"attacks={self.attacks}, weaknesses={self.weaknesses}, flags={self.flags})"
