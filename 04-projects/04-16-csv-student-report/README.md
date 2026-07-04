# 04-16: CSV Student Report

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_16-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 16">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Reads student scores from `students.csv`, calculates averages and letter grades, and generates a formatted report. Supports filtering by pass/fail or grade, sorting, and saving the summary to a new CSV file.

**Topics covered:** `csv.DictReader` · `csv.DictWriter` · `csv.writer` · type conversion · filtering with comprehensions · `sorted(key=lambda)` · `pathlib.Path` · functions

**Difficulty:** ⭐⭐ Intermediate

---

## How to Run

```bash
python main.py
```

A sample `students.csv` is auto-created if it doesn't exist.

---

## Sample Output

```
  Name            Avg   Grade   GPA  Status
  ────────────────────────────────────────────────
  Riya             95.2  A+     4.0  ✅ PASS
  Nasrin           91.8  A+     4.0  ✅ PASS
  Rahim            83.2  A-     3.7  ✅ PASS
  Karim            56.0  C      2.0  ✅ PASS
  Salma            43.0  F      0.0  ❌ FAIL
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `csv.DictReader` | Reading rows as dicts |
| `csv.DictWriter` | Writing structured output |
| `float(row["Math"])` | Type conversion from string |
| Comprehension + condition | `filter_by_grade()`, `filter_passing()` |
| `sorted(key=lambda s: s["average"])` | Flexible sorting |
