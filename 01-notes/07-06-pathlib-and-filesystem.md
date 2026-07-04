# 07-06: pathlib and File System Operations

`pathlib` (Python 3.4+) provides an object-oriented, cross-platform way to work with file paths and the file system. It is modern Python's preferred replacement for string-based `os.path` operations.

---

## The Path Object

```python
from pathlib import Path

# Create a Path object — just a smart string for now
p = Path("folder/subfolder/file.txt")

# Parts
print(p.name)        # 'file.txt'      — filename with extension
print(p.stem)        # 'file'          — filename without extension
print(p.suffix)      # '.txt'          — extension
print(p.suffixes)    # ['.txt']
print(p.parent)      # folder/subfolder
print(p.parents[0])  # folder/subfolder
print(p.parents[1])  # folder
print(p.parts)       # ('folder', 'subfolder', 'file.txt')

# Absolute path
print(Path.cwd())             # current working directory
print(Path.home())            # user's home directory  e.g. C:\Users\alice
p_abs = Path("file.txt").resolve()  # absolute path
print(p_abs)
```

---

## Building Paths

```python
from pathlib import Path

# Join with / operator (works on all OS!)
base = Path("C:/Users/alice")
full = base / "Documents" / "report.txt"
print(full)   # C:\Users\alice\Documents\report.txt

# Equivalent to os.path.join
import os
old_way = os.path.join("C:\\Users\\alice", "Documents", "report.txt")

# Change extension
p = Path("image.png")
print(p.with_suffix(".jpg"))    # image.jpg
print(p.with_stem("thumbnail")) # thumbnail.png
print(p.with_name("new.txt"))   # new.txt
```

---

## Checking Existence and Type

```python
from pathlib import Path

p = Path("myfile.txt")

print(p.exists())     # True/False — path exists at all
print(p.is_file())    # True if it's a file (not a directory)
print(p.is_dir())     # True if it's a directory
print(p.is_symlink()) # True if it's a symbolic link
print(p.is_absolute())# True if absolute path

# Safe access pattern
if p.exists():
    print(p.read_text())
else:
    print("File not found")
```

---

## Reading and Writing Files with pathlib

```python
from pathlib import Path

p = Path("notes.txt")

# Write (overwrites!)
p.write_text("Hello, World!\nSecond line", encoding="utf-8")

# Read entire file
content = p.read_text(encoding="utf-8")
print(content)

# Read binary
data = p.read_bytes()

# Write binary
p.write_bytes(b"\x89PNG\r\n")

# Append — pathlib doesn't have append directly; use open()
with p.open("at", encoding="utf-8") as f:
    f.write("\nThird line")
```

---

## Creating Directories

```python
from pathlib import Path

# Create a single directory
Path("new_folder").mkdir()

# Create nested directories
Path("a/b/c/d").mkdir(parents=True, exist_ok=True)
# parents=True  → create all missing parent dirs
# exist_ok=True → don't raise error if dir already exists

# Create from Path
base = Path.home() / "projects" / "myapp"
base.mkdir(parents=True, exist_ok=True)
(base / "data").mkdir(exist_ok=True)
(base / "output").mkdir(exist_ok=True)
```

---

## Listing Directory Contents

```python
from pathlib import Path

folder = Path(".")

# List all items in a directory
for item in folder.iterdir():
    print(item.name, "DIR" if item.is_dir() else "FILE")

# List only files
files = [p for p in folder.iterdir() if p.is_file()]

# List only directories
dirs = [p for p in folder.iterdir() if p.is_dir()]

# glob — match files by pattern
for f in folder.glob("*.txt"):
    print(f)

for f in folder.glob("*.py"):
    print(f)

# rglob — recursive glob (all subdirectories)
for f in folder.rglob("*.py"):
    print(f)   # finds all .py files everywhere under folder

# Find all .csv files under a project
project = Path("my_project")
csvs = list(project.rglob("*.csv"))
print(f"Found {len(csvs)} CSV files")
```

---

## File Metadata

```python
from pathlib import Path
from datetime import datetime

p = Path("document.pdf")

stat = p.stat()
print(f"Size:     {stat.st_size:,} bytes")
print(f"Size:     {stat.st_size / 1024:.1f} KB")
print(f"Modified: {datetime.fromtimestamp(stat.st_mtime)}")
print(f"Created:  {datetime.fromtimestamp(stat.st_ctime)}")
print(f"Accessed: {datetime.fromtimestamp(stat.st_atime)}")
```

---

## Copying, Moving, and Deleting

```python
from pathlib import Path
import shutil

src  = Path("source.txt")
dest = Path("destination.txt")

# Copy a file
shutil.copy2(src, dest)        # copy2 preserves metadata
shutil.copy(src, dest)         # copy without metadata

# Copy entire directory tree
shutil.copytree("source_dir", "backup_dir")

# Move / rename
src.rename(Path("renamed.txt"))       # rename in same directory
src.replace(Path("other/file.txt"))   # move (and overwrite if exists)

# Using shutil.move (more robust)
shutil.move("old_name.txt", "new_name.txt")
shutil.move("file.txt", "subdir/")    # move into subdir

# Delete a file
p = Path("to_delete.txt")
p.unlink()                         # delete file
p.unlink(missing_ok=True)          # don't error if already gone (3.8+)

# Delete empty directory
Path("empty_dir").rmdir()

# Delete directory and all contents (careful!)
shutil.rmtree("directory_to_delete")

# Safe delete pattern
if p.exists():
    p.unlink()
```

---

## Practical Patterns

### Find the largest files

```python
from pathlib import Path

folder = Path(".")
files = [(p, p.stat().st_size) for p in folder.rglob("*") if p.is_file()]
files.sort(key=lambda x: x[1], reverse=True)

print("Top 5 largest files:")
for path, size in files[:5]:
    print(f"  {size/1024:8.1f} KB  {path}")
```

### Organize files by extension

```python
from pathlib import Path
import shutil

source = Path("Downloads")
dest   = Path("Sorted")

for file in source.iterdir():
    if file.is_file():
        ext_folder = dest / file.suffix.lstrip(".").upper()
        ext_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, ext_folder / file.name)
        print(f"  {file.name} → {ext_folder.name}/")
```

### Batch rename files

```python
from pathlib import Path

folder = Path("photos")
for i, file in enumerate(sorted(folder.glob("*.jpg")), start=1):
    new_name = folder / f"photo_{i:04d}.jpg"
    file.rename(new_name)
    print(f"  {file.name} → {new_name.name}")
```

### Count files and total size

```python
from pathlib import Path

def directory_summary(path):
    p = Path(path)
    total_size = 0
    counts = {}
    for f in p.rglob("*"):
        if f.is_file():
            ext = f.suffix.lower() or "(no ext)"
            counts[ext] = counts.get(ext, 0) + 1
            total_size += f.stat().st_size
    print(f"Total size: {total_size / 1_048_576:.1f} MB")
    for ext, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {ext:10s}: {n} files")

directory_summary(".")
```

---

## pathlib vs os.path

| Task | `os.path` (old) | `pathlib` (modern) |
|------|-----------------|--------------------|
| Join paths | `os.path.join(a, b)` | `Path(a) / b` |
| File name | `os.path.basename(p)` | `p.name` |
| Directory | `os.path.dirname(p)` | `p.parent` |
| Extension | `os.path.splitext(p)[1]` | `p.suffix` |
| Exists | `os.path.exists(p)` | `p.exists()` |
| Is file | `os.path.isfile(p)` | `p.is_file()` |
| Absolute | `os.path.abspath(p)` | `p.resolve()` |
| Home dir | `os.path.expanduser("~")` | `Path.home()` |
| Current dir | `os.getcwd()` | `Path.cwd()` |
| Read text | manual `open()` | `p.read_text()` |
| Write text | manual `open()` | `p.write_text()` |
| List dir | `os.listdir()` | `p.iterdir()` |
| Recursive glob | `os.walk()` | `p.rglob("*")` |
| File size | `os.path.getsize(p)` | `p.stat().st_size` |

**Use `pathlib` for new code.** It's more readable, cross-platform, and object-oriented.

---

> **Exercises:** [07-06: Exercises — pathlib and File System Operations](../02-exercises/07-06-pathlib-and-filesystem-exe.md)

---

⬅️ Previous: [07-05: Working with PDF Files](07-05-pdf-files.md)
➡️ Next: [08-01: Modules and Imports](08-01-modules-and-imports.md)
