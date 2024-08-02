from src.combat.attack import Attack, WeaknessSet
from src.localization.localized_entity import LocalizedEntity


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
        self.dmg: int = in_dict["dmg"]
        self.crt: float = in_dict["crt"]
        self.acc: int = in_dict["acc"]
        self.dodge: int = in_dict["dodge"]
        self.armor: int = in_dict["armor"]
        self.weaknesses = WeaknessSet(in_dict["weaknesses"])

        self.flags = [fp(flag_name) for flag_name in in_dict["flags"]]

    def calculate_dmg_factor(self, attack: Attack) -> float:
        dmg_factor = 1.0

        dmg_factor *= self.weaknesses.attack_factor(attack)
        for flag in self.flags:
            dmg_factor *= flag.weaknesses.attack_factor(attack)

        return dmg_factor

    def get_le(self) -> LocalizedEntity:
        plural = False
        if "plural" in self.flags:
            plural = True

        return LocalizedEntity(
            name=self.name,
            title=self.title,
            plural=plural,
            pronouns=self.pronouns,
        )

