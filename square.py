
def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("side must be num")
    if a < 0:
        raise ValueError("side must be positive")
    if a == 0:
        raise ValueError("side must not be 0")
    return a * a


def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("side must be num")
    if a < 0:
        raise ValueError("side must be positive")
    if a == 0:
        raise ValueError("side must not be 0")
    return 4 * a
