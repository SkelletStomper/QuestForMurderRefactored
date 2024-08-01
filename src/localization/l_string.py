import re

from src.localization.localized_entity import LocalizedEntity


class LString:
    def __init__(self, lstr: str):
        lstr = lstr.replace("{atk.", "{attacking.")
        lstr = lstr.replace("{def.", "{defending.")
        lstr = lstr.replace("{pl.", "{player.")
        if not self.les_allowed():
            raise ValueError(f"LString {lstr} contains forbidden les!")
        self.lstr = lstr

    def les_allowed(self):
        allowed_les = ["attacking", "defending", "player"]
        le_pattern = r"{[a-zA-Z0-9\.\_]*}"
        les_used = re.findall(self.lstr, le_pattern)
        les_used = set({le[1:-1].split(".")[0] for le in les_used})

        for le in les_used:
            if le not in allowed_les:
                return False
        return True

    def parse(
            self,
            attacking: LocalizedEntity | None = None,
            defending: LocalizedEntity | None = None,
            ) -> str:

        return self.lstr.format(**locals())




