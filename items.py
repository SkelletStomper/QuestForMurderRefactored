
class Item:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight


class Weapon(Item):
    def __init__(self, inDict):
        Item.__init__(inDict["name"], inDict["weight"])
        self.damage = inDict["damage"]
        self.type = inDict["type"]
        self.attribute = inDict["attribute"]


class Offhand(Item):
    def __init__(self, inDict):
        Item.__init__(inDict["name"], inDict["weight"])
        self.damage = inDict["damage"]
        self.armor = inDict["armor"]
        self.heal = inDict["heal"]
        self.type = inDict["type"]
        self.attribute = inDict["attribute"]


class Armor(Item):
    def __init__(self, inDict):
        Item.__init__(inDict["name"], inDict["weight"])
        self.armor = inDict["armor"]

class Ability(Item):
    def __init__(self, inDict):
        Item.__init__(inDict["name"])
        self.duration = inDict["duration"]
        self.reload = inDict["reload"]
        self.description = inDict["description"]
