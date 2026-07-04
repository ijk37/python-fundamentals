# 04-19: Math Utilities Package

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_19-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 19">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Builds a real Python package (`mathutils/`) with four sub-modules: `basic`, `statistics`, `sequences`, and `geometry`. `__init__.py` re-exports key functions so they're accessible directly. An interactive `main.py` demonstrates every function.

**Topics covered:** `__init__.py` · package imports · `from package.module import fn` · `__version__` · `__name__ == "__main__"` guard · modular code organisation

**Difficulty:** ⭐⭐ Intermediate

---

## Package Structure

```
04-19-math-utilities-package/
├── main.py
└── mathutils/
    ├── __init__.py      ← re-exports all public functions
    ├── basic.py         ← add, subtract, multiply, safe_divide, power, absolute
    ├── statistics.py    ← mean, median, mode, variance, std_dev
    ├── sequences.py     ← factorial, fibonacci, is_prime, prime_factors
    └── geometry.py      ← circle_area, rectangle_area, triangle_area, hypotenuse
```

## How to Run

```bash
python main.py
```

To test a sub-module directly:

```bash
python -m mathutils.sequences
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `__init__.py` | Makes `mathutils/` a package |
| `from mathutils import mean` | Direct access via `__init__` |
| `from mathutils.sequences import fibonacci` | Sub-module import |
| `__version__` | Package metadata |
| `if __name__ == "__main__":` | Each module has its own self-test |
