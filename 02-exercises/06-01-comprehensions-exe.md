# 06-01: Exercises — Comprehensions

> **Notes reference:** [06-01: Comprehensions — list, set, dict](../01-notes/06-01-comprehensions.md)

---

## Q1: Basic list comprehension
Build a list of squares for numbers 1–10.

**Solution**
```python
squares = [n**2 for n in range(1, 11)]
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

## Q2: Comprehension with condition
From `numbers = list(range(1, 31))`, keep only numbers divisible by 3 but not by 9.

**Solution**
```python
numbers = list(range(1, 31))
result  = [n for n in numbers if n % 3 == 0 and n % 9 != 0]
print(result)   # [3, 6, 12, 15, 21, 24, 30]
```

---

## Q3: Transform a list
Given product prices in BDT, apply a 12% tax and round to 2 decimal places.

**Solution**
```python
prices_bdt = [500, 1200, 350, 8999]
taxed      = [round(p * 1.12, 2) for p in prices_bdt]
print(taxed)   # [560.0, 1344.0, 392.0, 10078.88]
```

---

## Q4: Ternary in comprehension
Replace negative numbers with `0` in `data = [5, -3, 8, -1, 0, 7, -6]`.

**Solution**
```python
data    = [5, -3, 8, -1, 0, 7, -6]
cleaned = [n if n > 0 else 0 for n in data]
print(cleaned)   # [5, 0, 8, 0, 0, 7, 0]
```

---

## Q5: Set comprehension
Build a set of unique lengths from the words `["Dhaka", "Berlin", "Tokyo", "Nairobi", "Seoul", "Oslo"]`.

**Solution**
```python
words   = ["Dhaka", "Berlin", "Tokyo", "Nairobi", "Seoul", "Oslo"]
lengths = {len(w) for w in words}
print(lengths)   # {4, 5, 6, 7}
```

---

## Q6: Dict comprehension
Build a dictionary mapping each word in `["node", "block", "ledger"]` to its length.

**Solution**
```python
words  = ["node", "block", "ledger"]
result = {w: len(w) for w in words}
print(result)   # {'node': 4, 'block': 5, 'ledger': 6}
```

---

## Q7: Dict comprehension — invert
Invert `{"a": 1, "b": 2, "c": 3}` (swap keys and values).

**Solution**
```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}
```

---

## Q8: Nested comprehension — flatten
Flatten `[[1, 2, 3], [4, 5], [6, 7, 8, 9]]` into a single list.

**Solution**
```python
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat   = [x for row in matrix for x in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Q9: Comprehension vs loop
Rewrite this loop as a comprehension:

```python
result = []
for n in range(1, 11):
    if n % 2 == 0:
        result.append(n ** 3)
```

**Solution**
```python
result = [n**3 for n in range(1, 11) if n % 2 == 0]
print(result)   # [8, 64, 216, 512, 1000]
```

---

⬅️ Previous: [05-07: Exercises — zip(), enumerate(), and Conversions](05-07-zip-enumerate-and-conversions-exe.md)
➡️ Next: [06-02: Exercises — Exception Handling](06-02-exception-handling-exe.md)
