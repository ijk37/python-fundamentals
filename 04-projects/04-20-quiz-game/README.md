# 04-20: Quiz Game (JSON-backed)

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_20-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 20">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Loads 12 multiple-choice Python questions from a JSON file. Supports full quiz, category quiz, 5-question quick quiz, timed mode, and persistent high scores (also in JSON). Each question shows an explanation after answering.

**Topics covered:** `json.load()` / `json.dump()` · `random.shuffle()` / `random.sample()` · `time.time()` · `pathlib.Path` · dicts · list filtering · functions

**Difficulty:** ⭐⭐ Intermediate

---

## How to Run

```bash
python main.py
```

`questions.json` and `high_scores.json` are created automatically.

---

## Sample Question

```
  Question 3/12 — Python Basics
  Which of these creates an empty list?

    A. list = {}
    B. list = ()
    C. list = []
    D. list = <>

  Your answer (A/B/C/D): C
  ✅ Correct!
  💡 Square brackets [] create a list. {} is a dict/set, () is a tuple.
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `json.load()` / `json.dump()` | Load questions and save scores |
| `random.shuffle(questions)` | Random question order each game |
| `random.sample(qs, 5)` | Quick quiz selection |
| `time.time()` | Per-question timer |
| High score logic | `update_high_score()` — only saves if better |
