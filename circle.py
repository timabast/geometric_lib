import math


def area(r):
    if not isinstance(r, (int, float)):
        raise TypeError("radius must be num")
    if r < 0:
        raise ValueError("radius must be positive")
    if r == 0:
        raise ValueError("radius must not be 0")
    return math.pi * r * r


def perimeter(r):
    if not isinstance(r, (int, float)):
        raise TypeError("radius must be num")
    if r < 0:
        raise ValueError("radius must be positive")
    if r == 0:
        raise ValueError("radius must not be 0")
    return 2 * math.pi * r
