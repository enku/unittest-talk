"""module that contains our Circle class"""
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

        return self.center.distance(other.center) <= self.radius + other.radius

    def inside(self, point: Point) -> bool:
        """Return true iff the point is inside the circle"""

        return self.center.distance(point) < self.radius

    def concentric(self, other: "Circle") -> bool:
        """Return True iff the circles are concentric"""
        return self.center == other.center
