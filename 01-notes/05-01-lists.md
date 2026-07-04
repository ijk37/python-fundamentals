# 05-01: Lists — The Complete Guide

A **list** is Python's most versatile built-in data structure. It is an **ordered**, **mutable** sequence that can hold items of **any type**.

---

## Creating Lists

```python
# Empty list
empty = []
empty2 = list()

# List of integers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]

# Mixed types
mixed = [1, "hello", 3.14, True, None]

# List of lists (2D)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# From range
evens = list(range(0, 10, 2))   # [0, 2, 4, 6, 8]

# From string
chars = list("Python")    # ['P', 'y', 't', 'h', 'o', 'n']
```

---

## Indexing

Lists are **zero-indexed**. Negative indices count from the end.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#          0        1         2         3       4
#         -5       -4        -3        -2      -1

print(fruits[0])    # 'apple'
print(fruits[2])    # 'cherry'
print(fruits[-1])   # 'elderberry'  (last)
print(fruits[-2])   # 'date'

# IndexError for out-of-range
print(fruits[10])   # IndexError!
```

---

## Slicing

Syntax: `list[start:stop:step]`

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])     # [2, 3, 4, 5]
print(nums[:4])      # [0, 1, 2, 3]
print(nums[5:])      # [5, 6, 7, 8, 9]
print(nums[:])       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  (full copy)
print(nums[::2])     # [0, 2, 4, 6, 8]   (every 2nd)
print(nums[1::2])    # [1, 3, 5, 7, 9]   (odd indices)
print(nums[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  (reversed)
print(nums[7:2:-1])  # [7, 6, 5, 4, 3]   (reverse slice)
```

---

## Modifying Lists (Mutable)

### Change a single element

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'cherry']
```

### Change a slice

```python
nums = [1, 2, 3, 4, 5]
nums[1:4] = [20, 30, 40]
print(nums)   # [1, 20, 30, 40, 5]

# Replace with fewer items (list shrinks)
nums[1:4] = [99]
print(nums)   # [1, 99, 5]

# Replace with more items (list grows)
nums[1:2] = [10, 11, 12]
print(nums)   # [1, 10, 11, 12, 5]

# Delete via empty replacement
nums[1:3] = []
print(nums)   # [1, 12, 5]
```

---

## Adding Elements

### `append()` — Add to end

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)   # ['apple', 'banana', 'cherry']

# append() adds the item as a single element
fruits.append(["date", "elderberry"])
print(fruits)   # ['apple', 'banana', 'cherry', ['date', 'elderberry']]
```

### `insert()` — Add at position

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")    # insert at index 1
print(fruits)   # ['apple', 'banana', 'cherry']

fruits.insert(0, "avocado")   # insert at beginning
print(fruits)   # ['avocado', 'apple', 'banana', 'cherry']

fruits.insert(100, "zucchini")  # beyond end → appended
print(fruits)   # ['avocado', 'apple', 'banana', 'cherry', 'zucchini']
```

### `extend()` — Add multiple items from another iterable

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)   # ['apple', 'banana', 'cherry', 'date']

# extend vs append
a = [1, 2]
a.append([3, 4])    # adds list as single element
print(a)            # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])    # adds elements individually
print(b)            # [1, 2, 3, 4]
```

### `+` operator — Concatenate

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)    # [1, 2, 3, 4, 5, 6]
print(a)    # [1, 2, 3]  — original unchanged

# += modifies in place
a += [7, 8]
print(a)    # [1, 2, 3, 7, 8]
```

### `*` operator — Repeat

```python
zeros = [0] * 5
print(zeros)    # [0, 0, 0, 0, 0]

pattern = [1, 2] * 3
print(pattern)  # [1, 2, 1, 2, 1, 2]
```

---

## Removing Elements

### `remove()` — Remove first occurrence of value

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")    # removes first 'banana'
print(fruits)   # ['apple', 'cherry', 'banana']

# ValueError if not found
fruits.remove("mango")    # ValueError!
```

### `pop()` — Remove and return by index

```python
fruits = ["apple", "banana", "cherry"]

last = fruits.pop()       # default: removes last
print(last)     # 'cherry'
print(fruits)   # ['apple', 'banana']

first = fruits.pop(0)     # remove at index 0
print(first)    # 'apple'
print(fruits)   # ['banana']
```

### `del` statement — Delete by index or slice

```python
nums = [10, 20, 30, 40, 50]
del nums[2]
print(nums)     # [10, 20, 40, 50]

del nums[1:3]
print(nums)     # [10, 50]

del nums        # delete the variable entirely
# print(nums)   # NameError!
```

### `clear()` — Remove all elements

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)   # []
```

---

## Searching

### `index()` — Find position of first occurrence

```python
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.index("banana"))      # 1 (first occurrence)
print(fruits.index("banana", 2))   # 3 (start search from index 2)

# ValueError if not found
print(fruits.index("mango"))       # ValueError!

# Safe way with `in` check first
if "mango" in fruits:
    print(fruits.index("mango"))
else:
    print("not found")
```

### `count()` — Count occurrences

```python
nums = [1, 2, 3, 2, 1, 2, 4, 1]
print(nums.count(2))   # 3
print(nums.count(1))   # 3
print(nums.count(5))   # 0
```

### `in` and `not in`

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("mango" in fruits)       # False
print("mango" not in fruits)   # True
```

---

## Sorting

### `sort()` — Sort in place

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()
print(nums)     # [1, 1, 2, 3, 4, 5, 6, 9]

nums.sort(reverse=True)
print(nums)     # [9, 6, 5, 4, 3, 2, 1, 1]

# Sort strings
words = ["banana", "Apple", "cherry", "date"]
words.sort()
print(words)    # ['Apple', 'banana', 'cherry', 'date']  (uppercase first)

words.sort(key=str.lower)   # case-insensitive
print(words)    # ['Apple', 'banana', 'cherry', 'date']

# Sort by key function
words.sort(key=len)         # by length
print(words)    # ['Apple', 'date', 'banana', 'cherry']
```

### `sorted()` — Return new sorted list

```python
nums = [3, 1, 4, 1, 5, 9]
s = sorted(nums)
print(s)        # [1, 1, 3, 4, 5, 9]
print(nums)     # [3, 1, 4, 1, 5, 9]  — unchanged!

# Works on any iterable
s2 = sorted("hello")
print(s2)       # ['e', 'h', 'l', 'l', 'o']
```

### `reverse()` — Reverse in place

```python
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)     # [5, 4, 3, 2, 1]
```

---

## Length and Other Info

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))    # 3
print(min(fruits))    # 'apple'  (lexicographic)
print(max(fruits))    # 'cherry'

nums = [3, 1, 4, 1, 5, 9]
print(len(nums))      # 6
print(min(nums))      # 1
print(max(nums))      # 9
print(sum(nums))      # 23
```

---

## Copying Lists

Careful — assignment creates a reference, not a copy!

```python
a = [1, 2, 3]
b = a           # b is another name for the SAME list
b.append(4)
print(a)        # [1, 2, 3, 4]  — a is affected!
```

### Shallow copy

```python
# Method 1: slice
a = [1, 2, 3]
b = a[:]        # shallow copy

# Method 2: copy()
b = a.copy()

# Method 3: list()
b = list(a)

b.append(4)
print(a)        # [1, 2, 3]  — unchanged
print(b)        # [1, 2, 3, 4]
```

### Deep copy (for nested lists)

```python
import copy
matrix = [[1, 2], [3, 4]]
deep = copy.deepcopy(matrix)
deep[0][0] = 99
print(matrix)   # [[1, 2], [3, 4]]  — unchanged
print(deep)     # [[99, 2], [3, 4]]
```

---

## Iterating

```python
fruits = ["apple", "banana", "cherry"]

# Basic iteration
for fruit in fruits:
    print(fruit)

# With index — enumerate
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Iterate backwards
for fruit in reversed(fruits):
    print(fruit)

# Iterate with zip
prices = [1.5, 0.75, 2.0]
for fruit, price in zip(fruits, prices):
    print(f"{fruit}: ${price:.2f}")
```

---

## List as Stack (LIFO)

```python
stack = []
stack.append("a")    # push
stack.append("b")
stack.append("c")

top = stack.pop()    # pop
print(top)           # 'c'
print(stack)         # ['a', 'b']
```

---

## List as Queue (FIFO)

For queue behavior, use `collections.deque` for efficiency:

```python
from collections import deque

queue = deque()
queue.append("first")    # enqueue
queue.append("second")
queue.append("third")

front = queue.popleft()  # dequeue
print(front)             # 'first'
print(queue)             # deque(['second', 'third'])
```

---

## 2D Lists (Matrix)

```python
# Create 3×3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element
print(matrix[1][2])    # 6  (row 1, col 2)

# Iterate rows
for row in matrix:
    print(row)

# Iterate all elements
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# Get a column
col1 = [row[1] for row in matrix]
print(col1)   # [2, 5, 8]
```

---

## Complete Method Reference

| Method | Description | Returns |
|--------|-------------|---------|
| `append(x)` | Add x to end | `None` |
| `insert(i, x)` | Insert x before index i | `None` |
| `extend(iterable)` | Add all items from iterable | `None` |
| `remove(x)` | Remove first x | `None` |
| `pop([i])` | Remove & return item at i (default last) | item |
| `clear()` | Remove all items | `None` |
| `index(x[,start[,end]])` | Find first index of x | `int` |
| `count(x)` | Count occurrences of x | `int` |
| `sort(key=None, reverse=False)` | Sort in place | `None` |
| `reverse()` | Reverse in place | `None` |
| `copy()` | Return shallow copy | `list` |

---

## Practice Problems

```python
# 1. Rotate list left by k positions
def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate_left([1, 2, 3, 4, 5], 2))   # [3, 4, 5, 1, 2]

# 2. Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

print(remove_duplicates([1, 3, 2, 1, 4, 3, 5]))   # [1, 3, 2, 4, 5]

# 3. Flatten nested list
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4], 5], 6]))   # [1, 2, 3, 4, 5, 6]

# 4. Second largest
def second_largest(nums):
    unique = sorted(set(nums), reverse=True)
    return unique[1] if len(unique) >= 2 else None

print(second_largest([3, 1, 4, 1, 5, 9, 2, 6]))   # 6

# 5. Chunk list into groups of n
def chunks(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(chunks([1,2,3,4,5,6,7,8,9], 3))   # [[1,2,3],[4,5,6],[7,8,9]]
```

---

> **Exercises:** [05-01: Exercises — Lists](../02-exercises/05-01-lists-exe.md)

---

⬅️ Previous: [04-01: Functions — Basics](04-01-functions-basics.md)
➡️ Next: [05-02: Tuples](05-02-tuples.md)
