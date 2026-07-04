# 02-09: Exercises — Boolean and None

> **Notes reference:** [02-09: Boolean and None Types](../01-notes/02-09-boolean-and-none.md)

---

## Q1: bool arithmetic
`True` and `False` are subclasses of `int`. Predict and verify the output of:
```python
True + True
False + 10
True * 7
True + False + True
```

**Solution**
```python
print(True + True)          # 2
print(False + 10)           # 10
print(True * 7)             # 7
print(True + False + True)  # 2
```

---

## Q2: Logical operators truth table
Fill in the results:

| A     | B     | A and B | A or B | not A |
|-------|-------|---------|--------|-------|
| True  | True  |         |        |       |
| True  | False |         |        |       |
| False | True  |         |        |       |
| False | False |         |        |       |

**Solution**
```python
for A in [True, False]:
    for B in [True, False]:
        print(f"{str(A):<5} {str(B):<5} | {str(A and B):<5} | {str(A or B):<5} | {str(not A):<5}")
```
```
True  True  | True  | True  | False
True  False | False | True  | False
False True  | False | True  | True
False False | False | False | True
```

---

## Q3: Truthy and falsy
Classify each value as truthy or falsy:
`0`, `""`, `" "`, `[]`, `[0]`, `None`, `0.0`, `"False"`, `False`

**Solution**
```python
values = [0, "", " ", [], [0], None, 0.0, "False", False]
for v in values:
    print(repr(v), "→", bool(v))
```
```
0       → False
""      → False
" "     → True    (non-empty string!)
[]      → False
[0]     → True    (non-empty list!)
None    → False
0.0     → False
"False" → True    (non-empty string!)
False   → False
```

---

## Q4: Short-circuit evaluation
Predict the output without running the code. Explain why no error occurs on line 2.

```python
x = 0
safe = (x != 0) and (1 / x > 0.5)
print(safe)
```

**Solution**
```
safe = False
No ZeroDivisionError because `and` short-circuits:
once (x != 0) evaluates to False, (1 / x > 0.5) is never evaluated.
```

---

## Q5: `or` as default value
Write a one-liner that assigns `"Guest"` to `display_name` if `username` is an empty string, otherwise uses `username`.

**Solution**
```python
username     = ""
display_name = username or "Guest"
print(display_name)   # Guest

username     = "Jahid"
display_name = username or "Guest"
print(display_name)   # Jahid
```

---

## Q6: Comparison chaining
Check whether `score = 85` is in the grade B range (80 ≤ score < 90) using a chained comparison.

**Solution**
```python
score = 85
is_B = 80 <= score < 90
print(is_B)   # True
```

---

## Q7: None checks
Write code that sets `result = None`, then checks if it is `None` using the correct operator.

**Solution**
```python
result = None

if result is None:
    print("No result yet")

# Incorrect (but works) — avoid this:
# if result == None: ...

# Also correct — checking if it has a value:
if result is not None:
    print("Result:", result)
else:
    print("Result is absent")
```

---

## Q8: bool() conversions
Use `bool()` to show that non-zero numbers are truthy and that all "empty" containers are falsy.

**Solution**
```python
print(bool(42))      # True
print(bool(-1))      # True
print(bool(0))       # False

print(bool("hi"))    # True
print(bool(""))      # False

print(bool([1, 2]))  # True
print(bool([]))      # False

print(bool(None))    # False
```

---

⬅️ Previous: [02-08: Exercises — String Formatting](02-08-string-formatting-exe.md)
➡️ Next: [02-10: Exercises — Type Conversion](02-10-type-conversion-exe.md)
