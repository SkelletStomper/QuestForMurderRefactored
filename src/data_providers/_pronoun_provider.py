from src.localization.pronouns import PronounSet


class PronounProvider:
    def __init__(self, all_pronoun_data: dict[str, dict]):

        self.pronouns: dict[str, PronounSet] = \
            {pronoun_name: PronounSet(pronoun_name, pronoun_data)
             for pronoun_name, pronoun_data in all_pronoun_data.items()}

    def __getitem__(self, item: str) -> PronounSet:
        return self.pronouns[item]

    def __repr__(self) -> str:
        return "PronounProvider"
