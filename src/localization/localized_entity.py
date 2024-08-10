from src.entities.entity import Entity


class LocalizedEntity:
    def __init__(self, entity: Entity):
        self.entity = entity

        self._name = entity.name
        self._title = entity.title
        self._plural = "plural" in entity.flags
        self._pronouns = entity.pronouns

    @property
    def subject(self) -> str:
        return self._pronouns.subject

    @property
    def object(self) -> str:
        return self._pronouns.object

    @property
    def poss_adjective(self) -> str:
        return self._pronouns.poss_adjective

    @property
    def possessive(self) -> str:
        return self._pronouns.possessive

    @property
    def reflexive(self) -> str:
        return self._pronouns.reflexive

    @property
    def s(self) -> str:
        if self._pronouns.third_s:
            return "s"
        return ""

    @property
    def es(self) -> str:
        if self._pronouns.third_s:
            return "es"
        return ""

    @property
    def name(self) -> str:
        if self._title == "":
            return self._name
        return f"{self._title} {self._name}"

    @property
    def are(self) -> str:
        if self._plural or self._pronouns == "3rd_they":
            return "are"
        return "is"

    @property
    def owns(self) -> str:
        if self._pronouns.form == 2:
            return self._pronouns.poss_adjective

        elif self._name.endswith("s"):
            return self._name + "'"
        else:
            return self._name + "'s"

    @property
    def blood(self) -> str:
        return self.entity.species.blood

    def __repr__(self) -> str:
        return f"LocalizedEntity(name={self._name}, title={self._title}, plural={self._plural}, pronouns={self._pronouns})"
