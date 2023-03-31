import unittest
import math
import src.libmath as libmath
import src.root_approx as root_approx
import src.main as main

ACCEPTABLE_ERROR = 0.0001
a = 2.309878472457841
INITIAL_CASE = 1


class TestMathFunctions(unittest.TestCase):

    def test_sin(self):
        # Test sin function against math.sin for various values of x
        self.assertAlmostEqual(libmath.sin(0), math.sin(0))
        self.assertAlmostEqual(libmath.sin(math.pi/2), math.sin(math.pi/2))
        self.assertAlmostEqual(libmath.sin(math.pi), math.sin(math.pi))

    def test_cos(self):
        # Test cos function against math.cos for various values of x
        self.assertAlmostEqual(libmath.cos(0), math.cos(0))
        self.assertAlmostEqual(libmath.cos(math.pi/2), math.cos(math.pi/2))
        self.assertAlmostEqual(libmath.cos(math.pi), math.cos(math.pi))

    def test_value_of_pi(self):
        # Test value_of_pi function against math.pi for various number of terms
        self.assertAlmostEqual(libmath.value_of_pi(1000), math.pi, places=2)

    def test_factorial(self):
        # Test factorial function for various values of n
        self.assertEqual(libmath.factorial(0), 1)
        self.assertEqual(libmath.factorial(1), 1)
        self.assertEqual(libmath.factorial(5), 120)

    def test_newton_method(self):
        assert abs(a - root_approx.newton_method(main.func, main.func_derivative,
                   INITIAL_CASE)) < ACCEPTABLE_ERROR
