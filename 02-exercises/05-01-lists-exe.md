# 05-01: Exercises — Lists

> **Notes reference:** [05-01: Lists — The Complete Guide](../01-notes/05-01-lists.md)

---

## Q1: Create and access
Create a list of 5 Bangladeshi districts. Print the first, last, and third item.

**Solution**
```python
districts = ["Dhaka", "Chittagong", "Sylhet", "Rajshahi", "Khulna"]
print(districts[0])    # Dhaka
print(districts[-1])   # Khulna
print(districts[2])    # Sylhet
```

---

## Q2: Modify an element
Change `"Rajshahi"` to `"Barisal"` in the list from Q1.

**Solution**
```python
districts = ["Dhaka", "Chittagong", "Sylhet", "Rajshahi", "Khulna"]
districts[3] = "Barisal"
print(districts)   # ['Dhaka', 'Chittagong', 'Sylhet', 'Barisal', 'Khulna']
```

---

## Q3: append, insert, remove, pop
Start with `items = [10, 20, 30]`. Then:
- append `40`
- insert `15` at index 1
- remove `20`
- pop the last element and print it

**Solution**
```python
items = [10, 20, 30]
items.append(40)
print(items)   # [10, 20, 30, 40]

items.insert(1, 15)
print(items)   # [10, 15, 20, 30, 40]

items.remove(20)
print(items)   # [10, 15, 30, 40]

popped = items.pop()
print(popped)  # 40
print(items)   # [10, 15, 30]
```

---

## Q4: sort and reverse
Sort `[64, 25, 12, 90, 3]` in ascending order, then descending order.

**Solution**
```python
nums = [64, 25, 12, 90, 3]
nums.sort()
print(nums)   # [3, 12, 25, 64, 90]

nums.sort(reverse=True)
print(nums)   # [90, 64, 25, 12, 3]

# Without modifying original:
print(sorted([64, 25, 12, 90, 3]))              # ascending
print(sorted([64, 25, 12, 90, 3], reverse=True)) # descending
```

---

## Q5: Slicing
Given `nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, extract:
- first 4 elements
- last 3 elements
- every other element
- the entire list reversed

**Solution**
```python
nums = list(range(10))
print(nums[:4])      # [0, 1, 2, 3]
print(nums[-3:])     # [7, 8, 9]
print(nums[::2])     # [0, 2, 4, 6, 8]
print(nums[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

## Q6: List methods — count, index, extend
Given `data = [3, 7, 3, 1, 3, 9, 7]`:
- how many times does `3` appear?
- at what index does `9` first appear?
- extend the list with `[11, 13]`

**Solution**
```python
data = [3, 7, 3, 1, 3, 9, 7]
print(data.count(3))      # 3
print(data.index(9))      # 5
data.extend([11, 13])
print(data)   # [3, 7, 3, 1, 3, 9, 7, 11, 13]
```

---

## Q7: Nested list
Create a 2-row, 3-column nested list representing a small grade table. Access the element in row 1, column 2.

**Solution**
```python
grades = [
    [88, 72, 95],   # student 0
    [60, 84, 78],   # student 1
]
print(grades[1][2])   # 78  (student 1, subject 2)
```

---

## Q8: List comprehension — filter
From `numbers = list(range(1, 21))`, build a new list of numbers divisible by 3.

**Solution**
```python
numbers    = list(range(1, 21))
div_by_3   = [n for n in numbers if n % 3 == 0]
print(div_by_3)   # [3, 6, 9, 12, 15, 18]
```

---

## Q9: Copy vs reference
Show the difference between a shallow copy and a direct reference assignment.

**Solution**
```python
original = [1, 2, 3]

ref  = original       # same object
copy = original[:]    # new object

ref.append(99)
print(original)   # [1, 2, 3, 99]  — ref changed original!

copy.append(55)
print(original)   # [1, 2, 3, 99]  — copy did NOT change original
print(copy)       # [1, 2, 3, 55]
```

---

## Q10: len, min, max, sum
Given `scores = [88, 74, 95, 62, 79, 91]`, print the count, minimum, maximum, and average.

**Solution**
```python
scores = [88, 74, 95, 62, 79, 91]
print("Count  :", len(scores))
print("Min    :", min(scores))
print("Max    :", max(scores))
print("Average:", sum(scores) / len(scores))
```

---

⬅️ Previous: [04-01: Exercises — Functions](04-01-functions-basics-exe.md)
➡️ Next: [05-02: Exercises — Tuples](05-02-tuples-exe.md)
