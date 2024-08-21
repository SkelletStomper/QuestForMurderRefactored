
class DialogueContext:
    def __init__(self):
        self.context_variables: dict[str, str] = {}

    def print(self, text: str):
        print(text)

    def add_context_variable(self, key, value):
        self.context_variables[key] = value

    def read_context_variable(self, key) -> str:
        return self.context_variables[key]

    def has_context_variable(self, key) -> bool:
        return key in self.context_variables


class Dialogue:
    def __init__(self, dialogue_id: str, in_dict: dict):
        self.id = dialogue_id
        self.entry: bool = in_dict["entry"]
        self.text: list[str] = in_dict["text"]
        self.effects: list[str] = []
        if "effects" in in_dict:
            self.effects = in_dict["effects"]

    def play(self, dc: DialogueContext) -> str:  # type: ignore
        """
        Executes a dialogue part in a given context. Returns the next dialogue ID, or EXIT if the dialogue is over.
        """
        # must return string in subclasses
        self.print_text_list(self.text, dc)

        if self.effects:
            self.apply_affects(self.effects)

    def apply_affects(self, effects: list[str]):
        pass  # not yet implemented

    @staticmethod
    def print_text_list(text_list: list[str], dc: DialogueContext):
        dc.print(text_list[0])
        for line in text_list[1:]:
            input()
            dc.print(line)


