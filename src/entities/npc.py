from src.items.inventory import Inventory


class NPC:
    def __init__(self) -> None:

        self.max_hp = 10
        self.hp = self.max_hp

        self.dodge = 0
        self.accuracy = 0

        self.inventory: Inventory = Inventory()
