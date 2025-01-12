# test_check_even_or_odd.py
import unittest
from even_odd_checker import check_even_or_odd


class TestCheckEvenOrOdd(unittest.TestCase):

    def test_even_number(self):
        result = check_even_or_odd(4)
        self.assertEqual(result, "even")

    def test_odd_number(self):
        result = check_even_or_odd(3)
        self.assertEqual(result, "odd")

    def test_zero(self):
        result = check_even_or_odd(0)
        self.assertEqual(result, "even")

    def test_negative_even_number(self):
        result = check_even_or_odd(-2)
        self.assertEqual(result, "even")

    def test_negative_odd_number(self):
        result = check_even_or_odd(-3)
        self.assertEqual(result, "odd")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_even_or_odd("not_a_number")


if __name__ == "__main__":
    unittest.main()
