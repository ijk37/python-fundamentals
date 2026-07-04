# 04-15: Personal Diary App

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_15-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 15">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Saves diary entries to a `diary.txt` file on disk. Each entry is timestamped and stored with a structured header. Supports listing, reading by number, and keyword searching — all backed by real file I/O.

**Topics covered:** `open()` in append/read mode · `pathlib.Path` · `datetime.now().strftime()` · text file parsing · `str.splitlines()` · `str.split(separator)` · functions · while-loop menu

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

A `diary.txt` file is created in the same directory automatically.

---

## File Format

```
============================================================
DATE: 2025-06-09 14:35
TITLE: My First Entry
----
Today I started learning Python file I/O.
It was really interesting!
============================================================
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `open(file, "a")` | Appending new entries |
| `open(file, "r")` | Reading all entries |
| `pathlib.Path.exists()` | Check file before reading |
| `content.split(SEPARATOR)` | Splitting entries |
| `datetime.now().strftime()` | Timestamp generation |
| `str.splitlines()` | Parsing entry header lines |
