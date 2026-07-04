# 08-01: Modules and Imports

A **module** is a Python file (`.py`) that contains functions, classes, and variables. Modules allow code to be organized into reusable units and avoid name conflicts.

---

## Importing a Module

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4
```

The module name acts as a **namespace** — its contents are accessed with `module.name`.

---

## Importing with an Alias

```python
import math as m
print(m.sqrt(9))    # 3.0

import numpy as np       # convention
import pandas as pd      # convention
import matplotlib.pyplot as plt  # convention
```

---

## Importing Specific Names

```python
from math import sqrt, pi, floor

# Now use without the `math.` prefix
print(sqrt(25))    # 5.0
print(pi)          # 3.141592653589793
print(floor(3.9))  # 3
```

### Import with alias

```python
from math import sqrt as sq
print(sq(16))   # 4.0
```

### Import all (use with caution!)

```python
from math import *
print(sin(pi))   # 0.0 (approximately)
print(exp(1))    # 2.718...
```

**Danger:** Pollutes the namespace — can overwrite existing variables with module names.

---

## The `math` Module

```python
import math

# Constants
print(math.pi)      # 3.141592653589793
print(math.e)       # 2.718281828459045
print(math.inf)     # inf (infinity)
print(math.nan)     # nan (Not a Number)

# Rounding
print(math.floor(3.7))  # 3    (toward -inf)
print(math.ceil(3.2))   # 4    (toward +inf)
print(math.trunc(3.9))  # 3    (toward zero)

# Roots and powers
print(math.sqrt(16))    # 4.0
print(math.pow(2, 10))  # 1024.0  (note: returns float)
print(math.log(math.e)) # 1.0  (natural log)
print(math.log(1000, 10)) # 3.0 (log base 10)
print(math.log2(8))     # 3.0
print(math.log10(100))  # 2.0

# Trig
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))           # 1.0
print(math.tan(math.pi/4))  # ~1.0
print(math.degrees(math.pi)) # 180.0
print(math.radians(180))     # pi

# Other
print(math.factorial(5))  # 120
print(math.gcd(36, 48))   # 12
print(math.isfinite(math.inf))  # False
print(math.isinf(math.inf))     # True
print(math.isnan(math.nan))     # True
```

---

## The `random` Module

```python
import random

# Random float in [0.0, 1.0)
print(random.random())

# Random float in [a, b]
print(random.uniform(1.0, 10.0))

# Random integer in [a, b] (both inclusive)
print(random.randint(1, 6))    # simulates a die

# Random integer — same as range()
print(random.randrange(0, 10, 2))   # even number 0-8

# Random choice from a sequence
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# Multiple random choices (with replacement)
print(random.choices(fruits, k=3))

# Sample without replacement
print(random.sample(fruits, k=2))

# Shuffle a list in place
random.shuffle(fruits)
print(fruits)

# Reproducible results — set seed
random.seed(42)
print(random.random())   # always the same
```

---

## The `os` Module

```python
import os

# Current working directory
print(os.getcwd())

# List directory contents
print(os.listdir("."))

# Check existence
print(os.path.exists("file.txt"))    # True/False
print(os.path.isfile("file.txt"))
print(os.path.isdir("mydir"))

# File info
print(os.path.getsize("file.txt"))   # bytes
print(os.path.basename("/dir/file.txt"))  # 'file.txt'
print(os.path.dirname("/dir/file.txt"))   # '/dir'
print(os.path.splitext("file.txt"))       # ('file', '.txt')

# Join paths (cross-platform)
path = os.path.join("folder", "subfolder", "file.txt")
print(path)   # folder/subfolder/file.txt (or folder\subfolder\... on Windows)

# Create / remove directories
os.makedirs("new/nested/dir", exist_ok=True)
os.rmdir("empty_dir")

# Environment variables
print(os.environ.get("PATH"))
print(os.environ.get("HOME", "/default"))
```

---

## The `sys` Module

```python
import sys

# Python version
print(sys.version)
print(sys.version_info.major)   # 3

# Command-line arguments
# When running: python script.py arg1 arg2
print(sys.argv)        # ['script.py', 'arg1', 'arg2']

# Exit the program
# sys.exit(0)   # 0 = success, non-zero = error

# Path where Python looks for modules
print(sys.path)

# Platform
print(sys.platform)    # 'win32', 'linux', 'darwin'

# stdin/stdout/stderr
sys.stdout.write("Hello\n")
sys.stderr.write("Error message\n")
```

---

## The `datetime` Module

```python
from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)                            # 2024-06-09 15:30:45.123456
print(now.year, now.month, now.day)   # 2024 6 9
print(now.hour, now.minute, now.second)

# Format as string
print(now.strftime("%Y-%m-%d"))         # '2024-06-09'
print(now.strftime("%B %d, %Y"))        # 'June 09, 2024'
print(now.strftime("%I:%M %p"))         # '03:30 PM'

# Parse from string
dt = datetime.strptime("2024-06-09", "%Y-%m-%d")
print(dt)

# Date arithmetic
today = date.today()
in_week = today + timedelta(days=7)
print(in_week)

delta = date(2025, 1, 1) - date.today()
print(f"Days until New Year: {delta.days}")

# Timestamps
import time
ts = time.time()   # Unix timestamp (seconds since 1970)
print(ts)
```

---

## The `collections` Module

```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter — count occurrences
c = Counter("hello world")
print(c.most_common(3))   # [('l', 3), ('o', 2), ('h', 1)]

# defaultdict — dict with default values
dd = defaultdict(list)
dd["a"].append(1)   # no KeyError

# deque — efficient queue
q = deque([1, 2, 3])
q.appendleft(0)     # add to front
q.append(4)         # add to back
q.popleft()         # remove from front

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print(p.x, p.y)    # 3 7
```

---

## The `itertools` Module

```python
import itertools

# count — infinite counter
for i in itertools.islice(itertools.count(10, 2), 5):
    print(i, end=" ")
# 10 12 14 16 18

# cycle — infinite cycle
colors = itertools.islice(itertools.cycle(["red", "green", "blue"]), 7)
print(list(colors))   # ['red', 'green', 'blue', 'red', 'green', 'blue', 'red']

# chain — concatenate iterables
chained = list(itertools.chain([1,2], [3,4], [5,6]))
print(chained)   # [1, 2, 3, 4, 5, 6]

# combinations and permutations
print(list(itertools.combinations("ABC", 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(itertools.permutations("AB", 2)))
# [('A', 'B'), ('B', 'A')]

# product — cartesian product
print(list(itertools.product([1,2], ["a","b"])))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

---

## Creating a Module

Any `.py` file is a module. Create `utils.py`:

```python
# utils.py

TAX_RATE = 0.08

def net_price(price):
    return round(price * (1 + TAX_RATE), 2)

def discount(price, pct):
    return round(price * (1 - pct / 100), 2)

if __name__ == "__main__":
    # This runs only when utils.py is executed directly
    print("Testing utils module")
    print(net_price(50))
```

Use it in another file:

```python
# main.py
import utils

print(utils.TAX_RATE)
print(utils.net_price(100))

# Or import specific names
from utils import discount
print(discount(200, 15))   # 170.0
```

---

## Module Search Path

When a module is imported, Python searches these locations in order:

1. Current directory
2. Directories in `PYTHONPATH` environment variable
3. Standard library directories
4. Third-party packages (site-packages)

```python
import sys
print(sys.path)    # list of directories Python searches
```

---

## Installing Third-Party Packages

```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install requests

# Install specific version
pip install numpy==1.24.0

# List installed packages
pip list

# Uninstall
pip uninstall numpy

# Save requirements
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

---

## Quick Summary

| Import form | Access |
|-------------|--------|
| `import math` | `math.sqrt(4)` |
| `import math as m` | `m.sqrt(4)` |
| `from math import sqrt` | `sqrt(4)` |
| `from math import sqrt as sq` | `sq(4)` |
| `from math import *` | `sqrt(4)` (pollutes namespace) |

---

> **Exercises:** [08-01: Exercises — Modules and Imports](../02-exercises/08-01-modules-and-imports-exe.md)

---

⬅️ Previous: [07-06: pathlib and File System Operations](07-06-pathlib-and-filesystem.md)
➡️ Next: [08-02: Module Structure — `__name__` and `__main__`](08-02-module-structure.md)
