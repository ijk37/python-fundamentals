# 04-13: Inventory Manager

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_13-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 13">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Manages a shop's stock with add, restock, sell, delete, and low-stock reporting. Sorting by name/qty/price/category. Total stock value calculated automatically. Low-stock items flagged with ⚠️.

**Topics covered:** nested dicts · list comprehensions · `raise ValueError/KeyError` · `try/except` · `sorted(key=lambda)` · `del dict[key]` · accumulation · functions

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

---

## Sample Output

```
  Product                Qty      Price  Category
  ───────────────────────────────────────────────────────
  Bread                   45    ৳  60.00  Bakery
  Chicken                 80    ৳ 280.00  Protein
  Eggs                     6    ৳ 155.00  Protein ⚠️
  Milk                    30    ৳  90.00  Dairy
  Salt                     8    ৳  20.00  Groceries ⚠️
  ...
  8 product(s)   Total stock value: ৳97,810.00
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `raise ValueError` | Input validation in `add_product()`, `sell()` |
| `raise KeyError` | Product-not-found in `restock()`, `sell()` |
| List comprehension + condition | `get_low_stock()` |
| Lambda sort key | `sorted(inventory.items(), key=key_func)` |
| Dict of dicts | `inventory = {name: {qty, price, category}}` |
