# 02-01: Exercises — Basic Syntax

> **Notes reference:** [02-01: Basic Syntax](../01-notes/02-01-basic-syntax.md)

---

## Q1: Print a greeting
Print your name and current city on two separate lines using a single `print()` call.

**Solution**
```python
print("Jahid\nNew York")
```

---

## Q2: Print with separator
Print the three values `"Dhaka"`, `110`, and `True` on one line, separated by `" | "`.

**Solution**
```python
print("Dhaka", 110, True, sep=" | ")
# Output: Dhaka | 110 | True
```

---

## Q3: Print without newline
Print `"Loading"` followed by `"..."` on the same line without a newline at the end, then print `" Done"` after.

**Solution**
```python
print("Loading", end="")
print("...", end="")
print(" Done")
# Output: Loading... Done
```

---

## Q4: Comments
Write a line that calculates the area of a rectangle (width=8, height=5) and add a comment explaining each variable.

**Solution**
```python
width = 8    # width of the rectangle in cm
height = 5   # height of the rectangle in cm
area = width * height  # area = width × height
print(area)  # 40
```

---

## Q5: Fix the indentation error
The following code has an indentation error. Identify and fix it.

```python
x = 10
    print(x)
```

**Solution**
```python
x = 10
print(x)   # print() must be at the top level, not indented
```

---

## Q6: Line continuation
Write a long arithmetic expression (sum of 6 numbers) split across two physical lines using `\`.

**Solution**
```python
total = 10 + 20 + 30 + \
        40 + 50 + 60
print(total)  # 210
```

**Alternative** — use parentheses (preferred):
```python
total = (10 + 20 + 30 +
         40 + 50 + 60)
print(total)  # 210
```

---

## Q7: String with quotes inside
Print the sentence:  `She said, "Python is great!"`

**Solution**
```python
print('She said, "Python is great!"')

# Alternative — escape the inner quotes
print("She said, \"Python is great!\"")
```

---

## Q8: Case sensitivity
Predict what happens when this code runs and explain why.

```python
Name = "Jahid"
print(name)
```

**Solution**
```
NameError: name 'name' is not defined
```
`Name` and `name` are two different variables. Python is case-sensitive — the variable was defined as `Name` (capital N) but referenced as `name` (lowercase).

---

➡️ Next: [02-02: Exercises — Variables and Data Types](02-02-variables-and-datatypes-exe.md)
