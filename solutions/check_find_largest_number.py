import unittest
from largest_number import largest_number  # Assuming your main function is in 'largest_number.py'

class TestLargestNumber(unittest.TestCase):

    def test_largest(self):
        numbers = [1, 2, 3, 4, 21, 12, 8]
        result = largest_number(numbers)
        self.assertEqual(result, 21)

if __name__ == "__main__":
    unittest.main()
