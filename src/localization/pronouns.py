
class PronounSet:
    """
    Usage examples:
    subject: She walks down the road to the store.\n
    object: Did you hear of her walking down the road to the store?\n
    poss_adjective: When Olivia bought milk, it became her milk.\n
    poss: Milk!! Hers!!!\n
    reflexive: Olivia is contempt with herself now that she owns milkers.\n
    """

    def __init__(self, p_id: str, init_dict: dict):
        self.id = p_id
        self.subject: str = init_dict["subject"]
        self.object: str = init_dict["object"]
        self.poss_adjective: str = init_dict["poss_adjective"]
        self.possessive: str = init_dict["possessive"]
        self.reflexive: str = init_dict["reflexive"]
        self.third_s: bool = init_dict["3rdS"]
        self.form: int = init_dict["form"]

    def __eq__(self, other):
        return self.id == other
