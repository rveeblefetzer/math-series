"""Fibonacci and Lucas Series Functions."""


def fibonacci(n):
    """Return the nth value of the fibonacci series."""
    if n < 1:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth value of the lucas series."""
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=1, second=2):
    """Return the nth value of a user initiated series."""
    if n < 1:
        return None
    elif n == 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)


if __name__ == "__main__":
    print('This module defines functions that implement mathematical series.')
    print('...')
    print('fibonacci(2) >>>', fibonacci(2))