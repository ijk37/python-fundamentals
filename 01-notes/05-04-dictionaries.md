# 05-04: Dictionaries

A **dictionary** (`dict`) is an **unordered** (Python 3.7+ preserves insertion order), **mutable** collection of **key-value pairs**. It provides fast lookup by key.

---

## Creating Dictionaries

```python
# Curly brace syntax
person = {"name": "Alice", "age": 30, "job": "Engineer"}

# Empty dict
empty = {}
empty2 = dict()

# dict() constructor with keyword arguments
d = dict(name="Bob", age=25, city="NYC")

# dict() from list of tuples
d2 = dict([("x", 10), ("y", 20), ("z", 30)])

# From zip
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d3 = dict(zip(keys, vals))
print(d3)   # {'a': 1, 'b': 2, 'c': 3}

# Dict comprehension
squares = {x: x**2 for x in range(6)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Keys and Values

- **Keys** must be **hashable** (immutable): strings, numbers, tuples — not lists or dicts
- **Values** can be anything — including lists, dicts, functions, etc.
- **Keys must be unique** — assigning to an existing key updates its value

```python
# Various key types
mixed_keys = {
    "string_key": "value1",
    42: "value2",
    (1, 2): "value3",    # tuple key OK
    True: "value4",
}

# List as key — NOT allowed
# {[1,2]: "value"}   # TypeError: unhashable type: 'list'
```

---

## Accessing Values

### Direct access with `[]`

```python
person = {"name": "Alice", "age": 30}
print(person["name"])    # Alice
print(person["age"])     # 30

# KeyError if key doesn't exist
print(person["email"])   # KeyError!
```

### `get()` — safe access with default

```python
print(person.get("name"))          # Alice
print(person.get("email"))         # None (no error)
print(person.get("email", "N/A"))  # N/A (custom default)
```

---

## Adding and Updating

```python
person = {"name": "Alice", "age": 30}

# Add new key
person["email"] = "alice@example.com"
print(person)   # {..., 'email': 'alice@example.com'}

# Update existing key
person["age"] = 31
print(person["age"])   # 31

# update() — merge another dict
person.update({"city": "NYC", "age": 32})
print(person)

# update() with keyword arguments
person.update(zip=10001, country="USA")

# setdefault() — add key only if not present
person.setdefault("nickname", "Ally")
person.setdefault("name", "Bob")     # does nothing, 'name' already exists
print(person["nickname"])    # Ally
print(person["name"])        # Alice (unchanged)
```

---

## Removing Items

```python
person = {"name": "Alice", "age": 30, "city": "NYC", "job": "Eng"}

# del — delete by key (KeyError if not found)
del person["city"]
print(person)

# pop() — remove and return value
age = person.pop("age")
print(age)      # 30
print(person)   # {'name': 'Alice', 'job': 'Eng'}

# pop with default (no error if key absent)
email = person.pop("email", "not found")
print(email)    # not found

# popitem() — remove and return last inserted item as tuple
item = person.popitem()
print(item)     # ('job', 'Eng')

# clear() — remove all items
person.clear()
print(person)   # {}
```

---

## Iterating

```python
inventory = {"apple": 50, "banana": 30, "cherry": 80}

# Iterate over keys (default)
for key in inventory:
    print(key)

# Iterate over keys explicitly
for key in inventory.keys():
    print(key)

# Iterate over values
for value in inventory.values():
    print(value)

# Iterate over key-value pairs
for key, value in inventory.items():
    print(f"{key}: {value}")

# Sorted iteration
for key in sorted(inventory):
    print(f"{key}: {inventory[key]}")
```

---

## Checking Keys

```python
d = {"a": 1, "b": 2, "c": 3}

print("a" in d)         # True
print("z" in d)         # False
print("a" not in d)     # False

# Check values
print(1 in d.values())  # True
print(99 in d.values()) # False

# Check key-value pair
print(("a", 1) in d.items())   # True
```

---

## Dictionary Methods

```python
d = {"a": 1, "b": 2, "c": 3}

print(len(d))           # 3
print(list(d.keys()))   # ['a', 'b', 'c']
print(list(d.values())) # [1, 2, 3]
print(list(d.items()))  # [('a', 1), ('b', 2), ('c', 3)]

# Convert to dict
print(dict(d.items()))  # {'a': 1, 'b': 2, 'c': 3}
```

---

## Dictionary Comprehensions

```python
# Basic
squares = {x: x**2 for x in range(6)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)   # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Invert a dict
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# From two lists
keys = ["name", "age", "job"]
vals = ["Alice", 30, "Engineer"]
profile = {k: v for k, v in zip(keys, vals)}
print(profile)

# Filtering
inventory = {"apple": 50, "banana": 0, "cherry": 30, "date": 0}
in_stock = {k: v for k, v in inventory.items() if v > 0}
print(in_stock)   # {'apple': 50, 'cherry': 30}
```

---

## Nested Dictionaries

```python
students = {
    "alice": {"grade": "A", "score": 95, "courses": ["Math", "Physics"]},
    "bob":   {"grade": "B", "score": 82, "courses": ["English", "History"]},
}

print(students["alice"]["grade"])          # A
print(students["bob"]["courses"][0])       # English

# Add a new student
students["charlie"] = {"grade": "A+", "score": 98, "courses": ["CS", "Math"]}

# Update nested
students["alice"]["score"] = 97

# Iterate nested
for name, info in students.items():
    print(f"{name}: grade={info['grade']}, score={info['score']}")
```

---

## Merging Dictionaries

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

# Python 3.9+ — merge operator
merged = d1 | d2            # d2 wins on conflict
print(merged)   # {'a': 1, 'b': 20, 'c': 3}

# Python 3.5+ — double star unpacking
merged2 = {**d1, **d2}      # same result
print(merged2)

# update() — modifies d1 in place
d1.update(d2)
print(d1)   # {'a': 1, 'b': 20, 'c': 3}
```

---

## `defaultdict` — Default Values for Missing Keys

```python
from collections import defaultdict

# Count word frequencies
word_count = defaultdict(int)
text = "the cat sat on the mat the cat"
for word in text.split():
    word_count[word] += 1    # no KeyError!

print(dict(word_count))
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# Group items
from collections import defaultdict
groups = defaultdict(list)
data = [("Alice", "Math"), ("Bob", "Physics"), ("Alice", "CS"), ("Bob", "Math")]
for name, course in data:
    groups[name].append(course)

print(dict(groups))
# {'Alice': ['Math', 'CS'], 'Bob': ['Physics', 'Math']}
```

---

## `Counter` — Count Occurrences

```python
from collections import Counter

# Count characters
c = Counter("banana")
print(c)        # Counter({'a': 3, 'n': 2, 'b': 1})
print(c['a'])   # 3
print(c['z'])   # 0 (no KeyError)

# Most common
print(c.most_common(2))   # [('a', 3), ('n', 2)]

# Count words
text = "one two three one two one"
word_count = Counter(text.split())
print(word_count)   # Counter({'one': 3, 'two': 2, 'three': 1})
```

---

## OrderedDict (Pre-Python 3.7)

In Python 3.7+, regular dicts maintain insertion order. `OrderedDict` is still useful for:
- Move-to-end operations
- LRU cache patterns
- Equality that considers order

```python
from collections import OrderedDict

od = OrderedDict()
od["first"]  = 1
od["second"] = 2
od["third"]  = 3

od.move_to_end("first")   # move 'first' to end
print(list(od.keys()))    # ['second', 'third', 'first']
```

---

## Complete Method Reference

| Method | Description |
|--------|-------------|
| `d[key]` | Get value (KeyError if missing) |
| `d[key] = val` | Set value |
| `del d[key]` | Delete key (KeyError if missing) |
| `d.get(key[, def])` | Get value, or def if missing |
| `d.setdefault(key[, def])` | Get or set default |
| `d.pop(key[, def])` | Remove & return value |
| `d.popitem()` | Remove & return last (key, value) |
| `d.update(other)` | Merge other dict |
| `d.clear()` | Remove all |
| `d.keys()` | View of all keys |
| `d.values()` | View of all values |
| `d.items()` | View of all (key, value) pairs |
| `key in d` | Membership test |
| `len(d)` | Number of items |

---

## Practice Problems

```python
# 1. Word frequency counter
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

print(word_frequency("the cat sat on the mat the cat"))

# 2. Group anagrams
def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# 3. Phone book
phonebook = {}
while True:
    cmd = input("add/find/quit: ").strip().lower()
    if cmd == "quit":
        break
    elif cmd == "add":
        name = input("Name: ")
        number = input("Number: ")
        phonebook[name] = number
    elif cmd == "find":
        name = input("Name: ")
        print(phonebook.get(name, "Not found"))

# 4. Invert dictionary (handle duplicate values)
def invert_dict(d):
    inverted = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k)
    return inverted

d = {"a": 1, "b": 2, "c": 1, "d": 3}
print(invert_dict(d))   # {1: ['a', 'c'], 2: ['b'], 3: ['d']}
```

---

> **Exercises:** [05-04: Exercises — Dictionaries](../02-exercises/05-04-dictionaries-exe.md)

---

⬅️ Previous: [05-03: Sets](05-03-sets.md)
➡️ Next: [05-05: Slicing — Extracting Subsequences](05-05-slicing.md)
