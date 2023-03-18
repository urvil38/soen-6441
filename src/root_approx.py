"""
The module includes function for computing roots of equations using Newton's method.
"""
from typing import Callable

def newton_method(func: Callable[[float], float],
                  func_prime: Callable[[float], float],
                  x0: float,
                  epsilon: float = 0.0001) -> float:
    """
    Compute the value of alpha using Newton's method.

    Args:
        func: A callable function that represents the equation for which we want to find the root.
        func_prime: A callable function that represents the derivative of `func`.
        x0: The initial guess value of the root.
        epsilon: The desired accuracy of the root.

    Returns:
        The calculated root value of `f` using Newton's method.

    Raises:
        ValueError: If `x0` is not a numeric value or if `epsilon` is not a positive numeric value.

    """
    # Check if x0 is numeric.
    if not isinstance(x0, (int, float)):
        raise ValueError("x0 must be a numeric value")

    # Check if epsilon is positive.
    if epsilon <= 0:
        raise ValueError("epsilon must be a positive numeric value")

    try:
        x1 = x0 - func(x0) / func_prime(x0)
    except ZeroDivisionError:
        print("ERROR: divide by zero, func_prime cannot be result in zero")
        return None

    while abs(x1 - x0) >= epsilon:
        x0 = x1
        try:
            x1 = x0 - func(x0) / func_prime(x0)
        except ZeroDivisionError:
            print("ERROR: divide by zero, func_prime cannot be result in zero")
            return None

    return x1
