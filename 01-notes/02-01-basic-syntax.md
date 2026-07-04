# 02-01: Basic Syntax

Python syntax is the set of rules that define how Python code is written and interpreted.

---

## print() Function

Used to display output on the screen.

### Example:

```python
print("Hello, World!")
```

or,

```python
print('Hello, World!')
```

Explanation:

- print() is a built-in function

- Text inside quotes is called a string

- can be used both single or double quote

👉 Output:

```
Hello, World!
```

---

## input() Function

The `input()` function is used to take input from the user.

### Example

```python
name = input("Enter your name: ")
print(name)
```

👉 Sample run:

```
Enter your name: Imran
Imran
```

Explanation:

- input() waits for user input

- The text inside " " is a prompt

- The entered value is stored in the variable

⚠️ Important: input() Always Returns String

```python
age = input("Enter your age: ")
print(type(age))
```

👉 Sample run:

```
Enter your age: 25
<class 'str'>
```

👉 Even a number is entered, it will be stored as a string

---

## Comments

Comments are used to explain code. They are ignored by Python.

Single-line comment: # is used for comment

### Example

```python
# This is a comment
print("Hello")
```

👉 Output:

```
Hello
```

Inline comment:

```python
print("Hello")  # This prints Hello
```

## Indentation (VERY IMPORTANT)

Python uses indentation (spaces) to define blocks of code.

### Example:

```python
age = 18

if age >= 18:
    print("Adult")
```

👉 Output:

```
Adult
```

Explanation:

- The indented line belongs to the if block

- Without indentation → ❌ Error

### ❌ Wrong:

```python
if age >= 18:
print("Adult")
```

```
IndentationError: expected an indented block after 'if' statement
```

---

## Case Sensitivity

Python is case-sensitive.

### Example:

```python
name = "Imran"
Name = "Jahid"

print(name)
print(Name)
```

👉 Output:

```
Imran
Jahid
```

👉 These are treated as different variables

---

## Statements & Lines

Each line is usually one statement.

### Example:

```python
x = 10
y = 20
print(x + y)
```

👉 Output:

```
30
```

---

## Multiple Statements in One Line

Multiple statements in single line can be written ; (but not recommended).

```python
x = 10; y = 20; print(x + y)
```

👉 Output:

```
30
```

👉 Better to use separate lines for readability

---

## Line Continuation

Used to break long lines into multiple lines.

Using backslash:

```python
total = 10 + 20 + 30 + \
        40 + 50
```

Using parentheses (recommended):

```python
total = (10 + 20 + 30 +
         40 + 50)
```

---

## Strings and Quotes

Strings can be written using both double and single quote:

```python
"Hello"
'Hello'
```

Multi-line string is written within triple quotes:

```python
text = """This is
a multi-line
string"""
```

or,

```python
text = '''This is
a multi-line
string'''
```

---

## Basic Output Formatting

### 🔹 1. Comma Formatting (Basic Print)

```python
name = "Imran"
print("Name:", name)
```

👉 Output:

```
Name: Imran
```

- "Name:" → string (fixed text)
- name → variable
- , → separates items in print()


### 🔹 2. f-String Formatting (Modern Way)

```python
age = 25
print(f"My age is {age}")
```

👉 Output:

```
My age is 25
```

- f"" → formatted string
- "My age is " → string
- {age} → variable inserted inside string

- 👉 Python replaces {age} with its value

---
---

> **Exercises:** [02-01: Exercises — Basic Syntax](../02-exercises/02-01-basic-syntax-exe.md)

---

⬅️ Previous: [01-05: Writing and Executing Python Code in VS Code](01-05-write-execute-python-code-in-vscode.md)
➡️ Next: [02-02: Variables and Data Types](02-02-variables-and-datatypes.md)
