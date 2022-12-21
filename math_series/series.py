def finbonacci(n):
    """
    Returns the nth value in the finbonacci series.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas():
    """
    Returns the nth value in the lucas numbers.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n > 1:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    """
    The required parameter will determine which element in the series to print.
    The two optional parameters will have default values of 0 and 1 and will
    determine the first two values for the series to be produced.
    """
    if n == 0:
        return x
    if n == 1:
        return y
    if n > 1:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)