# 03-02: for Loops

A `for` loop iterates over every item in a **sequence** or **iterable**, executing the loop body for each item.

---

## Basic Syntax

```python
for variable in iterable:
    # loop body — runs for each item
    statement
    ...
```

- `variable` — a name that holds each item in turn
- `iterable` — any sequence or collection (list, string, range, tuple, etc.)

---

## Iterating over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# apple
# banana
# cherry
```

```python
scores = [85, 92, 78, 95, 60]

total = 0
for score in scores:
    total += score

print("Total:", total)         # Total: 410
print("Average:", total / len(scores))  # Average: 82.0
```

---

## Iterating over a String

A string is a sequence of characters — it can be looped over directly:

```python
for char in "Python":
    print(char)
# P
# y
# t
# h
# o
# n

# Count vowels
vowel_count = 0
for ch in "Hello World":
    if ch.lower() in "aeiou":
        vowel_count += 1
print(vowel_count)   # 3
```

---

## The `range()` Function

`range()` generates a sequence of numbers for use in loops.

### Forms of `range()`

```python
range(stop)           # 0, 1, 2, ..., stop-1
range(start, stop)    # start, start+1, ..., stop-1
range(start, stop, step)  # start, start+step, ..., < stop
```

### Examples

```python
# range(stop) — from 0 to stop-1
for i in range(5):
    print(i, end=" ")
# 0 1 2 3 4

# range(start, stop)
for i in range(3, 8):
    print(i, end=" ")
# 3 4 5 6 7

# range(start, stop, step)
for i in range(0, 20, 4):
    print(i, end=" ")
# 0 4 8 12 16

# Counting down (negative step)
for i in range(10, 0, -1):
    print(i, end=" ")
# 10 9 8 7 6 5 4 3 2 1

# Odd numbers
for i in range(1, 20, 2):
    print(i, end=" ")
# 1 3 5 7 9 11 13 15 17 19
```

### range() with negative step

```python
for i in range(5, -1, -1):
    print(i, end=" ")
# 5 4 3 2 1 0

# Countdown
for i in range(3, 0, -1):
    print(i)
print("Go!")
# 3
# 2
# 1
# Go!
```

### Converting range to list

```python
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(1, 6)))      # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
```

---

## Iterating with `enumerate()`

`enumerate()` provides both the **index** and the **value** at each step:

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

# Start numbering from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

---

## Iterating with `zip()`

`zip()` combines two or more iterables element-by-element:

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# Three iterables
for name, score, rank in zip(names, scores, range(1, 4)):
    print(f"#{rank} {name} — {score}")
# #1 Alice — 85
# #2 Bob — 92
# #3 Charlie — 78
```

---

## Nested for Loops

A loop inside another loop:

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")
    print("---")
# 1 × 1 = 1
# 1 × 2 = 2
# 1 × 3 = 3
# ---
# ...

# Pattern printing
for row in range(5):
    for col in range(row + 1):
        print("*", end="")
    print()
# *
# **
# ***
# ****
# *****
```

---

## Looping Over Dictionaries

```python
student = {"name": "Alice", "age": 22, "grade": "A"}

# Iterate over keys (default)
for key in student:
    print(key)

# Iterate over values
for value in student.values():
    print(value)

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
# name: Alice
# age: 22
# grade: A
```

---

## Looping Over a File

```python
with open("data.txt", "rt", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")  # remove newline
        print(line)
```

---

## `break` — Exit the Loop Early

`break` immediately exits the loop, skipping any remaining iterations:

```python
numbers = [3, 7, 2, 9, 4, 1, 8]

# Find first number > 5
for n in numbers:
    if n > 5:
        print("Found:", n)
        break
# Found: 7
```

---

## `continue` — Skip to Next Iteration

`continue` skips the rest of the current iteration and moves to the next:

```python
# Print only even numbers
for i in range(10):
    if i % 2 != 0:
        continue
    print(i, end=" ")
# 0 2 4 6 8

# Skip empty strings
words = ["hello", "", "world", "", "python"]
for word in words:
    if not word:
        continue
    print(word)
# hello
# world
# python
```

---

## `else` Clause on a `for` Loop

The `else` block runs **only if the loop completed without hitting a `break`**:

```python
target = 7
numbers = [1, 3, 5, 9, 11]

for n in numbers:
    if n == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in list")
# 7 not found in list

# Useful for search patterns:
def find_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")

find_prime(17)   # 17 is prime
find_prime(15)   # 15 is not prime
```

---

## `pass` — Do Nothing

`pass` is a placeholder for an empty block:

```python
for i in range(5):
    pass   # loop runs but does nothing (placeholder)
```

---

## Common Loop Patterns

### Accumulating a sum

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for n in numbers:
    total += n
print(total)   # 55
# Alternatively: sum(numbers)
```

### Building a new list

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)   # [1, 4, 9, 16, 25]
```

### Filtering items

```python
numbers = [1, -2, 3, -4, 5, -6]
positives = []
for n in numbers:
    if n > 0:
        positives.append(n)
print(positives)   # [1, 3, 5]
```

### Finding min/max manually

```python
numbers = [8, 3, 12, 5, 1, 9]
max_val = numbers[0]
for n in numbers:
    if n > max_val:
        max_val = n
print("Max:", max_val)   # Max: 12
```

### Flattening nested list

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = []
for row in matrix:
    for val in row:
        flat.append(val)
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Quick Summary

| Construct | Purpose |
|-----------|---------|
| `for x in iterable` | Loop over every item |
| `range(n)` | Numbers 0 to n-1 |
| `range(a, b)` | Numbers a to b-1 |
| `range(a, b, s)` | Numbers a to <b, step s |
| `enumerate(it)` | Index + value pairs |
| `zip(it1, it2)` | Parallel iteration |
| `break` | Exit loop immediately |
| `continue` | Skip to next iteration |
| `else` | Runs if no `break` occurred |

---

## Practice Problems

```python
# 1. Print multiplication table for 7
for i in range(1, 13):
    print(f"7 × {i:2d} = {7*i}")

# 2. Sum of all even numbers from 1 to 100
total = sum(i for i in range(2, 101, 2))
print(total)   # 2550

# 3. Fibonacci sequence up to n terms
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()   # 0 1 1 2 3 5 8 13 21 34

# 4. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 50) if is_prime(n)]
print(primes)

# 5. Matrix diagonal sum
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
print(diagonal_sum)   # 15 (1+5+9)
```

---

> **Exercises:** [03-02: Exercises — for Loops](../02-exercises/03-02-for-loops-exe.md)

---

⬅️ Previous: [03-01: Conditional Statements — if, elif, else](03-01-if-elif-else.md)
➡️ Next: [03-03: while Loops](03-03-while-loops.md)
