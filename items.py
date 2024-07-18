
class Item:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight


class Weapon(Item):
    def __init__(self, in_dict):
        Item.__init__(in_dict["name"], in_dict["weight"])
        self.damage = in_dict["damage"]
        self.type = in_dict["type"]
        self.attribute = in_dict["attribute"]


class Offhand(Item):
    def __init__(self, in_dict):
        Item.__init__(in_dict["name"], in_dict["weight"])
        self.damage = in_dict["damage"]
        self.armor = in_dict["armor"]
        self.heal = in_dict["heal"]
        self.type = in_dict["type"]
        self.attribute = in_dict["attribute"]


class Armor(Item):
    def __init__(self, in_dict):
        Item.__init__(in_dict["name"], in_dict["weight"])
        self.armor = in_dict["armor"]

class Ability(Item):
    def __init__(self, in_dict):
        Item.__init__(name = in_dict["name"])
        self.duration = in_dict["duration"]
        self.reload = in_dict["reload"]
        self.description = in_dict["description"]
