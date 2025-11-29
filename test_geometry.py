import unittest
import time
import math
from geometry import (area_rect, perimeter_rect, diagonal_rect,is_square,scale_rect,
    is_valid_triangle, triangle_perimeter, triangle_area
)


class GeometryTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area_rect(5, 10), 50)

    def test_area_negative(self):
        self.assertIsNone(area_rect(-3, 10))

    def test_perimeter_normal(self):
        self.assertEqual(perimeter_rect(4, 6), 20)

    def test_diagonal(self):
        self.assertEqual(diagonal_rect(3, 4), 5)

    def test_is_square(self):
        self.assertTrue(is_square(7, 7))
        self.assertFalse(is_square(7, 9))

    def test_scale(self):
        self.assertEqual(scale_rect(2, 3, 4), (8, 12))

    def test_scale_zero(self):
        self.assertEqual(scale_rect(5, 7, 0), (0, 0))

    def test_triangle_valid(self):
        self.assertTrue(is_valid_triangle(3, 4, 5))
        self.assertFalse(is_valid_triangle(1, 2, 3))

    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 4, 5), 6)

    def test_triangle_invalid_area(self):
        self.assertIsNone(triangle_area(10, 1, 1))

    def test_triangle_perimeter_normal(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)



    def test_security_negative_sides(self):
        self.assertIsNone(area_rect(-1000, -2000))
        self.assertIsNone(perimeter_rect(-5, 10))
        self.assertFalse(is_square(-5, -5))

    def test_security_invalid_triangle(self):
        self.assertFalse(is_valid_triangle(-3, 4, 5))
        self.assertIsNone(triangle_perimeter(100, 3, 1))


    def test_performance_large_values(self):
        start = time.time()
        
        for _ in range(500000):
            area_rect(1000000, 2000000)
            perimeter_rect(999999, 123456)
        
        end = time.time()
        duration = end - start
        self.assertLess(duration, 1.5)


    def test_performance_triangle(self):
        start = time.time()

        for _ in range(300000):
            triangle_area(300, 400, 500)
        
        end = time.time()
        duration = end - start
        self.assertLess(duration, 1.5)


if __name__ == "__main__":
    unittest.main()
