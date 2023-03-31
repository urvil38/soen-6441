import unittest
import math
from src.libmath import sin, cos, PI, factorial, value_of_pi
from src.root_approx import newton_method
from src.main import func, func_derivative

ACCEPTABLE_ERROR = 0.0001
a = 2.309878472457841
INITIAL_CASE = 1


class TestMathFunctions(unittest.TestCase):

    def test_sin(self):
        # Test sin function against math.sin for various values of x
        self.assertAlmostEqual(sin(0), math.sin(0))
        self.assertAlmostEqual(sin(math.pi/2), math.sin(math.pi/2))
        self.assertAlmostEqual(sin(math.pi), math.sin(math.pi))

    def test_cos(self):
        # Test cos function against math.cos for various values of x
        self.assertAlmostEqual(cos(0), math.cos(0))
        self.assertAlmostEqual(cos(math.pi/2), math.cos(math.pi/2))
        self.assertAlmostEqual(cos(math.pi), math.cos(math.pi))

    def test_value_of_pi(self):
        # Test value_of_pi function against math.pi for various number of terms
        self.assertAlmostEqual(value_of_pi(1000), math.pi, places=2)

    def test_factorial(self):
        # Test factorial function for various values of n
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_newton_method(self):
        assert abs(a - newton_method(func, func_derivative,
                   INITIAL_CASE)) < ACCEPTABLE_ERROR


if __name__ == '__main__':
    unittest.main()
