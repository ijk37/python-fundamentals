# 📘 Notes

<div align="center" markdown>

![Python: Fundamentals](../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/01_·_Notes-8_chapters-306998?style=for-the-badge&labelColor=1E4B73" alt="Notes">

[Home](../index.md) &nbsp;|&nbsp; [Exercises](../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../03-quiz/) &nbsp;|&nbsp; [Projects](../04-projects/README.md) &nbsp;|&nbsp; [Resources](../05-resources/README.md)

</div>

Structured Python notes from first setup through modules and packages — 37 lessons across 8 chapters. Each file covers one topic and links to its matching exercise file at the bottom.

---

## 01 — Setup & Environment

| File | Topic |
|------|-------|
| [01-01-what-and-why-python.md](01-01-what-and-why-python.md) | What Python is, why it is widely used, and where it is applied |
| [01-02-IDE.md](01-02-IDE.md) | What an IDE is and how it helps development |
| [01-03-python-platforms-and-ides.md](01-03-python-platforms-and-ides.md) | VS Code, PyCharm, Jupyter, Colab, Replit — comparison and choice |
| [01-04-environment-setup.md](01-04-environment-setup.md) | Installing Python, pip, and creating virtual environments |
| [01-05-write-execute-python-code-in-vscode.md](01-05-write-execute-python-code-in-vscode.md) | Writing and running Python scripts and notebooks in VS Code |

---

## 02 — Core Language

| File | Topic |
|------|-------|
| [02-01-basic-syntax.md](02-01-basic-syntax.md) | `print()`, comments, indentation rules, line continuation, case sensitivity |
| [02-02-variables-and-datatypes.md](02-02-variables-and-datatypes.md) | Variable assignment, naming rules, `type()`, dynamic typing, multiple assignment |
| [02-03-input-output.md](02-03-input-output.md) | `input()`, `print()` with `sep`/`end`, type coercion of input |
| [02-04-operators.md](02-04-operators.md) | Arithmetic, comparison, logical, assignment, membership, identity, bitwise |
| [02-05-number-types-int-float.md](02-05-number-types-int-float.md) | `int`, `float`, bases, underscores, `math` module, precision |
| [02-06-string-basics.md](02-06-string-basics.md) | Literals, indexing, slicing, concatenation, escape chars, immutability |
| [02-07-string-methods.md](02-07-string-methods.md) | `upper/lower`, `strip`, `split/join`, `find/replace`, alignment, `translate` |
| [02-08-string-formatting.md](02-08-string-formatting.md) | f-strings, format spec mini-language, `format()`, `%`, debug `=` |
| [02-09-boolean-and-none.md](02-09-boolean-and-none.md) | `True`/`False`, truthiness, `None`, short-circuit evaluation, `bool()` |
| [02-10-type-conversion.md](02-10-type-conversion.md) | Implicit widening, `int()`, `float()`, `str()`, `bool()`, collection conversions, `ord`/`chr` |

---

## 03 — Control Flow

| File | Topic |
|------|-------|
| [03-01-if-elif-else.md](03-01-if-elif-else.md) | Conditionals, nested `if`, ternary expressions |
| [03-02-for-loops.md](03-02-for-loops.md) | `for`, `range()`, `enumerate()`, `zip()`, `break`/`continue`, `for/else` |
| [03-03-while-loops.md](03-03-while-loops.md) | `while`, `break`/`continue`, `while/else`, do-while pattern |

---

## 04 — Functions

| File | Topic |
|------|-------|
| [04-01-functions-basics.md](04-01-functions-basics.md) | `def`, parameters, return, default args, `*args`, `**kwargs`, docstrings, scope, lambda |

---

## 05 — Data Structures

| File | Topic |
|------|-------|
| [05-01-lists.md](05-01-lists.md) | Creation, indexing, mutation, `append`/`insert`/`pop`, sort, comprehensions, copy |
| [05-02-tuples.md](05-02-tuples.md) | Immutability, unpacking, swap, `namedtuple`, use as dict key |
| [05-03-sets.md](05-03-sets.md) | `add`/`remove`, union, intersection, difference, subset/superset |
| [05-04-dictionaries.md](05-04-dictionaries.md) | CRUD, `.get()`, `.items()`, comprehensions, nesting, `setdefault`, `Counter` |
| [05-05-slicing.md](05-05-slicing.md) | `start:stop:step`, negative indices, `slice()` objects, assignment slicing |
| [05-06-data-structures-comparison.md](05-06-data-structures-comparison.md) | When to use list vs tuple vs set vs dict |
| [05-07-zip-enumerate-and-conversions.md](05-07-zip-enumerate-and-conversions.md) | `zip()`, `enumerate()`, `list()`/`tuple()`/`set()` conversions, `range()` |

---

## 06 — Advanced Patterns

| File | Topic |
|------|-------|
| [06-01-comprehensions.md](06-01-comprehensions.md) | List, set, dict comprehensions; nested comprehensions; ternary in comprehension |
| [06-02-exception-handling.md](06-02-exception-handling.md) | `try/except/else/finally`, `raise`, chaining, custom exception classes |

---

## 07 — File I/O

| File | Topic |
|------|-------|
| [07-01-file-io.md](07-01-file-io.md) | `open()`, modes, `read/readline/readlines`, `write/writelines`, `with`, file position |
| [07-02-csv-files.md](07-02-csv-files.md) | `csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`, delimiters |
| [07-03-json-files.md](07-03-json-files.md) | `json.load/dump`, `json.loads/dumps`, JSONL, custom encoders/decoders |
| [07-04-excel-files.md](07-04-excel-files.md) | `openpyxl` read/write/format, multiple sheets, Pandas `read_excel`/`to_excel` |
| [07-05-pdf-files.md](07-05-pdf-files.md) | `pypdf`: read, merge, split, rotate; `reportlab`: create PDFs |
| [07-06-pathlib-and-filesystem.md](07-06-pathlib-and-filesystem.md) | `Path` objects, `glob`/`rglob`, metadata, copy/move/delete, `pathlib` vs `os.path` |

---

## 08 — Modules & Packages

| File | Topic |
|------|-------|
| [08-01-modules-and-imports.md](08-01-modules-and-imports.md) | `import`, aliases, `from … import`, stdlib: `math`, `random`, `os`, `sys`, `datetime`, `collections`, `itertools` |
| [08-02-module-structure.md](08-02-module-structure.md) | `__name__`, `if __name__ == '__main__'`, `main()` pattern, packages, `__init__.py` |
| [08-03-python-ecosystem-libraries.md](08-03-python-ecosystem-libraries.md) | Overview of major third-party libraries by domain |

---
