"""Fibonacci and Lucas Series Functions."""


# def fibonacci(n):
#     """Return the nth value of the fibonacci series."""
#     if n < 1:
#         return None
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

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

# def lucas(n):
#     """Return the nth value of the lucas series."""
#     if n < 1:
#         return None
#     elif n == 1:
#         return 2
#     elif n == 2:
#         return 1
#     else:
#         return lucas(n - 1) + lucas(n - 2)


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


# def sum_series(n, first=1, second=2):
#     """Return the nth value of a user initiated series."""
#     if n < 1:
#         return None
#     elif n == 1:
#         return first
#     elif n == 2:
#         return second
#     else:
#         return sum_series(n - 1) + sum_series(n - 2)

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
