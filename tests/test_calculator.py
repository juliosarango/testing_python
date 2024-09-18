import unittest
from src.calculator import suma, resta, multiplicacion, division


class CalculatorTest(unittest.TestCase):

    def test_suma(self):
        assert suma(2, 5) == 7

    def test_resta(self):
        assert resta(10, 5) == 5

    def test_multiplicacion(self):
        assert multiplicacion(2, 4) == 8

    def test_division(self):
        assert division(24, 3) == 8

        with self.assertRaises(ZeroDivisionError):
            division(10, 0)
