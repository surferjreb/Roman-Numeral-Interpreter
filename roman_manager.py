from roman_validater import RomanValidator
from roman_calc import RomanCalc


class RomanManager:
    def __init__(self):
        self.roman_valid = RomanValidator()

    def start_manager(self, user_input):
        try:
            user_numerals = self.roman_valid.run_validater(user_input)
            rom_calc = RomanCalc(user_numerals)
            rom_calc.find_letter_value()
            user_total = rom_calc.calculate_value()
            return user_total
        except Exception as err:
            return err
