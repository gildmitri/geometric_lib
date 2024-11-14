import unittest
from circle import area, perimeter
import math


class TestCircle(unittest.TestCase):
    def test_area(self):
        # Arrange (given)
        radius = 1

        # Act (when)
        result = area(radius)

        # Assert (then)
        self.assertEqual(result, math.pi)

    def test_area_zero(self):
        radius = 0

        result = area(radius)

        self.assertEqual(result, 0)

    def test_perimeter(self):
        radius = 1

        result = perimeter(radius)

        self.assertEqual(result, 2 * math.pi)

    def test_perimeter_zero(self):
        radius = 0

        result = perimeter(radius)

        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
