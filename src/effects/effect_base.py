
class Effect:
    keyword = "effect"

    def __init__(self, parameters: list[str]) -> None:
        self.parameters = parameters

    def execute(self) -> None:
        pass  # abstract
