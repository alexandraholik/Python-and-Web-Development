import pytest
@pytest.mark.parametrize("age, voting_age, result", [
    (18, 18, True),
    (99, 18, True),
    (15, 18, False),
])

def test_can_vote(age, voting_age, result):
    person = age_exercise.Person(age)
    assert person.can_vote(voting_age) == result

@pytest.mark.parametrize("age, years_remaining", [
    (70, 0),
    (1, 64),
])

def test_years_till_retirement(age, years_remaining):
    person = age_exercise.Person(age)
    assert person.year_until_retirement() == years_remaining

@pytest.mark.parametrize("age, years_remaining", [
    (20, "40"),
    (1, "59"),
])

def test_years_till_preretirement(age, years_remaining):
    person = age_exercise.Person(age)
    assert person.pre_retirement() == years_remaining

@pytest.mark.parametrize("age, drinking_age, result", [
    (19, 18, True),
    (25, 21, True),
])

def test_can_drink(age, drinking_age, result):
    person = age_exercise.Person(age)
    assert person.legal_drinking_age(drinking_age) == result