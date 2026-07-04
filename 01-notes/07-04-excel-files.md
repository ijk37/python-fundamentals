# 07-04: Working with Excel Files

Python can read and write Excel files (`.xlsx`, `.xls`) using third-party libraries. The two most common are **openpyxl** (for `.xlsx`) and **Pandas** (uses openpyxl/xlrd under the hood).

```bash
pip install openpyxl    # for .xlsx read/write
pip install xlrd        # for legacy .xls read-only
pip install pandas      # uses both for Excel I/O
```

---

## Reading Excel with openpyxl

```python
import openpyxl

# Open a workbook
wb = openpyxl.load_workbook("students.xlsx")

# List sheet names
print(wb.sheetnames)         # ['Sheet1', 'Sheet2']

# Access a sheet
ws = wb.active               # active/default sheet
ws = wb["Sheet1"]            # by name

# Dimensions
print(ws.max_row)            # number of rows with data
print(ws.max_column)         # number of columns with data
print(ws.dimensions)         # e.g. 'A1:D10'

# Read a single cell
print(ws["A1"].value)        # value of cell A1
print(ws.cell(row=1, column=2).value)  # row/col indexing (1-based!)

# Read all rows
for row in ws.iter_rows(values_only=True):
    print(row)   # tuple of values

# Read with header
rows = list(ws.iter_rows(values_only=True))
header = rows[0]           # ('name', 'age', 'city', 'score')
data   = rows[1:]          # rest of the data

# Read as list of dicts
records = [dict(zip(header, row)) for row in data]
print(records[0])   # {'name': 'Alice', 'age': 30, ...}

# Read a range only
for row in ws.iter_rows(min_row=2, max_row=10, min_col=1, max_col=3, values_only=True):
    print(row)
```

---

## Writing Excel with openpyxl

### Create a new workbook

```python
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Students"

# Write header
header = ["Name", "Age", "City", "Score"]
ws.append(header)

# Write data rows
students = [
    ["Alice",   30, "New York", 88.5],
    ["Bob",     25, "London",   92.0],
    ["Charlie", 35, "Tokyo",    79.3],
]
for row in students:
    ws.append(row)

# Save
wb.save("output.xlsx")
print("Saved!")
```

### Write with formatting

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active

# Bold header with background color
header = ["Name", "Age", "Score"]
ws.append(header)

# Format header row
for col_num, title in enumerate(header, start=1):
    cell = ws.cell(row=1, column=col_num)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(fill_type="solid", fgColor="4472C4")  # blue
    cell.alignment = Alignment(horizontal="center")

# Set column widths
ws.column_dimensions["A"].width = 20
ws.column_dimensions["B"].width = 10
ws.column_dimensions["C"].width = 10

# Add data
data = [["Alice", 30, 88.5], ["Bob", 25, 92.0]]
for row in data:
    ws.append(row)

# Format a specific cell
ws["C2"].font = Font(bold=True, color="FF0000")  # red bold

# Freeze the top row (header stays visible when scrolling)
ws.freeze_panes = "A2"

wb.save("formatted.xlsx")
```

### Multiple sheets

```python
import openpyxl

wb = openpyxl.Workbook()

# First sheet
ws1 = wb.active
ws1.title = "Sales"
ws1.append(["Month", "Revenue"])
ws1.append(["January", 10000])
ws1.append(["February", 12000])

# Second sheet
ws2 = wb.create_sheet(title="Summary")
ws2.append(["Total", "=SUM(Sales!B2:B3)"])   # formula!

wb.save("workbook.xlsx")
```

---

## Excel with Pandas (easiest approach)

```python
import pandas as pd

# Read Excel
df = pd.read_excel("students.xlsx")
print(df.head())
print(df.dtypes)

# Read specific sheet
df = pd.read_excel("students.xlsx", sheet_name="Sheet1")

# Read specific columns
df = pd.read_excel("students.xlsx", usecols=["name", "score"])

# Read multiple sheets — returns a dict of DataFrames
sheets = pd.read_excel("workbook.xlsx", sheet_name=None)  # all sheets
for name, df in sheets.items():
    print(f"Sheet: {name}, Shape: {df.shape}")

# Write to Excel
df.to_excel("output.xlsx", index=False)

# Write multiple sheets
with pd.ExcelWriter("multi.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Students", index=False)
    df2.to_excel(writer, sheet_name="Summary",  index=False)
```

---

## Modifying an Existing Excel File

```python
import openpyxl

# Load existing file (preserves all formatting)
wb = openpyxl.load_workbook("existing.xlsx")
ws = wb.active

# Update a specific cell
ws["B2"] = 35              # change age of first student
ws.cell(row=3, column=4).value = 95.0   # update score

# Add a new row
ws.append(["Diana", 28, "Paris", 95.5])

# Insert a row (shifts existing rows down)
ws.insert_rows(2)          # insert empty row above row 2

# Delete a row
ws.delete_rows(5)          # delete row 5

# Save — must use a different name or overwrite
wb.save("existing.xlsx")
```

---

## Reading Cell Formulas vs. Values

```python
import openpyxl

# By default, reads the cached formula result
wb = openpyxl.load_workbook("data.xlsx")
ws = wb.active
print(ws["D2"].value)   # shows the calculated value

# To read the formula text itself
wb = openpyxl.load_workbook("data.xlsx", data_only=False)
ws = wb.active
print(ws["D2"].value)   # shows the formula like "=SUM(A2:C2)"

# data_only=True — read cached values (default Excel behavior)
wb = openpyxl.load_workbook("data.xlsx", data_only=True)
```

---

## Practical Examples

### Read scores, calculate grade, save back

```python
import openpyxl

wb = openpyxl.load_workbook("students.xlsx")
ws = wb.active

# Read header to find score column
header = [ws.cell(1, c).value for c in range(1, ws.max_column + 1)]
score_col = header.index("score") + 1   # 1-based

# Add a "Grade" column header
grade_col = ws.max_column + 1
ws.cell(1, grade_col).value = "Grade"

# Fill grade for each student
for row in range(2, ws.max_row + 1):
    score = ws.cell(row, score_col).value
    if score is None:
        grade = ""
    elif score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    ws.cell(row, grade_col).value = grade

wb.save("students_graded.xlsx")
```

### Export DataFrame analysis to Excel

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Math": [88, 92, 75, 95],
    "English": [82, 78, 90, 88],
    "Science": [91, 85, 80, 92],
}
df = pd.DataFrame(data)
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1).round(1)
df["Grade"] = df["Average"].apply(lambda x: "A" if x>=90 else "B" if x>=80 else "C")

with pd.ExcelWriter("report.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Scores", index=False)

    # Also write a summary sheet
    summary = pd.DataFrame({
        "Subject": ["Math", "English", "Science"],
        "Class Avg": [df["Math"].mean(), df["English"].mean(), df["Science"].mean()]
    })
    summary.to_excel(writer, sheet_name="Summary", index=False)
```

---

## Quick Summary

| Task | Library | Code |
|------|---------|------|
| Read `.xlsx` | openpyxl | `load_workbook()` + `iter_rows()` |
| Write `.xlsx` | openpyxl | `Workbook()` + `ws.append()` + `wb.save()` |
| Format cells | openpyxl | `Font`, `PatternFill`, `Alignment` |
| Read to DataFrame | pandas | `pd.read_excel("file.xlsx")` |
| Write from DataFrame | pandas | `df.to_excel("file.xlsx", index=False)` |
| Multiple sheets | pandas | `pd.ExcelWriter()` context manager |

---

> **Exercises:** [07-04: Exercises — Excel Files](../02-exercises/07-04-excel-files-exe.md)

---

⬅️ Previous: [07-03: Working with JSON Files](07-03-json-files.md)
➡️ Next: [07-05: Working with PDF Files](07-05-pdf-files.md)
