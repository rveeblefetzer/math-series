"""Fibonacci and Lucas Series Functions."""


def fibonacci(n):
    """Return nth value of Fibonacci series."""
    result = [0]
    a, b = 0, 1
    while len(result) <= n:
        result.append(b)
        a, b = b, a + b
    return result[n - 1]


def lucas(n):
    """Return nth value of Fibonacci series."""
    result = [2]
    a, b = 2, 1
    while len(result) <= n:
        result.append(b)
        a, b = b, a + b
    return result[n - 1]


def sum_series(n, first=0, second=1):
    """Return nth value of custom series."""
    result = [first]
    a, b = first, second
    while len(result) <= n:
        result.append(b)
        a, b = b, a + b
    return result[n - 1]


if __name__ == "__main__":
    # not sure quite yet what to put here.
    print (fibonacci(2))
