# 02-09: Boolean and None Types

---

## The bool Type

A `bool` (Boolean) can hold only two values: `True` or `False`.

```python
is_active  = True
is_logged  = False

print(type(True))    # <class 'bool'>
print(type(False))   # <class 'bool'>
```

**Important:** `True` and `False` are case-sensitive.
```python
true   # NameError — not valid!
TRUE   # NameError — not valid!
True   # ✓ correct
```

---

## bool is a Subclass of int

In Python, `bool` is actually a subclass of `int`:
- `True` has the integer value `1`
- `False` has the integer value `0`

```python
print(True + True)     # 2
print(True + False)    # 1
print(False + False)   # 0
print(True * 5)        # 5
print(False * 100)     # 0

print(int(True))       # 1
print(int(False))      # 0

print(True == 1)       # True
print(False == 0)      # True
print(True > False)    # True
```

This makes it possible to count `True` values in a list:
```python
results = [True, False, True, True, False]   # lists are covered in Section 05
print(sum(results))   # 3  (number of True values)
```

---

## Comparison Operators Return bool

```python
print(5 > 3)      # True
print(5 < 3)      # False
print(5 == 5)     # True
print(5 != 3)     # True
print(5 >= 5)     # True
print(5 <= 4)     # False
```

---

## Logical Operators — and, or, not

### `and` — both conditions must be True

```python
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

x = 10
print(x > 5 and x < 20)   # True
print(x > 5 and x < 8)    # False
```

### `or` — at least one condition must be True

```python
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

x = 10
print(x < 5 or x > 8)    # True
print(x < 5 or x > 15)   # False
```

### `not` — reverses the truth value

```python
print(not True)    # False
print(not False)   # True

x = 10
print(not (x > 5))   # False
print(not (x > 20))  # True
```

### Operator precedence for logical operators

`not` > `and` > `or`

```python
print(True or False and False)   # True
# Because: True or (False and False) → True or False → True

print(not True or False)         # False
# Because: (not True) or False → False or False → False
```

---

## Short-Circuit Evaluation

Python evaluates logical expressions **lazily** — it stops as soon as the result is known.

### `and` short-circuits on `False`

```python
# If left side is False, right side is never evaluated
x = 0
result = (x != 0) and (10 / x > 1)
print(result)   # False — no ZeroDivisionError!
```

### `or` short-circuits on `True`

```python
# If left side is True, right side is never evaluated
name = "Jahid"
display = name or "Unknown"
print(display)   # 'Jahid'

name = ""
display = name or "Unknown"
print(display)   # 'Unknown'  (empty string is falsy)
```

---

## Truthy and Falsy Values

Every Python value has a truth value. Explicit `== True` or `== False` comparisons are not always necessary.

### Falsy values (evaluate as False in boolean context)

```python
bool(False)     # False
bool(0)         # False
bool(0.0)       # False
bool("")        # False  — empty string
bool([])        # False  — empty list
bool(())        # False  — empty tuple
bool({})        # False  — empty dict/set
bool(set())     # False  — empty set
bool(None)      # False
```

### Truthy values (everything else)

```python
bool(True)      # True
bool(1)         # True
bool(-1)        # True   — any non-zero int
bool(3.14)      # True
bool("hello")   # True   — non-empty string
bool(" ")       # True   — even a space!
bool([0])       # True   — non-empty list (even if contains 0)
bool([False])   # True   — non-empty list
```

### Using truthy/falsy in conditions

```python
name = input("Enter your name: ")
if name:                  # same as: if name != ""
    print("Hello", name)
else:
    print("No name entered")

items = []
if not items:             # same as: if len(items) == 0
    print("List is empty")

count = 5
if count:                 # same as: if count != 0
    print("There are items")
```

---

## The `bool()` Function

Explicitly convert any value to bool:

```python
print(bool(0))         # False
print(bool(42))        # True
print(bool(""))        # False
print(bool("hello"))   # True
print(bool([]))        # False
print(bool([1, 2]))    # True
print(bool(None))      # False
```

---

## The NoneType — None

`None` is Python's way of representing **nothing**, **no value**, or **absence of a value**.

```python
result = None
print(result)          # None
print(type(None))      # <class 'NoneType'>
```

### Common uses of None

```python
# Default variable before assignment
winner = None
if score > 90:
    winner = "Alice"

# Functions that don't return a value produce None
# (Functions are covered in Section 04 — just know that None is the "no value" value)
result = print("Hello Bob")   # print() itself returns None
print(result)                 # None
```

### Checking for None — always use `is` not `==`

```python
x = None

# Correct way
if x is None:
    print("x has no value")

if x is not None:
    print("x has a value:", x)

# Also works but less idiomatic
if x == None:    # works but not recommended
    print("x is None")
```

**Why use `is` instead of `==`?** Because `is` checks identity (same object in memory), and `None` is a singleton — there is only one `None` object in Python.

```python
a = None
b = None
print(a is b)    # True — same object
print(id(a) == id(b))  # True
```

### None vs. False vs. 0 vs. ""

```python
print(None == False)   # False
print(None == 0)       # False
print(None == "")      # False
print(None is None)    # True
print(bool(None))      # False  (None is falsy)
```

---

## Comparison Chaining

Python allows chaining comparisons, which is very readable:

```python
x = 5
print(1 < x < 10)     # True   (1 < 5 and 5 < 10)
print(10 > x > 0)     # True
print(1 < x < 4)      # False

age = 25
print(18 <= age <= 65)  # True — working age

# Invalid in most languages but valid in Python!
print(1 < 2 < 3 < 4 < 5)  # True
```

---

## Quick Summary

| Type | Values | Falsy values |
|------|--------|-------------|
| `bool` | `True`, `False` | `False` |
| `NoneType` | `None` | `None` |
| `int` | any integer | `0` |
| `float` | any float | `0.0` |
| `str` | any string | `""` (empty) |

### Logical truth table

| A | B | `A and B` | `A or B` | `not A` |
|---|---|-----------|----------|---------|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

---

## Practice Problems

```python
# 1. Check if a number is in range [1, 100]
n = 75
print(1 <= n <= 100)   # True

# 2. Check if string is non-empty and doesn't start with space
text = "hello"
if text and not text.startswith(" "):
    print("Valid text:", text)

# 3. Count True values in a list
flags = [True, False, True, True, False, True]
print(sum(flags))     # 4

# 4. Default to "Guest" if name is empty
name = ""
display_name = name or "Guest"
print(display_name)   # Guest

# 5. All three must pass
age = 22
has_license = True
is_sober = True
can_drive = age >= 18 and has_license and is_sober
print(can_drive)   # True
```

---

> **Exercises:** [02-09: Exercises — Boolean and None](../02-exercises/02-09-boolean-and-none-exe.md)

---

⬅️ Previous: [02-08: String Formatting](02-08-string-formatting.md)
➡️ Next: [02-10: Type Conversion](02-10-type-conversion.md)
