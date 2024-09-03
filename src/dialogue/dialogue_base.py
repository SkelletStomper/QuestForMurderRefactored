from src.effects import apply_effects

import logging
logger = logging.getLogger(__name__)


class DialogueContext:
    def __init__(self):
        self.context_variables: dict[str, str] = {}

    def print(self, text: str):
        context = self.context_variables
        try:
            print(text.format(**locals()))
        except ValueError as ve:
            logger.critical(f"Encountered ValueError when parsing following text: {text}")

    def add_context_variable(self, key, value):
        self.context_variables[key] = value

    def read_context_variable(self, key) -> str:
        return self.context_variables[key]

    def has_context_variable(self, key) -> bool:
        return key in self.context_variables

    def start_dialogue(self, dialogue_id: str):
        from src.data_providers import dialogue_provider as dp
        dialogue = dp[dialogue_id]
        if not dialogue.entry:
            logger.warning(f"Dialogue '{dialogue.id}' is not an entrypoint!")
        next_dialogue = ""
        while True:
            next_dialogue = dialogue.play(self)
            if next_dialogue == "EXIT":
                break
            dialogue = dp[next_dialogue]


class Dialogue:
    @staticmethod
    def new_dialogue(dialogue_id: str, dialogue_data: dict):
        from src.dialogue.dialogue_oneway import DialogueOneWay
        from src.dialogue.dialogue_choice import DialogueChoice
        from src.dialogue.dialogue_conditional import DialogueConditional
        from src.dialogue.dialogue_query import DialogueQuery

        dialogue_type = dialogue_data["dialogue_type"]

        if dialogue_type == "query":
            dialogue_class = DialogueQuery
        elif dialogue_type == "oneway":
            dialogue_class = DialogueOneWay
        elif dialogue_type == "conditional":
            dialogue_class = DialogueConditional
        elif dialogue_type == "choice":
            dialogue_class = DialogueChoice
        else:
            raise ValueError(f"Unknown Dialogue Type: {dialogue_type}")

        return dialogue_class(dialogue_id, dialogue_data)

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
        logger.debug(f"Started dialogue: {self.id}")
        # must return string in subclasses
        self.print_text_list(self.text, dc)

        if self.effects:
            self.apply_affects(self.effects)

    @staticmethod
    def apply_affects(effects: list[str]):
        apply_effects(effects)

    @staticmethod
    def print_text_list(text_list: list[str], dc: DialogueContext):
        if text_list:
            dc.print(text_list[0])

        for line in text_list[1:]:
            input()
            dc.print(line)
