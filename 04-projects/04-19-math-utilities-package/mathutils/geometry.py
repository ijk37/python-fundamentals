"""
mathutils.geometry
===================
Area and distance formulas for basic shapes.
"""

import math


def circle_area(radius):
    """Return the area of a circle: π × r²"""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2


def rectangle_area(width, height):
    """Return the area of a rectangle: width × height"""
    if width < 0 or height < 0:
        raise ValueError("Width and height cannot be negative.")
    return width * height


def triangle_area(base, height):
    """Return the area of a triangle: ½ × base × height"""
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    return 0.5 * base * height


def hypotenuse(a, b):
    """Return the hypotenuse of a right triangle: √(a² + b²)"""
    return math.sqrt(a ** 2 + b ** 2)


if __name__ == "__main__":
    print("geometry.py self-test:")
    print(f"  circle_area(5)           = {circle_area(5):.4f}")
    print(f"  rectangle_area(4, 6)     = {rectangle_area(4, 6)}")
    print(f"  triangle_area(3, 8)      = {triangle_area(3, 8)}")
    print(f"  hypotenuse(3, 4)         = {hypotenuse(3, 4)}")
