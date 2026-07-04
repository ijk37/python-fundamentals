# 04-01: Mad Libs Story Generator

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_01-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 01">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

A classic word-substitution game. The player supplies nouns, verbs, adjectives, and other word types without seeing the story — then reads the (often hilarious) result.

**Topics covered:** `input()` · f-strings · string methods (`.strip()`, `.title()`, `.isalpha()`) · functions · dictionaries · while-loop input validation

**Difficulty:** ⭐ Beginner

---

## Two Versions

This folder contains two versions of the project:

1. **`main.py`** — the AI-written code.
2. **`project01.ipynb`** — the practiced, human-made version (it's a `.ipynb` file because it was practiced in Jupyter Notebook).

The two are similar in structure and behaviour. The explanation below is for **`main.py`** only.

---

## How to Run

```bash
python main.py
```

No external libraries required — pure Python 3.

---

## Sample Session

```
============================================================
       Welcome to the Mad Libs Story Generator!
============================================================

Available stories:
  1. Adventure
  2. Cooking Show

Choose a story number: 1

------------------------------------------------------------
  Story: Adventure
  Fill in each blank — no peeking at the story!
------------------------------------------------------------

  Enter an adjective (e.g. brave): tiny
  Enter an animal: elephant
  Enter a person's name: Rahim
  ...

============================================================
                  YOUR MAD LIBS STORY
============================================================

Once upon a time, a Tiny Elephant named Rahim
lived in the city of Dhaka ...
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `input()` + `.strip()` | Collecting user words |
| `.isalpha()` / `.isdigit()` | Input validation |
| `.title()` | Capitalising words |
| f-strings | Assembling the story |
| Dictionary | Storing collected words |
| Functions with parameters | `get_word()`, `story_adventure()` |
| `while True` + `break` | Retry loop for invalid input |
