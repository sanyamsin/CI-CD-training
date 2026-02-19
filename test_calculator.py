"""Tests unitaires pour la calculatrice."""
import pytest
from app import add, subtract, multiply, divide


# ========== Tests de add() ==========

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_mixed_numbers():
    assert add(-1, 1) == 0


def test_add_zeros():
    assert add(0, 0) == 0


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


# ========== Tests de subtract() ==========

def test_subtract_positive():
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def test_subtract_from_zero():
    assert subtract(0, 5) == -5


# ========== Tests de multiply() ==========

def test_multiply_positive():
    assert multiply(4, 3) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_multiply_negatives():
    assert multiply(-3, -4) == 12


def test_multiply_mixed():
    assert multiply(3, -4) == -12


# ========== Tests de divide() ==========

def test_divide_exact():
    assert divide(10, 2) == 5.0


def test_divide_decimal_result():
    result = divide(10, 3)
    assert round(result, 4) == 3.3333


def test_divide_negative():
    assert divide(-10, 2) == -5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_zero_by_number():
    assert divide(0, 5) == 0.0
