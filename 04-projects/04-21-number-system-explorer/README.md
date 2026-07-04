# 04-21: Number System Explorer

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_21-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 21">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Converts numbers between decimal, binary, octal, and hexadecimal using built-ins (`bin()`, `oct()`, `hex()`, `int(x, base)`) and a manual algorithm. Also demonstrates bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) and the `math` module.

**Topics covered:** `bin()` · `oct()` · `hex()` · `int(string, base)` · bitwise operators · `math.sqrt/log2/gcd/lcm/factorial` · manual base-conversion algorithm

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

---

## Sample: Conversion Table (0–5)

```
  Dec  Binary        Octal     Hex
  ──────────────────────────────────
    0  0             0         0
    1  1             1         1
    2  10            2         2
    3  11            3         3
    4  100           4         4
    5  101           5         5
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `bin(n)[2:]` | Strip "0b" prefix |
| `int("1010", 2)` | Binary string → decimal |
| `n % 2` / `n // 2` | Manual binary algorithm |
| `a & b`, `a \| b`, `a ^ b` | Bitwise AND/OR/XOR |
| `a << 1` | Left shift (×2) |
| `math.gcd(a, b)` | Greatest common divisor |
