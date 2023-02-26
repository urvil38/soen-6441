N_TERM=11

# computing sin function using Taylor series expansion.
# https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
def sin(x,n=N_TERM):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i+1))/(factorial(2*i+1))
    return result

# computing cos function using Taylor series expansion.
# https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
def cos(x,n=N_TERM):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i))/(factorial(2*i))
    return result

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