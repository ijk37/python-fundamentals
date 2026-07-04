# 04-02: BMI Calculator & Health Advisor

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_02-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 02">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Calculates BMI from weight and height (metric or imperial), shows the WHO health category, and prints a personalised advice message alongside the healthy weight range for the user's height.

**Topics covered:** arithmetic operators · `if/elif/else` · `float()` type conversion · `try/except` input validation · functions · f-strings · named constants

**Difficulty:** ⭐ Beginner

---

## Two Versions

This folder contains two versions of the project:

1. **`main.py`** — the AI-written code.
2. **`project02.ipynb`** — the practiced, human-made version (it's a `.ipynb` file because it was practiced in Jupyter Notebook).

The two are similar in structure and behaviour. The explanation below is for **`main.py`** only.

---

## How to Run

```bash
python main.py
```

No external libraries — pure Python 3.

---

## Sample Output

```
═══════════════════════════════════════════════════════
       BMI Calculator & Health Advisor
═══════════════════════════════════════════════════════

Your name: Jahid
Unit system: metric / imperial: metric
Weight (kg): 72
Height (m): 1.75

═══════════════════════════════════════════════════════
  BMI Report for Jahid
═══════════════════════════════════════════════════════
  Weight   : 72.0 kg  (158.7 lbs)
  Height   : 1.75 m  (175 cm)
  BMI      : 23.5
  Category : Normal weight
─────────────────────────────────────────────────────
  Advice   : Great work! Maintain your current lifestyle ...
─────────────────────────────────────────────────────
  Healthy weight range for your height:
    56.7 kg – 76.6 kg
═══════════════════════════════════════════════════════
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| Arithmetic operators (`/`, `**`) | BMI formula |
| `float()` + `try/except` | Input validation |
| `if/elif/else` | BMI category |
| Named constants | `BMI_UNDERWEIGHT`, `BMI_NORMAL_HIGH` |
| Functions with return values | `calculate_bmi()`, `bmi_category()` |
| Unit conversion | Imperial → metric |
| f-strings with format spec | Results display |
