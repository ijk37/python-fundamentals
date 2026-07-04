"""
mathutils.basic
================
Basic arithmetic operations with input validation.
"""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a × b."""
    return a * b


def safe_divide(a, b):
    """
    Return a / b.
    Returns None (not raises) if b == 0, so callers decide how to handle it.
    """
    if b == 0:
        return None
    return a / b


def power(base, exp):
    """Return base raised to exp."""
    return base ** exp


def absolute(n):
    """Return the absolute value of n without using abs()."""
    return n if n >= 0 else -n


if __name__ == "__main__":
    # Quick self-test when this module is run directly
    print("basic.py self-test:")
    print(f"  add(3, 4)          = {add(3, 4)}")
    print(f"  safe_divide(10, 0) = {safe_divide(10, 0)}")
    print(f"  power(2, 8)        = {power(2, 8)}")
