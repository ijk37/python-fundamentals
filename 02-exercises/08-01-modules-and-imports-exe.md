# 08-01: Exercises — Modules and Imports

> **Notes reference:** [08-01: Modules and Imports](../01-notes/08-01-modules-and-imports.md)

---

## Q1: Import and use math
Use the `math` module to compute the hypotenuse of a right triangle with legs 3 and 4.

**Solution**
```python
import math

a, b = 3, 4
hypotenuse = math.sqrt(a**2 + b**2)
print(f"Hypotenuse: {hypotenuse}")   # 5.0

# Also try
print(math.hypot(a, b))   # 5.0 (built-in shortcut)
```

---

## Q2: Import with alias
Import `math` as `m` and compute log base 2 of 1024, and `math.pi` rounded to 4 places.

**Solution**
```python
import math as m

print(m.log2(1024))           # 10.0
print(round(m.pi, 4))         # 3.1416
print(m.factorial(10))        # 3628800
```

---

## Q3: from-import specific names
Import only `sqrt`, `floor`, `ceil` from `math` and demonstrate each.

**Solution**
```python
from math import sqrt, floor, ceil

print(sqrt(144))    # 12.0
print(floor(7.9))   # 7
print(ceil(7.1))    # 8
```

---

## Q4: random module
Simulate rolling two dice 5 times. Print each roll and count how many times both dice match.

**Solution**
```python
import random

random.seed(0)
doubles = 0

for roll in range(1, 6):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    match = " ← double!" if d1 == d2 else ""
    print(f"Roll {roll}: {d1} + {d2}{match}")
    if d1 == d2:
        doubles += 1

print(f"Doubles: {doubles}/5")
```

---

## Q5: random — sample and shuffle
Shuffle a list of 5 Bangladeshi cities and pick 3 at random without replacement.

**Solution**
```python
import random

cities = ["Dhaka", "Chittagong", "Sylhet", "Rajshahi", "Khulna"]

random.shuffle(cities)
print("Shuffled:", cities)

chosen = random.sample(cities, k=3)
print("Chosen 3:", chosen)
```

---

## Q6: os module — path utilities
Use `os.path` to demonstrate `basename`, `dirname`, `splitext`, and `join`.

**Solution**
```python
import os

path = "/home/jahid/projects/data_analysis.py"

print(os.path.basename(path))      # data_analysis.py
print(os.path.dirname(path))       # /home/jahid/projects
print(os.path.splitext(path))      # ('/home/jahid/projects/data_analysis', '.py')
print(os.path.join("data", "2025", "report.csv"))   # data/2025/report.csv
```

---

## Q7: datetime module
Print today's date, add 30 days, and calculate how many days until the next New Year.

**Solution**
```python
from datetime import date, timedelta

today    = date.today()
in_30    = today + timedelta(days=30)
new_year = date(today.year + 1, 1, 1)
countdown = (new_year - today).days

print(f"Today:           {today}")
print(f"In 30 days:      {in_30}")
print(f"Next New Year:   {new_year}")
print(f"Days to New Year: {countdown}")
```

---

## Q8: collections.Counter
Count word frequency in a sentence and print the 3 most common words.

**Solution**
```python
from collections import Counter

text  = "dhaka is a great city and new york is also a great city to live in"
words = text.split()
freq  = Counter(words)

print("Most common:")
for word, count in freq.most_common(3):
    print(f"  '{word}': {count}")
```

---

## Q9: collections.defaultdict
Group Bangladeshi cities by their first letter using `defaultdict(list)`.

**Solution**
```python
from collections import defaultdict

cities = ["Dhaka", "Dinajpur", "Chittagong", "Comilla", "Sylhet", "Rajshahi"]
groups = defaultdict(list)

for city in cities:
    groups[city[0]].append(city)

for letter, group in sorted(groups.items()):
    print(f"{letter}: {group}")
```

---

## Q10: itertools
Use `itertools.combinations` to generate all 2-player match-ups from 4 teams.

**Solution**
```python
import itertools

teams    = ["Dhaka Tigers", "Chittagong Eagles", "Sylhet Storm", "Rajshahi Royals"]
matchups = list(itertools.combinations(teams, 2))

print(f"Total matchups: {len(matchups)}")
for home, away in matchups:
    print(f"  {home}  vs  {away}")
```

---

## Q11: Create and use your own module
Create `pricing.py` with `net_price(price)` and `discount(price, pct)`, then import it.

**pricing.py**
```python
# pricing.py
TAX_RATE = 0.08

def net_price(price):
    return round(price * (1 + TAX_RATE), 2)

def discount(price, pct):
    return round(price * (1 - pct / 100), 2)

if __name__ == "__main__":
    print("pricing module test")
    print(net_price(100))    # 108.0
    print(discount(200, 15)) # 170.0
```

**main.py**
```python
# main.py
import pricing

print(pricing.TAX_RATE)          # 0.08
print(pricing.net_price(500))    # 540.0
print(pricing.discount(1000, 20))# 800.0

# Or import specific names
from pricing import discount
print(discount(250, 10))         # 225.0
```

---

⬅️ Previous: [07-06: Exercises — pathlib and File System Operations](07-06-pathlib-and-filesystem-exe.md)
➡️ Next: [08-02: Exercises — Module Structure](08-02-module-structure-exe.md)
