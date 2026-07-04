# 02-04: Exercises — Operators

> **Notes reference:** [02-04: Operators](../01-notes/02-04-operators.md)

---

## Q1: Arithmetic operators
Given `a = 17` and `b = 5`, compute and print: sum, difference, product, quotient (float), floor quotient, remainder, and a to the power b.

**Solution**
```python
a, b = 17, 5
print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4
print(a // b)   # 3
print(a % b)    # 2
print(a ** b)   # 1419857
```

---

## Q2: Floor division vs truncation
What is the difference between `int(-7 / 2)` and `-7 // 2`? Verify with code.

**Solution**
```python
print(int(-7 / 2))   # -3  (truncates toward zero: -3.5 → -3)
print(-7 // 2)       # -4  (floor: rounds toward -infinity)
# They differ for negative numbers!
```

---

## Q3: Operator precedence
Predict the output of each expression, then verify.

```python
2 + 3 * 4
(2 + 3) * 4
2 ** 3 ** 2
10 - 4 - 2
100 / 10 * 2
```

**Solution**
```python
print(2 + 3 * 4)      # 14   (* before +)
print((2 + 3) * 4)    # 20   (parentheses first)
print(2 ** 3 ** 2)    # 512  (right-to-left: 2**(3**2) = 2**9)
print(10 - 4 - 2)     # 4    (left-to-right: (10-4)-2)
print(100 / 10 * 2)   # 20.0 (left-to-right: (100/10)*2)
```

---

## Q4: Comparison operators
Write expressions using `>`, `<`, `>=`, `<=`, `==`, `!=` to check if a score of 72 is:
- above 60
- not equal to 100
- at least 70
- at most 80

**Solution**
```python
score = 72
print(score > 60)    # True
print(score != 100)  # True
print(score >= 70)   # True
print(score <= 80)   # True
```

---

## Q5: Logical operators
A person can vote if age >= 18 AND is a citizen. A service is free if age < 12 OR age >= 65. Write both conditions for age = 20, citizen = True.

**Solution**
```python
age     = 20
citizen = True

can_vote  = age >= 18 and citizen
is_free   = age < 12 or age >= 65

print(can_vote)   # True
print(is_free)    # False
```

---

## Q6: Assignment operators
Start with `total = 100`. Apply these in order: add 50, multiply by 2, subtract 30, floor-divide by 3. Print after each step.

**Solution**
```python
total = 100
total += 50;   print(total)   # 150
total *= 2;    print(total)   # 300
total -= 30;   print(total)   # 270
total //= 3;   print(total)   # 90
```

---

## Q7: Membership and identity operators
Check whether `"dhaka"` is in a list of cities, and whether two variables point to the same object.

**Solution**
```python
cities = ["dhaka", "berlin", "tokyo", "nairobi"]
print("dhaka" in cities)     # True
print("paris" not in cities) # True

a = None
b = None
print(a is b)    # True  (None is a singleton)
print(a is not b)# False
```

---

## Q8: Bitwise operators
Given `x = 12` (`0b1100`) and `y = 10` (`0b1010`), compute AND, OR, XOR, and left-shift x by 1.

**Solution**
```python
x, y = 12, 10
print(x & y)   # 8    (0b1000)
print(x | y)   # 14   (0b1110)
print(x ^ y)   # 6    (0b0110)
print(x << 1)  # 24   (0b11000 — same as x * 2)
print(x >> 1)  # 6    (0b0110  — same as x // 2)
```

---

## Q9: Short-circuit evaluation
Without running the code, predict: will line 2 raise a ZeroDivisionError? Why?

```python
x = 0
result = (x != 0) and (100 / x > 1)
print(result)
```

**Solution**
```
No error. result = False.
Because `and` short-circuits: if the left operand (x != 0) is False,
Python never evaluates the right operand (100 / x > 1).
```

---

⬅️ Previous: [02-03: Exercises — Input and Output](02-03-input-output-exe.md)
➡️ Next: [02-05: Exercises — Number Types: int and float](02-05-number-types-int-float-exe.md)
