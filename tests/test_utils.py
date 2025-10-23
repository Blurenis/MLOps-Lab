import pytest
from src import utils


# ---------- Tests pour multiply ----------

def test_multiply_basic():
    assert utils.multiply(2, 3) == 6
    assert utils.multiply(1, 2, 3, 4) == 24


def test_multiply_with_zero():
    assert utils.multiply(0, 5, 10) == 0
    assert utils.multiply(5, 0) == 0


def test_multiply_negative_numbers():
    assert utils.multiply(-2, 3) == -6
    assert utils.multiply(-2, -3) == 6


def test_multiply_single_argument():
    assert utils.multiply(7) == 7


def test_multiply_no_arguments():
    # Aucun argument => product démarre à 1 et ne change pas
    assert utils.multiply() == 1


# ---------- Tests pour divide ----------

def test_divide_basic():
    assert utils.divide(10, 2) == 5


def test_divide_multiple_args():
    # 100 / 2 / 5 = 10
    assert utils.divide(100, 2, 5) == 10


def test_divide_negative_numbers():
    assert utils.divide(-10, 2) == -5
    assert utils.divide(-10, -2) == 5


def test_divide_single_argument():
    # Diviser un seul nombre => il est retourné tel quel
    assert utils.divide(10) == 10


def test_divide_no_arguments():
    # Aucun argument => tu retournes None
    assert utils.divide() is None


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        utils.divide(10, 0)
        