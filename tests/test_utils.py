import pytest
from src.utils import add, subtract, multiply


def test_add_integers():
    assert add(1, 2, 3) == 6


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_add_negatifs():
    assert add(-2, 5, -3) == 0


def test_subtract_chain():
    assert subtract(10, 3, 2) == 5  # 10-3-2


def test_subtract_floats():
    assert subtract(1.0, 0.1) == pytest.approx(0.9)


@pytest.mark.parametrize(
    "args,expected",
    [
        ((0,), 0),  # un seul arg
        ((1_000_000, 1_000_000), 2_000_000),  # grands nombres
    ],
)
def test_add_param(args, expected):
    assert add(*args) == expected


def test_add_type_error():
    with pytest.raises(TypeError):
        add(1, "2")


def test_subtract_single_arg():
    assert subtract(5) == 5


def test_multiply_basic():
    assert multiply(2, 3, 4) == 24


def test_multiply_par_zero():
    assert multiply(7, 0, 5) == 0


def test_multiply_negatifs():
    assert multiply(-2, 3) == -6


def test_multiply_floats():
    assert multiply(0.1, 0.2) == pytest.approx(0.02)


def test_multiply_type_error():
    with pytest.raises(TypeError):
        multiply(2, "x")
