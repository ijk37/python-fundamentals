# 02-10: Type Conversion

Type conversion is the process of changing a value from one data type to another.

Python supports two kinds:
1. **Implicit conversion** — Python converts automatically
2. **Explicit conversion (casting)** — values are converted manually using built-in functions

---

## Implicit Type Conversion

Python automatically converts compatible types when needed, typically from narrower to wider type.

```python
# int + float → float (int is "upcast" to float)
result = 5 + 2.0
print(result)        # 7.0
print(type(result))  # <class 'float'>

result2 = 10 / 4     # division always returns float
print(result2)       # 2.5
print(type(result2)) # <class 'float'>

# bool + int → int
print(True + 5)      # 6
print(False + 10)    # 10
print(True + 3.5)    # 4.5  (bool → float)
```

Python will **not** implicitly convert between incompatible types:

```python
print("10" + 5)   # TypeError: can only concatenate str (not "int") to str
```

---

## Explicit Type Conversion (Casting)

### `int()` — Convert to integer

```python
# From float (truncates, does NOT round)
print(int(3.9))     # 3
print(int(3.1))     # 3
print(int(-3.9))    # -3   (toward zero, NOT -4)

# From string
print(int("42"))    # 42
print(int("  100  "))  # 100  (strips whitespace)

# From bool
print(int(True))    # 1
print(int(False))   # 0

# From hex/binary/octal strings
print(int("FF", 16))    # 255
print(int("1010", 2))   # 10
print(int("17", 8))     # 15

# What fails:
# int("3.14")     → ValueError (can't convert float string directly)
# int("hello")    → ValueError
# int([1, 2])     → TypeError
```

### `float()` — Convert to float

```python
# From int
print(float(5))       # 5.0
print(float(-3))      # -3.0

# From string
print(float("3.14"))  # 3.14
print(float("1e3"))   # 1000.0
print(float("inf"))   # inf
print(float("nan"))   # nan
print(float("  2.5 ")) # 2.5  (strips whitespace)

# From bool
print(float(True))    # 1.0
print(float(False))   # 0.0

# What fails:
# float("hello")  → ValueError
# float("1,000")  → ValueError (comma not allowed)
```

### `str()` — Convert to string

```python
print(str(42))          # '42'
print(str(3.14))        # '3.14'
print(str(True))        # 'True'
print(str(False))       # 'False'
print(str(None))        # 'None'
print(str([1, 2, 3]))   # '[1, 2, 3]'
print(str((1, 2)))      # '(1, 2)'
print(str({1, 2}))      # '{1, 2}'

# Scientific notation
print(str(1234500000.0))  # '1234500000.0'
print(str(1.5e-10))       # '1.5e-10'
```

### `bool()` — Convert to boolean

```python
# Falsy values → False
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))      # False
print(bool([]))      # False
print(bool(()))      # False
print(bool({}))      # False
print(bool(None))    # False

# Everything else → True
print(bool(1))       # True
print(bool(-1))      # True  (any non-zero)
print(bool(3.14))    # True
print(bool("hi"))    # True
print(bool([0]))     # True  (non-empty, even if contains 0)
print(bool(" "))     # True  (space is non-empty)
```

---

## Converting Between Collection Types

*(Collection types — list, tuple, set — are covered in depth in Section 05. The conversions below are shown here for completeness; revisit them after finishing Section 05.)*

```python
# list(), tuple(), set() can convert any iterable

# Range to list
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(tuple(range(5)))         # (0, 1, 2, 3, 4)

# String to list (characters)
print(list("hello"))           # ['h', 'e', 'l', 'l', 'o']
print(set("hello"))            # {'h', 'e', 'l', 'o'}  (unique only)

# List to tuple and back
ls = [1, 2, 3, 4]
tup = tuple(ls)                # (1, 2, 3, 4)
back = list(tup)               # [1, 2, 3, 4]

# Remove duplicates via set
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(sorted(unique))          # [1, 2, 3, 4]
```

---

## Safe Conversion with Error Handling

User input and external data can be unpredictable. Always handle conversion errors:

```python
# Bad (crashes on invalid input)
n = int(input("Enter a number: "))   # crashes if user types "abc"

# Good (handles error gracefully)
raw = input("Enter a number: ")
try:
    n = int(raw)
    print("You entered:", n)
except ValueError:
    print(f"'{raw}' is not a valid integer")
```

### Robust input with validation

```python
# Single attempt with try/except
# (Retry loops using while are covered in Section 03)
raw = input("Enter your age: ")
try:
    age = int(raw)
    if 0 <= age <= 120:
        print(f"Your age is: {age}")
    else:
        print("Age must be between 0 and 120")
except ValueError:
    print(f"'{raw}' is not a valid number.")
```

---

## Common Conversion Patterns

### String to int (multi-step for float strings)

```python
s = "3.7"
# int(s)          → ValueError (can't convert "3.7" directly)
n = int(float(s))  # 3  (convert to float first, then truncate)
```

### Number to formatted string

```python
price = 1234.5678
formatted = f"${price:,.2f}"   # $1,234.57
print(formatted)

n = 42
binary_str = bin(n)    # '0b101010'
hex_str    = hex(n)    # '0x2a'
oct_str    = oct(n)    # '0o52'
print(binary_str, hex_str, oct_str)
```

### ASCII and Unicode conversion

```python
# Character to number
print(ord('A'))     # 65
print(ord('a'))     # 97
print(ord('0'))     # 48
print(ord('€'))     # 8364

# Number to character
print(chr(65))      # 'A'
print(chr(97))      # 'a'
print(chr(8364))    # '€'

# Encode/decode
s = "hello"
b = s.encode("utf-8")     # bytes: b'hello'
s2 = b.decode("utf-8")    # back to str: 'hello'
```

---

## Type Conversion Summary Table

| From ↓ \ To → | `int` | `float` | `str` | `bool` |
|--------------|-------|---------|-------|--------|
| `int` | — | `float(n)` | `str(n)` | `bool(n)` |
| `float` | `int(f)` truncates | — | `str(f)` | `bool(f)` |
| `str` | `int(s)` | `float(s)` | — | `bool(s)` |
| `bool` | `int(b)` → 0 or 1 | `float(b)` → 0.0/1.0 | `str(b)` → "True"/"False" | — |
| `None` | ❌ TypeError | ❌ TypeError | `str(None)` → "None" | `bool(None)` → False |

---

## Practice Problems

```python
# 1. Convert user input to float and compute area
radius = float(input("Enter radius: "))
import math
area = math.pi * radius ** 2
print(f"Area = {area:.2f}")

# 2. Convert temperature string
temp_str = "98.6F"
temp_f = float(temp_str[:-1])   # strip 'F' and convert
temp_c = (temp_f - 32) * 5 / 9
print(f"{temp_f}°F = {temp_c:.1f}°C")

# 3. Count digits in a number
n = 123456789
digits = len(str(abs(n)))
print(digits)   # 9

# 4. Sum digits of a number
n = 12345
s = str(n)          # '12345'
# Manual approach — works for this specific 5-digit number
total = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4])
print(total)   # 15
# General approach (any length) uses a loop (Section 03) or comprehension (Section 06)
```

---

> **Exercises:** [02-10: Exercises — Type Conversion](../02-exercises/02-10-type-conversion-exe.md)

---

⬅️ Previous: [02-09: Boolean and None Types](02-09-boolean-and-none.md)
➡️ Next: [03-01: Conditional Statements — if, elif, else](03-01-if-elif-else.md)
