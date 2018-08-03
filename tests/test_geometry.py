import unittest

from geometry import Point


class PointTests(unittest.TestCase):
    """Tests that are on Point"""
    def test_x_attribute(self):
        # given the point
        point = Point(5, -5)

        # then we get the expected x attribute
        self.assertEqual(point.x, 5)

    def test_y_attribute(self):
        # given the point
        point = Point(5, -5)

        # then we get the expected y attribute
        self.assertEqual(point.y, -5)

    def test_repr(self):
        # given the point
        point = Point(5, 5)

        # when we call repr() on it
        value = repr(point)

        # then we get the expected string
        self.assertEqual(value, 'Point(5, 5)')

    def test_str(self):
        # given the point
        point = Point(5, 5)

        # when we call str() on it
        value = str(point)

        # then we get the expected string
        self.assertEqual(value, '(5, 5)')

    def test_equality_true(self):
        # given the two points with the same coordinates
        point1 = Point(5, 0)
        point2 = Point(5, 0)

        # then they are equal
        self.assertEqual(point1, point2)

    def test_equality_false(self):
        # given the two points with different coordinates
        point1 = Point(5, 0)
        point2 = Point(5, 5)

        # then they are not equal
        self.assertNotEqual(point1, point2)

    def test_distance(self):
        # given the two points
        point1 = Point(5, 0)
        point2 = Point(5, 5)

        # when we use one to calculate the distance to the other
        distance = point1.distance(point2)

        # then we get the distance between the two points
        self.assertEqual(distance, 5)
