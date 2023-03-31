import unittest
from src.root_approx import newton_method

class TestNewtonMethod(unittest.TestCase):

    def test_numeric_x0(self):
        # Test that ValueError is raised if x0 is not numeric.
        with self.assertRaises(ValueError):
            newton_method(lambda x: x**2, lambda x: 2*x, 'a')

    def test_positive_epsilon(self):
        # Test that ValueError is raised if epsilon is not positive.
        with self.assertRaises(ValueError):
            newton_method(lambda x: x**2, lambda x: 2*x, 1, epsilon=-0.01)

    def test_divide_by_zero(self):
        # Test that None is returned and "divide by zero" error message is printed if func_prime(x0) = 0.
        self.assertIsNone(newton_method(lambda x: x**2, lambda x: 0, 1))

    def test_correct_result(self):
        # Test that the function returns the correct root value.
        self.assertAlmostEqual(newton_method(lambda x: x**2 - 2, lambda x: 2*x, 1), 1.41421356, places=5)
