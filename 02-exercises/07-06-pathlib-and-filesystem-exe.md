# 07-06: Exercises — pathlib and File System Operations

> **Notes reference:** [07-06: pathlib and File System Operations](../01-notes/07-06-pathlib-and-filesystem.md)

---

## Q1: Path object — parts and properties
Create a `Path` object and explore its `.name`, `.stem`, `.suffix`, `.parent`.

**Solution**
```python
from pathlib import Path

p = Path("reports/2025/annual_report.pdf")

print(p.name)     # annual_report.pdf
print(p.stem)     # annual_report
print(p.suffix)   # .pdf
print(p.parent)   # reports/2025
print(p.parts)    # ('reports', '2025', 'annual_report.pdf')
```

---

## Q2: Build paths with `/`
Build a file path from components using the `/` operator (cross-platform).

**Solution**
```python
from pathlib import Path

base   = Path.home()
docs   = base / "Documents" / "python_notes"
target = docs / "summary.txt"

print(target)          # e.g. C:\Users\jahid\Documents\python_notes\summary.txt
print(target.parent)   # C:\Users\jahid\Documents\python_notes
print(Path.cwd())      # current working directory
```

---

## Q3: Change extension and name
Given `p = Path("data/report.csv")`, create variants with different extensions.

**Solution**
```python
from pathlib import Path

p = Path("data/report.csv")

print(p.with_suffix(".xlsx"))       # data/report.xlsx
print(p.with_suffix(".json"))       # data/report.json
print(p.with_stem("summary"))       # data/summary.csv
print(p.with_name("backup.csv"))    # data/backup.csv
```

---

## Q4: Create directories
Create the nested directory structure `output/2025/june/` (no error if it already exists).

**Solution**
```python
from pathlib import Path

folder = Path("output/2025/june")
folder.mkdir(parents=True, exist_ok=True)
print(f"Created: {folder}")
print(f"Exists: {folder.exists()}")
print(f"Is dir: {folder.is_dir()}")
```

---

## Q5: Write and read with pathlib
Write a text file and read it back using `Path.write_text()` and `Path.read_text()`.

**Solution**
```python
from pathlib import Path

p = Path("output/2025/june/notes.txt")

# Write
p.write_text("Line 1: Dhaka\nLine 2: New York\nLine 3: Berlin\n", encoding="utf-8")

# Read
content = p.read_text(encoding="utf-8")
print(content)

# Check size
print(f"Size: {p.stat().st_size} bytes")
```

---

## Q6: List directory contents — glob
List all `.txt` files in the current directory, then all `.py` files recursively.

**Solution**
```python
from pathlib import Path

folder = Path(".")

# All .txt files in this folder only
txt_files = list(folder.glob("*.txt"))
print("TXT files:", [f.name for f in txt_files])

# All .py files in this folder and all subfolders
py_files = list(folder.rglob("*.py"))
print(f"Found {len(py_files)} .py files")
for f in py_files[:5]:
    print(f"  {f}")
```

---

## Q7: File metadata
Print the size (in KB), modified time, and whether a file exists.

**Solution**
```python
from pathlib import Path
from datetime import datetime

p = Path("output/2025/june/notes.txt")

if p.exists():
    stat = p.stat()
    size_kb  = stat.st_size / 1024
    modified = datetime.fromtimestamp(stat.st_mtime)
    print(f"File:     {p.name}")
    print(f"Size:     {size_kb:.2f} KB")
    print(f"Modified: {modified:%Y-%m-%d %H:%M:%S}")
else:
    print("File does not exist.")
```

---

## Q8: Copy and rename files
Copy `notes.txt` to a backup, then rename the original.

**Solution**
```python
from pathlib import Path
import shutil

src    = Path("output/2025/june/notes.txt")
backup = Path("output/2025/june/notes_backup.txt")

# Copy
shutil.copy2(src, backup)
print(f"Backup created: {backup.name}")

# Rename original
new_path = src.with_stem("notes_v2")
src.rename(new_path)
print(f"Renamed to: {new_path.name}")
```

---

## Q9: Directory summary — count files by extension
Scan the current directory recursively and count files by extension.

**Solution**
```python
from pathlib import Path

def dir_summary(root="."):
    counts = {}
    total_size = 0
    for f in Path(root).rglob("*"):
        if f.is_file():
            ext = f.suffix.lower() or "(no ext)"
            counts[ext] = counts.get(ext, 0) + 1
            total_size += f.stat().st_size
    print(f"Total size: {total_size / 1_048_576:.2f} MB")
    for ext, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {ext:12s}: {n} files")

dir_summary(".")
```

---

## Q10: pathlib vs os.path — side-by-side comparison
Perform the same operations with `os.path` and `pathlib` to see the difference.

**Solution**
```python
import os
import os.path
from pathlib import Path

path = "data/report.csv"

# --- os.path style ---
print(os.path.basename(path))          # report.csv
print(os.path.dirname(path))           # data
print(os.path.splitext(path)[1])       # .csv
print(os.path.exists(path))            # True/False
print(os.path.join("data", "out.csv")) # data/out.csv  (or data\out.csv on Windows)

# --- pathlib style ---
p = Path(path)
print(p.name)                          # report.csv
print(p.parent)                        # data
print(p.suffix)                        # .csv
print(p.exists())                      # True/False
print(p.parent / "out.csv")            # data/out.csv
```

---

⬅️ Previous: [07-05: Exercises — PDF Files](07-05-pdf-files-exe.md)
➡️ Next: [08-01: Exercises — Modules and Imports](08-01-modules-and-imports-exe.md)
