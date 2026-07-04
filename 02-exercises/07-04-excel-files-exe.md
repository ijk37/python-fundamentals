# 07-04: Exercises — Excel Files

> **Notes reference:** [07-04: Working with Excel Files](../01-notes/07-04-excel-files.md)

---

## Q1: Create an Excel file with openpyxl
Write a student score sheet to `scores.xlsx`.

**Solution**
```python
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Scores"

header = ["Name", "City", "Math", "English", "Science"]
ws.append(header)

students = [
    ["Rahim",  "Dhaka",    88, 82, 91],
    ["Sara",   "New York", 92, 78, 85],
    ["James",  "Berlin",   75, 90, 80],
    ["Nadia",  "Tokyo",    95, 88, 92],
]
for row in students:
    ws.append(row)

wb.save("scores.xlsx")
print("scores.xlsx created.")
```

---

## Q2: Read an Excel file
Open `scores.xlsx` and print every row (skip header).

**Solution**
```python
import openpyxl

wb = openpyxl.load_workbook("scores.xlsx")
ws = wb.active

rows = list(ws.iter_rows(values_only=True))
header = rows[0]
print("Columns:", header)

for row in rows[1:]:
    print(row)
```

---

## Q3: Read as list of dicts
Load `scores.xlsx` and convert rows to dictionaries keyed by header.

**Solution**
```python
import openpyxl

wb = openpyxl.load_workbook("scores.xlsx")
ws = wb.active

rows    = list(ws.iter_rows(values_only=True))
header  = rows[0]
records = [dict(zip(header, row)) for row in rows[1:]]

for rec in records:
    avg = (rec["Math"] + rec["English"] + rec["Science"]) / 3
    print(f"{rec['Name']}: avg = {avg:.1f}")
```

---

## Q4: Modify an existing file — add a Grade column
Load `scores.xlsx`, compute the average, assign a grade, and save back.

**Solution**
```python
import openpyxl

wb = openpyxl.load_workbook("scores.xlsx")
ws = wb.active

# Add header for new column
ws.cell(1, 6).value = "Average"
ws.cell(1, 7).value = "Grade"

for row_idx in range(2, ws.max_row + 1):
    math    = ws.cell(row_idx, 3).value
    english = ws.cell(row_idx, 4).value
    science = ws.cell(row_idx, 5).value
    avg     = (math + english + science) / 3
    grade   = "A" if avg >= 90 else "B" if avg >= 80 else "C"
    ws.cell(row_idx, 6).value = round(avg, 1)
    ws.cell(row_idx, 7).value = grade

wb.save("scores.xlsx")
print("Grades added.")
```

---

## Q5: Multiple sheets
Create a workbook with two sheets: `Scores` and `Summary`.

**Solution**
```python
import openpyxl

wb = openpyxl.Workbook()

ws1 = wb.active
ws1.title = "Scores"
ws1.append(["Name", "Score"])
ws1.append(["Rahim", 88])
ws1.append(["Sara",  92])
ws1.append(["James", 75])

ws2 = wb.create_sheet(title="Summary")
ws2.append(["Metric", "Value"])
ws2.append(["Count",  3])
ws2.append(["Max",    "=MAX(Scores!B2:B4)"])
ws2.append(["Average","=AVERAGE(Scores!B2:B4)"])

wb.save("report.xlsx")
print("report.xlsx with two sheets created.")
```

---

## Q6: Pandas — read and analyse
Read `scores.xlsx` with Pandas and compute the class average per subject.

**Solution**
```python
import pandas as pd

df = pd.read_excel("scores.xlsx")
print(df.head())

for subject in ["Math", "English", "Science"]:
    print(f"{subject} average: {df[subject].mean():.1f}")
```

---

## Q7: Pandas — write to Excel
Create a DataFrame and export it to `summary.xlsx`.

**Solution**
```python
import pandas as pd

data = {
    "City":     ["Dhaka", "New York", "Berlin", "Tokyo"],
    "Students": [120, 95, 80, 110],
    "Avg Score":[84.5, 88.2, 79.1, 91.3],
}
df = pd.DataFrame(data)
df["Grade"] = df["Avg Score"].apply(lambda x: "A" if x >= 88 else "B" if x >= 80 else "C")

df.to_excel("summary.xlsx", index=False)
print("summary.xlsx written.")
```

---

⬅️ Previous: [07-03: Exercises — JSON Files](07-03-json-files-exe.md)
➡️ Next: [07-05: Exercises — PDF Files](07-05-pdf-files-exe.md)
