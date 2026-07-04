# 07-01: Exercises — File I/O

> **Notes reference:** [07-01: File I/O — Reading and Writing Files](../01-notes/07-01-file-io.md)

---

## Q1: Write and read a file
Write three lines to `greetings.txt`, then read the entire file and print it.

**Solution**
```python
# Write
with open("greetings.txt", "wt", encoding="utf-8") as f:
    f.write("Hello from Dhaka!\n")
    f.write("Hello from New York!\n")
    f.write("Hello from Berlin!\n")

# Read back
with open("greetings.txt", "rt", encoding="utf-8") as f:
    content = f.read()
print(content)
```

---

## Q2: Read line by line
Read `greetings.txt` line by line and print each line stripped of its trailing newline.

**Solution**
```python
with open("greetings.txt", "rt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip("\n"))
```

**Alternative — using readlines():**
```python
with open("greetings.txt", "rt", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())
```

---

## Q3: Append to a file
Append two more lines to `greetings.txt` without overwriting the existing content.

**Solution**
```python
with open("greetings.txt", "at", encoding="utf-8") as f:
    f.write("Hello from Tokyo!\n")
    f.write("Hello from Nairobi!\n")

# Verify
with open("greetings.txt", "rt", encoding="utf-8") as f:
    print(f.read())
```

---

## Q4: writelines() and print() to file
Write a shopping list using `writelines()`, then append a total using `print(..., file=f)`.

**Solution**
```python
items = ["Rice\n", "Lentils\n", "Fish\n", "Vegetables\n"]

with open("shopping.txt", "wt", encoding="utf-8") as f:
    f.writelines(items)
    print("--- Total: 4 items ---", file=f)

with open("shopping.txt", "rt") as f:
    print(f.read())
```

---

## Q5: File position — tell() and seek()
Write some text, then use `seek()` to re-read from the beginning without closing the file.

**Solution**
```python
with open("pos_test.txt", "wt", encoding="utf-8") as f:
    f.write("abcdefghij")

with open("pos_test.txt", "rt", encoding="utf-8") as f:
    chunk = f.read(4)
    print(f"First 4 chars: {chunk}")    # abcd
    print(f"Position: {f.tell()}")      # 4
    f.seek(0)
    print(f"From start: {f.read()}")    # abcdefghij
```

---

## Q6: Error handling — FileNotFoundError
Try to open a non-existent file and handle the error gracefully.

**Solution**
```python
def safe_read(path):
    try:
        with open(path, "rt", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None
    except PermissionError:
        print(f"No permission to read '{path}'.")
        return None

content = safe_read("missing_file.txt")
print(content)   # None
```

---

## Q7: Copy a file
Copy `greetings.txt` to `greetings_backup.txt` line by line.

**Solution**
```python
with open("greetings.txt", "rt", encoding="utf-8") as src, \
     open("greetings_backup.txt", "wt", encoding="utf-8") as dst:
    for line in src:
        dst.write(line)
print("Backup created.")
```

---

## Q8: Log writer
Write a function `log(msg, level)` that appends a timestamped log entry to `app.log`.

**Solution**
```python
from datetime import datetime

def log(message, level="INFO", logfile="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{level}] {message}\n"
    with open(logfile, "at", encoding="utf-8") as f:
        f.write(entry)

log("Server started")
log("User 'jahid' logged in")
log("Database timeout", level="ERROR")

with open("app.log", "rt") as f:
    print(f.read())
```

---

## Q9: Simple config reader
Read a plain key=value config file (skip blank lines and lines starting with `#`).

**Solution**
```python
# First create a sample config
with open("config.txt", "wt") as f:
    f.write("# App configuration\n")
    f.write("host = localhost\n")
    f.write("port = 8080\n")
    f.write("\n")
    f.write("debug = true\n")

# Read it
def read_config(path):
    config = {}
    with open(path, "rt") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, _, value = line.partition("=")
            config[key.strip()] = value.strip()
    return config

cfg = read_config("config.txt")
print(cfg)   # {'host': 'localhost', 'port': '8080', 'debug': 'true'}
```

---

## Q10: Word frequency from file
Count the most common 5 words in a text file (ignore punctuation, case-insensitive).

**Solution**
```python
from collections import Counter

# Create sample file
with open("article.txt", "wt") as f:
    f.write("Python is great. Python is simple. Python is popular.\n")
    f.write("Many developers use Python for data science and automation.\n")

with open("article.txt", "rt") as f:
    text = f.read().lower()

words = text.split()
words = [w.strip(".,!?;:\"'()") for w in words]
freq  = Counter(words)

print("Top 5 words:")
for word, count in freq.most_common(5):
    print(f"  {word}: {count}")
```

---

⬅️ Previous: [06-02: Exercises — Exception Handling](06-02-exception-handling-exe.md)
➡️ Next: [07-02: Exercises — CSV Files](07-02-csv-files-exe.md)
