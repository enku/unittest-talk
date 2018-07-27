"""Geometry according to Albert

Disclaimer: Albert is not good at geometry.
"""
import math
import unittest
from typing import Any


class Point:
    """A point in 2-dimensional space

    >>> x = 4
    >>> y = 5
    >>> p = Point(x, y)
    >>> p
    Point(4, 5)
    >>> p.x
    4
    >>> p.y
    5
    """
    def __init__(self, x: float, y: float) -> None:
        """Initialize with x and y coordinates."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        klass = self.__class__.__name__

        return '{klass}({x!r}, {y!r})'.format(
            klass=klass,
            x=self.x,
            y=self.y,
        )

    def __eq__(self, value: Any) -> bool:
        if hasattr(value, 'x') and hasattr(value, 'y'):
            return bool((self.x == value.x) and (self.y == value.y))

        return NotImplemented

    def __str__(self) -> str:
        return '({x!r}, {y!r})'.format(x=self.x, y=self.y)

    def distance(self, other: "Point") -> float:
        """Return the distance this and other point."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


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


if __name__ == '__main__':

    unittest.main()
