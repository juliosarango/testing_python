import pytest

from src.calculator import suma, resta, multiplicacion, division


def test_suma():
    assert suma(4, 5) == 9
    assert suma(4, 15) == 19


def test_resta():
    assert resta(10, 8) == 2
    assert resta(20, 8) == 12


def test_multiplicacion():
    assert multiplicacion(2, 4) == 8
    assert multiplicacion(6, 4) == 24


def test_division():
    assert division(40, 10) == 4
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
