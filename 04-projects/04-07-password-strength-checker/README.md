# 04-07: Password Strength Checker & Generator

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_07-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 07">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Analyses a password against 8 weighted criteria (length, character classes, repeats, common patterns) and produces a strength score from Weak to Excellent. Also generates cryptographically secure passwords using `secrets`.

**Topics covered:** `string` module · `any()` · lambda functions · list comprehensions · `secrets` module · f-strings · tuples · functions

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

No external libraries — pure Python 3.

---

## Sample Output

```
====================================================
    Password Strength Checker & Generator
====================================================

Options:
  1. Check a password
  2. Generate a strong password
  3. Quit

Choose: 1
Enter the password to check: MyP@ssw0rd!

════════════════════════════════════════════════════
  Password  : My*******!  (length: 11)
  Strength  : Good      🟡
  Score     : 7 / 10
────────────────────────────────────────────────────
  ✅  At least 8 characters  (+1)
  ✅  Contains lowercase letter  (+1)
  ✅  Contains uppercase letter  (+1)
  ✅  Contains a digit  (+1)
  ✅  Contains a special character  (+2)
  ✅  No repeated characters (3×+)  (+1)
  ❌  At least 12 characters
  ❌  No common patterns
════════════════════════════════════════════════════
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `any(c.isupper() for c in p)` | Character-class checks |
| Lambda in data structure | `CRITERIA` list of tuples |
| `secrets` module | Secure password generation |
| Fisher-Yates shuffle | Character ordering randomisation |
| `string.ascii_letters` etc. | Character pool construction |
