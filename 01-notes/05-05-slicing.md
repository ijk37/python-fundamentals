# 05-05: Slicing — Extracting Subsequences

Slicing extracts a portion of a sequence (string, list, tuple, range, bytes). The syntax is `seq[start:stop:step]`.

---

## Basic Syntax

```python
seq[start:stop]        # items from start to stop-1
seq[start:stop:step]   # items from start, step apart, up to stop-1
```

- `start` — index to begin (inclusive), default `0`
- `stop` — index to end (exclusive), default `len(seq)`
- `step` — how many positions to advance, default `1`

All three are optional. Missing values use their defaults.

---

## String Slicing

```python
s = "Hello, Python!"
#    0123456789...

print(s[0:5])      # 'Hello'
print(s[7:13])     # 'Python'
print(s[:5])       # 'Hello'    (start defaults to 0)
print(s[7:])       # 'Python!'  (stop defaults to end)
print(s[:])        # 'Hello, Python!'  (full copy)
print(s[-7:-1])    # 'Python'
print(s[-1])       # '!'  (negative index = from end)
```

---

## List Slicing

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])     # [2, 3, 4, 5]
print(nums[:4])      # [0, 1, 2, 3]
print(nums[6:])      # [6, 7, 8, 9]

# Slice returns a new list — original unchanged
sub = nums[2:5]
print(sub)           # [2, 3, 4]
print(nums)          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modifying via slice
nums[2:5] = [20, 30, 40]
print(nums)          # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]
```

---

## The `step` Parameter

```python
s = "abcdefghij"

print(s[::2])      # 'acegi'    — every 2nd character
print(s[1::2])     # 'bdfhj'    — every 2nd, start at 1
print(s[::3])      # 'adgj'     — every 3rd

# Negative step — go backwards
print(s[::-1])     # 'jihgfedcba'  — reversed
print(s[8:2:-1])   # 'ihgfed'   — from index 8 down to 3
print(s[::-2])     # 'jhfdb'    — every 2nd, reversed
```

---

## Negative Indices in Slices

Negative indices count from the end of the sequence:

```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5
#   -6 -5 -4 -3 -2 -1

print(s[-3:])      # 'hon'   — last 3 chars
print(s[:-3])      # 'Pyt'   — all except last 3
print(s[-4:-1])    # 'tho'   — from -4 to -2
```

---

## Common Slicing Patterns

```python
s = "Hello, World!"

# First n characters
print(s[:5])          # 'Hello'

# Last n characters
print(s[-6:])         # 'World!'

# All except first n
print(s[3:])          # 'lo, World!'

# All except last n
print(s[:-1])         # 'Hello, World'

# Reverse
print(s[::-1])        # '!dlroW ,olleH'

# Every other character
print(s[::2])         # 'Hlo ol!'

# Middle part
n = len(s)
print(s[n//4: 3*n//4])  # middle half

# Capitalize first character
print(s[0].upper() + s[1:])
```

---

## Slicing Lists

```python
lst = [10, 20, 30, 40, 50, 60, 70]

# First half
half = len(lst) // 2
print(lst[:half])    # [10, 20, 30]
print(lst[half:])    # [40, 50, 60, 70]

# Rotate left by k
def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate_left([1,2,3,4,5], 2))   # [3, 4, 5, 1, 2]

# Rotate right by k
def rotate_right(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_right([1,2,3,4,5], 2))  # [4, 5, 1, 2, 3]

# Reverse
print(lst[::-1])     # [70, 60, 50, 40, 30, 20, 10]
```

---

## Slice Assignment

Lists support assigning to a slice — this can change the list's size:

```python
lst = [1, 2, 3, 4, 5]

# Replace a slice
lst[1:3] = [20, 30]
print(lst)    # [1, 20, 30, 4, 5]

# Replace with different length (list grows)
lst[1:3] = [10, 11, 12, 13]
print(lst)    # [1, 10, 11, 12, 13, 4, 5]

# Delete a slice (replace with empty)
lst[1:4] = []
print(lst)    # [1, 13, 4, 5]

# Insert at position (replace empty slice)
lst[2:2] = [99, 98]
print(lst)    # [1, 13, 99, 98, 4, 5]
```

---

## Slicing Tuples

Tuples support slicing but not slice assignment (immutable):

```python
t = (1, 2, 3, 4, 5)

print(t[1:4])    # (2, 3, 4)
print(t[::-1])   # (5, 4, 3, 2, 1)
print(t[::2])    # (1, 3, 5)

# Reassemble with slicing
first, *middle, last = t
print(first, middle, last)   # 1 [2, 3, 4] 5
```

---

## Slicing `range()`

```python
r = range(10)
print(r[2:7])       # range(2, 7)
print(list(r[2:7])) # [2, 3, 4, 5, 6]
print(list(r[::3])) # [0, 3, 6, 9]
```

---

## The `slice` Object

A reusable slice object can be created:

```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Create named slices
first_half = slice(None, len(data)//2)
last_half  = slice(len(data)//2, None)
every_odd  = slice(None, None, 2)

print(data[first_half])   # [10, 20, 30, 40]
print(data[last_half])    # [50, 60, 70, 80, 90]
print(data[every_odd])    # [10, 30, 50, 70, 90]

# Useful for spreadsheet-like column access
PRICE  = slice(0, 8)
VOLUME = slice(8, 16)
row = "1234.569987654"
print(row[PRICE])          # '1234.569'
print(row[VOLUME])         # '987654'
```

---

## Practical Examples

### Extracting parts of a string

```python
# Email parsing
email = "alice.smith@example.com"
at_pos = email.index("@")
dot_pos = email.rindex(".")

username = email[:at_pos]       # 'alice.smith'
domain   = email[at_pos+1:]     # 'example.com'
tld      = email[dot_pos+1:]    # 'com'

# Phone formatting
phone = "1234567890"
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(formatted)   # (123) 456-7890

# Credit card masking
card = "4111111111111234"
masked = "*" * 12 + card[-4:]
print(masked)   # ************1234
```

### Checking palindromes

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))   # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))     # False
```

### Chunking a list

```python
def chunk(lst, n):
    """Split list into chunks of size n"""
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(chunk([1,2,3,4,5,6,7,8,9], 3))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## Quick Reference

| Pattern | Result |
|---------|--------|
| `s[a:b]` | chars/items from a to b-1 |
| `s[:b]` | first b items |
| `s[a:]` | from a to end |
| `s[:]` | copy of entire sequence |
| `s[-n:]` | last n items |
| `s[:-n]` | all except last n |
| `s[::k]` | every k-th item |
| `s[::-1]` | reversed |
| `s[a:b:k]` | from a to b-1, step k |

---

> **Exercises:** [05-05: Exercises — Slicing](../02-exercises/05-05-slicing-exe.md)

---

⬅️ Previous: [05-04: Dictionaries](05-04-dictionaries.md)
➡️ Next: [05-06: Data Structures Comparison — str, list, tuple, set, dict](05-06-data-structures-comparison.md)
