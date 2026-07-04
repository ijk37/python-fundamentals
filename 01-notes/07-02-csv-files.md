# 07-02: Working with CSV Files

**CSV** (Comma-Separated Values) is the most common format for tabular data — spreadsheets, exports from databases, and datasets. Python's built-in `csv` module handles it cleanly, and Pandas makes complex operations trivial.

---

## What is a CSV file?

```
name,age,city,score
Alice,30,New York,88.5
Bob,25,London,92.0
Charlie,35,Tokyo,79.3
```

- First row is usually a **header**
- Each row is one record
- Fields are separated by a delimiter (usually `,` but can be `;`, `\t`, `|`)
- Text fields with commas inside are **quoted**: `"Smith, John"`

---

## Reading CSV — Built-in `csv` Module

### Basic reader

```python
import csv

with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        # ['Alice', '30', 'New York', '88.5']

# Note: always pass newline="" to open() with csv to handle \r\n correctly
```

### Skip header row

```python
import csv

with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)          # consume the first row
    print("Columns:", header)

    for row in reader:
        name, age, city, score = row
        print(f"{name} (age {age}) from {city}, score: {score}")
```

### DictReader — rows as dictionaries

```python
import csv

with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # row is an OrderedDict/dict keyed by header names
        print(row["name"], row["score"])

# Load all rows into a list
with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    records = list(csv.DictReader(f))

print(records[0])   # {'name': 'Alice', 'age': '30', ...}
```

### Convert types (CSV values are always strings)

```python
import csv

with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    students = []
    for row in reader:
        students.append({
            "name":  row["name"],
            "age":   int(row["age"]),
            "city":  row["city"],
            "score": float(row["score"]),
        })

# Now work with proper types
ages = [s["age"] for s in students]
print(f"Average age: {sum(ages) / len(ages):.1f}")

high_scorers = [s["name"] for s in students if s["score"] >= 85]
print("High scorers:", high_scorers)
```

---

## Writing CSV

### Basic writer

```python
import csv

header = ["name", "age", "city", "score"]
data = [
    ["Alice",   30, "New York", 88.5],
    ["Bob",     25, "London",   92.0],
    ["Charlie", 35, "Tokyo",    79.3],
]

with open("output.csv", "wt", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)    # write header
    writer.writerows(data)     # write all rows at once
```

### DictWriter — write from dicts

```python
import csv

students = [
    {"name": "Alice",   "age": 30, "score": 88.5},
    {"name": "Bob",     "age": 25, "score": 92.0},
    {"name": "Charlie", "age": 35, "score": 79.3},
]

fields = ["name", "age", "score"]

with open("output.csv", "wt", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()        # write header row automatically
    writer.writerows(students)
```

### Appending rows

```python
import csv

new_student = ["Diana", 28, "Paris", 95.5]

with open("students.csv", "at", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_student)
```

---

## Custom Dialects and Delimiters

```python
import csv

# Tab-separated (TSV)
with open("data.tsv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

# Semicolon-separated (common in European locales)
with open("data.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(row)

# Custom quote character
with open("data.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, quotechar="'")
    for row in reader:
        print(row)

# Write with pipe delimiter
with open("out.csv", "wt", newline="") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(["a", "b", "c"])
```

---

## Handling Edge Cases

### Fields that contain commas or quotes

```python
# csv module handles this automatically with quoting
import csv

data = [
    ["Alice Smith", 30, "New York, NY"],   # city has a comma
    ['Bob "The Rock" Jones', 25, "LA"],    # name has quotes
]

with open("tricky.csv", "wt", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# File will look like:
# Alice Smith,30,"New York, NY"
# "Bob ""The Rock"" Jones",25,LA
```

### Missing values

```python
import csv

with open("data.csv", "rt", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        score = row.get("score", "N/A")
        age = int(row["age"]) if row["age"] else None
        print(f"{row['name']}: score={score}, age={age}")
```

### Large files — process line by line

```python
import csv

total = 0
count = 0

with open("large_data.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += float(row["value"])
        count += 1

print(f"Sum: {total:.2f}, Count: {count}")
# Memory efficient — reads one row at a time, doesn't load whole file
```

---

## CSV with Pandas (recommended for data analysis)

```python
import pandas as pd

# Read CSV into a DataFrame
df = pd.read_csv("students.csv")
print(df)
print(df.dtypes)

# Pandas infers types automatically
# Read with specific options
df = pd.read_csv(
    "students.csv",
    sep=",",               # delimiter
    encoding="utf-8",
    header=0,              # row 0 is the header
    index_col=None,        # don't use any column as index
    usecols=["name", "score"],  # only load these columns
    dtype={"age": int, "score": float},
    na_values=["N/A", ""],     # treat these as NaN
    skiprows=0,
    nrows=100,             # read only first 100 rows
)

# Write DataFrame to CSV
df.to_csv("output.csv", index=False)   # index=False: don't write row numbers
df.to_csv("output.csv", index=False, float_format="%.2f")

# Quick analysis
print(df.head())           # first 5 rows
print(df.describe())       # statistics
print(df["score"].mean())  # column mean
```

---

## Practical Examples

### Filter and save

```python
import csv

# Read, filter rows where score >= 80, save to new file
with open("students.csv", "rt", newline="") as infile, \
     open("high_scorers.csv", "wt", newline="") as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        if float(row["score"]) >= 80:
            writer.writerow(row)
```

### Aggregate by group

```python
import csv
from collections import defaultdict

# Average score by city
city_scores = defaultdict(list)

with open("students.csv", "rt", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        city_scores[row["city"]].append(float(row["score"]))

for city, scores in city_scores.items():
    avg = sum(scores) / len(scores)
    print(f"{city}: {avg:.1f} (n={len(scores)})")
```

### CSV to list of dicts (utility function)

```python
import csv

def read_csv(path, delimiter=",", encoding="utf-8"):
    """Read CSV and return list of dicts with auto type conversion."""
    with open(path, "rt", encoding=encoding, newline="") as f:
        return list(csv.DictReader(f, delimiter=delimiter))

def write_csv(path, records, fieldnames=None, encoding="utf-8"):
    """Write list of dicts to CSV."""
    if not records:
        return
    fieldnames = fieldnames or list(records[0].keys())
    with open(path, "wt", encoding=encoding, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

students = read_csv("students.csv")
high = [s for s in students if float(s["score"]) >= 80]
write_csv("high_scorers.csv", high)
```

---

## Quick Summary

| Task | Code |
|------|------|
| Read CSV rows as lists | `csv.reader(f)` |
| Read CSV rows as dicts | `csv.DictReader(f)` |
| Write list of lists | `csv.writer(f)` → `writerows()` |
| Write list of dicts | `csv.DictWriter(f, fieldnames)` → `writerows()` |
| Custom delimiter | `csv.reader(f, delimiter="\t")` |
| With Pandas | `pd.read_csv("file.csv")` |
| Always use | `newline=""` in `open()` for CSV |

---

> **Exercises:** [07-02: Exercises — CSV Files](../02-exercises/07-02-csv-files-exe.md)

---

⬅️ Previous: [07-01: File I/O — Reading and Writing Files](07-01-file-io.md)
➡️ Next: [07-03: Working with JSON Files](07-03-json-files.md)
