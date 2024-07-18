from attack import Attack, WeaknessSet
from flag import flagProvider
import json

class Monster:
    def __init__(self, in_dict: dict):
        self.name: str = in_dict["name"]
        self.title: str = in_dict["title"]
        self.info: str = in_dict["info"]
        self.death_messages: list[str] = in_dict["death_messages"]
        self.hp_max: int = in_dict["hp"]
        self.dmg: int = in_dict["dmg"]
        self.crit_modifier: float = in_dict["crit"]
        self.armor: int = in_dict["armor"]
        self.weaknesses  = WeaknessSet(in_dict["weaknesses"])
        self.typ: str = in_dict["typ"]

        self.flags = [flagProvider[flag_name] for flag_name in in_dict["flags"]]


    def calculate_dmg_factor(self, attack: Attack) -> float:
        dmg = attack.dmg
        dmg *= self.weaknesses.attack_factor(attack)
        for flag in self.flags:
            dmg *= flag.weaknesses.attack_factor(attack)

        return dmg


class MonsterProvider:
    def __init__(self):

        with open("./json/monsters.json", "r") as f:
            json_dict = json.load(f)

        self.monsters = {monster_name: Monster(monster_data) for monster_name, monster_data in json_dict.items()}
        print(self.monsters)

    def __getitem__(self, value) -> Monster:
        return self.monsters[value]

monsterProvider = MonsterProvider()