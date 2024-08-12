from src.items.inventory import Inventory


class InventoryDialogue:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def dialogue(self) -> None:
        player_input = ""
        while player_input != "0":
            print("What do you want to do?")
            print("(1): Inspect equipped Items")
            print("(2): Inspect Inventory")
            print("(0): Back")
            player_input = input(">: ")
            if player_input == "1":
                self.dialogue_equip()
            if player_input == "2":
                self.dialogue_inventory()

    def dialogue_inventory(self) -> None:
        inv = self.inventory
        player_input = ""

        while player_input != "0":
            for i in range(1, inv.item_count()+1):
                print(f"({i}): {inv[i-1].info_short()}")

            print("(0): Back")
            player_input = input("Select an item to interact with it, or 0 to go back.")
            index = int(player_input)-1
            if inv.valid_index(index):
                self.sub_dialogue_inventory(index)

    def sub_dialogue_inventory(self, index: int) -> None:
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

            if player_input == "1":
                inv.try_equip(index)
                return
            if player_input == "2":
                inv.remove(index)
                return

    def dialogue_equip(self) -> None:
        pass
