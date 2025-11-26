import math


def area_rect(a, b):
    if a < 0 or b < 0:
        return None
    return a * b


def perimeter_rect(a, b):
    if a < 0 or b < 0:
        return None
    return 2 * (a + b)


def diagonal_rect(a, b):
    if a < 0 or b < 0:
        return None
    return math.sqrt(a * a + b * b)


def is_square(a, b):
    if a < 0 or b < 0:
        return False
    return a == b


def scale_rect(a, b, k):
    if k < 0:
        return (0, 0)
    return a * k, b * k


def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


def triangle_perimeter(a, b, c):
    if not is_valid_triangle(a, b, c):
        return None
    return a + b + c


def triangle_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        return None
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
