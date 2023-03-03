from libmath import cos, sin, PI, compute_alpha, func, func_derivative

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
