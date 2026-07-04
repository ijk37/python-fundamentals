# 05-07: Exercises — zip(), enumerate(), and Conversions

> **Notes reference:** [05-07: zip(), enumerate(), and Collection Conversions](../01-notes/05-07-zip-enumerate-and-conversions.md)

---

## Q1: enumerate() with a custom start
Print a numbered list of cities starting from 1.

**Solution**
```python
cities = ["Dhaka", "New York", "Berlin", "Nairobi", "Tokyo"]
for i, city in enumerate(cities, start=1):
    print(f"{i}. {city}")
```

---

## Q2: zip() — pair two lists
Pair student names with their grades and print each pair.

**Solution**
```python
names  = ["Alice", "Bob", "Carol", "David"]
grades = ["A", "B+", "A-", "B"]

for name, grade in zip(names, grades):
    print(f"{name}: {grade}")
```

---

## Q3: zip() to build a dictionary
Build a dictionary from two lists: one of keys and one of values.

**Solution**
```python
keys   = ["name", "age", "city"]
values = ["Jahid", 28, "New York"]

profile = dict(zip(keys, values))
print(profile)   # {'name': 'Jahid', 'age': 28, 'city': 'New York'}
```

---

## Q4: zip() with unequal lengths
Zip two lists of different lengths. Show what happens.

**Solution**
```python
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]

print(list(zip(a, b)))   # [(1, 'a'), (2, 'b'), (3, 'c')] — stops at shortest
```

---

## Q5: list(), tuple(), set() conversions
Convert a string to a list of characters, then to a set of unique characters, then back to a sorted list.

**Solution**
```python
word      = "Chittagong"
chars     = list(word)
unique    = set(chars)
sorted_ch = sorted(unique)

print(chars)      # ['C', 'h', 'i', 't', 't', 'a', 'g', 'o', 'n', 'g']
print(unique)     # {'C', 'h', 'i', 't', 'a', 'g', 'o', 'n'} (order may vary)
print(sorted_ch)  # ['C', 'a', 'g', 'h', 'i', 'n', 'o', 't']
```

---

## Q6: range() to list
Convert `range(0, 20, 3)` to a list, and `range(10, 0, -1)` to a tuple.

**Solution**
```python
print(list(range(0, 20, 3)))     # [0, 3, 6, 9, 12, 15, 18]
print(tuple(range(10, 0, -1)))   # (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
```

---

## Q7: enumerate() + zip() together
Given names and scores, print a numbered ranking.

**Solution**
```python
names  = ["Rahul", "Sara", "James", "Nadia"]
scores = [92, 88, 95, 79]

ranked = sorted(zip(scores, names), reverse=True)
for rank, (score, name) in enumerate(ranked, start=1):
    print(f"{rank}. {name} — {score}")
# 1. James — 95
# 2. Rahul — 92
# 3. Sara  — 88
# 4. Nadia — 79
```

---

⬅️ Previous: [05-05: Exercises — Slicing](05-05-slicing-exe.md)
➡️ Next: [06-01: Exercises — Comprehensions](06-01-comprehensions-exe.md)
