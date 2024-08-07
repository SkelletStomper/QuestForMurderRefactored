import re
from typing import Union

from src.localization.localized_entity import LocalizedEntity

import logging
logger = logging.getLogger(__name__)


class LString:
    def __init__(self, lstr: str):
        lstr = lstr.replace("{atk.", "{attacking.")
        lstr = lstr.replace("{def.", "{defending.")
        lstr = lstr.replace("{pl.", "{player.")

        self._lstr = lstr
        self.les_allowed()

    def __eq__(self, other:  "String"):
        if isinstance(other, str):
            return self._lstr == other
        elif isinstance(other, LString):
            return self._lstr == other._lstr
        return False

    def les_allowed(self):
        """
        Checks for references to only allow references to special localized entities. This is to prevent access of random local variables.
        """

        allowed_les = ["attacking", "defending", "player", ""]
        le_pattern = r"{[a-zA-Z0-9\.\_]*}"
        les_used = re.findall(self._lstr, le_pattern)
        les_used = set({le[1:-1].split(".")[0] for le in les_used})

        for le in les_used:
            if le not in allowed_les:
                logger.error(f"{les_used} contains les not in {allowed_les}")
                lstr = self._lstr
                self._lstr = None
                raise ValueError(f"LString {lstr} contains forbidden les!")
        return True

    def parse(
            self,
            attacking: LocalizedEntity | None = None,
            defending: LocalizedEntity | None = None,
            ) -> str:

        result = self._lstr.format(**locals()).capitalize()
        logger.debug(f"Parsed {self._lstr} to {result}")
        return result



String = Union[str|LString]
