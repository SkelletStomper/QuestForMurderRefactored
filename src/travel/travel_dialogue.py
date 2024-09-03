from src.state.gamestate import global_state as gs

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
                pass
            elif player_input in ["2", "(2)", "interact"]:
                pass
            elif player_input in ["3", "(3)", "leave"]:
                pass
            elif player_input in ["0", "(0)", "back"]:
                break
            else:
                print("Make a valid answer!")