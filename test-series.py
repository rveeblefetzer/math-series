"""Test for fibonacci calculator function"""
import pytest

PARAMS_TABLE = [
        (10, 55),
        (5, 5),
        (12, 144)
        (15, 610),
        ]

@pytest.mark.parametrize('n, the_answer', PARAMS_TABLE)
def test_fibonacci():
    """Test for nth Fibonacci values."""
    from series import fibonacci
    assert fibonacci(n) == the_answer



