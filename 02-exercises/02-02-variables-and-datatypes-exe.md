# 02-02: Exercises — Variables and Data Types

> **Notes reference:** [02-02: Variables and Data Types](../01-notes/02-02-variables-and-datatypes.md)

---

## Q1: Create and print variables
Create variables for a person: name (string), age (int), height in metres (float), and is_student (bool). Print all four.

**Solution**
```python
name       = "Jahid"
age        = 28
height     = 1.75
is_student = True

print(name, age, height, is_student)
# Output: Jahid 28 1.75 True
```

---

## Q2: Check data types
What does `type()` return for each of the following? Predict first, then verify.

```python
type(42)
type(3.14)
type("Dhaka")
type(True)
type(None)
```

**Solution**
```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Dhaka"))  # <class 'str'>
print(type(True))     # <class 'bool'>
print(type(None))     # <class 'NoneType'>
```

---

## Q3: Multiple assignment
Assign the values `"New York"`, `10001`, and `True` to variables `city`, `zip_code`, and `is_capital` in a single line.

**Solution**
```python
city, zip_code, is_capital = "New York", 10001, True
print(city, zip_code, is_capital)
```

---

## Q4: Same value, multiple variables
Assign the value `0` to three variables `x`, `y`, `z` in one line.

**Solution**
```python
x = y = z = 0
print(x, y, z)  # 0 0 0
```

---

## Q5: Spot the invalid variable names
Which of the following are invalid variable names? Explain each.

```
1st_place
total_score
my-variable
_hidden
class
user name
```

**Solution**
```
1st_place   → Invalid: cannot start with a digit
total_score → Valid
my-variable → Invalid: hyphen (-) is not allowed
_hidden     → Valid
class       → Invalid: reserved keyword
user name   → Invalid: spaces are not allowed
```

---

## Q6: Dynamic typing
Assign an integer to a variable, print its type, then reassign a string to the same variable and print its type again.

**Solution**
```python
data = 100
print(type(data))   # <class 'int'>

data = "one hundred"
print(type(data))   # <class 'str'>
# Python allows the same variable to hold different types
```

---

## Q7: Swap two variables
Swap the values of `a = "Dhaka"` and `b = "Chittagong"` without using a third variable.

**Solution**
```python
a = "Dhaka"
b = "Chittagong"

a, b = b, a

print(a)  # Chittagong
print(b)  # Dhaka
```

---

## Q8: Type conversion basics
Convert the string `"55"` to an integer, the integer `7` to a float, and the float `9.8` to a string. Print the type of each result.

**Solution**
```python
n = int("55")
print(type(n), n)      # <class 'int'> 55

f = float(7)
print(type(f), f)      # <class 'float'> 7.0

s = str(9.8)
print(type(s), s)      # <class 'str'> 9.8
```

---

⬅️ Previous: [02-01: Exercises — Basic Syntax](02-01-basic-syntax-exe.md)
➡️ Next: [02-03: Exercises — Input and Output](02-03-input-output-exe.md)
