# 05-02: Exercises — Tuples

> **Notes reference:** [05-02: Tuples](../01-notes/05-02-tuples.md)

---

## Q1: Create and access
Create a tuple of 4 capital cities (one from Bangladesh, one from USA, one from Germany, one from Japan). Access each element.

**Solution**
```python
capitals = ("Dhaka", "Washington D.C.", "Berlin", "Tokyo")
print(capitals[0])    # Dhaka
print(capitals[-1])   # Tokyo
print(len(capitals))  # 4
```

---

## Q2: Immutability
Try to change the first element of a tuple. What error appears?

**Solution**
```python
point = (3, 7)
# point[0] = 10   → TypeError: 'tuple' object does not support item assignment
print("Tuples cannot be modified after creation.")
```

---

## Q3: Tuple unpacking
Unpack `coords = (40.7128, -74.0060)` (latitude and longitude of New York) into two separate variables.

**Solution**
```python
coords = (40.7128, -74.0060)
lat, lon = coords
print(f"Latitude: {lat}, Longitude: {lon}")
```

---

## Q4: Swap with tuple unpacking
Swap the values of `a = "red"` and `b = "blue"` using tuple unpacking in one line.

**Solution**
```python
a, b = "red", "blue"
a, b = b, a
print(a, b)   # blue red
```

---

## Q5: Function returning multiple values
Write a function `min_max(numbers)` that returns the minimum and maximum of a list as a tuple.

**Solution**
```python
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([5, 3, 9, 1, 7])
print(f"Min: {lo}, Max: {hi}")   # Min: 1, Max: 9
```

---

## Q6: Tuple as dictionary key
Create a dictionary that maps coordinate tuples to city names.

**Solution**
```python
locations = {
    (23.8103, 90.4125): "Dhaka",
    (40.7128, -74.0060): "New York",
    (52.5200, 13.4050): "Berlin",
}
print(locations[(23.8103, 90.4125)])   # Dhaka
```

---

## Q7: count and index
Given `t = (1, 2, 3, 2, 4, 2, 5)`, find how many times `2` appears and the index of `4`.

**Solution**
```python
t = (1, 2, 3, 2, 4, 2, 5)
print(t.count(2))    # 3
print(t.index(4))    # 4
```

---

⬅️ Previous: [05-01: Exercises — Lists](05-01-lists-exe.md)
➡️ Next: [05-03: Exercises — Sets](05-03-sets-exe.md)
