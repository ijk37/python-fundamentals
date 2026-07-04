# 04-23: Full Expense Tracker

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_23-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 23">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

A comprehensive CRUD expense tracker that ties together the whole course: JSON persistence, CSV export, datetime filtering, pathlib, exception handling, and clean function design. Includes per-category budget tracking with over/warning/OK status.

**Topics covered:** `json.load/dump` · `csv.DictWriter` · `datetime` · `pathlib.Path` · CRUD with JSON · budget comparison · monthly filtering · `try/except` · functions

**Difficulty:** ⭐⭐⭐ Intermediate–Advanced

---

## How to Run

```bash
python main.py
```

Data stored in `expense_tracker.json`. Exports to `expenses_export.csv`.

---

## Sample Budget Report

```
  Budget Report — June 2025
  Category          Spent     Budget     %  Status
  ──────────────────────────────────────────────────────
  Food            ৳  2,120   ৳  5,000   42%  ✅ OK
  Transport       ৳     60   ৳  2,000    3%  ✅ OK
  Education       ৳    550   ৳  3,000   18%  ✅ OK
  Entertainment   ৳    250   ৳  2,000   13%  ✅ OK
  ──────────────────────────────────────────────────────
  TOTAL           ৳  3,960   ৳ 28,000   14%
```

---

## Skills Demonstrated

| Skill | Where |
|-------|-------|
| JSON persistence | `load_store()` / `save_store()` |
| CSV export | `export_csv()` using `DictWriter` |
| `datetime` formatting | Date input and monthly filter |
| `pathlib.Path` | `DATA_FILE.exists()`, `.resolve()` |
| Exception handling | All numeric `input()` calls |
| Budget comparison | `budget_report()` with `%` and status |
| CRUD pattern | `add/delete/update_expense()` |
