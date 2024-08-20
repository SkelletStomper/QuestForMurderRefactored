
class DialogueContext:
    def __init__(self):
        self.local: dict[str, str] = {}




class Dialogue:
    def __init__(self, dialogue_id: str, in_dict: dict):
        self.id = dialogue_id
        self.entry: bool = in_dict["entry"]
        self.text: list[str] = in_dict["text"]
        self.effects = []
        if "effects" in in_dict:
            self.effects = in_dict["effects"]

    def play(self, dc: DialogueContext) -> None:
        self.print_text_list(self.text, dc)

        if self.effects:
            self.apply_affects(self.effects)


    def apply_affects(self, effects:list[str]):
        pass  # not yet implemented

    def print_text_list(self, text_list: list[str], dc: DialogueContext):
        print(text_list[0])
        for line in text_list[1:]:
            input()
            print(line)



class DialogueOneWay(Dialogue):
    def __init__(self, dialogue_id: str, in_dict: dict):
        super().__init__(
            dialogue_id=dialogue_id,
            in_dict=in_dict
        )
        self.follow_up = in_dict["follow_up"]

    def play(self, dc: DialogueContext):
        pass  # TODO