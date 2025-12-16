import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class CircleTest(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_normal(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_area_large(self):
        self.assertAlmostEqual(circle_area(10), 314.1592653589793)

    def test_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(circle_perimeter(3), 18.84955592153876)

    def test_perimeter_large(self):
        self.assertAlmostEqual(circle_perimeter(10), 62.83185307179586)

class SquareTest(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_area_normal(self):
        self.assertEqual(square_area(5), 25)

    def test_area_large(self):
        self.assertEqual(square_area(100), 10000)

    def test_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_perimeter_large(self):
        self.assertEqual(square_perimeter(100), 400)

class RectangleTest(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(rectangle_area(10, 0), 0)
        self.assertEqual(rectangle_area(0, 10), 0)

    def test_area_normal(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_area_large(self):
        self.assertEqual(rectangle_area(100, 200), 20000)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(0, 10), 20)
        self.assertEqual(rectangle_perimeter(10, 0), 20)

    def test_perimeter_normal(self):
        self.assertEqual(rectangle_perimeter(4, 5), 18)

    def test_perimeter_large(self):
        self.assertEqual(rectangle_perimeter(100, 200), 600)

class TriangleTest(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 10), 0)
        self.assertEqual(triangle_area(10, 0), 0)

    def test_area_normal(self):
        self.assertEqual(triangle_area(6, 4), 12.0)

    def test_area_large(self):
        self.assertEqual(triangle_area(100, 50), 2500.0)

    def test_perimeter_zero_side(self):
        self.assertEqual(triangle_perimeter(0, 4, 5), 9)
        self.assertEqual(triangle_perimeter(3, 0, 5), 8)
        self.assertEqual(triangle_perimeter(3, 4, 0), 7)

    def test_perimeter_normal(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_perimeter_large(self):
        self.assertEqual(triangle_perimeter(100, 200, 300), 600)

if __name__ == '__main__':
    unittest.main()
if __name__ == '__rectangle__':
    unittest.RectangleTest()
