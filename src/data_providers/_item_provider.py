from src.items.items import Item

from src.items.armor import Armor
from src.items.weapon import Weapon

import logging
logger = logging.getLogger(__name__)


class ItemProvider:
    def __init__(self, item_data: dict[str, dict]):
        self.items: dict[str, Item] = {}

        logger.info("Start parsing item data")

        for item_id, item in item_data.items():
            item_type = item["json_type"].split(".")[1]
            add_item = None
            if item_type == "armor":
                add_item = Armor(item_id, item)
            if item_type == "weapon":
                add_item = Weapon(item_id, item)

            self.items[item_id] = add_item

        logger.info("Finished parsing item data")

    def __repr__(self) -> str:
        return "ItemProvider"
