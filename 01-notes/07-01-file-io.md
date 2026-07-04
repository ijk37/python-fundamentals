# 07-01: File I/O — Reading and Writing Files

---

## Opening a File

```python
file = open(path, mode, encoding=...)
```

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default). Error if file doesn't exist |
| `"w"` | Write. Creates file or **overwrites** if exists |
| `"a"` | Append. Creates or appends to existing file |
| `"x"` | Exclusive create. Error if file already exists |
| `"r+"` | Read and write |
| `"b"` | Binary mode (add to others: `"rb"`, `"wb"`) |
| `"t"` | Text mode (default, add to others: `"rt"`, `"wt"`) |

---

## The `with` Statement — Recommended Approach

The `with` statement ensures the file is **always closed**, even if an exception occurs:

```python
with open("myfile.txt", "rt", encoding="utf-8") as f:
    content = f.read()
# File is automatically closed here

# Without with (error-prone)
f = open("myfile.txt", "rt")
content = f.read()
f.close()   # easy to forget!
```

---

## Reading Files

### `read()` — Read entire file as one string

```python
with open("poem.txt", "rt", encoding="utf-8") as f:
    content = f.read()
    print(content)
    print(f"Length: {len(content)} characters")
```

### `readlines()` — Read all lines into a list

```python
with open("data.txt", "rt") as f:
    lines = f.readlines()
    # Each line includes the trailing \n
    print(lines)   # ['line1\n', 'line2\n', 'line3\n']
    print(len(lines), "lines")
```

### `readline()` — Read one line at a time

```python
with open("data.txt", "rt") as f:
    line1 = f.readline()   # reads first line
    line2 = f.readline()   # reads second line
    print(repr(line1))
    print(repr(line2))
```

### Iterating line by line (most efficient)

```python
with open("data.txt", "rt", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")   # remove trailing newline
        print(line)
```

### Reading into a list with comprehension

```python
with open("data.txt", "rt") as f:
    lines = [line.rstrip("\n") for line in f]
    # Or strip all whitespace
    lines = [line.strip() for line in f if line.strip()]  # skip empty lines
```

---

## Writing Files

### `write()` — Write a string

```python
with open("output.txt", "wt", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")
    count = f.write("Third line\n")   # returns number of chars written
    print(count)   # 11
```

### `writelines()` — Write a list of strings

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "wt") as f:
    f.writelines(lines)  # note: does NOT add \n automatically
```

### Using `print()` to write to file

```python
with open("output.txt", "wt") as f:
    print("Hello!", file=f)          # adds \n by default
    print("Value:", 42, file=f)
    print("A", "B", "C", sep=",", file=f)
```

---

## Appending to a File

```python
with open("log.txt", "at", encoding="utf-8") as f:
    f.write("New log entry\n")
    f.write(f"Timestamp: {__import__('datetime').datetime.now()}\n")
```

---

## Copying a File

```python
with open("source.txt", "rt", encoding="utf-8") as fin, \
     open("destination.txt", "wt", encoding="utf-8") as fout:
    for line in fin:
        fout.write(line)
```

Or copy all at once:
```python
with open("source.txt", "rt") as fin:
    content = fin.read()
with open("destination.txt", "wt") as fout:
    fout.write(content)
```

---

## Working with CSV Files

### Reading CSV manually

```python
with open("students.csv", "rt", encoding="utf-8") as f:
    for line in f:
        cols = line.strip().split(",")
        name, age, grade = cols
        print(f"{name} is {age} years old, grade: {grade}")
```

### Using the `csv` module (recommended)

```python
import csv

# Reading
with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)     # skip header
    for row in reader:
        print(row)            # ['Alice', '22', 'A']

# Reading as dicts
with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["grade"])

# Writing
data = [["Alice", 22, "A"], ["Bob", 21, "B"]]
with open("out.csv", "wt", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])   # header
    writer.writerows(data)
```

---

## Working with JSON Files

```python
import json

# Write JSON
data = {"name": "Alice", "age": 30, "scores": [85, 92, 78]}
with open("data.json", "wt", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("data.json", "rt", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["name"])   # Alice
print(loaded["scores"]) # [85, 92, 78]

# JSON string ↔ Python object
json_str = json.dumps(data, indent=2)    # Python → JSON string
data2 = json.loads(json_str)             # JSON string → Python
```

---

## File Position

```python
with open("test.txt", "rt") as f:
    print(f.tell())        # 0 — at beginning
    chunk = f.read(5)      # read 5 chars
    print(f.tell())        # 5

    f.seek(0)              # go back to beginning
    content = f.read()     # read from start

    f.seek(0, 2)           # seek to end (0=begin, 1=current, 2=end)
    print(f.tell())        # file size in bytes
```

---

## Error Handling with Files

```python
def read_file(path):
    try:
        with open(path, "rt", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError:
        print(f"Permission denied: {path}")
        return None
    except UnicodeDecodeError:
        print(f"Encoding error — try a different encoding")
        return None
    except OSError as e:
        print(f"OS error: {e}")
        return None
```

---

## Checking File Existence

```python
import os
import os.path

path = "myfile.txt"

# Check if path exists
print(os.path.exists(path))    # True or False

# Check if it's a file (not directory)
print(os.path.isfile(path))    # True

# Check if it's a directory
print(os.path.isdir("mydir"))  # True

# Get file size
print(os.path.getsize(path))   # size in bytes
```

Using `pathlib` (modern, recommended):

```python
from pathlib import Path

p = Path("myfile.txt")
print(p.exists())      # True/False
print(p.is_file())     # True/False
print(p.stat().st_size)  # file size

# Create parent directories
p.parent.mkdir(parents=True, exist_ok=True)

# Read/write with pathlib
content = p.read_text(encoding="utf-8")
p.write_text("new content", encoding="utf-8")
```

---

## Working with Binary Files

```python
# Read binary file
with open("image.png", "rb") as f:
    header = f.read(8)    # read first 8 bytes
    print(header.hex())

# Write binary file
data = bytes([0x89, 0x50, 0x4E, 0x47])
with open("test.bin", "wb") as f:
    f.write(data)
```

---

## Practical Examples

### Log file writer

```python
from datetime import datetime

def log(message, level="INFO", logfile="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{level}] {message}\n"
    with open(logfile, "at", encoding="utf-8") as f:
        f.write(entry)

log("Application started")
log("User logged in: Alice")
log("Database connection failed", level="ERROR")
```

### Word frequency counter (from file)

```python
from collections import Counter

with open("document.txt", "rt", encoding="utf-8") as f:
    text = f.read().lower()

# Clean and count
words = text.split()
words = [w.strip(".,!?;:\"'()-") for w in words]
freq = Counter(words)

print("Top 10 words:")
for word, count in freq.most_common(10):
    print(f"  {word}: {count}")
```

### Simple config file reader

```python
def read_config(path):
    config = {}
    with open(path, "rt") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):  # skip empty/comments
                continue
            key, _, value = line.partition("=")
            config[key.strip()] = value.strip()
    return config

# config.txt:
# host = localhost
# port = 8080
# debug = true
cfg = read_config("config.txt")
print(cfg["host"])   # localhost
```

---

## Quick Summary

| Operation | Code |
|-----------|------|
| Open for reading | `open(path, "rt", encoding="utf-8")` |
| Open for writing | `open(path, "wt", encoding="utf-8")` |
| Open for appending | `open(path, "at", encoding="utf-8")` |
| Read all | `f.read()` |
| Read lines into list | `f.readlines()` |
| Read line-by-line | `for line in f:` |
| Write string | `f.write(text)` |
| Write list of lines | `f.writelines(lines)` |
| Write with print | `print(text, file=f)` |
| Auto-close | `with open(...) as f:` |

---

> **Exercises:** [07-01: Exercises — File I/O](../02-exercises/07-01-file-io-exe.md)

---

⬅️ Previous: [06-02: Exception Handling](06-02-exception-handling.md)
➡️ Next: [07-02: Working with CSV Files](07-02-csv-files.md)
