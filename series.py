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
        return sum_series(n - 1) + sum_series(n - 2)


if __name__ == "__main__":
    # not sure quite yet what to put here.
    print (sum_series(10, 2, 3))
    print (sum_series(1, 5, 6))
    print (sum_series(2, 4, 8))
    print (sum_series(5, 1, 2))
