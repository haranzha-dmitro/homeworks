import unittest

<<<<<<< HEAD
from math import pow, sqrt

from homework import Rectangle


class TestCases(unittest.TestCase):
=======
from homework import Rectangle
from math import sqrt, pow


class TestCases(unittest.TestCase):

>>>>>>> 1be9d3d54ced579c92070a8d0da2c34150340dd6
    test_rectangle1 = Rectangle(1.5, 4)
    test_rectangle2 = Rectangle(10, 20)
    test_rectangle3 = Rectangle(10, 10)

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.test_rectangle1.get_rectangle_perimeter(), 11)
        self.assertEqual(self.test_rectangle2.get_rectangle_perimeter(), 60)

    def test_get_rectangle_square(self):
        self.assertEqual(self.test_rectangle1.get_rectangle_square(), 6)
        self.assertEqual(self.test_rectangle2.get_rectangle_square(), 200)

    def test_get_sum_of_corners_too_many(self):
<<<<<<< HEAD
        with self.assertRaises(ValueError):
            self.test_rectangle1.get_sum_of_corners(5)

    def test_get_sum_of_corners_right(self):
        for corner in range(1, 5):
            with self.subTest(corner=corner):
                self.assertEqual(self.test_rectangle1.get_sum_of_corners(corner),
                                 corner * 90)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.test_rectangle1.get_rectangle_diagonal(),
                         sqrt(pow(1.5, 2) + pow(4, 2)))
        self.assertEqual(self.test_rectangle2.get_rectangle_diagonal(),
                         sqrt(pow(10, 2) + pow(20, 2)))

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.test_rectangle1.get_radius_of_circumscribed_circle(),
                         sqrt(pow(1.5, 2) + pow(4, 2)) / 2)
        self.assertEqual(self.test_rectangle2.get_radius_of_circumscribed_circle(),
                         sqrt(pow(10, 2) + pow(20, 2)) / 2)

    def test_get_radius_of_inscribed_circle(self):
        with self.assertRaises(ValueError):
            self.test_rectangle1.get_radius_of_inscribed_circle()
        self.assertEqual(self.test_rectangle3.get_radius_of_inscribed_circle(),
                         sqrt(pow(10, 2) + pow(10, 2)) / (2 * sqrt(2)))
=======
        self.assertRaises(ValueError, self.test_rectangle1.get_sum_of_corners, 5)

    def test_get_sum_of_corners_right(self):
        for corner in range(1, 5):
            self.assertEqual(self.test_rectangle1.get_sum_of_corners(corner), corner * 90)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.test_rectangle1.get_rectangle_diagonal(), sqrt(pow(1.5, 2) + pow(4, 2)))
        self.assertEqual(self.test_rectangle2.get_rectangle_diagonal(), sqrt(pow(10, 2) + pow(20, 2)))

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.test_rectangle1.get_radius_of_circumscribed_circle(), sqrt(pow(1.5, 2) + pow(4, 2))/2)
        self.assertEqual(self.test_rectangle2.get_radius_of_circumscribed_circle(), sqrt(pow(10, 2) + pow(20, 2))/2)

    def test_get_radius_of_inscribed_circle(self):
        self.assertRaises(ValueError, self.test_rectangle1.get_radius_of_inscribed_circle)
        self.assertEqual(self.test_rectangle3.get_radius_of_inscribed_circle(), sqrt(pow(10, 2) + pow(10, 2)) / (2* sqrt(2)))

>>>>>>> 1be9d3d54ced579c92070a8d0da2c34150340dd6


if __name__ == '__main__':
    unittest.main()
