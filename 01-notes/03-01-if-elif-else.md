# 03-01: Conditional Statements — if, elif, else

Conditional statements allow a program to **make decisions** — executing different code depending on whether a condition is `True` or `False`.

---

## Basic `if` Statement

```python
if condition:
    # this block runs only if condition is True
    statement1
    statement2
```

### Example

```python
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")
```

The indented block only runs when `age >= 18` is `True`.

---

## `if-else` Statement

```python
if condition:
    # runs when condition is True
    ...
else:
    # runs when condition is False
    ...
```

### Example

```python
score = 45

if score >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## `if-elif-else` Statement

Use `elif` ("else if") to check multiple conditions in sequence. Python stops at the **first** true condition.

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:           # optional — catches everything else
    ...
```

### Example: Grade classifier

```python
score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
# Score: 78, Grade: C
```

**Note:** Only one block runs. Once a condition is `True`, the rest are skipped.

---

## Indentation is Mandatory

Python uses **indentation** (spaces or tabs) to define code blocks — there are no curly braces `{}`.

```python
# Correct
if True:
    print("inside if")
    print("still inside")

print("outside if")
```

```python
# Wrong — IndentationError
if True:
print("missing indent")   # IndentationError!
```

```python
# Wrong — inconsistent indent
if True:
    x = 5
      y = 6   # IndentationError: unexpected indent
```

**Convention:** Use **4 spaces** per level (PEP 8 standard).

---

## Conditions in Detail

Any expression that evaluates to `True` or `False` can be used as a condition.

### Comparison operators

```python
x = 10

print(x == 10)   # True  (equal to)
print(x != 5)    # True  (not equal)
print(x > 8)     # True  (greater than)
print(x < 8)     # False (less than)
print(x >= 10)   # True  (greater or equal)
print(x <= 9)    # False (less or equal)
```

### Truthy/falsy as conditions

```python
name = ""
if name:             # False — empty string is falsy
    print("Hello", name)
else:
    print("Name is empty")

items = [1, 2, 3]
if items:            # True — non-empty list is truthy
    print("List has", len(items), "items")
```

### Logical operators in conditions

```python
age = 25
income = 50000

# and — both must be True
if age >= 18 and income >= 30000:
    print("Eligible for loan")

# or — at least one must be True
if age < 18 or age > 65:
    print("Not working age")

# not — reverses condition
is_holiday = False
if not is_holiday:
    print("Go to work")
```

### Chained comparisons

```python
x = 7
if 5 < x < 10:         # same as: 5 < x and x < 10
    print("In range")

age = 25
if 18 <= age <= 64:    # working age
    print("Working age")
```

---

## Nested `if` Statements

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young — no entry")
```

Same logic using `and`:
```python
if age >= 18 and has_id:
    print("Entry allowed")
elif age >= 18:
    print("ID required")
else:
    print("Too young — no entry")
```

---

## Ternary (Conditional) Expression

A compact one-line `if-else`:

```python
# Syntax: value_if_true if condition else value_if_false

x = 10
label = "even" if x % 2 == 0 else "odd"
print(label)   # even

# Works in assignments
max_val = a if a > b else b

# Works in print
print("Adult" if age >= 18 else "Minor")

# Works nested (but gets hard to read)
category = "high" if x > 100 else ("medium" if x > 50 else "low")
```

---

## `match` Statement (Python 3.10+)

The `match` statement (structural pattern matching) is Python's modern version of `switch`:

```python
command = "quit"

match command:
    case "quit":
        print("Quitting...")
    case "start":
        print("Starting...")
    case "help":
        print("Showing help...")
    case _:              # default case
        print(f"Unknown command: {command}")
```

### Matching with values

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 6 | 7:          # multiple values with |
        print("Weekend")
    case _:
        print("Another day")
```

---

## Common Patterns

### Validating input

```python
age_str = input("Enter your age: ")
try:
    age = int(age_str)
    if 0 <= age <= 120:
        print(f"Age {age} accepted")
    else:
        print("Age out of valid range")
except ValueError:
    print("Please enter a number")
```

### Multiple conditions with the same result

```python
day = "Saturday"

# Using `or`
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

# Using `in` (cleaner for many values)
if day in ["Saturday", "Sunday"]:
    print("Weekend!")
```

### Checking type

```python
value = 42

if isinstance(value, int):
    print("It's an integer")
elif isinstance(value, float):
    print("It's a float")
elif isinstance(value, str):
    print("It's a string")
```

---

## Flowchart of if-elif-else

```
       ┌──────────────┐
       │   condition1  │
       └──────┬───────┘
          True│          False
          ▼              ▼
     [block 1]    ┌──────────────┐
                  │   condition2  │
                  └──────┬───────┘
                     True│          False
                     ▼              ▼
                [block 2]    ┌──────────────┐
                             │  else block   │
                             └──────────────┘
```

---

## Quick Summary

| Statement | When it runs |
|-----------|-------------|
| `if` | condition is True |
| `elif` | previous conditions False, this one True |
| `else` | all previous conditions False |
| ternary | inline if-else for single expressions |

---

## Practice Problems

```python
# 1. BMI Calculator
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / height ** 2
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"BMI: {bmi:.1f} — {category}")

# 2. Fizzbuzz (classic)
for n in range(1, 21):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# 3. Triangle type
a, b, c = 3, 4, 5
if a == b == c:
    kind = "equilateral"
elif a == b or b == c or a == c:
    kind = "isosceles"
else:
    kind = "scalene"
print(f"Triangle is {kind}")

# 4. Leap year
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is {'a leap' if is_leap else 'not a leap'} year")
```

---

> **Exercises:** [03-01: Exercises — Conditional Statements](../02-exercises/03-01-if-elif-else-exe.md)

---

⬅️ Previous: [02-10: Type Conversion](02-10-type-conversion.md)
➡️ Next: [03-02: for Loops](03-02-for-loops.md)
