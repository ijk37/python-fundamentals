# 03-03: while Loops

A `while` loop **repeatedly executes** a block of code as long as a condition remains `True`. Unlike a `for` loop, a `while` loop doesn't need to know the number of iterations in advance.

---

## Basic Syntax

```python
while condition:
    # body — runs as long as condition is True
    statement
    ...
```

---

## Simple Examples

```python
# Count from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1      # IMPORTANT: update the variable!
# 1
# 2
# 3
# 4
# 5

# Countdown
n = 3
while n > 0:
    print(n)
    n -= 1
print("Blast off!")
# 3
# 2
# 1
# Blast off!
```

---

## The Update is Critical

If the variable is never updated, the result is an **infinite loop**:

```python
# DANGER — infinite loop!
i = 1
while i <= 5:
    print(i)
    # forgot i += 1 — runs forever!
```

Press **Ctrl+C** to stop an infinite loop in the terminal.

---

## while vs. for

| | `for` loop | `while` loop |
|---|---|---|
| Best for | Known number of iterations | Unknown / condition-based |
| Iterates over | Sequence / iterable | Any condition |
| Risk | Rarely infinite | Infinite loop risk |
| Common use | Lists, ranges, files | User input, search, games |

```python
# for — when the number of iterations is known
for i in range(10):
    print(i)

# while — when the number of iterations is unknown
response = ""
while response != "quit":
    response = input("Enter command (or 'quit'): ")
```

---

## User Input Validation

One of the most common uses of `while`:

```python
# Keep asking until valid input
age = -1
while age < 0 or age > 120:
    try:
        age = int(input("Enter your age (0-120): "))
        if age < 0 or age > 120:
            print("Invalid age. Try again.")
    except ValueError:
        print("Please enter a number.")
        age = -1

print(f"Age accepted: {age}")
```

### Robust number input

```python
def get_positive_number(prompt):
    while True:
        try:
            n = float(input(prompt))
            if n > 0:
                return n
            print("Must be positive. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

radius = get_positive_number("Enter radius: ")
print(f"Area: {3.14159 * radius**2:.2f}")
```

---

## `break` in a while Loop

`break` exits the loop immediately:

```python
while True:    # "infinite" loop — broken by break
    command = input("Enter command: ")
    if command == "quit":
        break
    print(f"Running: {command}")
print("Goodbye!")
```

```python
# Find first number divisible by both 7 and 11
n = 1
while True:
    if n % 7 == 0 and n % 11 == 0:
        print(f"Found: {n}")
        break
    n += 1
```

---

## `continue` in a while Loop

`continue` skips to the next iteration check:

```python
# Print only numbers not divisible by 3
i = 0
while i < 20:
    i += 1
    if i % 3 == 0:
        continue
    print(i, end=" ")
# 1 2 4 5 7 8 10 11 13 14 16 17 19 20
```

---

## `else` Clause

The `else` block runs only if the loop condition became `False` naturally (not via `break`):

```python
# Search for an item
target = 5
i = 0
numbers = [1, 3, 7, 9, 11]

while i < len(numbers):
    if numbers[i] == target:
        print(f"Found {target} at index {i}")
        break
    i += 1
else:
    print(f"{target} not found")
# 5 not found
```

---

## Accumulating with while

```python
# Sum numbers until 0 is entered
total = 0
count = 0

while True:
    n = float(input("Enter number (0 to stop): "))
    if n == 0:
        break
    total += n
    count += 1

if count > 0:
    print(f"Sum: {total}")
    print(f"Average: {total / count:.2f}")
else:
    print("No numbers entered")
```

---

## Iterating with while (vs for)

```python
# Using while with a list
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Equivalent for loop (preferred)
for fruit in fruits:
    print(fruit)
```

---

## Game Loop Pattern

`while` loops are essential in games and simulations:

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Guess the number (1-100)!")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts+1}/{max_attempts}: "))
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid number")
else:
    print(f"Game over! The number was {secret}")
```

---

## While Loop Patterns

### Do-while simulation

Python has no `do-while` loop, but the behaviour can be simulated:

```python
# This always runs at least once
while True:
    name = input("Enter your name: ")
    if name.strip():    # exit if name is not empty
        break
    print("Name cannot be empty")
```

### Fibonacci with while

```python
a, b = 0, 1
while a < 1000:
    print(a, end=" ")
    a, b = b, a + b
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
```

### Binary search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15]
idx = binary_search(nums, 7)
print(f"Found at index: {idx}")   # Found at index: 3
```

---

## Nested while Loops

```python
# Printing a rectangle of stars
rows = 4
cols = 6
r = 0
while r < rows:
    c = 0
    while c < cols:
        print("*", end="")
        c += 1
    print()
    r += 1
# ******
# ******
# ******
# ******
```

---

## Quick Summary

| Concept | Syntax | Effect |
|---------|--------|--------|
| Basic loop | `while cond:` | Run body while cond is True |
| Infinite loop | `while True:` | Run forever (until break) |
| Exit early | `break` | Leave loop immediately |
| Skip iteration | `continue` | Jump to condition check |
| Post-loop | `else:` | Runs if no break occurred |

---

## Practice Problems

```python
# 1. Reverse digits of a number
n = 12345
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)   # 54321

# 2. Count digits
n = 987654
count = 0
temp = abs(n)
while temp > 0:
    count += 1
    temp //= 10
print(count)   # 6

# 3. Power without ** operator
base, exp = 2, 8
result = 1
while exp > 0:
    result *= base
    exp -= 1
print(result)   # 256

# 4. ATM simulation
balance = 1000.0
while True:
    print(f"\nBalance: ${balance:.2f}")
    print("1. Deposit  2. Withdraw  3. Exit")
    choice = input("Choice: ")
    if choice == "1":
        amount = float(input("Deposit amount: "))
        balance += amount
    elif choice == "2":
        amount = float(input("Withdraw amount: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
    elif choice == "3":
        print("Goodbye!")
        break
```

---

> **Exercises:** [03-03: Exercises — while Loops](../02-exercises/03-03-while-loops-exe.md)

---

⬅️ Previous: [03-02: for Loops](03-02-for-loops.md)
➡️ Next: [04-01: Functions — Basics](04-01-functions-basics.md)
