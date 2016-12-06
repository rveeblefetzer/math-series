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
