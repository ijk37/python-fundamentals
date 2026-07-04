"""
mathutils package
==================
A collection of reusable math utility modules.

Importing this package exposes the most-used functions directly:

    from mathutils import add, factorial, is_prime

Sub-modules:
    mathutils.basic      — add, subtract, multiply, safe_divide, power, absolute
    mathutils.statistics — mean, median, mode, variance, std_dev
    mathutils.sequences  — factorial, fibonacci, is_prime, prime_factors
    mathutils.geometry   — circle_area, rectangle_area, triangle_area, hypotenuse
"""

# Import key functions so users can do: from mathutils import mean
from mathutils.basic      import add, subtract, multiply, safe_divide, power, absolute
from mathutils.statistics import mean, median, mode, variance, std_dev
from mathutils.sequences  import factorial, fibonacci, is_prime, prime_factors
from mathutils.geometry   import circle_area, rectangle_area, triangle_area, hypotenuse

__version__ = "1.0.0"
__author__  = "Python Learner"
