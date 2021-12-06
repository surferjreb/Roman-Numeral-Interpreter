from roman_validater import RomanValidator
import pytest


@pytest.fixture
def valid_u_input():
    valid_input1 = 'CDXVI'
    valid_input2 = 'III'
    valid_input3 = 'XVIII'
    return (valid_input1, valid_input2, valid_input3)


@pytest.fixture
def invalid_u_input():
    non_alpha = 'IV67DM'
    non_roman = 'ABCMHJI'
    bad_roman = 'IIII'
    return (non_alpha, non_roman, bad_roman)


@pytest.fixture
def validator():
    rv = RomanValidator()
    return rv


def test_constructor():
    rv = RomanValidator()
    assert isinstance(rv, object)


def test_validate_input(valid_u_input, invalid_u_input, validator):
    valid_input = validator.validate_input(valid_u_input[0])
    invalid_input = validator.validate_input(invalid_u_input[0])
    assert isinstance(valid_input, list)
    assert type(invalid_input) is TypeError


def test_validate_numerals(valid_u_input, invalid_u_input, validator):
    valid_numerals = validator.validate_numerals(valid_u_input[0])
    non_valid = validator.validate_numerals(invalid_u_input[1])
    assert isinstance(valid_numerals, list)
    assert type(non_valid) is TypeError


def test_run_validater(valid_u_input, invalid_u_input, validator):
    valid_test1 = validator.run_validater(valid_u_input[0])
    valid_test2 = validator.run_validater(valid_u_input[1])
    valid_test3 = validator.run_validater(valid_u_input[2])
    invalid_test1 = validator.run_validater(invalid_u_input[0])
    invalid_test2 = validator.run_validater(invalid_u_input[1])
    assert isinstance(valid_test1, list)
    assert isinstance(valid_test2, list)
    assert isinstance(valid_test3, list)
    assert type(invalid_test1) is TypeError
    assert type(invalid_test2) is TypeError
