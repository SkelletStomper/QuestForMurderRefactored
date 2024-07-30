import json


class PronounSet:
    """
    Usage examples:
    subject: She walks down the road to the store.\n
    object: Did you hear of her walking down the road to the store?\n
    poss_adjective: When Olivia bought milk, it became her milk.\n
    poss: Milk!! Hers!!!\n
    reflexive: Olivia is contempt with herself now that she owns milkers.\n
    """

    def __init__(self, init_dict: dict[str, str]):
        self.subject = init_dict["subject"]
        self.object = init_dict["object"]
        self.poss_adjective = init_dict["poss_adjective"]
        self.possessive = init_dict["possessive"]
        self.reflexive = init_dict["reflexive"]


class PronounProvider:
    def __init__(self):
        with open("data/pronouns.json", "r") as f:
            json_dict = json.load(f)

        self.pronouns: dict[str, PronounSet] = {pronoun_name: PronounSet(pronoun_data) for pronoun_name, pronoun_data in json_dict.items()}

    def __getitem__(self, item: str) -> PronounSet:
        return self.pronouns[item]






pronoun_provider = 0