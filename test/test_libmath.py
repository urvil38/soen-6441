import math
from src.libmath import sin, cos, PI, factorial
from src.root_approx import newton_method
from src.main import func, func_derivative

ACCEPTABLE_ERROR = 0.0001
a = 2.309878472457841
INITIAL_CASE = 1


def test_libmath_sin():
    assert abs(1-sin(PI/2)) < ACCEPTABLE_ERROR
    assert abs(0.5-sin(PI/6)) < ACCEPTABLE_ERROR


def test_libmath_cos():
    assert abs(0-cos(PI/2)) < ACCEPTABLE_ERROR
    assert abs(0.5-cos(PI/3)) < ACCEPTABLE_ERROR


def test_libmath_pi():
    assert abs(math.pi-PI) < ACCEPTABLE_ERROR


def test_libmath_factorial():
    assert factorial(4) == 24
    assert factorial(6) == 720


def test_newton_method():
    assert abs(a - newton_method(func, func_derivative,
               INITIAL_CASE)) < ACCEPTABLE_ERROR
