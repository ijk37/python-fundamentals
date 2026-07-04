# 04-08: Shopping Cart System

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_08-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 08">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

A CLI supermarket cart. Browse a product catalogue, add/remove items by ID, apply percentage-off discount codes, and print a formatted receipt with VAT.

**Topics covered:** lists of dicts · dict lookup · functions · `for` loop · accumulation · f-string alignment · type conversion · while-loop menu

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

---

## Sample Receipt

```
══════════════════════════════════════════════════
              RECEIPT
══════════════════════════════════════════════════
  Rice (5 kg)                         ৳   700
  Eggs (dozen)                        ৳   155
  Milk (1 L)                          ৳    90
──────────────────────────────────────────────────
  Subtotal                            ৳   945
  Discount (WELCOME10) -10%           -৳  94.5
  VAT (5%)                            ৳   42.5
──────────────────────────────────────────────────
  TOTAL                               ৳   893.0
══════════════════════════════════════════════════
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| List of dicts | `CATALOGUE`, `cart` |
| Dict lookup | `DISCOUNT_CODES[code]` |
| Searching a list | `find_product()` |
| `list.pop(i)` | `remove_from_cart()` |
| Accumulation | `cart_total()` |
| Formatted receipt | `print_receipt()` |
