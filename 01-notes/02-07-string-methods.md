# 02-07: String Methods — Complete Reference

Strings in Python have a rich set of built-in methods. Since strings are **immutable**, every method returns a **new string** — the original is never changed.

---

## Case Methods

```python
s = "python Programming"

# Uppercase / Lowercase
print(s.upper())       # 'PYTHON PROGRAMMING'
print(s.lower())       # 'python programming'
print(s.swapcase())    # 'PYTHON pROGRAMMING' (toggles each char's case)

# Title and sentence case
print(s.title())       # 'Python Programming' (capitalizes each word)
print(s.capitalize())  # 'Python programming' (only first char of string)

# Checking case
print("PYTHON".isupper())    # True
print("python".islower())    # True
print("Python Code".istitle())  # True
print("Python Code".isupper())  # False

print("python".isupper())   # False
print("PYTHON".islower())   # False
```

---

## Checking Content

```python
# Character type checks — return True only if ALL chars match AND len > 0
print("hello".isalpha())    # True  — all letters
print("hello1".isalpha())   # False — has digit
print("".isalpha())         # False — empty

print("123".isdigit())      # True  — all digits
print("12.3".isdigit())     # False — dot is not a digit
print("²".isdigit())        # True  — superscript is a digit

print("12.3".isnumeric())   # False
print("½".isnumeric())      # True  — fraction is numeric
print("¼²".isnumeric())     # True

print("hello123".isalnum()) # True  — alphanumeric
print("hello!".isalnum())   # False — exclamation is not alnum

print("   ".isspace())      # True  — all whitespace
print("  \t\n".isspace())   # True
print("  a".isspace())      # False

print("my_var".isidentifier())   # True  — valid Python identifier
print("2var".isidentifier())     # False — starts with digit
print("class".isidentifier())    # True  — identifiers include keywords

# Check for ASCII
print("hello".isascii())    # True
print("héllo".isascii())    # False
```

---

## Searching and Finding

```python
s = "the cat sat on the mat"

# find — returns index of first occurrence, -1 if not found
print(s.find("cat"))        # 4
print(s.find("dog"))        # -1
print(s.find("at", 5))      # 5  (search starting at index 5)
print(s.find("at", 5, 12))  # 5  (search in s[5:12])

# rfind — find from the right (last occurrence)
print(s.rfind("at"))        # 20

# index — like find but raises ValueError if not found
print(s.index("cat"))       # 4
# print(s.index("dog"))     # ValueError: substring not found

# rindex — like rfind but raises ValueError
print(s.rindex("at"))       # 20

# count — count non-overlapping occurrences
print(s.count("at"))        # 3 (c_at, s_at, m_at)
print(s.count("the"))       # 2
print("aaa".count("aa"))    # 1 (non-overlapping)

# Prefix / Suffix checks
print(s.startswith("the"))  # True
print(s.startswith("cat"))  # False
print(s.endswith("mat"))    # True
print(s.endswith("cat"))    # False

# Check multiple prefixes/suffixes using tuple
print(s.startswith(("the", "a", "cat")))  # True
print(s.endswith((".txt", ".csv", "mat"))) # True
```

---

## Replacing

```python
s = "the cat sat on the mat"

# replace(old, new) — replaces ALL occurrences
print(s.replace("at", "AT"))       # 'the cAT sAT on the mAT'

# replace(old, new, count) — replace only first N
print(s.replace("at", "AT", 1))    # 'the cAT sat on the mat'
print(s.replace("the", "a"))       # 'a cat sat on a mat'

# remove a substring
print(s.replace("the ", ""))       # 'cat sat on mat'

# chain replacements
text = "  hello,  world!  "
clean = text.strip().replace(",", "").replace("!", "")
print(clean)   # 'hello  world'
```

---

## Splitting

```python
# split — splits on whitespace by default, removes empty strings
"hello world".split()       # ['hello', 'world']
"  hello   world  ".split() # ['hello', 'world']

# split on a delimiter
"a,b,c,d".split(",")        # ['a', 'b', 'c', 'd']
"one::two::three".split("::") # ['one', 'two', 'three']

# split with maxsplit — limit number of splits
"a,b,c,d".split(",", 2)     # ['a', 'b', 'c,d']

# rsplit — split from the right
"a,b,c,d".rsplit(",", 2)    # ['a,b', 'c', 'd']

# splitlines — split on line endings
text = "line1\nline2\r\nline3\rline4"
print(text.splitlines())
# ['line1', 'line2', 'line3', 'line4']

# splitlines preserves line endings with keepends=True
print(text.splitlines(keepends=True))
# ['line1\n', 'line2\r\n', 'line3\r', 'line4']

# partition — split into exactly 3 parts at FIRST occurrence
"user@example.com".partition("@")  # ('user', '@', 'example.com')
"no-at-sign".partition("@")        # ('no-at-sign', '', '')

# rpartition — split at LAST occurrence
"/usr/local/bin".rpartition("/")   # ('/usr/local', '/', 'bin')
```

---

## Joining

`join()` is the reverse of `split()` — it glues a sequence of strings together with a separator.

```python
# join a string character by character
print("_".join("abc"))        # 'a_b_c'
print("-".join("Python"))     # 'P-y-t-h-o-n'

# join a sequence of strings (lists are covered in Section 05)
print(" ".join(["Hello", "World", "Python"]))    # 'Hello World Python'
print("-".join(["Hello", "World", "Python"]))    # 'Hello-World-Python'
print("".join(["Hello", "World"]))               # 'HelloWorld'
print(", ".join(["apple", "banana", "cherry"]))  # 'apple, banana, cherry'
print("\n".join(["line1", "line2", "line3"]))    # three lines

# join with split — round-trip
sentence = "  hello   world  "
rejoined = " ".join(sentence.split())
print(rejoined)   # 'hello world'  (extra spaces removed)
```

---

## Stripping Whitespace

```python
s = "   hello world   "

print(s.strip())           # 'hello world' (both ends)
print(s.lstrip())          # 'hello world   ' (left only)
print(s.rstrip())          # '   hello world' (right only)

# Strip specific characters
"***hello***".strip("*")   # 'hello'
"xxhelloxx".strip("x")     # 'hello'
"abcHELLOcba".strip("abc") # 'HELLO' (strips any combo of chars)
"...hello...".lstrip(".")  # 'hello...'

# removeprefix / removesuffix (Python 3.9+)
"Hello, World!".removeprefix("Hello, ")  # 'World!'
"Hello, World!".removesuffix("!")        # 'Hello, World'
"Hello".removeprefix("Bye")             # 'Hello' (unchanged if not found)
```

---

## Alignment and Padding

```python
s = "hello"

# center(width, fillchar=' ')
print(s.center(11))        # '   hello   '
print(s.center(11, "*"))   # '***hello***'
print(s.center(11, "-"))   # '---hello---'

# ljust / rjust — left/right justify
print(s.ljust(10))         # 'hello     '
print(s.rjust(10))         # '     hello'
print(s.ljust(10, "."))    # 'hello.....'
print(s.rjust(10, "0"))    # '00000hello'

# zfill — pad with zeros (respects sign for numbers)
print("42".zfill(5))       # '00042'
print("-42".zfill(6))      # '-00042' (sign preserved)
print("3.14".zfill(7))     # '0003.14'

# Practical: right-align text (individual examples)
print(f"{'Apple':<10} ${1.50:>6.2f}")    # Apple      $  1.50
print(f"{'Banana':<10} ${0.75:>6.2f}")   # Banana     $  0.75
print(f"{'Cherry':<10} ${3.00:>6.2f}")   # Cherry     $  3.00
```

---

## Other Useful Methods

```python
# expandtabs — replace \t with spaces (default tab size = 8)
print("a\tb\tc".expandtabs(4))  # 'a   b   c'
print("name\tage\ncity\tzip".expandtabs(8))

# encode / decode
b = "hello".encode("utf-8")   # b'hello' (bytes object)
s = b.decode("utf-8")         # 'hello'

# translate + maketrans — character-level substitution
table = str.maketrans("aeiou", "12345")
print("hello world".translate(table))   # 'h2ll4 w4rld'

# Remove specific chars
table = str.maketrans("", "", "aeiou")
print("hello world".translate(table))   # 'hll wrld'

# format — string formatting (covered in 06-02)
"Hello, {}!".format("World")   # 'Hello, World!'
```

---

## Complete Method Reference Table

| Method | Description | Returns |
|--------|-------------|---------|
| `s.upper()` | All uppercase | str |
| `s.lower()` | All lowercase | str |
| `s.swapcase()` | Toggle case | str |
| `s.title()` | Capitalize each word | str |
| `s.capitalize()` | Capitalize first char only | str |
| `s.isupper()` | All uppercase? | bool |
| `s.islower()` | All lowercase? | bool |
| `s.istitle()` | Title case? | bool |
| `s.isalpha()` | All letters? | bool |
| `s.isdigit()` | All digits? | bool |
| `s.isnumeric()` | All numeric? | bool |
| `s.isalnum()` | All letters + digits? | bool |
| `s.isspace()` | All whitespace? | bool |
| `s.isidentifier()` | Valid Python identifier? | bool |
| `s.isascii()` | All ASCII? | bool |
| `s.find(sub)` | First index of sub or -1 | int |
| `s.rfind(sub)` | Last index of sub or -1 | int |
| `s.index(sub)` | First index (raises ValueError) | int |
| `s.rindex(sub)` | Last index (raises ValueError) | int |
| `s.count(sub)` | Count of sub | int |
| `s.startswith(s2)` | Starts with s2? | bool |
| `s.endswith(s2)` | Ends with s2? | bool |
| `s.replace(old, new)` | Replace all old with new | str |
| `s.split(sep)` | Split on sep | list |
| `s.rsplit(sep)` | Split from right | list |
| `s.splitlines()` | Split on line endings | list |
| `s.partition(sep)` | Split at first sep → 3-tuple | tuple |
| `s.rpartition(sep)` | Split at last sep → 3-tuple | tuple |
| `s.join(iterable)` | Join iterable with s | str |
| `s.strip(chars)` | Remove leading/trailing | str |
| `s.lstrip(chars)` | Remove leading | str |
| `s.rstrip(chars)` | Remove trailing | str |
| `s.removeprefix(pre)` | Remove prefix if present | str |
| `s.removesuffix(suf)` | Remove suffix if present | str |
| `s.center(w, ch)` | Center in width w | str |
| `s.ljust(w, ch)` | Left justify | str |
| `s.rjust(w, ch)` | Right justify | str |
| `s.zfill(w)` | Zero-pad | str |
| `s.expandtabs(n)` | Replace tabs with spaces | str |
| `s.encode(enc)` | Encode to bytes | bytes |
| `s.format(...)` | Format string | str |
| `s.translate(table)` | Character substitution | str |

---

## Practical Patterns

```python
# 1. Normalize user input
user_input = input("Enter name: ")
name = user_input.strip().title()
print(f"Hello, {name}!")

# 2. Split a CSV-like line
line = "Alice, 30, Engineer"
parts = line.split(", ")
name_val = parts[0].strip()    # 'Alice'
age_val  = parts[1].strip()    # '30'
role_val = parts[2].strip()    # 'Engineer'
print(name_val, age_val, role_val)

# 3. Count a specific character
text = "Hello World"
vowel_count = text.lower().count("a") + text.lower().count("e") + \
              text.lower().count("i") + text.lower().count("o") + \
              text.lower().count("u")
print(vowel_count)   # 3

# 4. Remove punctuation (manual replace)
text = "Hello, World! How are you?"
clean = text.replace(",", "").replace("!", "").replace("?", "").replace(".", "")
print(clean)   # 'Hello World How are you'

# 5. Palindrome check
word = "racecar"
cleaned = word.lower().replace(" ", "")
is_palindrome = (cleaned == cleaned[::-1])
print(is_palindrome)   # True

word2 = "hello"
cleaned2 = word2.lower()
print(cleaned2 == cleaned2[::-1])   # False

# 6. Count word occurrences (basic)
text = "the cat sat on the mat the cat"
word_to_find = "the"
count = text.count(word_to_find)
print(f"'{word_to_find}' appears {count} times")   # 3

# 7. Extract parts from an email
email = "user@example.com"
at_pos  = email.find("@")
local   = email[:at_pos]       # 'user'
domain  = email[at_pos + 1:]   # 'example.com'
print(local, domain)
```

---

> **Exercises:** [02-07: Exercises — String Methods](../02-exercises/02-07-string-methods-exe.md)

---

⬅️ Previous: [02-06: Strings — The str Type](02-06-string-basics.md)
➡️ Next: [02-08: String Formatting](02-08-string-formatting.md)
