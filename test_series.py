"""Test for fibonacci and related calculator functions."""
import pytest

FIB_PARAMS_TABLE = [
    [10, 34],
    [5, 3],
    [12, 89],
    [2, 1],
    [1, 0],
    [8, 13],
    [13, 144]
]


@pytest.mark.parametrize("n, the_answer", FIB_PARAMS_TABLE)
def test_fibonacci(n, the_answer):
    """Test for nth Fibonacci values."""
    from series import fibonacci
    assert fibonacci(n) == the_answer


LUCAS_PARAMS_TABLE = [
    [1, 2],
    [2, 1],
    [3, 3],
    [4, 4],
    [5, 7],
    [6, 11],
    [7, 18],
    [8, 29],
    [9, 47],
    [10, 76],
    [11, 123]
]


@pytest.mark.parametrize("n, the_answer", LUCAS_PARAMS_TABLE)
def test_lucas(n, the_answer):
    """Test for nth lucas values."""
    from series import lucas
    assert lucas(n) == the_answer

SUM_PARAMS_TABLE = [
    [10, 2, 3, 89],
    [1, 5, 6, 5],
    [2, 4, 8, 8],
    [5, 1, 2, 8]
]


@pytest.mark.parametrize("n, first, second, the_answer", SUM_PARAMS_TABLE)
def test_sum(n, first, second, the_answer):
    """Test for nth sum values with input parameters."""
    from series import sum_series
    assert sum_series(n) == the_answer
