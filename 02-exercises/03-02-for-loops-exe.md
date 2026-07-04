# 03-02: Exercises — for Loops

> **Notes reference:** [03-02: for Loops](../01-notes/03-02-for-loops.md)

---

## Q1: Basic range loop
Print the numbers 1 through 10, one per line.

**Solution**
```python
for i in range(1, 11):
    print(i)
```

---

## Q2: Loop over a string
Print each character of `"Dhaka"` on its own line, preceded by its index.

**Solution**
```python
for i, ch in enumerate("Dhaka"):
    print(i, ch)
# 0 D
# 1 h
# 2 a
# 3 k
# 4 a
```

---

## Q3: Sum with a loop
Calculate the sum of all integers from 1 to 100.

**Solution**
```python
total = 0
for n in range(1, 101):
    total += n
print(total)   # 5050

# Alternative — built-in
print(sum(range(1, 101)))   # 5050
```

---

## Q4: Loop over a list
Given `scores = [88, 74, 95, 62, 79]`, print each score with a label `"Pass"` or `"Fail"` (pass if ≥ 70).

**Solution**
```python
scores = [88, 74, 95, 62, 79]
for score in scores:
    label = "Pass" if score >= 70 else "Fail"
    print(f"{score}: {label}")
```

---

## Q5: break and continue
Print numbers 1–20 but skip multiples of 4 and stop entirely when a multiple of 17 is reached.

**Solution**
```python
for n in range(1, 21):
    if n % 17 == 0:
        break
    if n % 4 == 0:
        continue
    print(n)
# Prints: 1 2 3 5 6 7 9 10 11 13 14 15
```

---

## Q6: for/else
Search for the first number divisible by both 7 and 11 in the range 1–100. Use `for/else` to handle the case where none is found.

**Solution**
```python
for n in range(1, 101):
    if n % 7 == 0 and n % 11 == 0:
        print(f"Found: {n}")
        break
else:
    print("Not found in range")
# Found: 77
```

---

## Q7: enumerate()
Given a list of cities, print each with a 1-based counter: `"1. Dhaka"`, `"2. Berlin"`, etc.

**Solution**
```python
cities = ["Dhaka", "Berlin", "Tokyo", "Nairobi", "New York"]
for i, city in enumerate(cities, start=1):
    print(f"{i}. {city}")
```

---

## Q8: zip()
Pair student names with their scores and print: `"Alice: 91"`.

**Solution**
```python
names  = ["Alice", "Bob", "Carol", "David"]
scores = [91, 78, 85, 62]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

## Q9: Nested loops — multiplication table
Print the 3 × 3 multiplication table (rows 1–3, cols 1–3).

**Solution**
```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:3}", end="")
    print()
#   1  2  3
#   2  4  6
#   3  6  9
```

---

## Q10: range with step
Print all even numbers from 2 to 20, then count down from 10 to 1.

**Solution**
```python
for n in range(2, 21, 2):
    print(n, end=" ")
# 2 4 6 8 10 12 14 16 18 20

print()

for n in range(10, 0, -1):
    print(n, end=" ")
# 10 9 8 7 6 5 4 3 2 1
```

---

⬅️ Previous: [03-01: Exercises — Conditional Statements](03-01-if-elif-else-exe.md)
➡️ Next: [03-03: Exercises — while Loops](03-03-while-loops-exe.md)
