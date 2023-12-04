import unittest

# The function to be tested
def add_numbers(a, b):
    return a + b

# The test case class
class TestAddNumbers(unittest.TestCase):

    # Test case for the add_numbers function
    def test_add_numbers(self):
        # Test with positive numbers
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

        # Test with negative numbers
        result = add_numbers(-2, 7)
        self.assertEqual(result, 5)

        # Test with zero
        result = add_numbers(0, 10)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
