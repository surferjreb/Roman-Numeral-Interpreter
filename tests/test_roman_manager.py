from roman_manager import RomanManager
import pytest


@pytest.fixture
def valid_input():
    valid_in = {"IIII": 4,
                "XIV": 14,
                "CDC": 500,
                "CDXIV": 414,
                "MMMMDCCCCLXXXXVIIII": 4999,
                "IIV": 5,
                "IIIX": 11,
                }
    return valid_in


@pytest.fixture
def invalid_input():
    invalid_in = ["IABC",
                  "487IX3",
                  "^&*(1T",
                  "//a"
                  ]
    return invalid_in


@pytest.fixture
def rom_man():
    rm = RomanManager()
    return rm


def test_start_manager(rom_man, valid_input, invalid_input):
    for key, value in valid_input.items():
        u_value = rom_man.start_manager(key)
        assert u_value == value

    for value in invalid_input:
        u_value = rom_man.start_manager(value)
        assert type(u_value) is TypeError
