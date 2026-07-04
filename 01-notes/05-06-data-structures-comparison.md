# 05-06: Data Structures Comparison — str, list, tuple, set, dict

Python's five main built-in collection types serve different purposes. Understanding when to use each is a key programming skill.

---

## At a Glance

| | `str` | `list` | `tuple` | `set` | `dict` |
|--|-------|--------|---------|-------|--------|
| **Ordered?** | Yes | Yes | Yes | No | Yes (insertion order, 3.7+) |
| **Mutable?** | No | Yes | No | Yes | Yes |
| **Indexed?** | Yes | Yes | Yes | No | By key |
| **Sliceable?** | Yes | Yes | Yes | No | No |
| **Duplicates?** | Yes | Yes | Yes | No | No (keys), Yes (values) |
| **Hashable?** | Yes | No | Yes* | No | No |
| **Use for** | Text | Collections | Fixed data | Unique items | Key-value pairs |

*Tuple is hashable only if all its elements are hashable.

---

## Creating Each Type

```python
# str
s = "hello"
s2 = str(42)        # '42'

# list
lst = [1, 2, 3]
lst2 = list("abc")  # ['a', 'b', 'c']
lst3 = list(range(5))  # [0, 1, 2, 3, 4]

# tuple
t = (1, 2, 3)
t2 = tuple("abc")   # ('a', 'b', 'c')
single = (1,)       # comma required for single-element!

# set
s = {1, 2, 3}
s2 = set("hello")   # {'h', 'e', 'l', 'o'}
empty_set = set()   # NOT {} which is dict!

# dict
d = {"a": 1, "b": 2}
d2 = dict(x=10, y=20)
d3 = dict(zip(["a","b"], [1, 2]))
```

---

## Mutability in Detail

### Mutable — can change in-place

```python
# list — mutable
lst = [1, 2, 3]
lst[0] = 10           # change item
lst.append(4)         # add item
lst.remove(2)         # remove item

# set — mutable
s = {1, 2, 3}
s.add(4)
s.discard(2)

# dict — mutable
d = {"a": 1}
d["b"] = 2            # add item
d["a"] = 99           # change value
del d["a"]            # remove item
```

### Immutable — cannot change in-place

```python
# str — immutable
s = "hello"
s[0] = "H"            # TypeError!
s = "H" + s[1:]       # must create new string

# tuple — immutable
t = (1, 2, 3)
t[0] = 99             # TypeError!
t = (99,) + t[1:]     # must create new tuple
```

---

## Iteration

All five types support `for` loop iteration:

```python
# str — characters
for ch in "hello":
    print(ch, end=" ")    # h e l l o

# list — items
for item in [1, 2, 3]:
    print(item, end=" ")  # 1 2 3

# tuple — items
for item in (4, 5, 6):
    print(item, end=" ")  # 4 5 6

# set — items (order not guaranteed)
for item in {7, 8, 9}:
    print(item, end=" ")  # 8 9 7  (any order)

# dict — keys by default
d = {"a": 1, "b": 2}
for key in d:
    print(key)            # a  b

for key, val in d.items():
    print(f"{key}={val}") # a=1  b=2
```

---

## Sorting

```python
lst = [3, 1, 4, 1, 5]
lst.sort()             # in-place, modifies list
s = sorted(lst)        # new sorted list

# tuple — sorted() returns a list
t = (3, 1, 4)
print(sorted(t))       # [1, 3, 4]  ← list, not tuple

# set — sorted() returns a list
st = {3, 1, 4}
print(sorted(st))      # [1, 3, 4]

# dict — sort by key
d = {"b": 2, "a": 1, "c": 3}
for k in sorted(d):
    print(k, d[k])

# sort by value
for k in sorted(d, key=lambda x: d[x]):
    print(k, d[k])
```

---

## Membership Testing Speed

```python
import timeit

data_list = list(range(10000))
data_set  = set(range(10000))
data_dict = {i: i for i in range(10000)}

# Searching for 9999 (worst case for list)
t_list = timeit.timeit("9999 in data_list", globals=globals(), number=100000)
t_set  = timeit.timeit("9999 in data_set",  globals=globals(), number=100000)
t_dict = timeit.timeit("9999 in data_dict", globals=globals(), number=100000)

print(f"list:  {t_list:.3f}s")   # ~1.0s
print(f"set:   {t_set:.3f}s")    # ~0.01s  (much faster!)
print(f"dict:  {t_dict:.3f}s")   # ~0.01s  (much faster!)
```

**Key insight:** Use `set` or `dict` for fast membership testing when collection is large.

---

## Deduplication

```python
original = [1, 3, 2, 1, 4, 3, 5]

# Via set — loses order
unique_unordered = list(set(original))

# Preserving order
seen = set()
unique_ordered = [x for x in original if not (x in seen or seen.add(x))]
print(unique_ordered)   # [1, 3, 2, 4, 5]
```

---

## Conversion Between Types

```python
# list ↔ tuple ↔ set
lst = [1, 2, 2, 3, 3, 4]
t   = tuple(lst)          # (1, 2, 2, 3, 3, 4)
st  = set(lst)            # {1, 2, 3, 4}
lst2 = list(st)           # some order

# str → list → str
s   = "hello"
lst = list(s)             # ['h', 'e', 'l', 'l', 'o']
s2  = "".join(lst)        # 'hello'

# dict → list of keys/values/items
d    = {"a": 1, "b": 2}
keys = list(d.keys())     # ['a', 'b']
vals = list(d.values())   # [1, 2]
items = list(d.items())   # [('a', 1), ('b', 2)]

# list of tuples → dict
pairs = [("a", 1), ("b", 2)]
d2 = dict(pairs)          # {'a': 1, 'b': 2}
```

---

## Slicing Support

```python
s  = "hello"
ls = [1, 2, 3, 4, 5]
t  = (1, 2, 3, 4, 5)

# All support slicing
print(s[1:4])    # 'ell'
print(ls[1:4])   # [2, 3, 4]
print(t[1:4])    # (2, 3, 4)

# set and dict do NOT support slicing
st = {1, 2, 3}
# st[1:3]   → TypeError!

d = {"a": 1}
# d[0:2]    → TypeError!
```

---

## Deletion

```python
# list — delete by index, slice, or value
lst = [1, 2, 3, 4, 5]
del lst[2]          # [1, 2, 4, 5]
del lst[1:3]        # [1, 5]
lst.remove(1)       # [5]
lst.pop()           # [], removed 5

# set — delete by value
s = {1, 2, 3}
s.discard(2)        # {1, 3}
s.remove(1)         # {3}

# dict — delete by key
d = {"a": 1, "b": 2}
del d["a"]          # {'b': 2}
d.pop("b")          # {}

# str, tuple — immutable, no direct deletion
# Must create a new object instead
```

---

## When to Use Which

| Situation | Use |
|-----------|-----|
| Text data | `str` |
| Ordered, changing collection | `list` |
| Ordered, fixed data (coordinates, records) | `tuple` |
| Unique items, fast membership test | `set` |
| Key-value mapping, fast lookup by key | `dict` |
| Return multiple values from function | `tuple` |
| Constant configuration data | `tuple` |
| Removing duplicates | `set` |
| Counting occurrences | `dict` (or `Counter`) |
| SQL-like records | `list` of `tuple`/`dict` |

---

## Common Patterns

```python
# Count items — dict
text = "hello world"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

# Remove duplicates from list
lst = [1, 2, 2, 3, 3]
unique = list(dict.fromkeys(lst))   # preserves order, Python 3.7+
# or
unique2 = list(set(lst))            # does NOT preserve order

# Group by property — dict of lists
data = [("Alice", "Math"), ("Bob", "CS"), ("Alice", "CS")]
groups = {}
for name, course in data:
    groups.setdefault(name, []).append(course)

# Check all unique — set
def all_unique(lst):
    return len(lst) == len(set(lst))

# Find duplicates
def find_duplicates(lst):
    seen = set()
    return {x for x in lst if x in seen or seen.add(x)}
```

---

⬅️ Previous: [05-05: Slicing — Extracting Subsequences](05-05-slicing.md)
➡️ Next: [05-07: zip(), enumerate(), and Collection Conversions](05-07-zip-enumerate-and-conversions.md)
