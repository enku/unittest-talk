"""Geometry according to Albert

Disclaimer: Albert is not good at geometry.
"""
import math
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
