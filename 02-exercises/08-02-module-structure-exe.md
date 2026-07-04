# 08-02: Exercises — Module Structure

> **Notes reference:** [08-02: Module Structure — `__name__` and `__main__`](../01-notes/08-02-module-structure.md)

---

## Q1: Check __name__ at runtime
Print `__name__` from a script run directly, and show what it would be when imported.

**Solution**
```python
# save as check_name.py and run: python check_name.py

print(f"__name__ = '{__name__}'")

if __name__ == "__main__":
    print("Running as a script (direct execution).")
else:
    print("Running as an imported module.")
```

Output when run directly:
```
__name__ = '__main__'
Running as a script (direct execution).
```

---

## Q2: The problem without `if __name__ == '__main__'`
Demonstrate that module-level test code runs unintentionally on import.

**scorer_bad.py**
```python
def letter_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    return "F"

# This runs on import — BAD!
print("Test:", letter_grade(75))
```

**main.py**
```python
import scorer_bad   # prints "Test: C" — unwanted side effect!
print(scorer_bad.letter_grade(92))
```

---

## Q3: Fix with `if __name__ == '__main__'`
Rewrite `scorer_bad.py` so test code only runs when executed directly.

**scorer.py**
```python
def letter_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

def gpa_points(score):
    return round(score / 25, 1)

if __name__ == "__main__":
    # Only runs when scorer.py is executed directly
    print(letter_grade(92))   # A
    print(gpa_points(85))     # 3.4
```

**main.py**
```python
import scorer
print(scorer.letter_grade(78))   # C  — clean, no side effects
```

---

## Q4: The main() function pattern
Structure a BMI calculator module correctly with a `main()` function.

**bmi.py**
```python
def bmi(weight_kg, height_m):
    """Calculate Body Mass Index."""
    return round(weight_kg / height_m ** 2, 1)

def bmi_category(val):
    """Return BMI category string."""
    if val < 18.5: return "Underweight"
    if val < 25.0: return "Normal"
    if val < 30.0: return "Overweight"
    return "Obese"

def main():
    records = [(70, 1.75), (90, 1.70), (55, 1.65)]
    print("BMI Report:")
    for w, h in records:
        b = bmi(w, h)
        print(f"  {w}kg / {h}m → BMI {b} ({bmi_category(b)})")

if __name__ == "__main__":
    main()
```

**Usage as a library:**
```python
import bmi as b
print(b.bmi(80, 1.80))          # 24.7
print(b.bmi_category(24.7))     # Normal
b.main()                         # can also call main() explicitly
```

---

## Q5: stats.py — reusable + runnable
Write a `stats.py` module with `mean()` and `std_dev()` functions, guarded by `__main__`.

**stats.py**
```python
import math

def mean(data):
    """Arithmetic mean of a list of numbers."""
    return sum(data) / len(data)

def std_dev(data):
    """Population standard deviation."""
    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

def main():
    data = [62, 71, 80, 55, 90, 78, 65]
    print(f"Data:    {data}")
    print(f"Mean:    {mean(data):.2f}")
    print(f"Std Dev: {std_dev(data):.2f}")

if __name__ == "__main__":
    main()
```

**Import and use:**
```python
from stats import mean, std_dev

scores = [85, 92, 78, 96, 88]
print(f"Mean: {mean(scores):.1f}")
print(f"SD:   {std_dev(scores):.1f}")
```

---

## Q6: vars() — inspect local scope
Use `vars()` inside a function to print all local variables.

**Solution**
```python
def describe_city(name, country, population):
    """Show details about a city."""
    area_km2 = None   # placeholder
    print(vars())     # shows all local variables

describe_city("Dhaka", "Bangladesh", 21_006_000)
# {'name': 'Dhaka', 'country': 'Bangladesh', 'population': 21006000, 'area_km2': None}
```

---

## Q7: Package structure — design exercise
Describe (in code comments and directory layout) how a `geo` package would be organized.

**Solution**
```
geo/
    __init__.py        ← makes it a package; exports public API
    distance.py        ← haversine distance, straight-line distance
    coordinates.py     ← latitude/longitude utilities
    cities.py          ← predefined city coordinates
```

**geo/__init__.py**
```python
from .distance import haversine
from .cities import CITIES

__version__ = "1.0.0"
```

**geo/cities.py**
```python
# Coordinates: (latitude, longitude)
CITIES = {
    "Dhaka":    (23.8103, 90.4125),
    "New York": (40.7128, -74.0060),
    "Berlin":   (52.5200, 13.4050),
    "Tokyo":    (35.6762, 139.6503),
    "Nairobi":  (-1.2921, 36.8219),
}
```

**Using the package:**
```python
from geo import CITIES, haversine

print(CITIES["Dhaka"])
```

---

## Q8: calculator.py — test with assert inside __main__
Write a four-function calculator with assert-based smoke tests guarded by `__main__`.

**calculator.py**
```python
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    assert add(3, 4)      == 7
    assert subtract(10, 3) == 7
    assert multiply(6, 7)  == 42
    assert divide(15, 3)   == 5.0

    try:
        divide(5, 0)
    except ValueError as e:
        print(f"Caught: {e}")

    print("All tests passed!")
```

---

⬅️ Previous: [08-01: Exercises — Modules and Imports](08-01-modules-and-imports-exe.md)
📚 [Back to Notes Index](../01-notes/README.md)
