# 04-04: Number Guessing Game

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_04-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 04">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

The computer picks a secret number; the player has limited attempts to guess it. Includes three difficulty levels, a hot/cold hint system, a points formula, and a session-high-score tracker.

**Topics covered:** `random.randint()` · `while` loop · `if/elif/else` · `int()` conversion · `try/except` · `break` · functions · dictionaries · f-strings

**Difficulty:** ⭐ Beginner

---

## How to Run

```bash
python main.py
```

No external libraries — pure Python 3.

---

## Sample Output

```
==================================================
        Number Guessing Game
==================================================

Difficulty levels:
  easy     — guess a number from 1 to 50  (10 attempts)
  medium   — guess a number from 1 to 100  (7 attempts)
  hard     — guess a number from 1 to 200  (5 attempts)

Choose difficulty: medium

  A number between 1 and 100 has been chosen.
  You have 7 attempts. Good luck!

  Attempts remaining: 7
Your guess (1–100): 50
  Cold 🧊 — go higher.

  Attempts remaining: 6
Your guess (1–100): 75
  Hot 🌡️ — go lower.

  Attempts remaining: 5
Your guess (1–100): 68

  ✅ Correct! The number was 68.
  You guessed it in 3 attempt(s). Score: 1000
  🏆 New high score for medium!
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `random.randint()` | Picking the secret number |
| `while` + `break` | Guessing loop |
| `int()` + `try/except` | Input validation |
| `if/elif/else` | Hint logic and outcome |
| Functions returning values | `hint()`, `calculate_score()` |
| Dictionary | Difficulty settings, high scores |
