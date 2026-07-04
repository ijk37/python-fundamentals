# 05-04: Exercises — Dictionaries

> **Notes reference:** [05-04: Dictionaries](../01-notes/05-04-dictionaries.md)

---

## Q1: Create and access
Create a dictionary for a student with keys `name`, `age`, `city`, `gpa`. Access each value.

**Solution**
```python
student = {
    "name": "Jahid",
    "age" : 28,
    "city": "New York",
    "gpa" : 3.8,
}
print(student["name"])        # Jahid
print(student.get("gpa"))     # 3.8
print(student.get("major", "Undeclared"))  # Undeclared (default)
```

---

## Q2: Add, update, delete
Start with `scores = {"Math": 85, "Physics": 78}`. Add `"Chemistry": 92`, update `"Math"` to `90`, and delete `"Physics"`.

**Solution**
```python
scores = {"Math": 85, "Physics": 78}
scores["Chemistry"] = 92
scores["Math"]      = 90
del scores["Physics"]
print(scores)   # {'Math': 90, 'Chemistry': 92}
```

---

## Q3: keys, values, items
Iterate over a country → capital dictionary and print each pair.

**Solution**
```python
capitals = {
    "Bangladesh": "Dhaka",
    "USA"       : "Washington D.C.",
    "Germany"   : "Berlin",
    "Japan"     : "Tokyo",
    "Kenya"     : "Nairobi",
}
for country, capital in capitals.items():
    print(f"{country}: {capital}")
```

---

## Q4: dict.get with default
Ask the user for a city name and look it up in the population dictionary. If not found, print `"City not found"`.

**Solution**
```python
population = {
    "Dhaka"   : 21_006_000,
    "New York": 8_336_817,
    "Berlin"  : 3_769_000,
}
city = input("Enter city: ")
pop  = population.get(city, "City not found")
print(pop)
```

---

## Q5: update() and merge
Merge two dictionaries: user defaults and user preferences.

**Solution**
```python
defaults = {"theme": "light", "language": "en", "font_size": 14}
prefs    = {"theme": "dark",  "font_size": 16}

settings = {**defaults, **prefs}   # merge, prefs override defaults
print(settings)
# {'theme': 'dark', 'language': 'en', 'font_size': 16}

# Alternative:
defaults.update(prefs)
print(defaults)
```

---

## Q6: Dictionary comprehension
Build a dictionary mapping numbers 1–8 to their cubes.

**Solution**
```python
cubes = {n: n**3 for n in range(1, 9)}
print(cubes)
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}
```

---

## Q7: Nested dictionary
Create a nested dictionary for two employees. Access a specific nested value.

**Solution**
```python
employees = {
    "E001": {"name": "Rahul", "dept": "Engineering", "salary": 95000},
    "E002": {"name": "Sarah", "dept": "Data Science", "salary": 105000},
}
print(employees["E002"]["name"])      # Sarah
print(employees["E001"]["salary"])    # 95000
```

---

## Q8: Count word frequency
Count how many times each word appears in a sentence.

**Solution**
```python
sentence = "the cat sat on the mat and the cat ate the rat"
freq     = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

for word, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(f"{word}: {count}")
```

**Alternative — using collections.Counter:**
```python
from collections import Counter
freq = Counter(sentence.split())
print(freq.most_common(5))
```

---

## Q9: setdefault and grouping
Group a list of names by their first letter.

**Solution**
```python
names  = ["Alice", "Bob", "Anna", "Ben", "Carol", "Chris"]
groups = {}
for name in names:
    groups.setdefault(name[0], []).append(name)

print(groups)
# {'A': ['Alice', 'Anna'], 'B': ['Bob', 'Ben'], 'C': ['Carol', 'Chris']}
```

---

⬅️ Previous: [05-03: Exercises — Sets](05-03-sets-exe.md)
➡️ Next: [05-05: Exercises — Slicing](05-05-slicing-exe.md)
