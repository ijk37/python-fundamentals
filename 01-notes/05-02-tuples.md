# 05-02: Tuples

A **tuple** is an **ordered**, **immutable** sequence. Once created, its elements cannot be changed.

---

## Creating Tuples

```python
# With parentheses
t = (1, 2, 3)

# Without parentheses (still a tuple)
t2 = 1, 2, 3

# Empty tuple
empty = ()
empty2 = tuple()

# Single-element tuple — trailing comma is required!
single = (42,)        # tuple with one item
not_tuple = (42)      # just an int in parentheses!

print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# From iterable
from_list   = tuple([1, 2, 3])    # (1, 2, 3)
from_string = tuple("hello")      # ('h', 'e', 'l', 'l', 'o')
from_range  = tuple(range(5))     # (0, 1, 2, 3, 4)
```

---

## Indexing and Slicing

Tuples support the same indexing and slicing as lists:

```python
t = (10, 20, 30, 40, 50)

print(t[0])       # 10
print(t[-1])      # 50
print(t[1:4])     # (20, 30, 40)
print(t[::-1])    # (50, 40, 30, 20, 10)  reversed
print(t[::2])     # (10, 30, 50)
```

---

## Immutability

The defining trait of tuples — elements **cannot be changed**:

```python
t = (1, 2, 3)
t[0] = 99         # TypeError: 'tuple' object does not support item assignment
t.append(4)       # AttributeError: 'tuple' has no attribute 'append'
```

However, if a tuple contains mutable objects (like lists), those objects can be modified:

```python
t = (1, [2, 3], 4)
t[1].append(99)   # OK — modifying the list inside
print(t)          # (1, [2, 3, 99], 4)
```

---

## Tuple Operations

```python
a = (1, 2, 3)
b = (4, 5, 6)

# Concatenation
print(a + b)      # (1, 2, 3, 4, 5, 6)

# Repetition
print(a * 3)      # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Length
print(len(a))     # 3

# Membership
print(2 in a)     # True
print(9 in a)     # False

# Iteration
for val in a:
    print(val)

# Count and index
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))   # 3
print(t.index(3))   # 3
```

---

## Tuple Packing and Unpacking

### Packing — multiple values → single tuple

```python
point = 3, 7        # packs into tuple (3, 7)
person = "Alice", 30, "Engineer"
print(person)       # ('Alice', 30, 'Engineer')
```

### Unpacking — tuple → individual variables

```python
# Exact match required
x, y = (3, 7)
print(x, y)   # 3 7

name, age, job = ("Alice", 30, "Engineer")
print(name)   # Alice
print(age)    # 30
print(job)    # Engineer

# Swap two variables elegantly
a, b = 10, 20
a, b = b, a        # tuple unpacking!
print(a, b)   # 20 10
```

### Extended unpacking with `*`

```python
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]  — rest is a list!

*start, last = (1, 2, 3, 4, 5)
print(start)   # [1, 2, 3, 4]
print(last)    # 5

first, *middle, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5
```

---

## Functions That Return Tuples

Returning multiple values from a function automatically creates a tuple:

```python
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 8, 2, 9])
print(lo, hi)   # 1 9

def divmod_manual(a, b):
    return a // b, a % b

q, r = divmod_manual(17, 5)
print(f"Quotient: {q}, Remainder: {r}")   # Quotient: 3, Remainder: 2
```

---

## Tuples in Dictionaries and Sets

Because tuples are **hashable** (immutable), they can be used as dictionary keys and set elements — unlike lists:

```python
# Tuple as dictionary key
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278):  "London",
    (35.6762, 139.6503): "Tokyo"
}
print(locations[(40.7128, -74.0060)])   # New York

# Tuple in a set
points = {(1, 2), (3, 4), (1, 2)}  # duplicates removed
print(points)   # {(1, 2), (3, 4)}

# List would fail!
# {[1, 2]}   # TypeError: unhashable type: 'list'
```

---

## Named Tuples

`namedtuple` creates tuple subclasses with named fields:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)

print(p.x)      # 3  — access by name
print(p.y)      # 7
print(p[0])     # 3  — still works by index
print(p)        # Point(x=3, y=7)

# Useful for structured data
Person = namedtuple("Person", ["name", "age", "job"])
alice = Person("Alice", 30, "Engineer")
print(alice.name)   # Alice
print(alice)        # Person(name='Alice', age=30, job='Engineer')
```

---

## When to Use Tuple vs. List

| | Tuple | List |
|--|-------|------|
| Mutable? | No | Yes |
| Faster? | Yes (slightly) | No |
| Hashable? | Yes (if elements are) | No |
| Use as dict key? | Yes | No |
| Best for | Fixed data, coordinates, records | Dynamic collections |
| Convention | Heterogeneous (name, age) | Homogeneous (same type) |

```python
# Tuple — fixed record (name, age, score)
student = ("Alice", 22, 95.5)

# List — collection that may change
scores = [85, 92, 78, 95, 60]
scores.append(88)
```

---

## Tuple Comprehensions? No — Generator Expressions

There is no tuple comprehension. Parentheses `()` with a comprehension create a **generator**:

```python
# Generator (not a tuple)
gen = (x**2 for x in range(5))
print(type(gen))   # <class 'generator'>

# To get a tuple, wrap in tuple()
t = tuple(x**2 for x in range(5))
print(t)           # (0, 1, 4, 9, 16)
```

---

## Performance: Tuple vs. List

```python
import timeit

# Tuple creation is faster
t_tuple = timeit.timeit("(1, 2, 3, 4, 5)", number=1_000_000)
t_list  = timeit.timeit("[1, 2, 3, 4, 5]", number=1_000_000)
print(f"Tuple: {t_tuple:.3f}s")
print(f"List:  {t_list:.3f}s")
# Tuple is typically 2-5x faster for creation
```

---

## Quick Summary

| Operation | Example | Result |
|-----------|---------|--------|
| Create | `(1, 2, 3)` | tuple |
| Index | `t[1]` | element |
| Slice | `t[1:3]` | tuple |
| Length | `len(t)` | int |
| Unpack | `a, b, c = t` | variables |
| Concatenate | `t1 + t2` | new tuple |
| Repeat | `t * 3` | new tuple |
| Count | `t.count(x)` | int |
| Find | `t.index(x)` | int |

---

## Practice Problems

```python
# 1. Swap without temp variable
x, y = 5, 10
x, y = y, x
print(x, y)   # 10 5

# 2. Unpack coordinates
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    dist = (x**2 + y**2) ** 0.5
    print(f"({x},{y}) → distance from origin: {dist:.2f}")

# 3. Tuple as immutable config
DB_CONFIG = ("localhost", 5432, "mydb", "admin")
host, port, dbname, user = DB_CONFIG
print(f"Connecting to {host}:{port}/{dbname} as {user}")

# 4. Sort list of tuples
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
for rank, (name, score) in enumerate(sorted_students, 1):
    print(f"#{rank} {name}: {score}")
```

---

> **Exercises:** [05-02: Exercises — Tuples](../02-exercises/05-02-tuples-exe.md)

---

⬅️ Previous: [05-01: Lists — The Complete Guide](05-01-lists.md)
➡️ Next: [05-03: Sets](05-03-sets.md)
