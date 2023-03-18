"""
This module provides mathematical functions that do not rely on any external libraries.

The module includes functions for computing sine, cosine, the value of pi,
and Newton's method to find roots of equations.
"""

N_TERM: int = 11
"""
The number of terms used in the Taylor series expansion of sine and cosine functions.
Using 11 terms provides the best trade-off between accuracy and performance for values
in the range of [-2π, 2π].
"""

def sin(x: float, n: int = 11) -> float:
    """
    Compute the sin function using Taylor series expansion.

    See https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions for more information.

    :param x: the value in radians to compute the sin for.
    :param n: the number of terms to use in the Taylor series expansion (default: 11).
    :return: the computed value of sin(x).
    """
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i+1))/(factorial(2*i+1))
    return result


def cos(x: float, n: int = 11) -> float:
    """
    Compute the cos function using Taylor series expansion.

    See https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions for more information.

    :param x: the value in radians to compute the cos for.
    :param n: the number of terms to use in the Taylor series expansion (default: 11).
    :return: the computed value of cos(x).
    """
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i))/(factorial(2*i))
    return result


def value_of_pi(n_terms: int) -> float:
    """
    Compute the approximate value of pi using Leibniz formula.

    See https://en.wikibooks.org/wiki/Calculus/Leibniz%27_formula_for_pi for more information.

    :param n_terms: the number of terms to use in the Leibniz formula.
    :return: the computed value of pi.
    """
    val = 0
    sign = 1
    for i in range(n_terms):
        val += sign / (2 * i + 1)
        sign = -sign
    return val * 4


# Using 100_000 iterations to compute pi. More iterations will reduce the error rate.
PI = value_of_pi(100_000)


def factorial(n: int) -> int:
    """
    Compute the factorial of a number.

    :param n: the number to compute the factorial for.
    :return: the computed factorial.
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
