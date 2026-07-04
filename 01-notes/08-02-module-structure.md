# 08-02: Module Structure — `__name__` and `__main__`

Understanding module structure is essential for writing Python code that works correctly both as a **standalone script** and as an **imported module**.

---

## `__name__` — What is it?

Every Python module has a built-in variable called `__name__` (pronounced "dunder name").

Its value depends on how the module is being run:

| How the file runs | `__name__` value |
|-------------------|------------------|
| Executed directly (`python myfile.py`) | `'__main__'` |
| Imported by another module | `'myfile'` (the module name) |

```python
# Checking __name__ in interactive shell
>>> __name__
'__main__'

>>> import math
>>> math.__name__
'math'

>>> import numpy as np
>>> np.__name__
'numpy'
```

---

## The Problem Without `if __name__ == '__main__'`

Consider this file, `scorer.py`:

```python
# scorer.py
def letter_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

# Test code at module level
print("Testing scorer:")
print(letter_grade(75))   # runs at import time!
```

When another file imports it:

```python
# main.py
import scorer as s   # ← This EXECUTES the print statements!
print(s.letter_grade(92))
```

**Output (unwanted):**
```
Testing scorer:
C
A
```

The test code ran when we imported — that's bad!

---

## The Solution: `if __name__ == '__main__'`

Wrap any code that should only run when the file is **executed directly**:

```python
# scorer.py (improved)

def letter_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

def gpa_points(score):
    return round(score / 25, 1)

if __name__ == '__main__':
    # Only runs when scorer.py is executed directly
    print("Testing scorer:")
    print(letter_grade(75))    # C
    print(gpa_points(85))      # 3.4
```

Now importing `scorer` works cleanly:

```python
# main.py
import scorer as s
print(s.letter_grade(92))   # A
# No unwanted output!
```

---

## The `main()` Function Pattern

A clean, professional module structure:

```python
# bmi.py

def bmi(weight_kg, height_m):
    """Calculate Body Mass Index."""
    return round(weight_kg / height_m ** 2, 1)

def bmi_category(bmi_val):
    """Return BMI category label."""
    if bmi_val < 18.5: return "Underweight"
    if bmi_val < 25.0: return "Normal"
    if bmi_val < 30.0: return "Overweight"
    return "Obese"

def main():
    """Main program logic."""
    records = [(70, 1.75), (90, 1.70), (55, 1.65)]
    print("BMI Report:")
    for w, h in records:
        b = bmi(w, h)
        print(f"  {w}kg / {h}m → BMI {b} ({bmi_category(b)})")
    print(f"\nThis module's name is: {__name__}")

if __name__ == '__main__':
    main()
```

**When run directly:** `main()` is called.

**When imported:**
```python
import bmi as mp

# Access the functions
print(mp.bmi(75, 1.80))  # works!
# main() is NOT called automatically

# But it CAN be called explicitly
mp.main()   # runs the main function
```

---

## Why This Pattern is Useful

### 1. Reusable library + runnable script

```python
# stats.py
import math

def mean(data):
    return sum(data) / len(data)

def std_dev(data):
    m = mean(data)
    variance = sum((x - m)**2 for x in data) / len(data)
    return math.sqrt(variance)

def main():
    # Demo/test the functions
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    print(f"Mean: {mean(data)}")
    print(f"Std Dev: {std_dev(data):.2f}")

if __name__ == '__main__':
    main()
```

Now `stats.py` can be:
- Run directly as a demo
- Imported by other scripts as a library

### 2. Testing

```python
# calculator.py
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    # Quick smoke tests
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5.0
    print("All tests passed!")
```

---

## Module vs. Script

| | Module | Script |
|--|--------|--------|
| Purpose | Provide reusable code | Do a specific task |
| Import? | Yes | Usually not |
| `if __name__` | Wraps demo/test code | Sometimes used |
| Examples | `math`, `os`, e.g. `utils.py` | `data_analysis.py`, `web_scraper.py` |

---

## Packages — Organizing Multiple Modules

A **package** is a directory of modules with an `__init__.py` file:

```
mypackage/
    __init__.py       ← makes it a package
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

```python
# Importing from packages
import mypackage.module1
from mypackage import module2
from mypackage.subpackage import module3
from mypackage.module1 import some_function
```

### `__init__.py`

```python
# mypackage/__init__.py
# Controls what's available when someone does:
# from mypackage import *

from .module1 import useful_function   # relative import
from .module2 import AnotherClass

__version__ = "1.0.0"
__author__ = "Your Name"
```

---

## The `vars()` Function

`vars()` returns a dict of all current variables in scope:

```python
x = 10
y = "hello"
z = [1, 2, 3]

v = vars()
print("x" in v)    # True
print(v["x"])       # 10

# vars() in a function shows local scope
def show_locals():
    a = 1
    b = 2
    print(vars())   # {'a': 1, 'b': 2}

show_locals()
```

---

## Complete Module Template

```python
#!/usr/bin/env python3
"""
Module Name: mymodule.py
Description: Brief description of what this module does.
Author: Your Name
"""

# Standard library imports
import os
import sys

# Third-party imports
# import numpy as np

# Local imports
# from . import utils

# Module-level constants
VERSION = "1.0.0"
MAX_SIZE = 1000

# === Functions ===

def function_one(arg1, arg2):
    """Docstring for function_one."""
    pass

def function_two(data):
    """Docstring for function_two."""
    pass

# === Main ===

def main():
    """Main entry point for direct execution."""
    print(f"Running {__name__} v{VERSION}")
    # ... main logic here

if __name__ == '__main__':
    main()
```

---

## Practice

```python
# geometry.py

import math

def circle_area(radius):
    """Area of a circle."""
    return math.pi * radius ** 2

def circle_perimeter(radius):
    """Perimeter (circumference) of a circle."""
    return 2 * math.pi * radius

def rectangle_area(w, h):
    """Area of a rectangle."""
    return w * h

def rectangle_perimeter(w, h):
    """Perimeter of a rectangle."""
    return 2 * (w + h)

def triangle_area(base, height):
    """Area of a triangle."""
    return 0.5 * base * height

def main():
    r = 5
    print(f"Circle (r={r}):")
    print(f"  Area:      {circle_area(r):.2f}")
    print(f"  Perimeter: {circle_perimeter(r):.2f}")

    w, h = 4, 6
    print(f"Rectangle ({w}x{h}):")
    print(f"  Area:      {rectangle_area(w, h)}")
    print(f"  Perimeter: {rectangle_perimeter(w, h)}")

if __name__ == '__main__':
    main()

# In another file:
# import geometry
# print(geometry.circle_area(3))
```

---

> **Exercises:** [08-02: Exercises — Module Structure](../02-exercises/08-02-module-structure-exe.md)

---

⬅️ Previous: [08-01: Modules and Imports](08-01-modules-and-imports.md)
➡️ Next: [08-03: Python Ecosystem — Common Libraries Overview](08-03-python-ecosystem-libraries.md)
