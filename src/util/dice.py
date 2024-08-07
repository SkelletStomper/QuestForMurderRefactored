import random


def d(sides: int):
    return random.randint(1, sides)


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"


class DiceSet:
    def __init__(self, die=None):
        if die is None:
            die = {}

        self.die: list[Dice] = []
        for sides, times in die.items():
            self.die += [Dice(sides) for _ in range(times)]

    def roll(self):
        return sum([dice.roll() for dice in self.die])

    def __repr__(self) -> str:
        return f"DiceSet(die={self.die})"
