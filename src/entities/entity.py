from src.localization.pronouns import PronounSet
from src.base.flag import Flag
from src.combat.attack import Attack


class Entity:
    def __init__(self,
                 name: str,
                 title: str,
                 pronouns: str,
                 hp_max: int = 10,
                 dodge: int = 0,
                 accuracy: int = 0,
                 armor: int = 0,
                 flags: list[str] = None,
                 species= "spec_unknown"
                 ) -> None:
        from src.data_providers import pronoun_provider as pp
        from src.data_providers import flag_provider as fp
        from src.data_providers import species_provider as sp

        self.name = name
        self.title = title
        self.pronouns: PronounSet = pp[pronouns]

        self.hp_max = hp_max

        self.dodge = dodge
        self.accuracy = accuracy
        self.armor = armor

        if flags is None:
            flags = []
        self.flags: list[Flag] = [fp(flag_name) for flag_name in flags]
        self.species = sp[species]

    def calculate_dmg_factor(self, attack: Attack) -> float:
        """
        Calculate the damage factor of a given attack against this entity.
        Takes into perspective the own WeaknessSet as well as the weaknesses of all Flags.
        """
        dmg_factor = 1.0

        dmg_factor *= self.species.weaknesses.attack_factor(attack)
        for flag in self.flags:
            dmg_factor *= flag.weaknesses.attack_factor(attack)

        return dmg_factor
