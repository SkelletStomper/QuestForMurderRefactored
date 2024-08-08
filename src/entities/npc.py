from src.entities.entity import Entity
from src.items.inventory import Inventory
from src.localization.localized_entity import LocalizedEntity
from src.combat.combat_basics import Attack


class NPC(Entity):
    def __init__(self,
                 name: str,
                 title: str = "",
                 pronouns: str = "3rd_they",
                 hp_max: int = 10,
                 dodge: int = 0,
                 accuracy: int = 0,
                 armor: int = 0,
                 flags: list[str]|None = None,
                 ) -> None:
        super().__init__(
            name=name,
            title=title,
            pronouns=pronouns,
            hp_max=hp_max,
            dodge=dodge,
            accuracy=accuracy,
            armor=armor,
            flags=flags,
        )

        self.hp = self.hp_max
        self.inventory: Inventory = Inventory()

    def calculate_dmg_factor(self, attack: Attack) -> float:
        """
        Calculate the damage factor of a given attack against this NPC.
        Takes into perspective the weaknesses of all Flags.
        """
        dmg_factor = 1.0

        for flag in self.flags:
            dmg_factor *= flag.weaknesses.attack_factor(attack)

        return dmg_factor

    def get_le(self) -> LocalizedEntity:
        """
        Get a Localized Entity describing the npc grammatically.
        """
        plural = "plural" in self.flags

        return LocalizedEntity(
            name=self.name,
            title=self.title,
            plural=plural,
            pronouns=self.pronouns,
            flags=self.flags
        )

    def __repr__(self) -> str:
        return f"NPC(name={self.name}, title={self.title}, pronouns={self.pronouns}, " \
               f" hp_max={self.hp_max}, dodge={self.dodge}, armor={self.armor}, " \
               f"inventory={self.inventory}, flags={self.flags})"
