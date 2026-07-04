# 04-10: Caesar Cipher

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_10-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 10">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Encrypts and decrypts messages using the Caesar cipher (letter-shifting). Also includes a brute-force mode that prints all 25 possible decryptions when the shift is unknown.

**Topics covered:** `ord()` / `chr()` · modular arithmetic · `str.isalpha()` · `str.islower()` · functions · `for` loop · while-loop menu

**Difficulty:** ⭐ Beginner

---

## How to Run

```bash
python main.py
```

---

## Sample Output

```
Encrypted (shift 3):
  Khoor, Zruog!

Brute-force (shift 3 found at row 3):
  Shift    Decrypted text
  1        Jgnnq, Yqtnf!
  2        Ifmmp, Xpsme!
  3        Hello, World!   ← readable!
  ...
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `ord(char) - ord('a')` | Convert letter → 0-based index |
| `% ALPHABET_SIZE` | Wrap-around (Z+1 → A) |
| `chr(base + shifted)` | Convert index back → letter |
| Preserving case | Choosing `ord('a')` vs `ord('A')` as base |
| Non-letter pass-through | `if char.isalpha()` guard |
