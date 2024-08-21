from dialogue.dialogue_base import DialogueContext, Dialogue


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
