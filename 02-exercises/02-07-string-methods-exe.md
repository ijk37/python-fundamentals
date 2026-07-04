# 02-07: Exercises — String Methods

> **Notes reference:** [02-07: String Methods — Complete Reference](../01-notes/02-07-string-methods.md)

---

## Q1: Case methods
Given `s = "data science with python"`, print it in uppercase, title case, and with the first letter capitalised.

**Solution**
```python
s = "data science with python"
print(s.upper())       # DATA SCIENCE WITH PYTHON
print(s.title())       # Data Science With Python
print(s.capitalize())  # Data science with python
```

---

## Q2: Content checks
Check whether each string meets the condition described:

```python
"2024"        → all digits?
"Dhaka123"    → all alphanumeric?
"   \t\n"     → all whitespace?
"myVariable"  → valid Python identifier?
```

**Solution**
```python
print("2024".isdigit())           # True
print("Dhaka123".isalnum())       # True
print("   \t\n".isspace())        # True
print("myVariable".isidentifier())# True
```

---

## Q3: Search and count
In the string `s = "the river flows through the green valley"`, find:
- the index of the first `"the"`
- the index of the last `"the"`
- how many times `"the"` appears

**Solution**
```python
s = "the river flows through the green valley"
print(s.find("the"))    # 0
print(s.rfind("the"))   # 24
print(s.count("the"))   # 2
```

---

## Q4: Replace
Given `text = "I love Java. Java is great. Java pays well."`, replace all `"Java"` with `"Python"`. Then replace only the first occurrence.

**Solution**
```python
text = "I love Java. Java is great. Java pays well."
print(text.replace("Java", "Python"))       # all replaced
print(text.replace("Java", "Python", 1))    # only first replaced
```

---

## Q5: Split and join
Split `"Dhaka,Chittagong,Sylhet,Rajshahi"` by `","`, print the list, then join it back with `" | "`.

**Solution**
```python
raw   = "Dhaka,Chittagong,Sylhet,Rajshahi"
parts = raw.split(",")
print(parts)               # ['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi']
print(" | ".join(parts))   # Dhaka | Chittagong | Sylhet | Rajshahi
```

---

## Q6: Strip and clean user input
A user entered `"   jahid@email.com   "` (with extra spaces). Strip the whitespace, convert to lowercase, and check that it ends with `".com"`.

**Solution**
```python
raw = "   jahid@email.com   "
clean = raw.strip().lower()
print(clean)                     # jahid@email.com
print(clean.endswith(".com"))    # True
```

---

## Q7: Alignment and padding
Print a small price list where item names are left-aligned in a field of 12 and prices are right-aligned in a field of 8 with 2 decimal places.

**Solution**
```python
print(f"{'Item':<12} {'Price':>8}")
print("-" * 22)
print(f"{'Notebook':<12} {35.00:>8.2f}")
print(f"{'Pen':<12} {12.50:>8.2f}")
print(f"{'USB Cable':<12} {250.00:>8.2f}")
```

---

## Q8: Partition an email
Given `email = "jahid.hassan@university.edu"`, use `partition("@")` to extract the local part and the domain separately.

**Solution**
```python
email = "jahid.hassan@university.edu"
local, sep, domain = email.partition("@")
print(local)    # jahid.hassan
print(domain)   # university.edu
```

---

## Q9: Translate / remove vowels
Remove all vowels from the string `"programming in python"` using `str.maketrans` and `translate`.

**Solution**
```python
s = "programming in python"
table = str.maketrans("", "", "aeiou")
print(s.translate(table))   # prgrmmng n pythn
```

---

## Q10: Practical — normalize a CSV line
Given `line = "  Alice , 30 , Engineer  "`, split by `","`, strip whitespace from each part, and print the clean list.

**Solution**
```python
line  = "  Alice , 30 , Engineer  "
parts = [p.strip() for p in line.split(",")]
print(parts)   # ['Alice', '30', 'Engineer']

# Without comprehensions (Section 06 — manual approach):
raw = line.split(",")
parts = [raw[0].strip(), raw[1].strip(), raw[2].strip()]
print(parts)
```

---

⬅️ Previous: [02-06: Exercises — String Basics](02-06-string-basics-exe.md)
➡️ Next: [02-08: Exercises — String Formatting](02-08-string-formatting-exe.md)
