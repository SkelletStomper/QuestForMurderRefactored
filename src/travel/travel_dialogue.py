from src.state.gamestate import global_state as gs

from src.travel.location import Location
from src.effects import apply_effects

class TravelDialogue:
    def __init__(self):
        pass

    def main_dialogue(self):


        while True:
            location = gs.current_location
            print(f"You are at: {location.name}")

            print("(1): Search for a monster to fight")
            print("(2): Look for things to talk to or interact with")
            print("(3): Look for exits from this shit-hole")

            print("(0): Back")
            player_input = input(">: ").lower()

            if player_input in ["1", "(1)", "fight"]:
                if location.monster_pool.empty():
                    print("It seems like there are no monsters at this location...")
                else:
                    gs.start_monster_fight(location.get_monster_id())
            elif player_input in ["2", "(2)", "interact"]:
                self.interact_dialogue(location.interactions, item_name="Interactions")
            elif player_input in ["3", "(3)", "leave"]:
                self.interact_dialogue(location.exits, item_name="Exits")
            elif player_input in ["0", "(0)", "back"]:
                return
            else:
                print("Make a valid answer!")

    @staticmethod
    def interact_dialogue(interactive_list: list[Location.Interactive], item_name):


        while True:
            filtered_interactive_list = [interactive for interactive in interactive_list if interactive.is_availaible()]

            print(item_name + ":")
            for i in range(len(filtered_interactive_list)):
                print(f"({i+1}): {filtered_interactive_list[i].name}")

            if len(filtered_interactive_list) == 0:
                print("There are currently no available " + item_name)

            print("(0): Back")
            player_input = input(">: ").lower()

            if player_input.isdigit():
                index = int(player_input)-1
                if 0 <= index < len(filtered_interactive_list):
                    filtered_interactive_list[index].apply_effects()
                    return
                if index == -1:
                    return
            print("Make a valid answer!")
