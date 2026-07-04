"""
Project 03-19: Math Utilities Package
========================================
Topics: modules, packages, __init__.py, __name__ guard,
        import forms, math functions, while loop menu
Difficulty: Intermediate

Demonstrates how to build and use a Python package
(mathutils) with multiple sub-modules. The main.py
imports from the package and provides an interactive
demo.

Package structure:
    mathutils/
        __init__.py      ← makes the folder a package
        basic.py         ← arithmetic
        statistics.py    ← mean, median, mode, std dev
        sequences.py     ← factorial, fibonacci, primes
        geometry.py      ← areas, hypotenuse
"""

# Import the whole package — __init__.py exposes everything
import mathutils

# Or import specific functions from specific modules
from mathutils.statistics import mean, std_dev
from mathutils.sequences  import fibonacci, is_prime


# =============================================================================
# DEMO SECTIONS
# =============================================================================

def demo_basic():
    """Show basic arithmetic operations from mathutils.basic."""
    print("\n  ── Basic Arithmetic ──")
    a, b = 15, 4
    print(f"  {a} + {b}          = {mathutils.add(a, b)}")
    print(f"  {a} - {b}          = {mathutils.subtract(a, b)}")
    print(f"  {a} × {b}          = {mathutils.multiply(a, b)}")
    result = mathutils.safe_divide(a, b)
    print(f"  {a} ÷ {b}          = {result:.4f}")
    print(f"  safe_divide(10, 0) = {mathutils.safe_divide(10, 0)}")
    print(f"  power(2, 10)       = {mathutils.power(2, 10)}")
    print(f"  absolute(-42)      = {mathutils.absolute(-42)}")


def demo_statistics():
    """Show statistics functions."""
    data = [88, 72, 90, 65, 81, 77, 92, 68, 84, 75]
    print("\n  ── Statistics ──")
    print(f"  Data   : {data}")
    print(f"  Mean   : {mathutils.mean(data):.2f}")
    print(f"  Median : {mathutils.median(data)}")
    print(f"  Mode   : {mathutils.mode(data)}")
    print(f"  Std Dev: {mathutils.std_dev(data):.4f}")
    print(f"  Variance: {mathutils.variance(data):.4f}")


def demo_sequences():
    """Show sequence and number-theory functions."""
    n = 10
    print("\n  ── Sequences ──")
    print(f"  factorial({n})   = {mathutils.factorial(n):,}")
    print(f"  fibonacci({n})   = {fibonacci(n)}")

    # List primes up to 50
    primes = [x for x in range(2, 51) if is_prime(x)]
    print(f"  Primes ≤ 50     = {primes}")
    print(f"  prime_factors(360) = {mathutils.prime_factors(360)}")


def demo_geometry():
    """Show geometric area and distance calculations."""
    print("\n  ── Geometry ──")
    print(f"  circle_area(radius=7)        = {mathutils.circle_area(7):.4f}")
    print(f"  rectangle_area(12, 8)        = {mathutils.rectangle_area(12, 8)}")
    print(f"  triangle_area(base=10, h=6)  = {mathutils.triangle_area(10, 6)}")
    print(f"  hypotenuse(3, 4)             = {mathutils.hypotenuse(3, 4)}")


def demo_custom_stats():
    """Let the user enter numbers and see statistics."""
    print("\n  Enter numbers separated by spaces:")
    raw = input("  Numbers: ").strip()

    try:
        numbers = [float(x) for x in raw.split()]
        if not numbers:
            print("  No numbers entered.\n")
            return
        print(f"\n  Input  : {numbers}")
        print(f"  Mean   : {mean(numbers):.4f}")
        print(f"  Std Dev: {std_dev(numbers):.4f}")
        print()
    except ValueError:
        print("  Please enter numeric values only.\n")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 55)
    print("       Math Utilities Package — Demo")
    print(f"       mathutils v{mathutils.__version__}")
    print("=" * 55)

    while True:
        print("\nDemonstrations:")
        print("  1. Basic arithmetic")
        print("  2. Statistics")
        print("  3. Sequences & primes")
        print("  4. Geometry")
        print("  5. Custom statistics (enter your own numbers)")
        print("  6. Quit")
        print()

        choice = input("Choose (1–6): ").strip()

        if   choice == "1": demo_basic()
        elif choice == "2": demo_statistics()
        elif choice == "3": demo_sequences()
        elif choice == "4": demo_geometry()
        elif choice == "5": demo_custom_stats()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
