"""module that contains our Circle class"""
import unittest
from math import pi

from geometry import Point


class Circle:
    """A class representing a circle"""
    def __init__(self, center: Point, radius: float) -> None:
        self.radius = radius
        self.center = center

    def diameter(self) -> float:
        """Return the diameter"""
        return 2 * self.radius

    def circumference(self) -> float:
        """Return the circumference

        The circumference is 2*pi* the radius of the circle.
        """
        return 2 * pi * self.radius

    def area(self) -> float:
        """Return the area of the circle"""
        return pi * self.radius**2

    def intersects(self, other: "Circle") -> bool:
        """Return True iff the other circle intersects"""
        x1 = self.center.x
        y1 = self.center.y
        r1 = self.radius
        x2 = other.center.x
        y2 = other.center.y
        r2 = other.radius

        return (x1 - x2)**2 + (y1 - y2)**2 <= (r1 + r2)**2

    def inside(self, point: Point) -> bool:
        """Return true iff the point is inside the circle"""
        x1 = self.center.x
        y1 = self.center.y
        r = self.radius
        x2 = point.x
        y2 = point.y

        # I copied this from Google
        return (x1 - x2)**2 + (y1 - y2)**2 < r**2

    def concentric(self, other: "Circle") -> bool:
        """Return True iff the circles are concentric"""
        return self.center == other.center


class CircleTests(unittest.TestCase):
    def setUp(self):
        self.solar_system = Circle(Point(0, 0), 4_545_000_000)
        self.earth = Circle(Point(149_600_000, 0), 6378)
        self.mercury = Circle(Point(-57_910_000, 0), 2_440)

    def test_radius(self):
        # given the circle
        circle = self.solar_system

        # when we access the .radius attribute
        radius = circle.radius

        # then we get the circle's radius
        self.assertEqual(radius, 4_545_000_000)

    def test_diameter(self):
        # given the circle
        circle = self.solar_system

        # when we get the circle's diameter
        diameter = circle.diameter()

        # then we get the circle's diameter
        expected_diameter = 4_545_000_000 * 2
        self.assertEqual(diameter, expected_diameter)

    def test_center(self):
        # given the circle
        circle = self.solar_system

        # when we access the .center attribute
        center = circle.center

        # then we get the circle's center
        self.assertEqual(center, Point(0, 0))

    def test_circumference(self):
        # given the circle
        circle = self.earth

        # when we get the circle's circumference
        c = circle.circumference()

        # then we get the expecte value
        circumference_of_earth = 40_074.1558  # km
        self.assertAlmostEqual(c, circumference_of_earth, places=3)

    def test_area(self):
        circle = self.earth

        area = circle.area()

        self.assertAlmostEqual(area, 127_796_483.1306, places=3)

    def test_intersects_true(self):
        circle1 = Circle(Point(0, 0), 5)
        circle2 = Circle(Point(1, 1), 5)

        # when we test if one intersects with the other
        circles_intersect = circle1.intersects(circle2)

        # then hopefully they do not
        self.assertTrue(circles_intersect)

    def test_intersects_false(self):
        # given the two circles
        earth = self.earth
        mercury = self.mercury

        # when we test if one intersects with the other
        circles_intersect = earth.intersects(mercury)

        # then hopefully they do not
        self.assertFalse(circles_intersect)

    def test_inside_true(self):
        # given the circle
        circle = self.solar_system

        # given the point inside the circle
        point = self.earth.center

        # then the center of the earth is inside the solar system
        self.assertTrue(circle.inside(point))

    def test_inside_false(self):
        # given the circle
        circle = self.earth

        # given the point inside the circle
        point = self.solar_system.center

        # then the center of the solar system is not inside the earth
        self.assertFalse(circle.inside(point))

    def test_concentric_true(self):
        # given the two circles
        circle1 = Circle(Point(0, 0), 5)
        circle2 = Circle(Point(0, 0), 10)

        # then the circles are cocentric
        self.assertTrue(circle1.concentric(circle2))

    def test_concentric_false(self):
        # given the two circles
        circle1 = self.earth
        circle2 = self.mercury

        # then the circles are not cocentric
        self.assertFalse(circle1.concentric(circle2))


if __name__ == '__main__':
    unittest.main()
