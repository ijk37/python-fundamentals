# 05-05: Exercises — Slicing

> **Notes reference:** [05-05: Slicing — Extracting Subsequences](../01-notes/05-05-slicing.md)

---

## Q1: Basic list slice
Given `data = [10, 20, 30, 40, 50, 60, 70, 80]`, extract:
- elements at index 2 through 5
- the last 3 elements
- the first 4 elements

**Solution**
```python
data = [10, 20, 30, 40, 50, 60, 70, 80]
print(data[2:6])    # [30, 40, 50, 60]
print(data[-3:])    # [60, 70, 80]
print(data[:4])     # [10, 20, 30, 40]
```

---

## Q2: Step slicing
From `nums = list(range(1, 21))`, extract every third element, and every other element starting from index 1.

**Solution**
```python
nums = list(range(1, 21))
print(nums[::3])     # [1, 4, 7, 10, 13, 16, 19]
print(nums[1::2])    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## Q3: Reverse with slicing
Reverse the string `"Bangladesh"` and the list `[1, 2, 3, 4, 5]` using slice notation.

**Solution**
```python
print("Bangladesh"[::-1])    # hsedalgnaB
print([1, 2, 3, 4, 5][::-1]) # [5, 4, 3, 2, 1]
```

---

## Q4: String slicing — extract parts
Given `timestamp = "2024-11-15 09:30:00"`, extract the year, month, day, and time separately using slices.

**Solution**
```python
timestamp = "2024-11-15 09:30:00"
year  = timestamp[:4]
month = timestamp[5:7]
day   = timestamp[8:10]
time  = timestamp[11:]

print(year, month, day, time)   # 2024 11 15 09:30:00
```

---

## Q5: Replace a slice
Replace elements at index 2–4 of `[1, 2, 3, 4, 5, 6]` with `[30, 40]`.

**Solution**
```python
nums = [1, 2, 3, 4, 5, 6]
nums[2:5] = [30, 40]
print(nums)   # [1, 2, 30, 40, 6]
```

---

## Q6: slice object
Create a reusable `slice` object for `start=1, stop=8, step=2` and apply it to both a list and a string.

**Solution**
```python
every_odd = slice(1, 8, 2)

nums   = list(range(10))
text   = "abcdefghij"

print(nums[every_odd])    # [1, 3, 5, 7]
print(text[every_odd])    # bdfh
```

---

## Q7: Palindrome check using slicing
Check whether `"racecar"` and `"python"` are palindromes.

**Solution**
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))   # True
print(is_palindrome("python"))    # False
```

---

⬅️ Previous: [05-04: Exercises — Dictionaries](05-04-dictionaries-exe.md)
➡️ Next: [05-07: Exercises — zip(), enumerate(), and Conversions](05-07-zip-enumerate-and-conversions-exe.md)
