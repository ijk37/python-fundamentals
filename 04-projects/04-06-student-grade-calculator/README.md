# 04-06: Student Grade Calculator

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_06-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 06">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Accepts subject scores for multiple students, computes averages, assigns letter grades and GPA, flags failing subjects, and prints formatted report cards plus a class-wide summary.

**Topics covered:** lists · tuples · dicts · `for` loop · `if/elif` · accumulation pattern · `zip()` · `sum()` · `sorted()` · f-string alignment · functions

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

---

## Sample Output

```
════════════════════════════════════════════════════
  REPORT CARD — RAHIM
────────────────────────────────────────────────────
  Subject               Score  Grade   GPA
────────────────────────────────────────────────────
  Mathematics            88.0     A+   4.0
  English                75.0     B+   3.3
  Science                92.0     A+   4.0
────────────────────────────────────────────────────
  AVERAGE                85.0      A   4.0  PASS ✅
════════════════════════════════════════════════════
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| List of tuples (grading scale) | `GRADE_SCALE` |
| `zip()` | Pairing subjects with scores |
| Dictionary | Student record |
| `sorted(..., key=..., reverse=True)` | Class ranking |
| f-string alignment (`:<20`, `:>6.1f`) | Report card columns |
| Accumulation pattern | `average()` |
