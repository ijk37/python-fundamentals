# 02-05: Number Types — int and float

Python has two primary numeric types: `int` (integer) and `float` (floating-point).

---

## int — Integer Type

An `int` represents whole numbers with **no decimal point**. Python 3 integers have **arbitrary precision** — they can be as large as memory allows.

```python
x = 10
y = -5
z = 0
big = 2 ** 1000000    # a huge number — Python handles it!
```

### Checking the type

```python
print(type(10))      # <class 'int'>
print(type(-3))      # <class 'int'>
```

### Integer literals in different bases

```python
decimal = 255         # base 10 (default)
binary  = 0b11111111 # base 2  → 255
octal   = 0o377      # base 8  → 255
hexadec = 0xFF       # base 16 → 255

print(decimal, binary, octal, hexadec)  # 255 255 255 255
```

### Underscores for readability

```python
million     = 1_000_000
pi_approx   = 3_141_592
account_no  = 1234_5678_9012
print(million)    # 1000000
```

---

## float — Floating-Point Type

A `float` represents real numbers with a decimal point. Internally it is stored as a 64-bit IEEE 754 double-precision value.

```python
pi    = 3.14159
temp  = -2.5
ratio = 0.0
```

### Range and precision

| Property | Value |
|----------|-------|
| Min positive value | ~5 × 10⁻³²⁴ |
| Max value | ~1.8 × 10³⁰⁸ |
| Decimal precision | ~15–17 significant digits |

```python
>>> 2.0 ** 10000
OverflowError: (34, 'Result too large')

>>> 2 ** 10000       # int — no overflow!
1995...9376          # a huge integer
```

### Scientific notation

```python
speed_of_light = 3e8       # 300,000,000.0
electron_mass  = 9.109e-31 # 0.0000...9109
avogadro       = 6.022e23

print(speed_of_light)   # 300000000.0
print(electron_mass)    # 9.109e-31
```

### Floating-point precision issue

Floats are approximations. This can cause surprises:

```python
print(0.1 + 0.2)          # 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # False!

# Solution: use round() for comparisons
print(round(0.1 + 0.2, 1) == 0.3)  # True

# Or use math.isclose()
# (import is covered fully in Section 08 — for now, just copy this line as-is)
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

---

## Arithmetic with int and float

### Division always returns float

```python
print(10 / 2)    # 5.0   — always float
print(7 / 3)     # 2.333...
```

### Mixed operations — int + float → float

When int and float are mixed in an expression, Python **upcasts** the int to float:

```python
print(3 + 2.0)   # 5.0   — float
print(4 * 1.5)   # 6.0   — float
print(type(3 + 2.0))    # <class 'float'>
```

### Floor division // — always truncates toward −∞

```python
print(12 // 5)    # 2    (int // int → int)
print(12 // 5.0)  # 2.0  (involves float → float)
print(-12 // 5)   # -3   (truncates toward -infinity!)
print(-12 // -5)  # 2
```

**Key difference — floor vs truncation:**
```python
import math
print(math.floor(-2.7))   # -3  (floor: always toward -inf)
print(int(-2.7))          # -2  (truncation: toward zero)
```

### Modulus % — remainder

```python
print(12 % 5)    # 2   (12 = 2*5 + 2)
print(-12 % 5)   # 3   (sign follows divisor)
print(12 % -5)   # -3  (sign follows divisor)

# Practical uses
is_even   = (n % 2 == 0)
last_two  = (1234567 % 100)    # 67
hour_wrap = (25 % 24)          # 1  (clock arithmetic)
```

### Exponentiation **

```python
print(2 ** 10)    # 1024   (int ** int → int)
print(2 ** 0.5)   # 1.4142... (float — square root)
print(2 ** -1)    # 0.5   (negative exponent → float)

# Right-to-left associativity
print(2 ** 3 ** 2)    # 512  — same as 2 ** (3**2) = 2**9
print((2 ** 3) ** 2)  # 64
```

---

## Converting between int and float

```python
# float → int (truncates toward zero, NOT floor)
print(int(4.9))    # 4
print(int(-4.9))   # -4   (not -5!)
print(int(3.0))    # 3

# int → float
print(float(5))    # 5.0
print(float(-3))   # -3.0

# string → number
print(int("42"))       # 42
print(float("3.14"))   # 3.14
print(int("3.7"))      # ValueError! (can't skip float step)
print(int(float("3.7")))  # 3  (correct way)
```

---

## Useful math functions

### Built-in functions

```python
print(abs(-7))       # 7    — absolute value
print(abs(-3.14))    # 3.14

print(round(3.14159, 2))   # 3.14  — round to 2 decimal places
print(round(2.5))           # 2     — banker's rounding (round to even)
print(round(3.5))           # 4

print(pow(2, 10))    # 1024  — same as 2**10
print(pow(2, 10, 100))  # 24  — (2**10) % 100

print(divmod(17, 5)) # (3, 2) — quotient and remainder together
q, r = divmod(17, 5)
print(q, r)          # 3 2
```

### math module functions

```python
import math

print(math.sqrt(16))       # 4.0   — square root
print(math.sqrt(2))        # 1.4142135623730951

print(math.floor(3.7))     # 3     — largest int ≤ x
print(math.ceil(3.2))      # 4     — smallest int ≥ x
print(math.trunc(3.9))     # 3     — toward zero

print(math.log(math.e))    # 1.0   — natural log
print(math.log(100, 10))   # 2.0   — log base 10
print(math.log10(1000))    # 3.0

print(math.sin(math.pi/2)) # 1.0
print(math.cos(0))         # 1.0

print(math.pi)             # 3.141592653589793
print(math.e)              # 2.718281828459045
print(math.inf)            # inf
print(math.nan)            # nan

print(math.factorial(5))   # 120
print(math.gcd(36, 48))    # 12
```

---

## Special float values

```python
import math

pos_inf = math.inf
neg_inf = -math.inf
not_a_num = math.nan

print(pos_inf + 1)     # inf
print(pos_inf * -1)    # -inf
print(pos_inf / pos_inf)  # nan

print(math.isinf(pos_inf))   # True
print(math.isnan(not_a_num)) # True
print(math.isfinite(3.14))   # True
```

---

## Operator precedence for arithmetic

From **highest** to **lowest**:

| Precedence | Operator | Description | Associativity |
|------------|----------|-------------|---------------|
| 1 (highest) | `()` | Parentheses | — |
| 2 | `**` | Exponentiation | Right to left |
| 3 | `+x`, `-x` | Unary plus/minus | — |
| 4 | `*`, `/`, `//`, `%` | Multiply, divide, floor div, mod | Left to right |
| 5 (lowest) | `+`, `-` | Add, subtract | Left to right |

```python
print(3 + 4 * 2)      # 11   — * before +
print((3 + 4) * 2)    # 14   — () overrides
print(-5 ** 2)        # -25  — ** before unary -
print((-5) ** 2)      # 25
print(2 ** 3 ** 2)    # 512  — right to left: 2**(3**2)
print(10 - 3 - 2)     # 5    — left to right: (10-3)-2
print(20 / 4 * 2)     # 10.0 — left to right: (20/4)*2
```

---

## Quick Summary

| | int | float |
|--|-----|-------|
| Precision | Unlimited | ~15 decimal digits |
| Memory | Grows with value | Fixed 64-bit |
| Example | `42`, `-7`, `0` | `3.14`, `-2.5`, `1e10` |
| Use for | Counting, indexing | Measurements, calculations |

---

## Practice Problems

```python
# 1. Calculate compound interest
principal = 1000
rate = 0.05
years = 10
amount = principal * (1 + rate) ** years
print(f"After {years} years: ${amount:.2f}")

# 2. Check if a number is odd or even
n = 17
print("odd" if n % 2 != 0 else "even")

# 3. Convert Fahrenheit to Celsius
fahr = 98.6
celsius = 5 / 9 * (fahr - 32)
print(f"{fahr}°F = {celsius:.2f}°C")

# 4. Floor and ceiling
import math
x = 7.3
print(math.floor(x), math.ceil(x))   # 7  8

# 5. Integer division and remainder together
total_seconds = 3725
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"{hours}h {minutes}m {seconds}s")   # 1h 2m 5s
```

---

> **Exercises:** [02-05: Exercises — Number Types: int and float](../02-exercises/02-05-number-types-int-float-exe.md)

---

⬅️ Previous: [02-04: Operators](02-04-operators.md)
➡️ Next: [02-06: Strings — The str Type](02-06-string-basics.md)
