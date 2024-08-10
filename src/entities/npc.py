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
                 armor: dict[str, int] = None,
                 flags: list[str] | None = None,
                 species: str = "spec_humanoid"
                 ) -> None:

        if armor is None:
            armor = {"skin": 0}

        super().__init__(
            name=name,
            title=title,
            pronouns=pronouns,
            hp_max=hp_max,
            dodge=dodge,
            accuracy=accuracy,
            armor=armor,
            flags=flags,
            species=species
        )

        self.hp = self.hp_max
        self.inventory: Inventory = Inventory()

    def calculate_dmg_factor(self, attack: Attack) -> float:
        """
        Calculate the damage factor of a given attack against this NPC.
        Takes into perspective the weaknesses of all Flags.
        """
        return super().calculate_dmg_factor(attack)

    def __repr__(self) -> str:
        return f"NPC(name={self.name}, title={self.title}, pronouns={self.pronouns}, " \
               f" hp_max={self.hp_max}, dodge={self.dodge}, armor={self.armor}, " \
               f"inventory={self.inventory}, flags={self.flags})"
