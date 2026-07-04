# 04-14: Safe Math Calculator

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_14-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 14">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

A command-line calculator built around custom exception classes. Demonstrates `try/except/else/finally` and the `raise` statement. Handles division by zero, invalid input, negative square roots, and unsupported operations through a clean exception hierarchy.

**Topics covered:** custom exception classes · `raise` · `try/except/else/finally` · exception inheritance · `math.sqrt()` · while-loop menu · functions · calculation history

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

---

## Exception Hierarchy

```
Exception
└── CalculatorError
    ├── DivisionByZeroError
    ├── InvalidInputError
    ├── NegativeSquareRootError
    └── UnsupportedOperationError
```

---

## Sample Session

```
Choose: 4
  First number : 10
  Second number: 0

  ❌ Math Error: Cannot divide 10 by zero.

Choose: 8
  First number : -9

  ❌ Math Error: Cannot take square root of negative number (-9.0).
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| Custom exception class | `DivisionByZeroError(CalculatorError)` |
| `raise ExceptionClass(args)` | Inside `divide()`, `square_root()` etc. |
| `try/except` specific type | `except DivisionByZeroError as e:` |
| `else` clause | Runs only when no exception raised |
| `finally` clause | Always runs — cleanup pattern |
