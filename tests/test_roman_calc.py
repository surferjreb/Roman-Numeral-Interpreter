from roman_calc import RomanCalc
import pytest


@pytest.fixture
def input():
    decimal_value = 416
    rn_input = 'CDXVI'
    numercal_list = ['C', 'D', 'X', 'V', 'I']
    value_list = [100, 500, 10, 5, 1]
    return (decimal_value, rn_input, numercal_list, value_list)


def test_constructor(input):
    numerical_list = input[1].split
    rom_calc = RomanCalc(numerical_list)
    assert isinstance(rom_calc, object)


def test_calculate_value(input):
    rn_list = input[2]
    rom_calc = RomanCalc(rn_list)
    rom_calc.find_letter_value()
    rn_total = rom_calc.calculate_value()
    assert type(rn_total) is int
    assert rn_total == input[0]
