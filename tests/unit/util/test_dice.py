import pytest
import random
from src.util.dice import d, Dice, DiceSet


def test_d():
    # Test if d() returns a value within the correct range for 6-sided die
    result = d(6)
    assert 1 <= result <= 6

    # Test if d() returns a value within the correct range for 20-sided die
    result = d(20)
    assert 1 <= result <= 20


def test_dice_roll():
    dice = Dice(sides=6)

    # Test if Dice.roll() returns a value within the correct range
    result = dice.roll()
    assert 1 <= result <= 6


def test_diceset_roll():
    dice_set = DiceSet(die={6: 2, 20: 1})

    # Test if DiceSet.roll() returns a value within the correct range
    result = dice_set.roll()
    assert 3 <= result <= (6 * 2 + 20)


def test_diceset_empty():
    dice_set = DiceSet()

    # Test if DiceSet.roll() returns 0 when there are no dice
    result = dice_set.roll()
    assert result == 0
