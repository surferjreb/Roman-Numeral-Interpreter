from roman_numerals import RomanNumerals


class RomanCalc:
    def __init__(self, numeral_list):
        self.rn = RomanNumerals()
        self._decimal_values = []
        self.numeral_list = numeral_list

    def calculate_value(self):
        prev_value = 0
        total = 0

        for value in self._decimal_values:
            if prev_value == 0:
                total += value

            elif value > prev_value:
                total -= prev_value
                total += (value - prev_value)

            else:
                total += value

            prev_value = value

        return total

    def find_letter_value(self):
        for letter in self.numeral_list:
            value = self.rn.roman_numerals.get(letter)
            self._decimal_values.append(value)
