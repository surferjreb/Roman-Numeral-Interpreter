"""Validates Input and verifies the input is roman numeral format"""
from roman_numerals import RomanNumerals


class RomanValidator:
    def __init__(self):
        self.user_numerals = None
        self.roman = RomanNumerals()

    def validate_numerals(self, user_input):
        # check_letters = re.compile('[CDILMVX]+')
        user_numerals = []
        p_letter = None
        count = 0
        try:
            for letter in user_input:
                if letter in self.roman.roman_numerals.keys():
                    if p_letter is None:
                        count = 1
                        p_letter = letter
                    elif letter == p_letter:
                        count += 1
                        p_letter = letter
                    else:
                        count = 1
                        p_letter = letter

                    if count > 3:
                        raise TypeError()
                    user_numerals.append(letter)
                else:
                    raise TypeError()

        except Exception as err:
            return err

        return user_numerals

    def validate_input(self, user_input):
        if user_input.isalpha():
            valid_input = self.validate_numerals(user_input.upper())
        else:
            return TypeError("Only Roman Numeral Letters")

        return valid_input

    def run_validater(self, user_input):
        try:
            self.user_numerals = self.validate_input(user_input)
        except Exception as err:
            return err

        return self.user_numerals

    # check user input is a string
    # check string is roman numerals
    # check that letters do not repeat more than three times
    #
