import numpy as np
import matplotlib.pyplot as plt

N_TERM=11
# NOTE: the precision of the result will depend on the number of iterations used in the series,
# the higher the number of terms, the more accurate the result will be but the execution time
# will increase as well.
# computing the approximate value of pi using Leibniz formula.
def value_of_pi(n_terms):
    val = 0
    sign = 1
    for i in range(n_terms):
        val += sign / (2 * i + 1)
        sign = -sign
    return val * 4

# using 100_000 iterations
# more iterations will reduce the error rate.
PI = value_of_pi(100_000)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# computing sin function using Taylor series expansion.
# https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
def sin(x,n):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i+1))/(factorial(2*i+1))
    return result

# computing cos function using Taylor series expansion.
# https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
def cos(x,n):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i))/(factorial(2*i))
    return result

def func(alpha):
    return alpha - sin(alpha,N_TERM) - PI/2

def func_derivative(alpha):
    return 1 - cos(alpha,N_TERM)

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
print("error: {:.17f}".format(a - sin(a,N_TERM) - PI/2))
radius = int(input("please provide the radius: "))

# l = 2R(1 – cos(α/2))
l = 2 * radius * (1 - cos(a/2,N_TERM))
print("l: ", l)

TERM=N_TERM
fn=cos
fnn=np.cos
angles = np.arange(-2*np.pi,2*np.pi,0.1)
p_fn = fnn(angles)

fig, ax = plt.subplots()
ax.plot(angles,p_fn)

# add lines for between 1 and 6 terms in the Taylor Series
for i in range(1,TERM+1):
    t_fn = [fn(angle,i) for angle in angles]
    ax.plot(angles,t_fn,linestyle='dotted')

ax.set_ylim([-7,4])

# set up legend
legend_lst = ['cos() function']
for i in range(1,TERM+1):
    legend_lst.append(f'{i} terms')
ax.legend(legend_lst, loc='best')
plt.show()
