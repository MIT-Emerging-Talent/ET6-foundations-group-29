import unittest
from even_odd_checker import check_even_or_odd  # Import the function to be tested

class TestEvenOddChecker(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(check_even_or_odd(4), "even")

    def test_odd_number(self):
        self.assertEqual(check_even_or_odd(5), "odd")

    def test_zero(self):
        self.assertEqual(check_even_or_odd(0), "even")

    def test_negative_even(self):
        self.assertEqual(check_even_or_odd(-2), "even")

    def test_negative_odd(self):
        self.assertEqual(check_even_or_odd(-3), "odd")

if __name__ == '__main__':
    unittest.main()
