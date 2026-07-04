# 04-22: Encryption Toolkit

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_22-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 22">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

Implements Caesar cipher, ROT13, and Vigenère cipher in pure Python. Includes a frequency analysis tool and a Caesar shift guesser (uses the English letter-frequency assumption that 'e' is most common).

**Topics covered:** `ord()` / `chr()` · modular arithmetic · string iteration · `Counter` · multi-key poly-alphabetic substitution · while-loop key cycling

**Difficulty:** ⭐⭐ Intermediate

---

## How to Run

```bash
python main.py
```

---

## Ciphers Compared

| Cipher | Key | Security | Example |
|--------|-----|----------|---------|
| Caesar | 1 integer (shift) | Very weak | "HELLO" → "KHOOR" (shift 3) |
| ROT13 | Fixed (13) | Very weak | "HELLO" → "URYYB" |
| Vigenère | Word/phrase | Moderate | "HELLO" + key "KEY" → "RIJVS" |

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| `(ord(c) - ord('a') + shift) % 26` | Caesar shift formula |
| `chr(base + shifted)` | Back to character |
| Key cycling: `key[key_index % len(key)]` | Vigenère key repeat |
| `Counter(letters).most_common()` | Frequency analysis |
| Shift guessing: `(cipher_pos - e_pos) % 26` | Crack Caesar |
