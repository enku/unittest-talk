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
