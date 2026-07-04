# 07-03: Exercises — JSON Files

> **Notes reference:** [07-03: Working with JSON Files](../01-notes/07-03-json-files.md)

---

## Q1: Write a JSON file
Write a Python dictionary as a pretty-printed JSON file.

**Solution**
```python
import json

profile = {
    "name": "Jahid",
    "city": "New York",
    "origin": "Dhaka",
    "skills": ["Python", "Data Science", "Blockchain"],
    "active": True,
    "rating": 4.8,
}

with open("profile.json", "wt", encoding="utf-8") as f:
    json.dump(profile, f, indent=2)
print("profile.json written.")
```

---

## Q2: Read a JSON file
Read `profile.json` and print individual fields.

**Solution**
```python
import json

with open("profile.json", "rt", encoding="utf-8") as f:
    data = json.load(f)

print(data["name"])
print(data["city"])
print("Skills:", ", ".join(data["skills"]))
```

---

## Q3: JSON strings (dumps / loads)
Convert a Python dict to a JSON string and back.

**Solution**
```python
import json

info = {"product": "Laptop", "price_bdt": 85000, "available": True}

# Python → JSON string
json_str = json.dumps(info, indent=2)
print(json_str)
print(type(json_str))   # <class 'str'>

# JSON string → Python
parsed = json.loads(json_str)
print(parsed["price_bdt"])   # 85000
print(type(parsed))          # <class 'dict'>
```

---

## Q4: Nested JSON — access and iterate
Parse a nested JSON string containing a list of employees. Print all engineers.

**Solution**
```python
import json

raw = """
{
  "company": "TechBD",
  "location": {"city": "Dhaka", "country": "Bangladesh"},
  "employees": [
    {"id": 1, "name": "Rahim",  "dept": "Engineering", "salary": 90000},
    {"id": 2, "name": "Karim",  "dept": "Marketing",   "salary": 70000},
    {"id": 3, "name": "Farida", "dept": "Engineering", "salary": 85000}
  ]
}
"""

data = json.loads(raw)
print(data["company"])
print(data["location"]["city"])

engineers = [e for e in data["employees"] if e["dept"] == "Engineering"]
avg = sum(e["salary"] for e in engineers) / len(engineers)
print(f"Avg engineer salary: {avg:,.0f} BDT")
```

---

## Q5: Update and save JSON
Load `profile.json`, add a new key, and save it back.

**Solution**
```python
import json

with open("profile.json", "rt", encoding="utf-8") as f:
    data = json.load(f)

data["joined_year"] = 2021
data["skills"].append("NumPy")

with open("profile.json", "wt", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
print("profile.json updated.")
```

---

## Q6: Error handling — JSONDecodeError
Parse a malformed JSON string and handle the error gracefully.

**Solution**
```python
import json

def safe_parse(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e.msg} at line {e.lineno}")
        return None

good = safe_parse('{"key": "value"}')
bad  = safe_parse('{key: value}')   # missing quotes

print(good)   # {'key': 'value'}
print(bad)    # None
```

---

## Q7: JSON Lines (JSONL)
Write three records in JSONL format, then read them back line by line.

**Solution**
```python
import json

records = [
    {"id": 1, "city": "Dhaka",    "population": 21_006_000},
    {"id": 2, "city": "New York", "population":  8_336_817},
    {"id": 3, "city": "Berlin",   "population":  3_769_000},
]

# Write
with open("cities.jsonl", "wt", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec) + "\n")

# Read back
with open("cities.jsonl", "rt", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line.strip())
        print(f"{obj['city']}: {obj['population']:,}")
```

---

## Q8: Custom encoder — datetime
Serialize a dictionary that contains a `datetime` object.

**Solution**
```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

event = {
    "name": "Python Workshop",
    "location": "Dhaka",
    "date": datetime(2025, 3, 15, 9, 0),
}

json_str = json.dumps(event, cls=DateTimeEncoder, indent=2)
print(json_str)
```

**Alternative — default parameter:**
```python
def serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Not serializable: {type(obj)}")

print(json.dumps(event, default=serialize, indent=2))
```

---

## Q9: Config file pattern
Implement `load_config()` and `save_config()` that persist settings to `settings.json`.

**Solution**
```python
import json, os

DEFAULTS = {"theme": "light", "language": "en", "font_size": 14}
CONFIG_FILE = "settings.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULTS)
        return DEFAULTS.copy()
    with open(CONFIG_FILE, "rt") as f:
        return {**DEFAULTS, **json.load(f)}

def save_config(config):
    with open(CONFIG_FILE, "wt") as f:
        json.dump(config, f, indent=2)

cfg = load_config()
cfg["theme"] = "dark"
cfg["font_size"] = 16
save_config(cfg)
print(load_config())
```

---

⬅️ Previous: [07-02: Exercises — CSV Files](07-02-csv-files-exe.md)
➡️ Next: [07-04: Exercises — Excel Files](07-04-excel-files-exe.md)
