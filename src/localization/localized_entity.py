from src.localization.pronouns import PronounSet


class LocalizedEntity:
    def __init__(self, name: str, title: str, plural: bool, pronouns: PronounSet):
        self._name = name
        self._title = title
        self._plural = plural
        self._pronouns = pronouns

    @property
    def subject(self):
        return self._pronouns.subject

    @property
    def object(self):
        return self._pronouns.object

    @property
    def poss_adjective(self):
        return self._pronouns.poss_adjective

    @property
    def possessive(self):
        return self._pronouns.possessive

    @property
    def reflexive(self):
        return self._pronouns.reflexive




