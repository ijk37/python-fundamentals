# 02-08: String Formatting

Python offers multiple ways to embed values inside strings. The modern recommended approach is **f-strings** (Python 3.6+). The `format()` method is also widely used. The old `%` formatting still appears in legacy code.

---

## f-Strings (Formatted String Literals) — Recommended

An f-string is prefixed with `f` or `F`. Expressions inside `{}` are evaluated at runtime:

```python
name = "Alice"
age = 30

# Basic substitution
print(f"Hello, {name}!")               # Hello, Alice!
print(f"You are {age} years old.")     # You are 30 years old.

# Expressions
print(f"Next year you'll be {age + 1}.")   # 31
print(f"2 + 2 = {2 + 2}")                 # 4

# Calling methods
print(f"{'hello'.upper()}")            # HELLO
print(f"{name.lower()} is great!")     # alice is great!

# Calling functions
print(f"Square root of 16 is {16**0.5:.1f}")   # Square root of 16 is 4.0

# Conditional expression
score = 85
print(f"Result: {'Pass' if score >= 60 else 'Fail'}")   # Result: Pass
```

### Multi-line f-strings

```python
name, city, age = "Bob", "London", 25
info = (
    f"Name: {name}\n"
    f"City: {city}\n"
    f"Age:  {age}"
)
print(info)
```

---

## Format Specifiers

Format specifiers go after a colon inside `{}`:

```python
{value:format_spec}
```

Syntax of format_spec:

```
[[fill]align][sign][#][0][width][grouping][.precision][type]
```

---

## Integer Formatting

```python
n = 1234567

# Type specifiers
print(f"{n:d}")      # 1234567  (decimal, default for int)
print(f"{n:b}")      # 100101101011010000111  (binary)
print(f"{n:o}")      # 4553207  (octal)
print(f"{n:x}")      # 12d687   (hex lowercase)
print(f"{n:X}")      # 12D687   (hex uppercase)
print(f"{n:#b}")     # 0b100101101011010000111  (with 0b prefix)
print(f"{n:#x}")     # 0x12d687 (with 0x prefix)

# Width — minimum field width
print(f"{42:8d}")    # '      42' (right-aligned, width 8)
print(f"{42:<8d}")   # '42      ' (left-aligned)
print(f"{42:^8d}")   # '   42   ' (centered)

# Zero-padding
print(f"{42:08d}")   # '00000042'
print(f"{-42:08d}")  # '-0000042'

# Thousands separator
print(f"{1234567:,}")   # '1,234,567'
print(f"{1234567:_}")   # '1_234_567'
```

---

## Float Formatting

```python
pi = 3.14159265358979

# f — fixed-point (precision = decimal places)
print(f"{pi:.2f}")    # 3.14
print(f"{pi:.5f}")    # 3.14159
print(f"{pi:.0f}")    # 3

# e — scientific notation
print(f"{pi:e}")      # 3.141593e+00
print(f"{pi:.2e}")    # 3.14e+00

# g — general (shorter of f and e)
print(f"{pi:.4g}")    # 3.142
print(f"{0.0001234:.4g}")  # 0.0001234
print(f"{12345678.0:.4g}") # 1.235e+07

# % — percentage (multiplies by 100, adds %)
accuracy = 0.9567
print(f"{accuracy:.1%}")   # 95.7%
print(f"{accuracy:.2%}")   # 95.67%

# Width + precision
print(f"{pi:10.3f}")   # '     3.142' (width=10, 3 decimal places)
print(f"{pi:<10.3f}")  # '3.142     ' (left-aligned)
print(f"{pi:^10.3f}")  # '  3.142   ' (centered)
print(f"{pi:010.3f}")  # '000003.142' (zero-padded)

# Sign
print(f"{+pi:+.2f}")   # '+3.14'
print(f"{-pi:+.2f}")   # '-3.14'
print(f"{pi: .2f}")    # ' 3.14' (space for positive, - for negative)
```

---

## String Formatting

```python
name = "Alice"

# s — string type (default)
print(f"{name:s}")      # 'Alice'
print(f"{name:10s}")    # 'Alice     ' (right-padded, width 10)
print(f"{name:<10}")    # 'Alice     ' (left-aligned)
print(f"{name:>10}")    # '     Alice' (right-aligned)
print(f"{name:^10}")    # '  Alice   ' (centered)

# Custom fill character
print(f"{name:*>10}")   # '*****Alice'
print(f"{name:*<10}")   # 'Alice*****'
print(f"{name:*^10}")   # '**Alice***'

# Truncation (max length via precision)
print(f"{'Hello, World!':.5}")  # 'Hello'

# Combine width + precision
print(f"{'Hello, World!':10.5}")  # 'Hello     '
```

---

## Building Tables with f-strings

```python
# Right-aligned numbers, left-aligned strings
# (Loops to iterate over data are covered in Section 03 — individual rows shown here)
header = f"{'Name':<15} {'Age':>5} {'Score':>8}"
sep = "-" * len(header)
print(header)
print(sep)
print(f"{'Alice':<15} {22:>5} {91.5:>8.1f}")
print(f"{'Bob':<15} {19:>5} {78.3:>8.1f}")
print(f"{'Charlie':<15} {25:>5} {85.0:>8.1f}")
```

**Output:**
```
Name              Age    Score
------------------------------
Alice              22     91.5
Bob                19     78.3
Charlie            25     85.0
```

---

## The `format()` Method

Before f-strings, `.format()` was the primary method:

```python
# Positional arguments
"Hello, {}!".format("Alice")            # 'Hello, Alice!'
"{} + {} = {}".format(1, 2, 3)          # '1 + 2 = 3'
"{0} and {0} and {1}".format("A", "B") # 'A and A and B' (reuse by index)

# Named arguments
"{name} is {age} years old.".format(name="Bob", age=25)

# With format specs
"{:.2f}".format(3.14159)        # '3.14'
"{:10.3f}".format(3.14159)      # '     3.142'
"{:,}".format(1234567)          # '1,234,567'
"{:>10}".format("right")        # '     right'
"{:^10}".format("center")       # '  center  '

# Named keyword arguments
"{name} is {age}".format(name="Alice", age=30)  # 'Alice is 30'
# (dict unpacking with **data also works — dicts are covered in Section 05)
```

---

## Format Spec Mini-Language Summary

```
[[fill]align][sign][#][0][width][grouping_option][.precision][type]
```

| Component | Meaning | Example |
|-----------|---------|---------|
| `fill` | Fill character (any char) | `*`, `.`, `0` |
| `align` | `<` left, `>` right, `^` center | `{:>10}` |
| `sign` | `+` always, `-` only negative, ` ` space for positive | `{:+.2f}` |
| `#` | Alternate form (0x prefix for hex, etc.) | `{:#x}` |
| `0` | Zero-pad (equivalent to `0` fill with `>` align) | `{:08d}` |
| `width` | Minimum field width | `{:10}` |
| `,` | Comma thousands separator | `{:,}` |
| `_` | Underscore thousands separator | `{:_}` |
| `.precision` | Decimal places for float, max chars for string | `{:.2f}` |
| `type` | `d` int, `f` float, `e` sci, `g` general, `s` str, `b` bin, `x` hex, `%` percent | `{:d}` |

---

## `%` Formatting (Legacy)

Still seen in old code and logging:

```python
name = "Alice"
age = 30
pi = 3.14159

print("Hello, %s!" % name)           # Hello, Alice!
print("%s is %d years old" % (name, age))  # Alice is 30 years old
print("Pi is %.2f" % pi)             # Pi is 3.14
print("%10s" % name)                 # '     Alice'
print("%-10s|" % name)               # 'Alice     |'
print("%010d" % 42)                  # '0000000042'
print("%e" % pi)                     # 3.141590e+00

# Using a dict
print("%(name)s is %(age)d" % {"name": name, "age": age})
```

| `%` specifier | Meaning |
|---------------|---------|
| `%s` | String |
| `%d` | Integer |
| `%f` | Float (fixed) |
| `%e` | Scientific notation |
| `%g` | General float |
| `%x` | Hex |
| `%o` | Octal |
| `%b` | Binary |
| `%%` | Literal `%` |

---

## Template Strings

For user-supplied templates where security matters — substitution only, no expressions.
*(Requires `from string import Template` — imports are covered in Section 08.)*

```python
from string import Template

t = Template("Hello, $name! You are $age years old.")
print(t.substitute(name="Alice", age=30))

# Safe substitute — leaves unknown keys unchanged instead of raising KeyError
t2 = Template("Hello, $name! $unknown_var here.")
print(t2.safe_substitute(name="Bob"))  # 'Hello, Bob! $unknown_var here.'

# From dict
data = {"name": "Charlie", "age": 25}
t3 = Template("$name is $age")
print(t3.substitute(data))   # 'Charlie is 25'
```

---

## Debugging with f-strings (Python 3.8+)

The `=` specifier prints both the expression and its value — great for debugging:

```python
x = 42
y = 3.14
name = "Alice"

print(f"{x=}")          # x=42
print(f"{y=:.2f}")      # y=3.14
print(f"{name=}")       # name='Alice'
print(f"{x + y=}")      # x + y=45.14
print(f"{x * 2 + 1=}")  # x * 2 + 1=85
```

---

## Common Patterns

```python
# Right-align numbers in columns (individual prints — loops are in Section 03)
print(f"{1:3}. {1:6,d}")       #   1.      1
print(f"{2:3}. {10:6,d}")      #   2.     10
print(f"{3:3}. {100:6,d}")     #   3.    100
print(f"{4:3}. {1000:6,d}")    #   4.  1,000

# Progress percentage
total = 150
done = 87
print(f"Progress: {done/total:.1%} ({done}/{total})")
# Progress: 58.0% (87/150)

# Date-like formatting
year, month, day = 2024, 6, 9
print(f"{year:04d}-{month:02d}-{day:02d}")   # 2024-06-09

# Money formatting
price = 1234.5
print(f"Total: ${price:,.2f}")   # Total: $1,234.50

# Hex color
r, g, b = 255, 128, 0
print(f"#{r:02X}{g:02X}{b:02X}")   # #FF8000

# Binary padding
num = 13
print(f"Binary: {num:08b}")   # Binary: 00001101
```

---

> **Exercises:** [02-08: Exercises — String Formatting](../02-exercises/02-08-string-formatting-exe.md)

---

⬅️ Previous: [02-07: String Methods — Complete Reference](02-07-string-methods.md)
➡️ Next: [02-09: Boolean and None Types](02-09-boolean-and-none.md)
