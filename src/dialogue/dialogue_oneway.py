from dialogue.dialogue_base import Dialogue, DialogueContext


class DialogueOneWay(Dialogue):
    def __init__(self, dialogue_id: str, in_dict: dict):
        super().__init__(dialogue_id, in_dict)

        self.follow_up: str = in_dict["follow_up"]

    def play(self, dc: DialogueContext) -> str:
        super().play(dc)

        return self.follow_up
