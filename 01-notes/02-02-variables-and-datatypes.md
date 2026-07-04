# 02-02: Variables and Data Types

---

## What is a Variable?

A variable can be thought of as a label attached to a value.

It represents a named reference to data stored in memory, allowing that data to be accessed and modified throughout a program.

```python
x = 10
name = "Imran"
```

x refers to the integer value 10

name refers to the string value "Imran"

---

## Rules for Naming Variables

### ✅ Valid Examples

```python
age = 25
user_name = "John"
_marks = 90
```

### ❌ Invalid Examples

```python
2age = 25      # cannot start with a number
user-name = 10 # hyphen not allowed
3 = num        # not allowed, variable has to be on the left
_3 = 10        # legal, but not recommended
```

### 🔹 Naming Rules
- Only letters (a–z, A–Z), digits (0–9), and **underscore (_)** are allowed in variable names
- A variable name must begin with a letter or an underscore (_)
- A variable name cannot begin with a digit
- Spaces and special characters (except underscore) are not allowed
- Variable names are case-sensitive (age and Age are different)

---

## Assigning Values to Variables

Values are assigned using the = operator.

```python
a = 5
b = 3.14
c = "Hello"
```

- **Python automatically determines the data type of the assigned value.**

### 🔄 Multiple Assignment

- Multiple variables can be assigned values in a single statement.

```python
x, y, z = 1, 2, 3
```

- It is also possible to assign the same value to multiple variables:

```python
a = b = c = 10
```

---

## Basic Data Types in Python

### 1️⃣ Integer (int)

Represents whole numbers.

```python
x = 10
y = -5
```

### 2️⃣ Float (float)

Represents decimal numbers.

```python
pi = 3.14
temp = -2.5
```

### 3️⃣ String (str)

Represents textual data enclosed in quotes.

```python
name = "Imran"
msg = 'Hello World'
```

### 4️⃣ Boolean (bool)

Represents logical values: True or False.

```python
is_active = True
is_logged_in = False
```

---

## Checking Data Type

- The type() function is used to determine the data type of a variable.

```python
x = 10
print(type(x))
```

👉 Output:

```
<class 'int'>
```

---

## Type Conversion (Casting)

- Type conversion is used to convert a value from one data type to another.

```python
x = "10"     # data type string
```

### Convert string to integer

```python
y = int(x)
```

### Convert integer to float

```python
z = float(y)
```

Putting it together:

```python
x = "10"
y = int(x)
z = float(y)

print(y, type(y))
print(z, type(z))
```

👉 Output:

```
10 <class 'int'>
10.0 <class 'float'>
```

---

### ⚠️ Important Notes: 🔹 Dynamic Typing

- Python is a dynamically typed language, meaning a variable can refer to different data types during execution.

```python
x = 10      # integer
x = "Hello" # now a string

print(x, type(x))
```

👉 Output:

```
Hello <class 'str'>
```

---
---

> **Exercises:** [02-02: Exercises — Variables and Data Types](../02-exercises/02-02-variables-and-datatypes-exe.md)

---

⬅️ Previous: [02-01: Basic Syntax](02-01-basic-syntax.md)
➡️ Next: [02-03: Input and Output](02-03-input-output.md)
