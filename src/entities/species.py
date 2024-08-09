from src.base.types import WeaknessSet

from enum import Enum


class BodyPart(Enum):
    HEAD = "HEAD"
    CHEST = "CHEST"
    LEG = "LEG"
    FOOT = "FOOT"
    ARM = "ARM"
    HAND = "HAND"
    EYE = "EYE"
    WING = "WING"
    HEART = "HEART"
    BRAIN = "BRAIN"
    TAIL = "TAIL"


class Anatomy:
    def __init__(self, in_dict: dict) -> None:
        self.parts: dict[BodyPart, int] = {body_part: 0 for body_part in BodyPart}

        for body_part, count in in_dict.items():
            enum_part = BodyPart(body_part)
            self.parts[enum_part] = count

    def __repr__(self) -> str:
        str_list = [f"{part.value}={count}" for part, count in self.parts.values() if part > 0]

        return f"Anatomy({', '.join(str_list)})"


class Species:
    inherit_string = "inherit"

    def __init__(self, species_id: str, in_dict: dict) -> None:
        self.id = species_id
        self.subspecies_of = in_dict["subspecies_of"]

        self.description = in_dict["description"]

        self.anatomy = in_dict["anatomy"]

        self.vital_organs: list[str] = in_dict["vital_organs"]

        self.blood: str = in_dict["blood"]
        self.skin = in_dict["skin"]

        self.flags: list[str] = in_dict["flags"]

        self.weaknesses = in_dict["weaknesses"]

    def _prepare_not_inherited(self) -> None:
        from src.data_providers import flag_provider as fp, armat_provider as amp
        from src.items.armor import ArmorMaterial

        inherit = self.inherit_string

        if self.anatomy != inherit and isinstance(self.anatomy, dict):
            self.anatomy = Anatomy(self.anatomy)

        if inherit not in self.flags and str in [type(f) for f in self.flags]:
            self.flags = [fp(flag_str) for flag_str in self.flags]

        if not isinstance(self.skin, ArmorMaterial):
            self.skin = amp[self.skin]

        if self.weaknesses != inherit and isinstance(self.weaknesses, dict):
            self.weaknesses = WeaknessSet(self.weaknesses)

    def _full_fledged(self) -> bool:
        inherit = self.inherit_string
        if self.anatomy == inherit:
            return False

        if inherit in self.vital_organs:
            return False

        if self.blood == inherit:
            return False

        if self.skin == inherit:
            return False

        if inherit in self.flags:
            return False

        if self.weaknesses == inherit:
            return False

        return True

    def _inherit(self, sp): #SP is the SpeciesProvider
        inherit = self.inherit_string
        parent: "Species" = sp[self.subspecies_of]
        if not parent._full_fledged():
            raise RuntimeError("Can only inherit from Full-Fledged parent")

        if self.anatomy == inherit:
            self.anatomy = parent.anatomy

        if inherit in self.vital_organs:
            parent_vitals = parent.vital_organs
            self.vital_organs.remove(inherit)
            self.vital_organs = parent_vitals + self.vital_organs

        if self.blood == inherit:
            self.blood = parent.blood

        if self.skin == inherit:
            self.skin = parent.skin

        if inherit in self.flags:
            parent_flags = parent.flags
            self.flags.remove(inherit)
            self.flags = parent_flags + self.vital_organs

        if self.weaknesses == inherit:
            return False

    def __repr__(self) -> str:
        return (f"Species(id={self.id}, subspecies_of={self.subspecies_of}, description={self.description}, "
                f"anatomy={self.anatomy}, vital_organs={self.vital_organs}, blood={self.blood}, skin={self.skin},"
                f"flags={self.flags}, weaknesses={self.weaknesses})")
