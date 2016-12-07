"""Fibonacci and Lucas Series Functions."""


def fibonacci(n):
    """Return nth value of Fibonacci series."""
    idx = 0
    result = [0]
    a, b = 0, 1
    while idx <= n:
        result.append(b)
        a, b = b, a + b
        idx += 1
    return result[n - 1]


def lucas(n):
    """Return nth value of Fibonacci series."""
    idx = 0
    result = [2]
    a, b = 2, 1
    while idx <= n:
        result.append(b)
        a, b = b, a + b
        idx += 1
    return result[n - 1] 



def sum_series(n, first = 0, second = 1):
     """Return nth value of custom series."""

    idx = 0
    result = [first]
    a, b = first, second
    while idx <= n
        result.append(b)
        a, b = b, a + b
        idx += 1
    return result[n - 1]


if __name__ == "__main__":
    # not sure quite yet what to put here.
    print (fibonacci(2))
