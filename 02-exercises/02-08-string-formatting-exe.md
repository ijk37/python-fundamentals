# 02-08: Exercises — String Formatting

> **Notes reference:** [02-08: String Formatting](../01-notes/02-08-string-formatting.md)

---

## Q1: Basic f-string substitution
Format a string that says: `"Jahid is 28 years old and lives in New York."` using f-strings.

**Solution**
```python
name = "Jahid"
age  = 28
city = "New York"
print(f"{name} is {age} years old and lives in {city}.")
```

---

## Q2: Expressions inside f-strings
Print the result of `7 ** 3` and the string `"python"` uppercased, both inside a single f-string.

**Solution**
```python
print(f"7 cubed is {7**3} and 'python' in caps is {'python'.upper()}")
# 7 cubed is 343 and 'python' in caps is PYTHON
```

---

## Q3: Float precision
Format the number `3.14159265` to:
- 2 decimal places
- 5 decimal places
- scientific notation with 2 decimal places

**Solution**
```python
pi = 3.14159265
print(f"{pi:.2f}")    # 3.14
print(f"{pi:.5f}")    # 3.14159
print(f"{pi:.2e}")    # 3.14e+00
```

---

## Q4: Integer bases
Print the number `255` as decimal, binary (with `0b` prefix), octal (with `0o` prefix), and hex (uppercase, with `0x` prefix).

**Solution**
```python
n = 255
print(f"{n:d}")    # 255
print(f"{n:#b}")   # 0b11111111
print(f"{n:#o}")   # 0o377
print(f"{n:#X}")   # 0XFF
```

---

## Q5: Width and alignment
Print the word `"Dhaka"` centred in a field of width 20, filled with `"-"`.

**Solution**
```python
print(f"{'Dhaka':-^20}")   # -------Dhaka--------
```

---

## Q6: Thousands separator and percentage
Format `1500000` with a comma separator, and `0.8765` as a percentage with 1 decimal place.

**Solution**
```python
n = 1_500_000
r = 0.8765
print(f"{n:,}")       # 1,500,000
print(f"{r:.1%}")     # 87.6%
```

---

## Q7: format() method
Reproduce the sentence `"Order #0042: 3 items, total $74.50"` using the `.format()` method.

**Solution**
```python
s = "Order #{:04d}: {} items, total ${:.2f}".format(42, 3, 74.5)
print(s)   # Order #0042: 3 items, total $74.50
```

---

## Q8: f-string debug with `=`
Use the `=` specifier inside f-strings to debug the values of `x = 15`, `y = 4`, and `x % y`.

**Solution**
```python
x, y = 15, 4
print(f"{x=}")       # x=15
print(f"{y=}")       # y=4
print(f"{x % y=}")   # x % y=3
```

---

## Q9: Legacy % formatting
Format the string `"Score: 87/100 (87.00%)"` using `%` formatting.

**Solution**
```python
score = 87
print("Score: %d/100 (%.2f%%)" % (score, score))
# Score: 87/100 (87.00%)
```

---

## Q10: Aligned table
Print a multiplication table for 1–5 × 3 with each number right-aligned in a width of 4.

**Solution**
```python
print(f"{'n':>4} {'n×3':>4}")
print("-" * 10)
print(f"{1:>4} {1*3:>4}")
print(f"{2:>4} {2*3:>4}")
print(f"{3:>4} {3*3:>4}")
print(f"{4:>4} {4*3:>4}")
print(f"{5:>4} {5*3:>4}")
```

---

⬅️ Previous: [02-07: Exercises — String Methods](02-07-string-methods-exe.md)
➡️ Next: [02-09: Exercises — Boolean and None](02-09-boolean-and-none-exe.md)
