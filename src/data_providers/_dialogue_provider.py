from src.dialogue import (Dialogue,
                          DialogueQuery,
                          DialogueConditional,
                          DialogueChoice,
                          DialogueOneWay)

import logging
logger = logging.getLogger(__name__)


class DialogueProvider:
    def __init__(self, item_data: dict[str, dict]):
        self.dialogue_sequences: dict[str, Dialogue] = {}

        logger.info("Start parsing item data")

        for dialogue_id, dialogue in item_data.items():
            dialogue_type = dialogue["dialogue_type"]

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

            self.dialogue_sequences[dialogue_id] = dialogue_class(dialogue_id, dialogue)

        logger.info("Finished parsing dialogue data")

    def __getitem__(self, item: str) -> Dialogue:
        return self.dialogue_sequences[item]

    def all_ids(self) -> list[str]:
        return list(self.dialogue_sequences.keys())

    def __repr__(self) -> str:
        return f"DialogueProvider({len(self.dialogue_sequences)} Dialogue Sequences)"
