import math

def f(a):
    return a - math.sin(a) - math.pi/2

def f_derivative(a):
    return 1 - math.cos(a)

def compute_alpha(guess):
    for i in range(100):
        guess -= f(guess)/f_derivative(guess)
    return guess

a = compute_alpha(1)
print("a: ", a)
radius = int(input("redius of the circles: "))

# l = 2R(1 – cos(α/2)), 
l = 2 * radius * (1 - math.cos(a/2))
print("l: ", l)