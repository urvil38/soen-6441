import sys
from libmath import cos, sin, PI, newton_method
from encoder import generate_xml_response, generate_csv_response

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


def compute_length(radius: float, alpha: float) -> float:
    """
    Computes the length of an arc of a circle given its radius and central angle in radians.

    Args:
        radius: A float representing the radius of the circle.
        alpha: A float representing the central angle in radians.

    Returns:
        A float representing the length of the arc.

    """
    return 2 * radius * (1 - cos(alpha/2))


def interactive(alpha: float) -> None:
    """
    A function that prompts the user to input a radius and calculates the corresponding length
    based on a given value of alpha.

    Args:
        alpha (float): The value of alpha to use in the length calculation.

    Returns:
        None
    """
    while True:
        try:
            radius = int(input("Please provide the radius: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # l = 2R(1 – cos(α/2))
    length = compute_length(radius, alpha)

    print('alpha:  {}'.format(alpha))
    print('radius: {}'.format(radius))
    print('length: {}'.format(length))


if __name__ == "__main__":
    # starting with initial guess of 1.
    INITIAL_GUESS = 1

    alpha = compute_alpha(INITIAL_GUESS)
    if alpha is None:
        print("cannot compute value of alpha")
        sys.exit(1)

    if len(sys.argv) > 2 and sys.argv[1] == "generate":
        R = [12, 14, 17, 23, 18, 29, 34, 38, 42, 41]

        records = []
        for radius in R:
            records.append((radius, compute_length(radius, alpha)))

        if sys.argv[2] == "xml":
            print(generate_xml_response(INITIAL_GUESS, alpha, records), end='')
        elif sys.argv[2] == "csv":
            print(generate_csv_response(alpha, records), end='')
    else:
        interactive(alpha)
