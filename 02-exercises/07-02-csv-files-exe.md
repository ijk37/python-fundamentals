# 07-02: Exercises — CSV Files

> **Notes reference:** [07-02: Working with CSV Files](../01-notes/07-02-csv-files.md)

---

## Q1: Write a CSV file
Write a CSV with columns `name`, `city`, `score` for five students.

**Solution**
```python
import csv

header = ["name", "city", "score"]
data = [
    ["Rahul",   "Dhaka",    88.5],
    ["Sara",    "New York", 92.0],
    ["James",   "Berlin",   79.3],
    ["Nadia",   "Tokyo",    95.1],
    ["Michael", "Nairobi",  81.7],
]

with open("students.csv", "wt", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
print("students.csv written.")
```

---

## Q2: Read a CSV with csv.reader
Read `students.csv` and print each row (skip header).

**Solution**
```python
import csv

with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Columns:", header)
    for row in reader:
        name, city, score = row
        print(f"{name} from {city} — score: {score}")
```

---

## Q3: DictReader — read as dictionaries
Read `students.csv` using `DictReader` and print each student's name and score.

**Solution**
```python
import csv

with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['score']}")
```

---

## Q4: Type conversion — CSV values are strings
Load `students.csv` and compute the average score (scores must be converted to float).

**Solution**
```python
import csv

with open("students.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    scores = [float(row["score"]) for row in reader]

avg = sum(scores) / len(scores)
print(f"Average score: {avg:.2f}")
```

---

## Q5: Filter and save
Read `students.csv` and write only students with score >= 85 to `high_scorers.csv`.

**Solution**
```python
import csv

with open("students.csv", "rt", newline="") as infile, \
     open("high_scorers.csv", "wt", newline="") as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if float(row["score"]) >= 85:
            writer.writerow(row)

print("high_scorers.csv created.")
```

---

## Q6: Append a row
Append a new student record to `students.csv`.

**Solution**
```python
import csv

new_student = ["Amina", "Chittagong", 90.4]

with open("students.csv", "at", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_student)
print("New student added.")
```

---

## Q7: DictWriter — write from dicts
Write a product catalogue CSV from a list of dictionaries.

**Solution**
```python
import csv

products = [
    {"product": "Laptop",     "price_bdt": 85000, "stock": 12},
    {"product": "Headphones", "price_bdt": 3500,  "stock": 45},
    {"product": "Keyboard",   "price_bdt": 1800,  "stock": 30},
]

with open("products.csv", "wt", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["product", "price_bdt", "stock"])
    writer.writeheader()
    writer.writerows(products)
print("products.csv written.")
```

---

## Q8: Custom delimiter
Write a pipe-delimited (`|`) version of `students.csv`.

**Solution**
```python
import csv

with open("students.csv", "rt", newline="") as infile, \
     open("students_pipe.txt", "wt", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter="|")
    for row in reader:
        writer.writerow(row)
print("Pipe-delimited file written.")
```

---

## Q9: Group and aggregate
Read `students.csv` and compute the average score per city.

**Solution**
```python
import csv
from collections import defaultdict

city_scores = defaultdict(list)

with open("students.csv", "rt", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        city_scores[row["city"]].append(float(row["score"]))

for city, scores in sorted(city_scores.items()):
    avg = sum(scores) / len(scores)
    print(f"{city}: {avg:.1f} (n={len(scores)})")
```

---

⬅️ Previous: [07-01: Exercises — File I/O](07-01-file-io-exe.md)
➡️ Next: [07-03: Exercises — JSON Files](07-03-json-files-exe.md)
