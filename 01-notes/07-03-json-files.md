# 07-03: Working with JSON Files

**JSON** (JavaScript Object Notation) is the universal format for structured data exchange — APIs, config files, databases, and web services all use it. Python's built-in `json` module handles it perfectly.

---

## What is JSON?

```json
{
  "name": "Alice",
  "age": 30,
  "is_active": true,
  "score": 88.5,
  "tags": ["python", "data-science"],
  "address": {
    "city": "New York",
    "zip": "10001"
  },
  "notes": null
}
```

JSON types map directly to Python:

| JSON | Python |
|------|--------|
| `object { }` | `dict` |
| `array [ ]` | `list` |
| `string "..."` | `str` |
| `number (int)` | `int` |
| `number (float)` | `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

---

## Reading JSON Files

```python
import json

# Load from file
with open("data.json", "rt", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))         # <class 'dict'>
print(data["name"])       # Alice
print(data["tags"])       # ['python', 'data-science']
print(data["address"]["city"])  # New York

# Load a JSON array from file
with open("students.json", "rt", encoding="utf-8") as f:
    students = json.load(f)   # list of dicts

for s in students:
    print(s["name"], s["score"])
```

---

## Writing JSON Files

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "scores": [85, 92, 78],
    "active": True,
    "notes": None,
}

# Basic write
with open("output.json", "wt", encoding="utf-8") as f:
    json.dump(data, f)

# Pretty-printed (human readable)
with open("output.json", "wt", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Pretty-printed with sorted keys
with open("output.json", "wt", encoding="utf-8") as f:
    json.dump(data, f, indent=2, sort_keys=True)

# Compact (no extra spaces) — for smaller file size
with open("output.json", "wt", encoding="utf-8") as f:
    json.dump(data, f, separators=(",", ":"))
```

---

## JSON Strings (in-memory)

When working with APIs or network data, JSON strings are handled rather than files:

```python
import json

# Python dict → JSON string
data = {"name": "Bob", "age": 25}
json_string = json.dumps(data)
print(json_string)            # '{"name": "Bob", "age": 25}'
print(type(json_string))      # <class 'str'>

# Pretty
print(json.dumps(data, indent=2))

# JSON string → Python dict
text = '{"name": "Bob", "age": 25, "active": true}'
parsed = json.loads(text)
print(parsed)             # {'name': 'Bob', 'age': 25, 'active': True}
print(parsed["name"])     # Bob
print(type(parsed))       # <class 'dict'>
```

---

## Working with Nested JSON

```python
import json

json_str = """
{
  "company": "Acme Corp",
  "employees": [
    {"id": 1, "name": "Alice", "dept": "Engineering", "salary": 90000},
    {"id": 2, "name": "Bob",   "dept": "Marketing",   "salary": 70000},
    {"id": 3, "name": "Carol", "dept": "Engineering", "salary": 85000}
  ],
  "location": {
    "city": "New York",
    "country": "USA"
  }
}
"""

data = json.loads(json_str)

# Access nested data
print(data["company"])                      # Acme Corp
print(data["location"]["city"])             # New York
print(data["employees"][0]["name"])         # Alice

# Iterate employees
for emp in data["employees"]:
    print(f"{emp['name']} — {emp['dept']} — ${emp['salary']:,}")

# Filter
engineers = [e for e in data["employees"] if e["dept"] == "Engineering"]
avg_salary = sum(e["salary"] for e in engineers) / len(engineers)
print(f"Avg engineer salary: ${avg_salary:,.0f}")

# Add new employee
data["employees"].append({"id": 4, "name": "Dave", "dept": "HR", "salary": 65000})

# Save back
with open("company.json", "wt", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
```

---

## Error Handling

```python
import json

def safe_load_json(path):
    """Load JSON with proper error handling."""
    try:
        with open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {path}: {e.msg} (line {e.lineno})")
        return None

def safe_parse_json(text):
    """Parse JSON string with error handling."""
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        return None

# Test
result = safe_parse_json('{"valid": true}')       # works
result = safe_parse_json('{invalid json here}')   # handled gracefully
```

---

## Custom JSON Encoding

By default, `json.dumps` cannot serialize Python objects like `datetime`, `set`, `Decimal`, etc. A custom encoder is needed:

```python
import json
from datetime import datetime, date
from decimal import Decimal

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()          # "2024-06-09T15:30:00"
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, set):
            return sorted(list(obj))        # convert set to sorted list
        if isinstance(obj, bytes):
            return obj.decode("utf-8")
        return super().default(obj)

data = {
    "event": "launch",
    "timestamp": datetime.now(),
    "price": Decimal("9.99"),
    "tags": {"python", "web"},
}

print(json.dumps(data, cls=CustomEncoder, indent=2))
```

### Simpler alternative — use `default` parameter

```python
def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

print(json.dumps({"ts": datetime.now()}, default=json_serializer))
```

---

## Custom JSON Decoding

When loading, convert specific strings back to Python types:

```python
import json
from datetime import datetime

def decode_datetime(d):
    """Restore ISO datetime strings back to datetime objects."""
    for key, value in d.items():
        if isinstance(value, str):
            try:
                d[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return d

json_str = '{"name": "Alice", "joined": "2024-01-15T10:30:00"}'
data = json.loads(json_str, object_hook=decode_datetime)
print(data["joined"])         # 2024-01-15 10:30:00
print(type(data["joined"]))   # <class 'datetime.datetime'>
```

---

## JSON Lines Format (JSONL)

JSONL (.jsonl) stores one JSON object per line — common for large datasets, logs, and streaming:

```jsonl
{"id": 1, "name": "Alice", "score": 88.5}
{"id": 2, "name": "Bob", "score": 92.0}
{"id": 3, "name": "Charlie", "score": 79.3}
```

```python
import json

# Read JSONL
def read_jsonl(path):
    records = []
    with open(path, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records

# Write JSONL
def write_jsonl(path, records, mode="wt"):
    with open(path, mode, encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

students = [
    {"id": 1, "name": "Alice", "score": 88.5},
    {"id": 2, "name": "Bob",   "score": 92.0},
]
write_jsonl("students.jsonl", students)
loaded = read_jsonl("students.jsonl")
print(loaded)
```

---

## Working with JSON APIs

```python
import json
import urllib.request   # built-in, no pip needed

def get_json(url):
    """Fetch JSON from a URL."""
    try:
        with urllib.request.urlopen(url) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw)
    except Exception as e:
        print(f"Request failed: {e}")
        return None

# Fetch a public API
data = get_json("https://jsonplaceholder.typicode.com/users/1")
if data:
    print(data["name"])
    print(data["email"])

# With requests library (more convenient, pip install requests)
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()   # auto-parses JSON response
print(f"Got {len(posts)} posts")
print(posts[0]["title"])
```

---

## Practical Patterns

### Config file reader/writer

```python
import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "debug": False,
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "output_dir": "./output",
}

def load_config():
    """Load config, creating with defaults if missing."""
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    with open(CONFIG_FILE, "rt", encoding="utf-8") as f:
        config = json.load(f)
    # Merge with defaults (new keys get defaults)
    return {**DEFAULT_CONFIG, **config}

def save_config(config):
    with open(CONFIG_FILE, "wt", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

config = load_config()
config["debug"] = True
save_config(config)
```

### Cache / persistence

```python
import json
import os
from datetime import datetime

CACHE_FILE = "cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rt") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "wt") as f:
        json.dump(cache, f, indent=2)

cache = load_cache()
key = "user_42"
if key not in cache:
    cache[key] = {"name": "Alice", "fetched_at": datetime.now().isoformat()}
    save_cache(cache)
print(cache[key])
```

---

## Quick Summary

| Task | Code |
|------|------|
| File → Python | `json.load(file_obj)` |
| String → Python | `json.loads(string)` |
| Python → File | `json.dump(data, file_obj, indent=2)` |
| Python → String | `json.dumps(data, indent=2)` |
| Handle parse error | `except json.JSONDecodeError` |
| Custom types | `cls=CustomEncoder` or `default=func` |
| One object per line | JSONL format |

---

> **Exercises:** [07-03: Exercises — JSON Files](../02-exercises/07-03-json-files-exe.md)

---

⬅️ Previous: [07-02: Working with CSV Files](07-02-csv-files.md)
➡️ Next: [07-04: Working with Excel Files](07-04-excel-files.md)
