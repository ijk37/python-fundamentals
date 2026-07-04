# 04-09: Hangman Game

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_09-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 09">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Classic word-guessing game with ASCII gallows art. Four word categories (animals, countries, fruits, programming). Tracks win/loss record across multiple rounds.

**Topics covered:** `set` · `str.isalpha()` · `random.choice()` · `all()` · `while` loop · `for` loop · list display · input validation · functions

**Difficulty:** ⭐ Beginner

---

## How to Run

```bash
python main.py
```

---

## Sample Session

```
   ------
   |    |
   |    O
   |   /|\
   |
  ---

  Word : p  _  _  h  o  _
  Wrong guesses (3/6):  a  e  i

  Guess a letter: t
  ✅ 't' is in the word!
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `set` | `guessed_letters`, `wrong_guesses` — fast lookup |
| `all(letter in set for letter in word)` | Win check |
| `random.choice(list)` | Word selection |
| List comprehension-style display | `build_display()` |
| ASCII art stages | `HANGMAN_STAGES[len(wrong_guesses)]` |
