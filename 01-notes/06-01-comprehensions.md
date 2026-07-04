# 06-01: Comprehensions — list, set, dict

A **comprehension** is a concise, readable way to build a new collection by transforming or filtering an existing iterable. It puts the loop *inside* the collection definition — which is Pythonic and often faster than an equivalent explicit loop.

---

## List Comprehensions

### Basic form

```python
[expression for variable in iterable]
```

```python
# Old way
squares = []
for x in range(6):
    squares.append(x**2)

# Comprehension — same result, one line
squares = [x**2 for x in range(6)]
print(squares)   # [0, 1, 4, 9, 16, 25]
```

### With a condition (filter)

```python
[expression for variable in iterable if condition]
```

```python
# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8]

# Positive numbers from a mixed list
nums = [3, -1, 4, -1, 5, -9, 2, -6]
positives = [n for n in nums if n > 0]
print(positives)   # [3, 4, 5, 2]

# Words longer than 3 chars
words = ["hi", "hello", "hey", "howdy", "ok"]
long_words = [w for w in words if len(w) > 3]
print(long_words)   # ['hello', 'howdy']
```

### With transformation

```python
# Convert prices from USD to BDT (rate = 110.0)
prices_usd = [10.0, 25.5, 4.99, 100.0]
prices_bdt = [round(p * 110.0, 2) for p in prices_usd]
print(prices_bdt)   # [1100.0, 2805.0, 548.9, 11000.0]

# Uppercase city names
cities = ["dhaka", "new york", "chittagong", "berlin", "tokyo", "nairobi"]
upper = [c.upper() for c in cities]
print(upper)   # ['DHAKA', 'NEW YORK', 'CHITTAGONG', 'BERLIN', 'TOKYO', 'NAIROBI']

# Strip whitespace from each tag
tags = ["  python  ", "  data  ", "  science  "]
clean = [t.strip() for t in tags]
print(clean)   # ['python', 'data', 'science']
```

---

## Comprehensions with Iterables

### Over string characters

```python
# Filter vowels from a string
text = "Hello, World!"
vowels = [c for c in text if c.lower() in "aeiou"]
print(vowels)   # ['e', 'o', 'o']

# ASCII codes of characters
codes = [ord(c) for c in "Python"]
print(codes)   # [80, 121, 116, 104, 111, 110]

# Reverse each word
words = ["code", "data", "neural", "graph"]
reversed_words = [w[::-1] for w in words]
print(reversed_words)   # ['edoc', 'atad', 'laruen', 'hparg']
```

### Over tuples and pairs

```python
pairs = [(1, "a"), (2, "b"), (3, "c")]
firsts  = [p[0] for p in pairs]
seconds = [p[1] for p in pairs]
print(firsts)    # [1, 2, 3]
print(seconds)   # ['a', 'b', 'c']

# Unpack in the comprehension
coords = [(0, 0), (1, 2), (3, 4), (5, 6)]
distances = [(x**2 + y**2)**0.5 for x, y in coords]
print([round(d, 2) for d in distances])   # [0.0, 2.24, 5.0, 7.81]
```

### Over a file

```python
with open("data.txt", "rt") as f:
    lines = [line.strip() for line in f if line.strip()]
```

---

## Nested Comprehensions

The expression in a comprehension can itself be a comprehension — useful for 2D structures:

```python
# 3×3 matrix (list of lists)
matrix = [[i + j*3 for i in range(3)] for j in range(3)]
print(matrix)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Identity matrix
n = 4
identity = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
for row in identity:
    print(row)
# [1, 0, 0, 0]
# [0, 1, 0, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
```

### Flattening a 2D list

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Multiple for clauses

```python
# All combinations of two lists
colors = ["red", "blue"]
sizes  = ["S", "M", "L"]
combos = [f"{color}-{size}" for color in colors for size in sizes]
print(combos)
# ['red-S', 'red-M', 'red-L', 'blue-S', 'blue-M', 'blue-L']

# Pythagorean triples up to 20
triples = [(a, b, c)
           for a in range(1, 20)
           for b in range(a, 20)
           for c in range(b, 20)
           if a**2 + b**2 == c**2]
print(triples)
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]
```

---

## Conditional Expression in the Output

A ternary expression can be used in the output part:

```python
# if-else in the OUTPUT (not filtering — transforms every item)
nums = [1, -2, 3, -4, 5]
signs = ["pos" if n > 0 else "neg" for n in nums]
print(signs)   # ['pos', 'neg', 'pos', 'neg', 'pos']

# Replace negatives with 0
clipped = [n if n > 0 else 0 for n in nums]
print(clipped)   # [1, 0, 3, 0, 5]

# FizzBuzz
fizzbuzz = [
    "FizzBuzz" if n % 15 == 0
    else "Fizz" if n % 3 == 0
    else "Buzz" if n % 5 == 0
    else str(n)
    for n in range(1, 21)
]
print(fizzbuzz)
```

---

## Set Comprehensions

Use `{}` instead of `[]` — automatically deduplicates:

```python
{expression for variable in iterable [if condition]}
```

```python
# Unique characters in a string
text = "blockchain network"
unique = {c for c in text if c != " "}
print(unique)   # set of unique chars (any order)

# Squares of odd numbers (unique)
odd_sq = {x**2 for x in range(-5, 6) if x % 2 != 0}
print(odd_sq)   # {1, 9, 25}

# Unique word lengths
words = ["node", "block", "chain", "ledger", "peer"]
lengths = {len(w) for w in words}
print(lengths)   # {4, 5, 6}
```

---

## Dict Comprehensions

Use `{key: value for ...}`:

```python
{key_expr: val_expr for variable in iterable [if condition]}
```

```python
# Number → square
squares = {x: x**2 for x in range(6)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Word → length
words = ["apple", "banana", "cherry"]
word_len = {w: len(w) for w in words}
print(word_len)   # {'apple': 5, 'banana': 6, 'cherry': 6}

# Invert a dict
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# Filter dict
inventory = {"apple": 50, "banana": 0, "cherry": 30, "date": 0}
in_stock = {k: v for k, v in inventory.items() if v > 0}
print(in_stock)   # {'apple': 50, 'cherry': 30}

# Uppercase keys
d = {"name": "Alice", "age": 30}
upper_keys = {k.upper(): v for k, v in d.items()}
print(upper_keys)   # {'NAME': 'Alice', 'AGE': 30}
```

---

## Generator Expressions

Similar to list comprehensions but use `()` and are **lazy** — they generate values one at a time without storing all in memory:

```python
# List comprehension — stores all values in memory
squares_list = [x**2 for x in range(1000000)]

# Generator — lazy, memory efficient
squares_gen = (x**2 for x in range(1000000))

# Both can be iterated
print(next(squares_gen))   # 0
print(next(squares_gen))   # 1
print(next(squares_gen))   # 4

# Commonly used directly in functions
print(sum(x**2 for x in range(10)))     # 285
print(max(len(w) for w in ["hi", "hello", "hey"]))  # 5
print(any(x > 10 for x in [1, 5, 15, 3]))  # True
print(all(x > 0 for x in [1, 2, 3]))       # True
```

---

## Performance Comparison

Comprehensions are generally faster than explicit loops because they're implemented at the C level:

```python
import timeit

# Loop approach
def using_loop():
    result = []
    for x in range(10000):
        if x % 2 == 0:
            result.append(x**2)
    return result

# Comprehension approach
def using_comp():
    return [x**2 for x in range(10000) if x % 2 == 0]

t_loop = timeit.timeit(using_loop, number=1000)
t_comp = timeit.timeit(using_comp, number=1000)
print(f"Loop:  {t_loop:.3f}s")
print(f"Comp:  {t_comp:.3f}s")
# Comprehension is typically 30-50% faster
```

---

## Readability Tips

**Good** — clear, concise:
```python
evens = [x for x in range(20) if x % 2 == 0]
squares = {x: x**2 for x in range(10)}
```

**Too complex** — split into multiple steps or use a loop:
```python
# Hard to read
result = [f(x) for x in [g(y) for y in z if p(y)] if q(x)]

# Better
temp = [g(y) for y in z if p(y)]
result = [f(x) for x in temp if q(x)]
```

---

## Practical Examples

### Word frequency counter

```python
text = "the cat sat on the mat the cat sat"
words = text.split()
word_set = set(words)
freq = {word: words.count(word) for word in word_set}
print(sorted(freq.items(), key=lambda x: -x[1]))
# [('the', 3), ('cat', 2), ('sat', 2), ('on', 1), ('mat', 1)]
```

### CSV processing

```python
csv_data = "Alice,85,A\nBob,92,B\nCharlie,78,C"
records = [line.split(",") for line in csv_data.strip().split("\n")]
students = [{"name": r[0], "score": int(r[1]), "grade": r[2]} for r in records]
print([s["name"] for s in students if s["score"] >= 85])
# ['Alice', 'Bob']
```

### Transpose matrix

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Or more elegantly:
transposed = [list(col) for col in zip(*matrix)]
print(transposed)   # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

---

## Quick Summary

| Type | Syntax | Returns |
|------|--------|---------|
| List comprehension | `[expr for x in it]` | `list` |
| List with filter | `[expr for x in it if cond]` | `list` |
| Set comprehension | `{expr for x in it}` | `set` |
| Dict comprehension | `{k: v for x in it}` | `dict` |
| Generator expression | `(expr for x in it)` | `generator` |

---

> **Exercises:** [06-01: Exercises — Comprehensions](../02-exercises/06-01-comprehensions-exe.md)

---

⬅️ Previous: [05-07: zip(), enumerate(), and Collection Conversions](05-07-zip-enumerate-and-conversions.md)
➡️ Next: [06-02: Exception Handling](06-02-exception-handling.md)
