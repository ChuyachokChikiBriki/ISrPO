import unittest
import math
import circle
import square

class Tests(unittest.TestCase):    
    def test_circle_area_zero_radius(self):
        self.assertEqual(circle.area(0), 0)
    
    def test_circle_area_positive_radius(self):
        self.assertAlmostEqual(circle.area(1), math.pi)
        self.assertAlmostEqual(circle.area(2), math.pi * 4)
        self.assertAlmostEqual(circle.area(5), math.pi * 25)
    
    def test_circle_perimeter_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)
    
    def test_circle_perimeter_positive_radius(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle.perimeter(2), 4 * math.pi)
        self.assertAlmostEqual(circle.perimeter(5), 10 * math.pi)
    
    def test_negative_radius(self):
        self.assertEqual(circle.area(-1), math.pi)  # (-1)^2 = 1
        self.assertEqual(circle.perimeter(-1), -2 * math.pi)
    
    def test_circle_area_type_error(self):
        with self.assertRaises(TypeError):
            circle.area("строка")

    def test_area_zero_side(self):
        self.assertEqual(square.area(0), 0)
    
    def test_area_positive_side(self):
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(10), 100)
    
    def test_perimeter_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)
    
    def test_perimeter_positive_side(self):
        self.assertEqual(square.perimeter(1), 4)
        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(10), 40)
    
    def test_negative_side(self):
        self.assertEqual(square.area(-5), 25)  # (-5)^2 = 25
        self.assertEqual(square.perimeter(-5), -20)  # 4 * (-5) = -20
    
    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            square.area("строка")
    


if __name__ == '__main__':
    unittest.main()
