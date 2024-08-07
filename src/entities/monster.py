from src.combat.attack import Attack, WeaknessSet, AttackType
from src.localization.localized_entity import LocalizedEntity
from src.localization.l_string import LString


class MonsterAttackStencil:
    def __init__(self, in_dict: dict) -> None:
        self.name = in_dict["name"]

        self.text = LString(in_dict["text"])
        if self.text == "":
            self.text = LString("{atk.name} hits {def.name} with a vicious attack!")

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


class Monster:
    def __init__(self, in_dict: dict):
        from src.data_providers import pronoun_provider as pp
        from src.data_providers import flag_provider as fp

        self.name: str = in_dict["name"]
        self.title: str = in_dict["title"]
        self.pronouns = pp[in_dict["pronouns"]]

        self.info: str = in_dict["information"]
        self.death_messages: list[str] = in_dict["death_messages"]

        self.hp_max: int = in_dict["hp_max"]
        self.dodge: int = in_dict["dodge"]
        self.armor: int = in_dict["armor"]

        self.attacks: dict[str, MonsterAttackStencil] = \
            {attack_name: MonsterAttackStencil(attack_data)
             for attack_name, attack_data
             in in_dict["attacks"].items()}

        self.weaknesses = WeaknessSet(in_dict["weaknesses"])

        self.flags = [fp(flag_name) for flag_name in in_dict["flags"]]

    def calculate_dmg_factor(self, attack: Attack) -> float:
        """
        Calculate the damage factor of a given attack against this monster.
        Takes into perspective the own WeaknessSet as well as the weaknesses of all Flags.
        """
        dmg_factor = 1.0

        dmg_factor *= self.weaknesses.attack_factor(attack)
        for flag in self.flags:
            dmg_factor *= flag.weaknesses.attack_factor(attack)

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
        )

    def __repr__(self) -> str:
        return f"Monster(name={self.name}, title={self.title}, pronouns={self.pronouns}, info={self.info}, " \
               f"death_messages={self.death_messages}, hp_max={self.hp_max}, dodge={self.dodge}, armor={self.armor}, " \
               f"attacks={self.attacks}, weaknesses={self.weaknesses}, flags={self.flags})"
