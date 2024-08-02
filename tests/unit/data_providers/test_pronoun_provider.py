from src.data_providers._pronoun_provider import PronounProvider, PronounSet



def test_pronoun_provider():
    read_data = {
        "3rd_she": {
            "json_type": "pronouns",
            "form": 3,
            "subject": "she",
            "object": "her",
            "poss_adjective": "her",
            "possessive": "hers",
            "reflexive": "herself",
            "3rdS": True
        },
        "3rd_they": {
            "json_type": "pronouns",
            "form": 3,
            "subject": "they",
            "object": "them",
            "poss_adjective": "their",
            "possessive": "theirs",
            "reflexive": "themself",
            "3rdS": False
        },
    }

    provider = PronounProvider(read_data)

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
