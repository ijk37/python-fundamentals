# 02-05: Exercises — Number Types: int and float

> **Notes reference:** [02-05: Number Types — int and float](../01-notes/02-05-number-types-int-float.md)

---

## Q1: Integer bases
Write the number 255 as a binary, octal, and hexadecimal literal. Print all three and confirm they are equal.

**Solution**
```python
binary  = 0b11111111
octal   = 0o377
hexadec = 0xFF

print(binary, octal, hexadec)          # 255 255 255
print(binary == octal == hexadec)      # True
```

---

## Q2: Underscores for readability
Write the number one billion (1,000,000,000) using underscores, and print it.

**Solution**
```python
billion = 1_000_000_000
print(billion)   # 1000000000
```

---

## Q3: Float precision issue
Print `0.1 + 0.2` and explain the result. Then show two ways to handle the imprecision.

**Solution**
```python
print(0.1 + 0.2)          # 0.30000000000000004  (IEEE 754 approximation)

# Fix 1: round()
print(round(0.1 + 0.2, 2) == 0.3)   # True

# Fix 2: math.isclose()
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

---

## Q4: int vs float division
What is the type and value of each expression? Predict, then verify.

```python
10 / 2
10 // 2
10 // 3.0
7 ** -1
```

**Solution**
```python
print(type(10 / 2),   10 / 2)     # float 5.0   (/ always returns float)
print(type(10 // 2),  10 // 2)    # int   5     (int // int → int)
print(type(10 // 3.0),10 // 3.0)  # float 3.0   (involves float → float)
print(type(7 ** -1),  7 ** -1)    # float 0.142... (negative exponent → float)
```

---

## Q5: math module functions
Using the `math` module, compute:
- square root of 144
- ceiling and floor of 7.3
- factorial of 6
- GCD of 48 and 36

**Solution**
```python
import math

print(math.sqrt(144))       # 12.0
print(math.ceil(7.3))       # 8
print(math.floor(7.3))      # 7
print(math.factorial(6))    # 720
print(math.gcd(48, 36))     # 12
```

---

## Q6: Built-in numeric functions
Use `abs()`, `round()`, `pow()`, and `divmod()` to:
- absolute value of -9.7
- round 3.14159 to 3 decimal places
- 3 to the power 4
- quotient and remainder of 29 ÷ 6

**Solution**
```python
print(abs(-9.7))             # 9.7
print(round(3.14159, 3))     # 3.142
print(pow(3, 4))             # 81
q, r = divmod(29, 6)
print(q, r)                  # 4 5  (29 = 4*6 + 5)
```

---

## Q7: Scientific notation
Express the speed of light (≈ 3 × 10⁸ m/s) and the electron charge (≈ 1.6 × 10⁻¹⁹ C) as float literals using scientific notation.

**Solution**
```python
speed_of_light   = 3e8
electron_charge  = 1.6e-19

print(speed_of_light)    # 300000000.0
print(electron_charge)   # 1.6e-19
```

---

## Q8: Operator precedence with exponentiation
Predict the output of each line:

```python
-3 ** 2
(-3) ** 2
2 ** 3 ** 2
(2 ** 3) ** 2
```

**Solution**
```python
print(-3 ** 2)         # -9   (** binds tighter than unary -: -(3**2))
print((-3) ** 2)       # 9    (parentheses applied first)
print(2 ** 3 ** 2)     # 512  (right-to-left: 2**(3**2) = 2**9)
print((2 ** 3) ** 2)   # 64
```

---

⬅️ Previous: [02-04: Exercises — Operators](02-04-operators-exe.md)
➡️ Next: [02-06: Exercises — String Basics](02-06-string-basics-exe.md)
