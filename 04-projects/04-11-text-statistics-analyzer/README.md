# 04-11: Text Statistics Analyzer

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_11-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 11">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Accepts typed text or a `.txt` file and produces a full statistics report: character/word/sentence counts, average word length, longest/shortest words, top-10 word frequency (stop words excluded), and top-8 letter frequency — each with a scaled bar chart.

**Topics covered:** `Counter` · `str.split()` · `str.strip(punctuation)` · `str.isalpha()` · comprehensions · `sorted()` / `.most_common()` · functions · f-string alignment

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

---

## Sample Output

```
══════════════════════════════════════════════════
  TEXT STATISTICS REPORT
══════════════════════════════════════════════════
  Total characters  : 512
  Words             : 91
  Sentences         : 6
  Words per sentence: 15.2
  Avg word length   : 5.1 letters
  Longest word      : comprehension

──────────────────────────────────────────────────
  TOP 10 WORDS (stop words excluded)
──────────────────────────────────────────────────
  python             12  ████████████████████
  variable            8  █████████████
  function            6  ██████████
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `collections.Counter` | Word and letter frequency |
| `.most_common(n)` | Top-N words and letters |
| Stop-word filtering | `[w for w in words if w not in STOP_WORDS]` |
| `str.strip(string.punctuation)` | `clean_word()` |
| Scaled bar chart | `int(count / max_count * 20)` |
