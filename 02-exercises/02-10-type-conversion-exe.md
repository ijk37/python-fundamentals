# 02-10: Exercises — Type Conversion

> **Notes reference:** [02-10: Type Conversion](../01-notes/02-10-type-conversion.md)

---

## Q1: Implicit conversion
Python automatically converts compatible types. Predict the type and value of each expression:

```python
3 + 4.0
True + 5
10 / 4
True + 3.5
```

**Solution**
```python
print(type(3 + 4.0),   3 + 4.0)    # float 7.0
print(type(True + 5),  True + 5)   # int   6
print(type(10 / 4),    10 / 4)     # float 2.5
print(type(True + 3.5),True + 3.5) # float 4.5
```

---

## Q2: int() truncation vs floor
Show the difference between `int()` and `math.floor()` for negative floats.

**Solution**
```python
import math
print(int(-4.9))         # -4   (truncates toward zero)
print(math.floor(-4.9))  # -5   (rounds toward -infinity)
print(int(4.9))          # 4
print(math.floor(4.9))   # 4    (same for positive numbers)
```

---

## Q3: Safe string-to-int conversion
Ask the user for a number and convert it to int. Handle the case where the user enters non-numeric input.

**Solution**
```python
raw = input("Enter a number: ")
try:
    n = int(raw)
    print("You entered:", n)
except ValueError:
    print(f"'{raw}' is not a valid integer.")
```

---

## Q4: Multi-step conversion
Convert the string `"7.85"` to an integer (the direct approach fails — show it, then fix it).

**Solution**
```python
s = "7.85"

# Direct int() fails:
# int(s)  → ValueError: invalid literal for int() with base 10: '7.85'

# Correct two-step approach:
n = int(float(s))
print(n)   # 7  (truncates)
```

---

## Q5: bool() edge cases
What does `bool()` return for each? Explain the surprising ones.

```python
bool(0)
bool(0.0)
bool(" ")
bool([])
bool([0])
bool("False")
```

**Solution**
```python
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(" "))     # True  — a space is a non-empty string!
print(bool([]))      # False
print(bool([0]))     # True  — the list is non-empty, even if its content is 0
print(bool("False")) # True  — "False" is a non-empty string!
```

---

## Q6: Collection conversions
Convert `"Bangladesh"` to a list of characters, then to a set of unique characters.

**Solution**
```python
s = "Bangladesh"
chars  = list(s)
unique = set(s)
print(chars)    # ['B', 'a', 'n', 'g', 'l', 'a', 'd', 'e', 's', 'h']
print(unique)   # {'B', 'n', 'a', 'g', 'l', 'd', 'e', 's', 'h'} (a appears once)
print(len(chars), len(unique))  # 10  9
```

---

## Q7: ASCII and Unicode
Print the ASCII code of `'A'`, `'a'`, `'0'`, and `'৳'` (BDT symbol). Then convert codes 66, 100, and 8364 back to characters.

**Solution**
```python
print(ord('A'))    # 65
print(ord('a'))    # 97
print(ord('0'))    # 48
print(ord('৳'))    # 2547

print(chr(66))     # B
print(chr(100))    # d
print(chr(8364))   # €
```

---

## Q8: Number to binary/hex string
Convert `200` to its binary string, hex string, and octal string representations.

**Solution**
```python
n = 200
print(bin(n))   # 0b11001000
print(hex(n))   # 0xc8
print(oct(n))   # 0o310

# Without prefix using format:
print(f"{n:b}")  # 11001000
print(f"{n:x}")  # c8
print(f"{n:o}")  # 310
```

---

⬅️ Previous: [02-09: Exercises — Boolean and None](02-09-boolean-and-none-exe.md)
➡️ Next: [03-01: Exercises — Conditional Statements](03-01-if-elif-else-exe.md)
