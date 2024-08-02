import pytest
from unittest.mock import patch
from src.localization.pronouns import PronounSet, PronounProvider


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
    pronoun_set = PronounSet(pronoun_data)

    assert pronoun_set.subject == "she"
    assert pronoun_set.object == "her"
    assert pronoun_set.poss_adjective == "her"
    assert pronoun_set.possessive == "hers"
    assert pronoun_set.reflexive == "herself"
    assert pronoun_set.third_s is True
    assert pronoun_set.form == 3


def test_pronoun_provider():
    provider = PronounProvider()

    she = provider["3rd_she"]
    assert isinstance(she, PronounSet)
    assert she.subject == "she"
    assert she.object == "her"
    assert she.possessive == "hers"

    they = provider["3rd_they"]
    assert isinstance(they, PronounSet)
    assert they.subject == "they"
    assert they.poss_adjective == "their"
    assert they.reflexive == "themself"

