from src.items.inventory import Inventory


class InventoryDialogue:
    def __init__(self, inventory: Inventory, timed: bool = False):
        self.inventory = inventory
        self.timed = timed

    def dialogue(self) -> bool:
        player_input = ""
        while player_input != "0":
            print("What do you want to do?")
            print("(1): Inspect equipped Items")
            print("(2): Inspect Inventory")
            print("(0): Back")
            player_input = input(">: ")

            took_turn = False
            if player_input == "1":
                took_turn = self.dialogue_equip()
            if player_input == "2":
                took_turn = self.dialogue_inventory()
            if self.timed and took_turn:
                return True

        return False

    def dialogue_inventory(self) -> bool:
        inv = self.inventory
        player_input = ""

        while player_input != "0":
            print(f"Inventory ({inv.item_count()}/{inv.item_capacity}):")
            for i in range(1, inv.item_count()+1):
                print(f"({i}): {inv[i-1].info_short()}")

            print("\n(0): Back")
            player_input = input(">: ")
            index = int(player_input)-1
            if inv.valid_index(index):
                took_turn = self.sub_dialogue_inventory(index)
                if self.timed and took_turn:
                    return True

        return False

    def sub_dialogue_inventory(self, index: int) -> bool:
        """Dialogue to inspect and equip/drop an item in the inventory at a specified index.\n
        Returns True if an action was taken that takes up a turn."""
        inv = self.inventory

        item = inv[index]
        equipable = inv.is_equipable(item)
        player_input = ""

        while player_input != "0":
            print(item.info_long())
            print("")
            if equipable:
                print("(1): Equip")
            else:
                print("(x): Equip (item not equipable)")
            print("(2) Drop Item")

            player_input = input(">: ")

            if player_input == "1" and equipable:
                inv.try_equip(index)
                return True
            if player_input == "2":
                inv.remove(index)
                return False
        return False

    def dialogue_equip(self) -> bool:
        equip_slots = self.inventory.equip_slots
        player_input = ""

        while player_input != "0":
            for i in range(1, len(equip_slots) + 1):
                print(f"({i}): {equip_slots[i-1].info_short()}")

            print("(0): Back")
            player_input = input(">: ")
            if player_input.isdigit():
                index = int(player_input) - 1
                if 0 <= index <= len(equip_slots):
                    took_turn = self.sub_dialogue_equip(index)

                    if self.timed and took_turn:
                        return True

        return False

    def sub_dialogue_equip(self, index: int) -> bool:
        """Opens the Item Dialogue for an equipped item at a specified index.\n
        Returns True if an action was taken that takes up a turn.
        """
        equip_slots = self.inventory.equip_slots

        slot = equip_slots[index]

        player_input = ""

        while player_input != "0":
            print(slot.info_long())
            print("")
            if not slot.free():
                print("(1): Unequip")
            else:
                print("(x): Unequip (No Item Equipped)")
            print("(0): Back")

            player_input = input(">: ")

            if player_input == "1" and not slot.free():
                self.inventory.add(slot.unequip())
                return True

        return False
