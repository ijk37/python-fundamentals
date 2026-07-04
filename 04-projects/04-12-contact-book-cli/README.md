# 04-12: Contact Book CLI

<div align="center" markdown>

![Python: Fundamentals](../../assets/banner.svg)

[![View the live site — ijk37.com](https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998?style=for-the-badge&labelColor=FFD43B)](https://ijk37.com/python-fundamentals/)

<img src="https://img.shields.io/badge/Project_12-Python-306998?style=for-the-badge&labelColor=1E4B73" alt="Project 12">

[Home](../../index.md) &nbsp;|&nbsp; [All Projects](../README.md) &nbsp;|&nbsp; [Notes](../../01-notes/README.md) &nbsp;|&nbsp; [Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; [Quiz Hub](../../03-quiz/)

</div>

An in-memory contact manager with full CRUD support. Contacts are stored in a dictionary keyed by an auto-incrementing ID. Supports listing (sorted A–Z), adding, viewing, editing, deleting, and substring searching.

**Topics covered:** nested dicts · `dict.get()` · `del dict[key]` · `sorted(..., key=lambda)` · CRUD pattern · `**kwargs` · while-loop menu · input validation · functions

**Difficulty:** ⭐⭐ Beginner–Intermediate

---

## How to Run

```bash
python main.py
```

---

## Sample Listing

```
  ID    Name                   Phone            Email
  ────────────────────────────────────────────────────────────
  4     Arif Hossain           01611-998877     arif@study.edu
  2     Karim Ahmed            01812-334455     karim@office.com
  3     Nasrin Begum           01919-667788
  1     Rahim Uddin            01711-001122     rahim@mail.com
```

---

## Key Concepts Practised

| Concept | Where used |
|---------|-----------|
| Dict as data store | `contacts = {}` |
| `dict.get(id)` | Safe lookup without KeyError |
| `del contacts[id]` | Delete by key |
| `sorted(dict.items(), key=...)` | Alphabetical listing |
| `**fields` (kwargs) | Flexible `update_contact()` |
| Substring search | `query in contact["name"].lower()` |
