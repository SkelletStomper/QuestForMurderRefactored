import pytest
from src.data_providers import pronoun_provider as pp
from src.localization.localized_entity import LocalizedEntity


@pytest.fixture
def pronoun_set_she():
    return pp["3rd_she"]


@pytest.fixture
def pronoun_set_they():
    return pp["3rd_they"]


def test_localized_entity_initialization(pronoun_set_she):
    entity = LocalizedEntity(name="Olivia", title="Ms.", plural=False, pronouns=pronoun_set_she)

    assert entity._name == "Olivia"
    assert entity._title == "Ms."
    assert entity._plural is False
    assert entity._pronouns == pronoun_set_she


def test_localized_entity_properties(pronoun_set_she):
    entity = LocalizedEntity(name="Olivia", title="Ms.", plural=False, pronouns=pronoun_set_she)

    assert entity.subject == "she"
    assert entity.object == "her"
    assert entity.poss_adjective == "her"
    assert entity.possessive == "hers"
    assert entity.reflexive == "herself"
    assert entity.s == "s"
    assert entity.es == "es"
    assert entity.name == "Ms. Olivia"
    assert entity.owns == "Olivia's"


def test_localized_entity_properties_they(pronoun_set_they):
    entity = LocalizedEntity(name="Ziri", title="", plural=False, pronouns=pronoun_set_they)

    assert entity.s == ""
    assert entity.es == ""
    assert entity.name == "Ziri"
    assert entity.owns == "Ziri's"


def test_localized_entity_owns_with_s(plural_pronoun_set):
    entity = LocalizedEntity(name="James", title="", plural=False, pronouns=plural_pronoun_set)

    assert entity.owns == "James'"


@pytest.fixture
def plural_pronoun_set():
    return pp["3rd_plural"]


def test_localized_entity_owns_plural(plural_pronoun_set):
    entity = LocalizedEntity(name="James", title="", plural=True, pronouns=plural_pronoun_set)

    assert entity.owns == "James'"

