import unittest

from areacalculator import square


class TestAreaCalculator(unittest.TestCase):
    def test_square_positive(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square(2.5), 6.25)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)


if __name__ == "__main__":
    unittest.main()
