from libmath import cos, sin, PI

def func(alpha):
    return alpha - sin(alpha) - PI/2

def func_derivative(alpha):
    return 1 - cos(alpha)

# The equation "a – sin(a) = π/2" is a transcendental equation,
# which means that there is no algebraic solution for a in terms of elementary functions.
# using newton method to to find a numerical solution using iterative method.
# https://en.wikipedia.org/wiki/Newton%27s_method
def compute_alpha(guess):
    for _ in range(100):
        print(guess)
        guess -= func(guess)/func_derivative(guess)
    return guess

# starting with initial guess of 1.
INITIAL_CASE = 1
print("initial_guess: ", INITIAL_CASE)
a = compute_alpha(INITIAL_CASE)
print("pi: ", PI)
print("a: ", a)
print("error: {:.17f}".format(a - sin(a) - PI/2))
radius = int(input("please provide the radius: "))

# l = 2R(1 – cos(α/2))
l = 2 * radius * (1 - cos(a/2))
print("l: ", l)
