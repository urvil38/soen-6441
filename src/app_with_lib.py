import math

def func(alpha):
    return alpha - math.sin(alpha) - math.pi/2

def f_derivative(alpha):
    return 1 - math.cos(alpha)

def compute_alpha(guess):
    for _ in range(100):
        guess -= func(guess)/f_derivative(guess)
    return guess

a = compute_alpha(1)
print("a: ", a)
radius = int(input("redius of the circles: "))

# l = 2R(1 – cos(α/2))
l = 2 * radius * (1 - math.cos(a/2))
print("l: ", l)
