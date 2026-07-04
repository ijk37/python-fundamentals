# 04-03: Multi-Currency Converter

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_03-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 03">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Converts amounts between BDT, USD, EUR, GBP, JPY, and INR using a "BDT as base" dictionary approach. Supports a live rate table and formatted output with correct decimal places per currency.

**Topics covered:** dictionaries · arithmetic · functions · f-string format spec · `while` loop · input validation · `float()` type conversion

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
═══════════════════════════════════════════════════════
         Multi-Currency Converter
═══════════════════════════════════════════════════════

Options:
  1. Convert an amount
  2. Show rate table
  3. Quit

Choose (1 / 2 / 3): 1

Amount to convert: 1000
  Available currencies: BDT, USD, EUR, GBP, JPY, INR
From currency: USD
To currency  : BDT

──────────────────────────────────────────────────────
  $1,000.00 USD
  =  ৳110,000.00 BDT
──────────────────────────────────────────────────────
  Rate: 1 USD = ৳110.00 BDT
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| Dictionary lookup | `RATES_TO_BDT[code]` |
| Two-step conversion via base currency | `convert()` |
| f-string format spec (`,.2f`) | `format_amount()` |
| `while True` menu loop | Main loop |
| `float()` + `.replace(",","")` | Accepting comma-formatted numbers |
| Named constants | `RATES_TO_BDT`, `SYMBOLS`, `DECIMALS` |
