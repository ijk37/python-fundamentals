# 04-05: Times Table Generator

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_05-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 05">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Prints multiplication tables in three modes: vertical list, full grid, and interactive quiz. Demonstrates nested loops, range(), and string format alignment.

**Topics covered:** `for` loops · nested loops · `range()` · string format spec (`:>5`, `:<3`) · `random.shuffle()` · input validation · functions

**Difficulty:** ⭐ Beginner

---

## How to Run

```bash
python main.py
```

---

## Sample Output (Grid mode, 3–5 × 1–6)

```
═══════════════════════════════════════════════════════════
  Multiplication Grid  (3–5  ×  1–6)
───────────────────────────────────────────────────────────
            1    2    3    4    5    6
───────────────────────────────────────────────────────────
  3  :      3    6    9   12   15   18
  4  :      4    8   12   16   20   24
  5  :      5   10   15   20   25   30
═══════════════════════════════════════════════════════════
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `for` + `range()` | Building each table row |
| Nested `for` | Grid: outer = row number, inner = multiplier |
| f-string alignment (`:>5`) | Grid column padding |
| `random.shuffle()` | Randomising quiz question order |
| `int()` + `try/except` | Input validation |
