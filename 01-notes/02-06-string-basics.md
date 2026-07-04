# 02-06: Strings — The str Type

A **string** (`str`) is a sequence of Unicode characters. Strings are **immutable** — once created, their contents cannot be changed in place.

---

## Creating Strings

```python
# Single quotes
s1 = 'hello'

# Double quotes
s2 = "world"

# Triple quotes (multi-line)
s3 = """This is
a multi-line
string"""

s4 = '''Another
multi-line'''

# Empty string
empty = ""
also_empty = ''
```

### When to use single vs. double quotes

```python
# Embed single quotes inside double-quoted string
msg1 = "It's a beautiful day"

# Embed double quotes inside single-quoted string
msg2 = 'She said "hello"'

# Both kinds using escape characters
msg3 = 'It\'s a "wonderful" life'
```

---

## Escape Characters

| Escape | Meaning |
|--------|---------|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |
| `\a` | Alert / Bell |
| `\0` | Null character |

```python
print("Hello\nWorld")     # two lines
print("A\tB\tC")          # tab-separated
print("path: C:\\Users")  # literal backslash
print('say: \'hi\'')      # escaped single quotes
```

### Raw strings — disable escape sequences

```python
# r"..." treats backslashes literally
path = r"C:\Users\jahid\Documents"
regex = r"\d+\.\d+"
print(path)   # C:\Users\jahid\Documents
```

---

## String Length

```python
s = "hello"
print(len(s))     # 5

s2 = "hi\nJoe"
print(len(s2))    # 6   (\n counts as one character)

print(len(""))    # 0
print(len("   ")) # 3  (spaces count)
```

---

## Indexing — Accessing Single Characters

Strings are **zero-indexed**. Indexing from the end is also possible using **negative indices**.

```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5
#   -6 -5 -4 -3 -2 -1

print(s[0])    # 'P'
print(s[1])    # 'y'
print(s[-1])   # 'n'  (last character)
print(s[-2])   # 'o'
print(s[-6])   # 'P'
```

### IndexError

```python
s = "hello"
print(s[5])   # IndexError: string index out of range
print(s[-6])  # IndexError
```

---

## Slicing — Extracting Substrings

Syntax: `s[start:stop:step]`

- `start` — index to begin (inclusive), defaults to 0
- `stop` — index to end (exclusive), defaults to `len(s)`
- `step` — how many characters to skip, defaults to 1

```python
s = "Python Programming"
#    0123456789...

print(s[0:6])    # 'Python'   (chars 0,1,2,3,4,5)
print(s[7:])     # 'Programming'
print(s[:6])     # 'Python'
print(s[-11:])   # 'Programming'
print(s[:])      # 'Python Programming'  (full copy)
```

### Step in slices

```python
s = "abcdefghij"
print(s[::2])     # 'acegi'    (every 2nd char)
print(s[1::2])    # 'bdfhj'    (odd-indexed chars)
print(s[::-1])    # 'jihgfedcba'  (reversed!)
print(s[8:2:-1])  # 'ihgfed'   (reverse slice)
```

### Practical slice examples

```python
email = "user@example.com"
username = email[:email.find('@')]    # 'user'
domain   = email[email.find('@')+1:]  # 'example.com'

url = "https://www.google.com"
print(url[8:])    # 'www.google.com'

# Last 4 characters of a string
card = "4111111111111234"
print(card[-4:])  # '1234'
```

---

## String Operators

### Concatenation with `+`

```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)     # 'Hello World'

# Can concatenate multiple strings
greeting = "Good" + " " + "morning" + "!"
```

### Repetition with `*`

```python
line = "-" * 30
print(line)       # '------------------------------'

laugh = "ha" * 3
print(laugh)      # 'hahaha'

header = "=" * 20 + " MENU " + "=" * 20
```

### Membership — `in` and `not in`

```python
s = "Python Programming"

print("Python" in s)       # True
print("Java" in s)         # False
print("pro" in s)          # False  (case-sensitive!)
print("Pro" in s)          # True

print("Java" not in s)     # True
```

---

## Comparing Strings

Strings are compared **lexicographically** (character by character using Unicode values).

```python
print("apple" < "banana")    # True  (a < b)
print("apple" < "Apple")     # False (lowercase > uppercase)
print("abc" == "abc")        # True
print("abc" != "xyz")        # True
print("hi" < "hello")        # False (i > e at index 1)

# Comparing by character code
print(ord('a'))   # 97
print(ord('A'))   # 65  (uppercase is smaller)
print(ord('z'))   # 122
```

---

## Iterating over Strings

A string is iterable — its characters can be looped through directly:

```python
for char in "hello":
    print(char)
# h
# e
# l
# l
# o

# Count vowels
vowels = 0
for ch in "Hello World":
    if ch.lower() in "aeiou":
        vowels += 1
print(vowels)   # 3

# Build reversed string manually
s = "Python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)   # nohtyP
```

---

## Strings are Immutable

Individual characters **cannot** be changed:

```python
s = "hello"
s[0] = "H"    # TypeError: 'str' object does not support item assignment
```

Instead, create a new string:

```python
s = "hello"
s = "H" + s[1:]   # 'Hello'

# Or using replace()
s = "hello"
s = s.replace("h", "H")   # 'Hello'
```

---

## String and Numbers — No Implicit Conversion

```python
age = 25
# print("Age: " + age)       # TypeError!
print("Age: " + str(age))    # correct
print("Age:", age)            # print handles it
print(f"Age: {age}")          # f-string handles it

# String repetition is not multiplication
print("5" * 3)    # '555'  (repetition)
print(5 * 3)      # 15     (multiplication)
```

---

## Splitting and Joining

```python
sentence = "the quick brown fox"
words = sentence.split(" ")
print(words)     # ['the', 'quick', 'brown', 'fox']
print(len(words)) # 4

# Split by any whitespace (default)
words2 = sentence.split()
print(words2)    # ['the', 'quick', 'brown', 'fox']

# Split with limit
parts = "a:b:c:d".split(":", 2)
print(parts)     # ['a', 'b', 'c:d']

# Join
joined = " ".join(words)
print(joined)    # 'the quick brown fox'

csv_line = ",".join(["Alice", "30", "Engineer"])
print(csv_line)  # 'Alice,30,Engineer'
```

---

## The `str()` Function — Converting to String

```python
print(str(42))         # '42'
print(str(3.14))       # '3.14'
print(str(True))       # 'True'
print(str(None))       # 'None'
print(str([1, 2, 3]))  # '[1, 2, 3]'
```

---

## Quick Summary

| Operation | Example | Result |
|-----------|---------|--------|
| Index | `"hello"[1]` | `'e'` |
| Negative index | `"hello"[-1]` | `'o'` |
| Slice | `"hello"[1:4]` | `'ell'` |
| Reverse | `"hello"[::-1]` | `'olleh'` |
| Concatenate | `"hi" + " there"` | `'hi there'` |
| Repeat | `"ab" * 3` | `'ababab'` |
| Length | `len("hello")` | `5` |
| Membership | `"ell" in "hello"` | `True` |
| Compare | `"abc" < "abd"` | `True` |

---

## Practice Problems

```python
# 1. Reverse a string using slicing
s = "Python"
print(s[::-1])   # nohtyP

# 2. Check if a word is a palindrome
word = "racecar"
print(word == word[::-1])   # True

# 3. Extract file extension
filename = "report.pdf"
dot_index = filename.rfind(".")
ext = filename[dot_index+1:]
print(ext)   # pdf

# 4. Count occurrences of a character
text = "banana"
count = 0
for ch in text:
    if ch == 'a':
        count += 1
print(count)   # 3

# 5. Capitalize every other character
s = "python"
result = ""
for i, ch in enumerate(s):
    result += ch.upper() if i % 2 == 0 else ch
print(result)   # PyThOn
```

---

> **Exercises:** [02-06: Exercises — String Basics](../02-exercises/02-06-string-basics-exe.md)

---

⬅️ Previous: [02-05: Number Types — int and float](02-05-number-types-int-float.md)
➡️ Next: [02-07: String Methods — Complete Reference](02-07-string-methods.md)
