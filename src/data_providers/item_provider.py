from src.items.items import Item

from src.items.armor import Armor
from src.items.weapon import Weapon

class ItemProvider:
    def __init__(self, items: dict[str, dict]):
        self.items: dict[str, Item] = {}
        for item_id, item in items.items():
            item_type = item["json_type"].split(".")[1]
            add_item = None
            if item_type == "armor":
                add_item = Armor(item)
            if item_type == "weapon":
                add_item = Weapon(item)

            self.items[item_id] = add_item




