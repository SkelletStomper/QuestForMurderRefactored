from src.localization.pronouns import PronounSet

import logging
logger = logging.getLogger(__name__)


class PronounProvider:
    def __init__(self, all_pronoun_data: dict[str, dict]):
        logger.info("Start parsing pronoun data")
        self.pronouns: dict[str, PronounSet] = \
            {pronoun_name: PronounSet(pronoun_name, pronoun_data)
             for pronoun_name, pronoun_data in all_pronoun_data.items()}
        logger.info("Finished parsing pronoun data")

    def __getitem__(self, item: str) -> PronounSet:
        return self.pronouns[item]

    def __repr__(self) -> str:
        return "PronounProvider"
