import pytest
from unittest.mock import patch
from src.localization.pronouns import PronounSet


# Sample JSON data for testing
sample_pronouns_data = {
    "she": {
        "subject": "she",
        "object": "her",
        "poss_adjective": "her",
        "possessive": "hers",
        "reflexive": "herself",
        "3rdS": True,
        "form": 3
    },
    "he": {
        "subject": "he",
        "object": "him",
        "poss_adjective": "his",
        "possessive": "his",
        "reflexive": "himself",
        "3rdS": True,
        "form": 3
    }
}


def test_pronoun_set_initialization():
    pronoun_data = sample_pronouns_data["she"]
    pronoun_set = PronounSet("she", pronoun_data)

    assert pronoun_set.subject == "she"
    assert pronoun_set.object == "her"
    assert pronoun_set.poss_adjective == "her"
    assert pronoun_set.possessive == "hers"
    assert pronoun_set.reflexive == "herself"
    assert pronoun_set.third_s is True
    assert pronoun_set.form == 3

