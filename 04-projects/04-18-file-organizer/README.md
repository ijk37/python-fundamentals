# 04-18: File Organizer

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_18-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 18">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Scans a directory and moves files into category sub-folders based on extension (Images, Videos, Audio, Documents, Code, etc.). Includes dry-run preview, conflict-safe renaming, and an undo/flatten mode.

**Topics covered:** `pathlib.Path` · `shutil.move()` · `Path.glob()` · `Path.mkdir(exist_ok=True)` · `Path.suffix` · dict mapping · functions · `Path.touch()`

**Difficulty:** ⭐⭐ Intermediate

---

## How to Run

```bash
python main.py
```

Use option 1 to create a demo folder with dummy files.

---

## Extension Categories

| Folder | Extensions |
|--------|-----------|
| Images | `.jpg` `.png` `.gif` `.svg` … |
| Documents | `.pdf` `.docx` `.txt` … |
| Code | `.py` `.html` `.js` `.css` … |
| Archives | `.zip` `.rar` `.tar` `.gz` … |
| Others | anything not matched |

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `Path.glob("*")` | List top-level files |
| `Path.suffix.lower()` | Get file extension |
| `Path.mkdir(exist_ok=True)` | Create folders on demand |
| `shutil.move(src, dst)` | Move files |
| `dict.setdefault(key, []).append()` | Group files by category |
| Conflict handling | Rename loop with `_1`, `_2` suffix |
