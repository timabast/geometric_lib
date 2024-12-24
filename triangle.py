def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("sides must be positive")
    if a == 0 or b == 0 or c == 0:
        raise ValueError("sides must not be 0")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("must be a triangle condition")
    if (not isinstance(a, (int, float)) or
            not isinstance(b, (int, float)) or
            not isinstance(c, (int, float))):
        raise TypeError("sides must be num")
    return (a + b + c) / 2


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("sides must be positive")
    if a == 0 or b == 0 or c == 0:
        raise ValueError("sides must not be 0")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("must be a triangle condition")
    if (not isinstance(a, (int, float)) or
            not isinstance(b, (int, float)) or
            not isinstance(c, (int, float))):
        raise TypeError("sides must be num")
    return a + b + c
