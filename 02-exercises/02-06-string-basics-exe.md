# 02-06: Exercises — String Basics

> **Notes reference:** [02-06: Strings — The str Type](../01-notes/02-06-string-basics.md)

---

## Q1: String creation
Create the same string `He said, "It's fine."` using: (a) single quotes, (b) double quotes, (c) triple quotes.

**Solution**
```python
a = 'He said, "It\'s fine."'
b = "He said, \"It's fine.\""
c = '''He said, "It's fine."'''
print(a)
print(b)
print(c)
```

---

## Q2: String indexing
Given `city = "Chittagong"`, print: the first character, the last character, and the 5th character (index 4).

**Solution**
```python
city = "Chittagong"
print(city[0])    # C
print(city[-1])   # g
print(city[4])    # t
```

---

## Q3: Negative indexing
Given `lang = "Bangladesh"`, print the last 3 characters using negative indexing.

**Solution**
```python
lang = "Bangladesh"
print(lang[-3])    # d
print(lang[-2])    # e
print(lang[-1])    # s

# Or as a slice:
print(lang[-3:])   # des
```

---

## Q4: String slicing
Given `s = "New York City"`, extract:
- `"New"`
- `"York"`
- `"City"`
- the whole string reversed

**Solution**
```python
s = "New York City"
print(s[:3])       # New
print(s[4:8])      # York
print(s[9:])       # City
print(s[::-1])     # ytiC kroY weN
```

---

## Q5: String length and membership
Given `country = "United States"`, print its length and check whether `"States"` is in it.

**Solution**
```python
country = "United States"
print(len(country))           # 13
print("States" in country)    # True
print("Canada" not in country)# True
```

---

## Q6: Concatenation and repetition
Build the string `"BangladeshBangladeshBangladesh"` using repetition, and build `"Dhaka, New York"` using concatenation.

**Solution**
```python
repeated    = "Bangladesh" * 3
print(repeated)     # BangladeshBangladeshBangladesh

city1, city2 = "Dhaka", "New York"
combined = city1 + ", " + city2
print(combined)     # Dhaka, New York
```

---

## Q7: Escape characters
Print the following output exactly:
```
Line 1
	Line 2 (tabbed)
She said, "Hello!"
C:\Users\jahid
```

**Solution**
```python
print("Line 1\n\tLine 2 (tabbed)\nShe said, \"Hello!\"\nC:\\Users\\jahid")
```

---

## Q8: Raw strings
Print the Windows path `C:\new_folder\test.py` without the `\n` and `\t` being treated as escape sequences.

**Solution**
```python
path = r"C:\new_folder\test.py"
print(path)   # C:\new_folder\test.py

# Without r prefix — wrong:
# print("C:\new_folder\test.py")  # \n becomes newline, \t becomes tab
```

---

## Q9: Multiline strings
Create a multiline string containing two lines of a poem and print it.

**Solution**
```python
poem = """Amar sonar Bangla,
Ami tomay bhalobashi."""
print(poem)
```

---

## Q10: String immutability
The following code tries to change the first character of a string. What error occurs? How would the fix look?

```python
word = "python"
word[0] = "P"
```

**Solution**
```
TypeError: 'str' object does not support item assignment
Strings are immutable — individual characters cannot be changed.
```

Fix:
```python
word = "python"
word = "P" + word[1:]   # create a new string
print(word)   # Python
```

---

⬅️ Previous: [02-05: Exercises — Number Types: int and float](02-05-number-types-int-float-exe.md)
➡️ Next: [02-07: Exercises — String Methods](02-07-string-methods-exe.md)
