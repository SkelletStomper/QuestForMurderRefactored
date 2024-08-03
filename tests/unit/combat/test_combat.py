import pytest
from unittest.mock import MagicMock, patch

from src.combat.combat_basics import attack_dodged


# Test for attack_dodged function
@patch("src.util.dice.d")
def test_attack_dodged(mock_dice):
    # Test case where dice_dodge is 1 (always misses)
    mock_dice.side_effect = [1]
    assert attack_dodged(accuracy=5, dodge=3) is False

    # Test case where dice_dodge is 8 (always hits)
    mock_dice.side_effect = [8]
    assert attack_dodged(accuracy=5, dodge=3) is True

    # Test case where dice_dodge is between 1 and 8
    mock_dice.side_effect = [4, 3]
    assert attack_dodged(accuracy=5, dodge=3) is False

    mock_dice.side_effect = [4, 3]
    assert attack_dodged(accuracy=5, dodge=6) is True

