

class Monster:
    def __init__(self, inDict):
        self.name = inDict["name"]
        self.title = inDict["title"]
        self.info = inDict["info"]
        self.deathMessage = inDict["death_message"]
        self.hpMax = inDict["hp"]
        self.dmg = inDict["dmg"]
        self.critModifier = inDict["crit"]
        self.armor = inDict["armor"]
        self.fireWeakness = inDict["fireWeakness"]
        self.typ = inDict["typ"]
        self.flags = inDict["flags"]
