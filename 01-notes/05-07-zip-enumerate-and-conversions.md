# 05-07: zip(), enumerate(), and Collection Conversions

---

## `enumerate()` — Index + Value Together

`enumerate()` wraps an iterable and yields `(index, value)` pairs:

```python
fruits = ["apple", "banana", "cherry"]

# Basic usage
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

### Why enumerate instead of range(len())?

```python
# Old (verbose) way
for i in range(len(fruits)):
    print(i, fruits[i])

# Pythonic way — enumerate is cleaner
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

### enumerate() with any iterable

```python
# With string
for i, char in enumerate("hello"):
    print(f"Index {i}: {char}")

# With dict
d = {"a": 1, "b": 2, "c": 3}
for i, key in enumerate(d):
    print(f"Item #{i}: {key} = {d[key]}")

# Convert enumerate to list of tuples
result = list(enumerate(["x", "y", "z"]))
print(result)   # [(0, 'x'), (1, 'y'), (2, 'z')]

# Build indexed dict
words = ["zero", "one", "two", "three"]
num_to_word = dict(enumerate(words))
print(num_to_word)   # {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
```

---

## `zip()` — Parallel Iteration

`zip()` combines multiple iterables element-by-element:

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
```

### zip() stops at the shortest iterable

```python
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]

for x, y in zip(a, b):
    print(x, y)
# 1 a
# 2 b
# 3 c
# (stops at length of shorter iterable)
```

### Three or more iterables

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")
# Alice: 85 (B)
# Bob: 92 (A)
# Charlie: 78 (C)
```

### Building a dict with zip()

```python
keys   = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

d = dict(zip(keys, values))
print(d)   # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Two lists → dict
students = ["Alice", "Bob", "Charlie"]
grades   = ["A", "B", "A+"]
grade_dict = dict(zip(students, grades))
print(grade_dict)   # {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A+'}
```

### Unzipping — transpose pairs

```python
pairs = [(1, "a"), (2, "b"), (3, "c")]

# Unzip using *
numbers, letters = zip(*pairs)
print(numbers)   # (1, 2, 3)
print(letters)   # ('a', 'b', 'c')

# Transposing a matrix
matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
transposed = list(zip(*matrix))
print(transposed)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

### `zip_longest()` — pad shorter iterables

```python
from itertools import zip_longest

a = [1, 2, 3]
b = ["a", "b"]

for x, y in zip_longest(a, b, fillvalue=None):
    print(x, y)
# 1 a
# 2 b
# 3 None
```

---

## Converting Between Collection Types

### list(), tuple(), set() — Universal Converters

```python
# Range → list / tuple / set
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(tuple(range(5)))         # (0, 1, 2, 3, 4)
print(set(range(5)))           # {0, 1, 2, 3, 4}

# String → list of characters
print(list("hello"))           # ['h', 'e', 'l', 'l', 'o']
print(tuple("hello"))          # ('h', 'e', 'l', 'l', 'o')
print(set("hello"))            # {'h', 'e', 'l', 'o'}  (unique)

# List ↔ tuple
lst = [1, 2, 3]
t   = tuple(lst)               # (1, 2, 3)
lst2 = list(t)                 # [1, 2, 3]

# List → set (removes duplicates)
lst = [1, 2, 2, 3, 3, 3]
s = set(lst)                   # {1, 2, 3}
lst3 = sorted(list(s))         # [1, 2, 3]
```

### dict() — Building Dictionaries

```python
# From list of 2-tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print(d)   # {'a': 1, 'b': 2, 'c': 3}

# From list of 2-lists
d2 = dict([["x", 10], ["y", 20]])
print(d2)  # {'x': 10, 'y': 20}

# From set of tuples (order undefined!)
d3 = dict({(1, "one"), (2, "two")})
print(d3)  # {1: 'one', 2: 'two'}

# Using keyword arguments
d4 = dict(alpha=1, beta=2, gamma=3)
print(d4)

# From enumerate
words = ["zero", "one", "two"]
d5 = dict(enumerate(words))
print(d5)   # {0: 'zero', 1: 'one', 2: 'two'}

# From zip
d6 = dict(zip("abc", [1, 2, 3]))
print(d6)   # {'a': 1, 'b': 2, 'c': 3}
```

### dict iterables → other types

```python
d = {"name": "Alice", "age": 30, "city": "NYC"}

# Keys
key_list  = list(d.keys())     # ['name', 'age', 'city']
key_tuple = tuple(d.keys())    # ('name', 'age', 'city')
key_set   = set(d.keys())      # {'name', 'age', 'city'}

# Values
val_list  = list(d.values())   # ['Alice', 30, 'NYC']
val_tuple = tuple(d.values())  # ('Alice', 30, 'NYC')

# Items (key, value pairs)
item_list  = list(d.items())   # [('name', 'Alice'), ('age', 30), ('city', 'NYC')]
item_tuple = tuple(d.items())  # (('name', 'Alice'), ...)
```

---

## `sorted()` with key Function

```python
# Sort list of tuples by second element
data = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
by_score = sorted(data, key=lambda x: x[1])
print(by_score)   # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort dict by value
d = {"banana": 3, "apple": 1, "cherry": 2}
by_value = sorted(d.items(), key=lambda x: x[1])
print(dict(by_value))   # {'apple': 1, 'cherry': 2, 'banana': 3}

# Sort by multiple keys
students = [("Alice", 85, "B"), ("Bob", 92, "A"), ("Alice", 78, "C")]
by_name_then_score = sorted(students, key=lambda x: (x[0], x[1]))
print(by_name_then_score)
```

---

## `map()` and `filter()` — Functional Transforms

### map() — Apply function to every item

```python
nums = [1, 2, 3, 4, 5]

# Old way
squares = []
for n in nums:
    squares.append(n**2)

# With map() — returns iterator
squares = list(map(lambda n: n**2, nums))
print(squares)   # [1, 4, 9, 16, 25]

# Convert strings to ints
strs = ["10", "20", "30"]
ints = list(map(int, strs))
print(ints)   # [10, 20, 30]

# Multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)   # [11, 22, 33]
```

### filter() — Keep only matching items

```python
nums = [1, -2, 3, -4, 5, -6]

positives = list(filter(lambda n: n > 0, nums))
print(positives)   # [1, 3, 5]

# Filter None/falsy values
mixed = [1, None, 2, 0, 3, "", 4, False]
truthy = list(filter(None, mixed))   # filter(None, ...) removes falsy
print(truthy)   # [1, 2, 3, 4]
```

---

## `dict.fromkeys()` — Create dict with default values

```python
keys = ["name", "age", "email"]

# All values set to None
template = dict.fromkeys(keys)
print(template)   # {'name': None, 'age': None, 'email': None}

# All values set to a default
init = dict.fromkeys(keys, "unknown")
print(init)   # {'name': 'unknown', 'age': 'unknown', 'email': 'unknown'}

# Remove duplicates from list, preserving order (Python 3.7+)
lst = [3, 1, 2, 1, 3, 4]
unique = list(dict.fromkeys(lst))
print(unique)   # [3, 1, 2, 4]
```

---

## Practice Problems

```python
# 1. Create a numbered menu
menu_items = ["Pizza", "Burger", "Sushi", "Tacos"]
for i, item in enumerate(menu_items, 1):
    print(f"  {i}. {item}")

# 2. Combine parallel lists into records
names  = ["Alice", "Bob", "Charlie"]
ages   = [30, 25, 35]
cities = ["NYC", "LA", "Chicago"]

records = [{"name": n, "age": a, "city": c}
           for n, a, c in zip(names, ages, cities)]
for r in records:
    print(r)

# 3. Word count with enumerate for indexing
words = "the quick brown fox jumps over the lazy dog".split()
word_index = {word: i for i, word in enumerate(words)}
print(word_index.get("fox"))   # 3

# 4. Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [list(row) for row in zip(*matrix)]
print(transposed)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 5. Progress bar with enumerate
import time
tasks = ["Loading", "Processing", "Saving", "Done"]
for i, task in enumerate(tasks, 1):
    print(f"[{i}/{len(tasks)}] {task}...")
    # time.sleep(0.5)
```

---

> **Exercises:** [05-07: Exercises — zip(), enumerate(), and Conversions](../02-exercises/05-07-zip-enumerate-and-conversions-exe.md)

---

⬅️ Previous: [05-06: Data Structures Comparison — str, list, tuple, set, dict](05-06-data-structures-comparison.md)
➡️ Next: [06-01: Comprehensions — list, set, dict](06-01-comprehensions.md)
