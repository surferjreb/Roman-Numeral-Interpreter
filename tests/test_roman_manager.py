from roman_manager import RomanManager
import pytest


@pytest.fixture
def valid_input():
    pass


@pytest.fixture
def invalid_input():
    pass


@pytest.fixture
def rom_man():
    rm = RomanManager()
    return rm


def test_start_manager(rom_man, valid_input, invalid_input):
    pass
