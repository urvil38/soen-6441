import sys
import math
import root_approx
import encoder

def func(alpha: float) -> float:
    """
    Computes the function f(alpha) = alpha - math.sin(alpha) - math.pi/2.

    Args:
        alpha: A numeric value representing the input for the function.

    Returns:
        A numeric value representing the output of the function.

    """
    return alpha - math.sin(alpha) - math.pi/2


def func_derivative(alpha: float) -> float:
    """
    Computes the derivative of the function f(alpha) = alpha - math.sin(alpha) - math.pi/2.

    Args:
        alpha: A numeric value representing the input for the function.

    Returns:
        A numeric value representing the output of the derivative.

    """
    return 1 - math.cos(alpha)


def compute_alpha(initial_guess: float) -> float:
    """
    Computes the value of alpha using Newton's method with an initial guess.

    Args:
        initial_guess: A numeric value representing the initial guess for alpha.

    Returns:
        A numeric value representing the calculated value of alpha.

    """
    return root_approx.newton_method(func, func_derivative, initial_guess)


def compute_length(radius: float, alpha: float) -> float:
    """
    Computes the length of an arc of a circle given its radius and central angle in radians.

    Args:
        radius: A float representing the radius of the circle.
        alpha: A float representing the central angle in radians.

    Returns:
        A float representing the length of the arc.

    """
    return 2 * radius * (1 - math.cos(alpha/2))


def interactive(alpha: float, intital_guess: float, output_type: str) -> None:
    """
    A function that prompts the user to input a radius and calculates the corresponding length
    based on a given value of alpha.

    Args:
        alpha (float): The value of alpha to use in the length calculation.
        initial_guess (float): A numeric value representing the initial guess for alpha.
        output_type (str): Type of output response. Value can be xml or csv or None.

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

    record = [(radius, length)]
    if output_type == "csv":
        print(encoder.generate_csv_response(alpha, record), end='')
    elif output_type == "xml":
        print(encoder.generate_xml_response(intital_guess, alpha, record), end='')
    else:
        print('alpha:  {}'.format(alpha))
        print('radius: {}'.format(radius))
        print('length: {}'.format(length))


def main() -> None:
    # starting with initial guess of 1.
    INITIAL_GUESS = 1
    argv = sys.argv

    alpha = compute_alpha(INITIAL_GUESS)
    if alpha is None:
        print("cannot compute value of alpha")
        sys.exit(1)

    if len(argv) > 2 and argv[1] == "generate":
        R = [12, 14, 17, 23, 18, 29, 34, 38, 42, 41]

        records = []
        for radius in R:
            records.append((radius, compute_length(radius, alpha)))

        if argv[2] == "xml":
            print(encoder.generate_xml_response(INITIAL_GUESS, alpha, records), end='')
        elif argv[2] == "csv":
            print(encoder.generate_csv_response(alpha, records), end='')
    else:
        OUTPUT_TYPE = None
        if len(argv) > 1:
            OUTPUT_TYPE = argv[1]
        interactive(alpha, INITIAL_GUESS, OUTPUT_TYPE)

if __name__ == "__main__":
    main()
