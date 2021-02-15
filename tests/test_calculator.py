import pytest

from calculator.calculator import Calculator

calculator = Calculator()


def test_add():
    assert calculator.add(3, 2) == 5
    assert calculator.add(1) == 6


def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(2) == 1


def test_multiply():
    assert calculator.multiply(3, 2) == 6
    assert calculator.multiply(2) == 12


def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(2) == 1.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(3, 0)


def test_take_root():
    assert calculator.take_root(27, 3) == 3
    assert calculator.take_root(4, 2) == 2
    assert calculator.take_root(9) == 3
    assert calculator.take_root(5, 0) == 0


def test_reset_memory():
    calculator.reset_memory()
    assert calculator.memory == 0
