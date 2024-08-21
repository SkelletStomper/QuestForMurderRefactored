from src.dialogue import Dialogue


import logging
logger = logging.getLogger(__name__)


class DialogueProvider:
    def __init__(self, all_dialogues: dict[str, dict]):
        self.dialogue_sequences: dict[str, Dialogue] = {}

        logger.info("Start parsing item data")

        for dialogue_id, dialogue_data in all_dialogues.items():
            self.dialogue_sequences[dialogue_id] = Dialogue.new_dialogue(dialogue_id, dialogue_data)

        logger.info("Finished parsing dialogue data")

    def __getitem__(self, item: str) -> Dialogue:
        return self.dialogue_sequences[item]

    def all_ids(self) -> list[str]:
        return list(self.dialogue_sequences.keys())

    def __repr__(self) -> str:
        return f"DialogueProvider({len(self.dialogue_sequences)} Dialogue Sequences)"
