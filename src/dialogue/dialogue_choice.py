from dialogue.dialogue_base import Dialogue, DialogueContext


class DialogueChoice(Dialogue):
    class SingleChoice:
        def __init__(self, choice_name: str, in_dict: dict) -> None:
            self.name = choice_name
            self.text: str = in_dict["text"]
            self.response: list[str] = in_dict["response"]
            self.follow_up: str = in_dict["follow_up"]

            if "requirements" in in_dict:
                self.requirements: list[str] = in_dict["requirements"]
            else:
                self.requirements = []

            if "effects" in in_dict:
                self.effects: list[str] = in_dict["effects"]
            else:
                self.effects = []

    def __init__(self, dialogue_id: str, in_dict: dict) -> None:
        super().__init__(dialogue_id, in_dict)

        self.choices: list[DialogueChoice.SingleChoice] = \
            [self.SingleChoice(choice_name, choice_data)
             for choice_name, choice_data in in_dict["choices"].items()]

    def play(self, dc: DialogueContext) -> str:
        super().play(dc)
        while True:
            for i, choice in enumerate(self.choices):
                dc.print(f"{i+1}: " + choice.text)

            chosen = input(">: ")

            index = -1
            if chosen.isdigit() and 0 <= int(chosen)-1 < len(self.choices):
                index = int(chosen)-1
            else:
                dc.print("That is not a valid choice!")
                continue

            choice = self.choices[index]
            self.print_text_list(choice.response, dc)
            self.apply_affects(choice.effects)

            return choice.follow_up
