from src.items.inventory import Inventory
from src.localization.localized_entity import LocalizedEntity


class NPC:
    def __init__(self) -> None:
        from src.data_providers import pronoun_provider as pp
        from src.data_providers import flag_provider as fp

        self.name: str = "Mary Jane"
        self.title: str = ""
        self.pronouns = pp["3rd_she"]

        self.hp_max = 10
        self.hp = self.hp_max

        self.dodge = 0
        self.accuracy = 0
        self.armor = 0

        self.inventory: Inventory = Inventory()
        self.flags = []

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
        )

    def __repr__(self) -> str:
        return f"NPC(name={self.name}, title={self.title}, pronouns={self.pronouns}, " \
               f" hp_max={self.hp_max}, dodge={self.dodge}, armor={self.armor}, " \
               f"inventory={self.inventory}, flags={self.flags})"
