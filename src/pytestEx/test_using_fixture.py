
import pytest

from Utils import dictionary_fixture

@pytest.fixture(scope="session")
def fixture_modify_list():
     data = dictionary_fixture()
     data["Country"] = "USA"
     data["Profession"] = "Engineer"
     return data


def test_check_age_in_dictionary(fixture_modify_list):
    data = fixture_modify_list
    assert data["Age"] == 30
def test_check_city_in_dictionary(fixture_modify_list):
    data = fixture_modify_list
    assert data["City"] == "New York"
def test_check_country_in_dictionary(fixture_modify_list):
    data = fixture_modify_list
    assert data["Country"] == "USA"
def test_check_profession_in_dictionary(fixture_modify_list):
    data = fixture_modify_list
    assert data["Profession"] == "DDDDDDDEngineer"



