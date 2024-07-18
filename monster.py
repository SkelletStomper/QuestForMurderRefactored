from attacks import AttackType

class Monster:
    def __init__(self, in_dict: dict):
        self.name: str = in_dict["name"]
        self.title: str = in_dict["title"]
        self.info: str = in_dict["info"]
        self.death_message: str = in_dict["death_message"]
        self.hp_max: int = in_dict["hp"]
        self.dmg: int = in_dict["dmg"]
        self.crit_modifier: float = in_dict["crit"]
        self.armor: int = in_dict["armor"]
        self.weaknesses: dict[AttackType, float] = in_dict["weaknesses"]
        self.typ: str = in_dict["typ"]
        self.flags: list[str] = in_dict["flags"]
