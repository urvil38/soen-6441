from libmath import cos, sin, PI, newton_method

def func(alpha: float) -> float:
    """
    Computes the function f(alpha) = alpha - sin(alpha) - PI/2.

    Args:
        alpha: A numeric value representing the input for the function.

    Returns:
        A numeric value representing the output of the function.

    """
    return alpha - sin(alpha) - PI/2

def func_derivative(alpha: float) -> float:
    """
    Computes the derivative of the function f(alpha) = alpha - sin(alpha) - PI/2.

    Args:
        alpha: A numeric value representing the input for the function.

    Returns:
        A numeric value representing the output of the derivative.

    """
    return 1 - cos(alpha)

def compute_alpha(initial_guess: float) -> float:
    """
    Computes the value of alpha using Newton's method with an initial guess.

    Args:
        initial_guess: A numeric value representing the initial guess for alpha.

    Returns:
        A numeric value representing the calculated value of alpha.

    """
    return newton_method(func, func_derivative, initial_guess)


# starting with initial guess of 1.
INITIAL_GUESS = 1
print("initial_guess: ", INITIAL_GUESS)
a = compute_alpha(INITIAL_GUESS)
print("pi: ", PI)
print("a: ", a)

while True:
    try:
        radius = int(input("Please provide the radius: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# l = 2R(1 – cos(α/2))
l = 2 * radius * (1 - cos(a/2))
print("l: ", l)
