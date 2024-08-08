from src.localization.pronouns import PronounSet
from src.base.flag import Flag


class Entity:
    def __init__(self,
                 name: str,
                 title: str,
                 pronouns: str,
                 hp_max: int = 10,
                 dodge: int = 0,
                 accuracy: int = 0,
                 armor: int = 0,
                 flags: list[str] = None,
                 ) -> None:
        from src.data_providers import pronoun_provider as pp
        from src.data_providers import flag_provider as fp

        self.name = name
        self.title = title
        self.pronouns = pp[pronouns]

        self.hp_max = hp_max

        self.dodge = dodge
        self.accuracy = accuracy
        self.armor = armor

        if flags is None:
            flags = []
        self.flags = [fp(flag_name) for flag_name in flags]
