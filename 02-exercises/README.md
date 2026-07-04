# ✏️ Exercises

<div align="center" markdown>

![Python: Fundamentals](../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/02_·_Exercises-practice_sets-E6B800?style=for-the-badge&labelColor=1E4B73" alt="Exercises">

[Home](../index.md) &nbsp;|&nbsp; [Notes](../01-notes/README.md) &nbsp;|&nbsp; [Quiz Hub](../03-quiz/) &nbsp;|&nbsp; [Projects](../04-projects/README.md) &nbsp;|&nbsp; [Resources](../05-resources/README.md)

</div>

Small, focused exercises for every topic in `01-notes/` — each file mirrors the matching notes file in number and subject.

Format per question: problem description → **Solution** code block → optional **Alternative** approach.

---

## How to Use

1. Open the exercise file that matches the notes topic being studied.
2. Read the question and attempt a solution independently.
3. Reveal the **Solution** block to compare approaches.
4. Where an **Alternative** is shown, understand why both work.

---

## 02 — Core Language

| File | Questions | Topics |
|------|:---------:|--------|
| [02-01-basic-syntax-exe.md](02-01-basic-syntax-exe.md) | 8 | print, sep/end, comments, indentation, line continuation, quotes, case sensitivity |
| [02-02-variables-and-datatypes-exe.md](02-02-variables-and-datatypes-exe.md) | 8 | assignment, `type()`, multiple assignment, invalid names, dynamic typing, swap |
| [02-03-input-output-exe.md](02-03-input-output-exe.md) | 8 | `input()`, type coercion, `sep`/`end`, multi-input, formatted receipt |
| [02-04-operators-exe.md](02-04-operators-exe.md) | 9 | all arithmetic, floor division, precedence, comparison, logical, bitwise, short-circuit |
| [02-05-number-types-int-float-exe.md](02-05-number-types-int-float-exe.md) | 8 | bases, underscores, float precision, `math` module, scientific notation |
| [02-06-string-basics-exe.md](02-06-string-basics-exe.md) | 10 | literals, indexing, slicing, length, concatenation, escapes, immutability |
| [02-07-string-methods-exe.md](02-07-string-methods-exe.md) | 10 | case, `isdigit`/`isalnum`, search, replace, split/join, strip, alignment, `translate` |
| [02-08-string-formatting-exe.md](02-08-string-formatting-exe.md) | 10 | f-strings, expressions, float/int format spec, fill/align, `format()`, debug `=`, `%` |
| [02-09-boolean-and-none-exe.md](02-09-boolean-and-none-exe.md) | 8 | bool arithmetic, truth table, truthy/falsy, short-circuit, `or`-default, `None` checks |
| [02-10-type-conversion-exe.md](02-10-type-conversion-exe.md) | 8 | implicit widening, `int()` vs `floor()`, safe parse, `bool()`, collection conversions, `ord`/`chr` |

---

## 03 — Control Flow

| File | Questions | Topics |
|------|:---------:|--------|
| [03-01-if-elif-else-exe.md](03-01-if-elif-else-exe.md) | 8 | simple `if`, even/odd, letter grade, nested, ternary, season, FizzBuzz, shipping |
| [03-02-for-loops-exe.md](03-02-for-loops-exe.md) | 10 | `range`, enumerate chars, sum 1–100, pass/fail, break/continue, for/else, zip, nested |
| [03-03-while-loops-exe.md](03-03-while-loops-exe.md) | 8 | basic while, sum threshold, validated input, break/continue, while/else prime, do-while |

---

## 04 — Functions

| File | Questions | Topics |
|------|:---------:|--------|
| [04-01-functions-basics-exe.md](04-01-functions-basics-exe.md) | 10 | `def`, defaults, keyword args, `*args`, `**kwargs`, docstring, scope, lambda, first-class |

---

## 05 — Data Structures

| File | Questions | Topics |
|------|:---------:|--------|
| [05-01-lists-exe.md](05-01-lists-exe.md) | 10 | create, modify, append/insert/pop, sort, slice, count/index, nested, comprehension, copy |
| [05-02-tuples-exe.md](05-02-tuples-exe.md) | 7 | create, immutability, unpacking, swap, function return, dict key, count/index |
| [05-03-sets-exe.md](05-03-sets-exe.md) | 7 | add/remove, union/intersection/difference, subset, unique chars, membership |
| [05-04-dictionaries-exe.md](05-04-dictionaries-exe.md) | 9 | CRUD, `.get()`, iterate, update/merge, comprehension, nested, word frequency, `setdefault` |
| [05-05-slicing-exe.md](05-05-slicing-exe.md) | 7 | basic slice, step slice, reverse, string extract, replace slice, `slice` object, palindrome |
| [05-07-zip-enumerate-and-conversions-exe.md](05-07-zip-enumerate-and-conversions-exe.md) | 7 | `enumerate`, `zip` pair/dict/unequal, conversions, `range` to list/tuple, combined |

---

## 06 — Advanced Patterns

| File | Questions | Topics |
|------|:---------:|--------|
| [06-01-comprehensions-exe.md](06-01-comprehensions-exe.md) | 9 | list, condition, transform, ternary, set, dict, invert dict, nested flatten, vs loop |
| [06-02-exception-handling-exe.md](06-02-exception-handling-exe.md) | 8 | try/except, multiple except, else, finally, raise, custom exception, re-raise, loop validation |

---

## 07 — File I/O

| File | Questions | Topics |
|------|:---------:|--------|
| [07-01-file-io-exe.md](07-01-file-io-exe.md) | 10 | write/read, readline, append, `writelines`, tell/seek, error handling, copy, log, config, word freq |
| [07-02-csv-files-exe.md](07-02-csv-files-exe.md) | 9 | write, reader, DictReader, type conversion, filter+save, append, DictWriter, delimiter, aggregate |
| [07-03-json-files-exe.md](07-03-json-files-exe.md) | 9 | dump/load, dumps/loads, nested, update+save, JSONDecodeError, JSONL, custom encoder, config |
| [07-04-excel-files-exe.md](07-04-excel-files-exe.md) | 7 | openpyxl write/read, list-of-dicts, modify+grade, multiple sheets, Pandas read/write |
| [07-05-pdf-files-exe.md](07-05-pdf-files-exe.md) | 8 | metadata, extract page/all, merge, split, extract pages, rotate, reportlab create |
| [07-06-pathlib-and-filesystem-exe.md](07-06-pathlib-and-filesystem-exe.md) | 10 | Path parts, `/` operator, `with_suffix`, `mkdir`, read/write, glob, metadata, copy/rename, summary |

---

## 08 — Modules & Packages

| File | Questions | Topics |
|------|:---------:|--------|
| [08-01-modules-and-imports-exe.md](08-01-modules-and-imports-exe.md) | 11 | `import`, alias, from-import, `random`, `os.path`, `datetime`, `Counter`, `defaultdict`, `itertools`, custom module |
| [08-02-module-structure-exe.md](08-02-module-structure-exe.md) | 8 | `__name__`, side-effect problem, `if __main__` fix, `main()` pattern, reusable module, `vars()`, package, assert tests |

---
