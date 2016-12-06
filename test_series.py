"""Test for fibonacci and related calculator functions."""
import pytest

FIBO_TABLE = [
        [10, 34],
        [9, 21],
        [11, 55],
        [15, 377],
        ]

LUCAS_TABLE = [
        [1, 2],
        [5, 7],
        [10, 76],
        [12, 199],
        [15, 843],
        ]


@pytest.mark.parametrize('n, the_answer', FIBO_TABLE)
def test_fibonacci(n, the_answer):
    """Test for nth Fibonacci values."""
    from series import fibonacci
    assert fibonacci(n) == the_answer


@pytest.mark.parametrize('n, the_answer', LUCAS_TABLE)
def test_lucas(n, the_answer):
    """Test for nth Fibonacci values."""
    from series import lucas
    assert lucas(n) == the_answer
