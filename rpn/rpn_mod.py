"""A simple rpn module
   This could be extended or edited to suit ones needs.  Currently takes in a
   equation as a list of strings.
   by: James R. E. Brown
"""


import operator
import re


class RpnMod:
    def __init__(self):
        self._numerals = []
        self.check_ops = re.compile('[\+\-\*/]+')

    def calculate(self, eq):
        try:
            self._read_equation(eq)
        except Exception as err:
            print('Check your input and try again.\n',
                  'Error: {}'.format(type(err)))

    def _read_equation(self, eq):
        for value in eq:
            if value.isdigit():
                self._numerals.append(int(value))
            elif self.check_ops.match(value):
                if len(self._numerals) >= 2:
                    ans = self._run_operation(value)
                    self._numerals.append(ans)

            else:
                raise TypeError

    def _run_operation(self, op):
        ans = None
        
        if op == '+':
            ans = operator.add(self._numerals.pop(), self._numerals.pop())
        elif op == '-':
            ans = operator.sub(self._numerals.pop(-2),
                               self._numerals.pop())
        elif op == '*':
            ans = operator.mul(self._numerals.pop(), self._numerals.pop())
        elif op == '/':
            ans = operator.floordiv(self._numerals(-2),
                                    self._numerals.pop())
        else:
            ans = 'not an operation'

        return ans
