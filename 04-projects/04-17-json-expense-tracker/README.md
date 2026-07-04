# 04-17: JSON Expense Tracker

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_17-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 17">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Stores daily expenses in a `expenses.json` file. CRUD operations: add (with auto-ID and today's date), delete by ID, filter by category, and monthly summary with a bar chart showing spending breakdown.

**Topics covered:** `json.load()` / `json.dump()` · `pathlib.Path` · `datetime.date.today()` · CRUD with JSON · dict accumulation · list comprehensions · functions

**Difficulty:** ⭐⭐ Intermediate

---

## How to Run

```bash
python main.py
```

An `expenses.json` file is created automatically with sample data.

---

## Sample Monthly Summary

```
  Monthly Summary — June 2025
  ───────────────────────────────────
  Food            ৳  1,480.00  ████████████████████
  Education       ৳    550.00  ████████
  Entertainment   ৳    250.00  ████
  Health          ৳    180.00  ███
  Transport       ৳     60.00  █
  ───────────────────────────────────
  TOTAL           ৳  2,720.00
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `json.load(f)` | Loading expenses from disk |
| `json.dump(data, f, indent=2)` | Pretty-saving to disk |
| `json.JSONDecodeError` | Handling corrupt file |
| `date.today().strftime()` | Auto-date for new entries |
| Dict accumulation | `summary[cat] = summary.get(cat, 0) + amt` |
| `max(e["id"] for e in expenses)` | Auto-increment ID |
