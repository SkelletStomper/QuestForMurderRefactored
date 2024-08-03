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

    @property
    def s(self):
        if self._pronouns.third_s:
            return "s"
        return ""

    @property
    def es(self):
        if self._pronouns.third_s:
            return "es"
        return ""

    @property
    def name(self):
        if self._title == "":
            return self._name
        return f"{self._title} {self._name}"

    @property
    def are(self):
        if self._plural or self._pronouns == "3rd_they":
            return "are"
        return "is"

    @property
    def owns(self):
        if self._pronouns.form == 2:
            return self._pronouns.poss_adjective

        elif self._name.endswith("s"):
            return self._name + "'"
        else:
            return self._name + "'s"




