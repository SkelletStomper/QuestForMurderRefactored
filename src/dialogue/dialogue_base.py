
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


class DialogueOneWay(Dialogue):
    def __init__(self, dialogue_id: str, in_dict: dict):
        super().__init__(dialogue_id, in_dict)

        self.follow_up: str = in_dict["follow_up"]

    def play(self, dc: DialogueContext) -> str:
        super().play(dc)

        return self.follow_up


class DialogueChoice(Dialogue):
    class SingleChoice:
        def __init__(self, choice_name: str, in_dict: dict) -> None:
            self.name = choice_name
            self.text: str = in_dict["text"]
            self.response: list[str] = in_dict["response"]
            self.follow_up: str = in_dict["follow_up"]
            self.requirements: list[str] = in_dict["requirements"]
            self.effects: list[str] = in_dict[""]

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
            if chosen.isdigit():
                index = int(chosen)
            else:
                dc.print("That is not a valid choice!")
                continue

            choice = self.choices[index]
            self.print_text_list(choice.response, dc)
            self.apply_affects(choice.effects)

            return choice.follow_up


class Condition:
    def __init__(self, condition_str: str) -> None:
        """Condition Structure: """
        self.condition_str = condition_str

    def resolve(self, dc: DialogueContext):
        key, value = self.condition_str.split("==")
        if "context[" in key:
            key = key[8:-1]

        if not dc.has_context_variable(key):
            raise KeyError(f"Context contains no variable '{key}'")

        value = value.split("||")

        return dc.read_context_variable(key) in value


class DialogueConditional(Dialogue):
    class Path:
        def __init__(self, path_name: str, in_dict: dict) -> None:
            self.name = path_name
            self.text: list[str] = in_dict["text"]
            self.follow_up: str = in_dict["follow_up"]
            self.conditions: list[Condition] = \
                [Condition(condition_str) for condition_str in in_dict["conditions"]]

            if "effects" in in_dict:
                self.effects = in_dict["effects"]
            else:
                self.effects = []

    def __init__(self, dialogue_id: str, in_dict: dict) -> None:
        super().__init__(dialogue_id, in_dict)

        self.paths: list[DialogueConditional.Path] = \
            [self.Path(path_id, path_data) for path_id, path_data in in_dict["paths"].items()]

    def play(self, dc: DialogueContext) -> str:
        super().play(dc)

        for path in self.paths:
            success = True
            for condition in path.conditions:
                if not condition.resolve(dc):
                    success = False
                    break
            if success:
                self.print_text_list(path.text, dc)
                self.apply_affects(path.effects)
                return path.follow_up

        raise RuntimeError("None of the paths in DialogueConditional '{self.id}' has its conditions fulfilled!")


class DialogueQuery(Dialogue):
    def __init__(self, dialogue_id: str, in_dict: dict):
        super().__init__(dialogue_id, in_dict)
        self.input_query: str = in_dict["input"]
        self.follow_up: str = in_dict["follow_up"]

    def play(self, dc: DialogueContext) -> str:
        super().play(dc)

        player_input = input(">: s")

        dc.add_context_variable(self.input_query, player_input)

        return self.follow_up


