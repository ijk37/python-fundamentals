# 05-03: Exercises — Sets

> **Notes reference:** [05-03: Sets](../01-notes/05-03-sets.md)

---

## Q1: Create a set and remove duplicates
Create a set from a list with duplicates: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]`.

**Solution**
```python
nums   = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique = set(nums)
print(unique)     # {1, 2, 3, 4, 5, 6, 9}  (order may vary)
print(len(nums), "→", len(unique))   # 10 → 7
```

---

## Q2: add and remove
Create `languages = {"Python", "Java", "C"}`. Add `"Rust"`, remove `"Java"`, and discard `"Go"` safely (without error).

**Solution**
```python
languages = {"Python", "Java", "C"}
languages.add("Rust")
languages.remove("Java")
languages.discard("Go")    # no error even if not present
print(languages)   # {'Python', 'C', 'Rust'}
```

---

## Q3: Union and intersection
Given students in Math `= {"Alice", "Bob", "Carol"}` and Physics `= {"Bob", "David", "Carol", "Eve"}`, find:
- all students (union)
- students in both (intersection)
- students only in Math (difference)

**Solution**
```python
math    = {"Alice", "Bob", "Carol"}
physics = {"Bob", "David", "Carol", "Eve"}

print(math | physics)     # all students
print(math & physics)     # {'Bob', 'Carol'}
print(math - physics)     # {'Alice'}
print(math ^ physics)     # symmetric difference: {'Alice', 'David', 'Eve'}
```

---

## Q4: Subset and superset
Check whether `{"Python", "C"}` is a subset of `{"Python", "C", "Java", "Rust"}`.

**Solution**
```python
small = {"Python", "C"}
big   = {"Python", "C", "Java", "Rust"}

print(small.issubset(big))     # True
print(big.issuperset(small))   # True
print(small <= big)            # True  (operator shorthand)
```

---

## Q5: Unique characters
Count the number of unique characters in `"Chittagong"`.

**Solution**
```python
word = "Chittagong"
unique_chars = set(word)
print(len(unique_chars))   # 7  (C,h,i,t,a,g,o,n — 'g' repeated)
print(unique_chars)
```

---

## Q6: Set from two lists
Find words that appear in sentence A but NOT in sentence B.

**Solution**
```python
a = set("the quick brown fox".split())
b = set("the lazy brown dog".split())

only_in_a = a - b
print(only_in_a)   # {'quick', 'fox'}
```

---

## Q7: Membership test performance
Show that `in` is O(1) for sets vs O(n) for lists — demonstrate by checking membership.

**Solution**
```python
large_list = list(range(1_000_000))
large_set  = set(large_list)

# Both return True, but set lookup is instant
print(999_999 in large_list)   # True  (slow — scans the list)
print(999_999 in large_set)    # True  (fast — hash lookup)
print(2_000_000 in large_set)  # False
```

---

⬅️ Previous: [05-02: Exercises — Tuples](05-02-tuples-exe.md)
➡️ Next: [05-04: Exercises — Dictionaries](05-04-dictionaries-exe.md)
