from dialogue.dialogue_base import Dialogue, DialogueContext


class DialogueQuery(Dialogue):
    def __init__(self, dialogue_id: str, in_dict: dict):
        super().__init__(dialogue_id, in_dict)
        self.input_query: str = in_dict["input"]
        self.query_prompt: str = in_dict["query_prompt"]
        self.follow_up: str = in_dict["follow_up"]

    def play(self, dc: DialogueContext) -> str:
        super().play(dc)

        player_input = input(self.query_prompt)

        dc.add_context_variable(self.input_query, player_input)

        return self.follow_up
