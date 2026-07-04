# 🧪 03 Quiz

<div align="center" markdown>

![Python: Fundamentals](../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

[![Launch Quiz Hub](https://img.shields.io/badge/▶_Launch_Quiz_Hub-306998?style=for-the-badge&labelColor=1E4B73)](https://ijk37.com/python-fundamentals/03-quiz/)

[Home](../index.md) &nbsp;|&nbsp; [Notes](../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../02-exercises/README.md) &nbsp;|&nbsp; [Projects](../04-projects/README.md)

</div>

Interactive multiple-choice quizzes for all 8 **Python Fundamentals** chapters, plus 5 cumulative mixed quizzes — blue & yellow theme, built with plain HTML + JavaScript, no server required.

**Locally:** open `index.html` in your browser.

---

## 🧪 Chapter Quizzes

Each attempt draws a random subset from the chapter's bank, re-drawn on every retry. Chapter 01 draws **10 of ~33**; chapters 02–08 draw **20 of ~74–76**.

| # | Chapter | Draw / Bank |
|---|---------|-------------|
| 01 | Setup & Environment | 10 / 33 |
| 02 | Core Language | 20 / 76 |
| 03 | Control Flow | 20 / 74 |
| 04 | Functions | 20 / 75 |
| 05 | Data Structures | 20 / 75 |
| 06 | Comprehensions & Exceptions | 20 / 74 |
| 07 | File I/O | 20 / 74 |
| 08 | Modules & Packages | 20 / 74 |

**≈ 555 chapter questions** in total.

## 🧩 Final Mixed Quizzes

Cumulative re-mixes sampled from all 8 chapter pools — each draws **50 of a 100-question bank**. The weighting shifts from the earliest chapters (Mixed 1) toward the later data-structure/file-I/O chapters (Mixed 5).

| Quiz | Focus | Draw / Bank |
|------|-------|-------------|
| Mixed 1 | Heavy on early chapters (01–04) | 50 / 100 |
| Mixed 2 | Moderate lean toward early chapters | 50 / 100 |
| Mixed 3 | Balanced across all chapters | 50 / 100 |
| Mixed 4 | Moderate lean toward later chapters | 50 / 100 |
| Mixed 5 | Comprehensive final (heavy on 05–08) | 50 / 100 |

---

## 🔁 Dynamic attempts

Each attempt draws a **random subset** from the pool, so no two attempts are the same. Retry re-draws a fresh set. Sizing lives in `data.js` (`QUIZ_CONFIG`); you can also override per attempt with a URL parameter:

```
quiz.html?topic=05        → 20 random questions
quiz.html?topic=05&n=10   → 10 random questions
quiz.html?topic=05&n=100  → up to the whole pool
```

> To grow a pool, add more `{ q, options, answer, explain }` objects to the matching `data-NN.js` base file or its `data-NN-b.js` expansion file — the engine keeps drawing the configured number. Chapter files load **before** the mixed quizzes, so mixed draws from the full pools too.

## 🎯 Answer positions

Every question's **options are shuffled on each render**, so the correct answer lands on A/B/C/D randomly — no positional bias even if the source data favored one letter.

## ✨ Features

- Random subset drawn each attempt (and re-drawn on retry)
- Options shuffled every render — no answer-position bias
- **Question navigator sidebar** — numbered grid of answered (green) vs unanswered, current highlighted; click any number to jump
- **Elapsed timer** shown while you work and on the results screen
- **Finish** button to submit at any time (warns about unanswered questions)
- **Skip** and **Back** navigation between questions
- Instant feedback — correct/wrong highlighted after each answer
- Explanation shown after every answer
- Score, grade, percentage, and time at the end
- Full end-of-quiz review of **every** question with your answer, the correct answer, and explanation

## 📁 Files

| File | Purpose |
|------|---------|
| `index.html` | Quiz hub — chapter selector |
| `quiz.html` | Quiz engine |
| `data.js` | TOPICS list, `QUIZ_CONFIG`, `QUESTIONS` object, and Chapter 01 |
| `data-02.js` … `data-08.js` | Base question file per chapter (02–08) |
| `data-01-b.js` … `data-08-b.js` | Expansion pools that `push()` more questions onto each chapter |
| `data-mixed-1.js` | Sampling helpers + Mixed 1 |
| `data-mixed-2.js` … `data-mixed-5.js` | Mixed quizzes 2–5 (built from the chapter pools) |

---

[← Back to Root](../README.md)
