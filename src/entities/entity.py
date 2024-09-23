from src.localization.pronouns import PronounSet
from src.localization.localized_entity import LocalizedEntity
from src.base.flag import Flag
from src.combat.attack import Attack
from src.items.armor import ArmorMaterial

import logging
logger = logging.getLogger(__name__)


class Entity:
    def __init__(self,
                 name: str,
                 title: str = "",
                 pronouns: str = "3rd_they",
                 hp_max: int = 10,
                 dodge: int = 0,
                 accuracy: int = 0,
                 armor: dict[str, int] = None,
                 flags: list[str] = None,
                 species="spec_unknown"
                 ) -> None:

        from src.data_providers import pronoun_provider as pp
        from src.data_providers import flag_provider as fp
        from src.data_providers import species_provider as sp
        from src.data_providers import armat_provider as amp

        self.name = name
        self.title = title
        self.pronouns: PronounSet = pp[pronouns]

        self.hp_max = hp_max

        self.dodge = dodge
        self.accuracy = accuracy

        self.speed = 0

        if flags is None:
            flags = []
        self.flags: list[Flag] = [fp(flag_name) for flag_name in flags]
        self.species = sp[species]

        if armor is None:
            armor = {"skin": 0}

        self.armor = {self.species.skin: armor["skin"]}
        del armor["skin"]

        self.armor.update({amp[armor_type]: armor_value for armor_type, armor_value in armor.items()})

    def calculate_dmg_factor(self, attack: Attack) -> float:
        """
        Calculate the damage factor of a given attack against this entity.
        Takes into perspective the own WeaknessSet as well as the weaknesses of all Flags.
        """
        dmg_factor = 1.0

        dmg_factor *= self.species.weaknesses.attack_factor(attack.types)
        for flag in self.flags:
            dmg_factor *= flag.weaknesses.attack_factor(attack.types)

        return dmg_factor

    def armor_layers(self) -> dict[ArmorMaterial, int]:
        return self.armor

    def calculate_effective_armor(self, attack: Attack) -> int:
        armor_sum = 0
        for armor_type, armor_value in self.armor.items():
            try:
                factor = armor_type.effective_factor(attack.types)
                armor_sum += armor_value*factor
            except AttributeError as ae:
                logger.error(f"Tried using effective_factor on str: {armor_type} (Exception: {ae})")
        return round(armor_sum)

    def get_le(self) -> LocalizedEntity:
        """
        Get a Localized Entity describing the entity grammatically.
        """
        return LocalizedEntity(self)
