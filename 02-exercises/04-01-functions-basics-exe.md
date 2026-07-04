# 04-01: Exercises — Functions

> **Notes reference:** [04-01: Functions — Basics](../01-notes/04-01-functions-basics.md)

---

## Q1: Define and call
Write a function `greet(name)` that returns `"Hello, <name>!"`. Call it with two different names.

**Solution**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Jahid"))      # Hello, Jahid!
print(greet("Amelia"))     # Hello, Amelia!
```

---

## Q2: Default arguments
Write a function `power(base, exponent=2)` that returns `base ** exponent`. Call it with and without the second argument.

**Solution**
```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))       # 25  (uses default exponent=2)
print(power(2, 10))   # 1024
print(power(3, 3))    # 27
```

---

## Q3: Keyword arguments
Write a function `describe_city(city, country="Bangladesh")` and call it with and without the keyword argument.

**Solution**
```python
def describe_city(city, country="Bangladesh"):
    return f"{city} is in {country}."

print(describe_city("Dhaka"))                     # Dhaka is in Bangladesh.
print(describe_city("Berlin", country="Germany")) # Berlin is in Germany.
print(describe_city(country="USA", city="New York"))  # keyword order doesn't matter
```

---

## Q4: *args — variable positional arguments
Write a function `total(*amounts)` that returns the sum of any number of numeric arguments.

**Solution**
```python
def total(*amounts):
    return sum(amounts)

print(total(10, 20))             # 30
print(total(5, 15, 25, 35))      # 80
print(total(100))                # 100
```

---

## Q5: **kwargs — variable keyword arguments
Write a function `profile(**info)` that prints each key-value pair from the keyword arguments.

**Solution**
```python
def profile(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

profile(name="Jahid", city="New York", role="Researcher")
# name: Jahid
# city: New York
# role: Researcher
```

---

## Q6: Docstring
Write a function `bmi(weight_kg, height_m)` with a complete docstring describing parameters and return value.

**Solution**
```python
def bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index.

    Parameters:
        weight_kg (float): Body weight in kilograms
        height_m  (float): Height in metres

    Returns:
        float: BMI value rounded to 1 decimal place
    """
    return round(weight_kg / height_m ** 2, 1)

print(bmi(70, 1.75))   # 22.9
help(bmi)
```

---

## Q7: Scope — local vs global
Predict the output, then verify:

```python
x = "global"

def show():
    x = "local"
    print(x)

show()
print(x)
```

**Solution**
```
local
global
```
The `x` inside `show()` is a new local variable. The global `x` is unchanged.

---

## Q8: Functions calling functions
Write `rect_area(w, h)` and `rect_perimeter(w, h)`, then write `rect_info(w, h)` that calls both and returns a formatted string.

**Solution**
```python
def rect_area(w, h):
    return w * h

def rect_perimeter(w, h):
    return 2 * (w + h)

def rect_info(w, h):
    return f"Rectangle {w}×{h}: area={rect_area(w, h)}, perimeter={rect_perimeter(w, h)}"

print(rect_info(4, 6))   # Rectangle 4×6: area=24, perimeter=20
```

---

## Q9: Lambda
Write a lambda that squares a number, and a lambda that returns the larger of two values. Assign each to a variable.

**Solution**
```python
square  = lambda x: x ** 2
larger  = lambda a, b: a if a > b else b

print(square(7))          # 49
print(larger(12, 9))      # 12
```

---

## Q10: Functions as values (first-class)
Write a function `apply(func, value)` that takes a function and a value and returns `func(value)`. Pass `abs`, `str`, and a custom function to it.

**Solution**
```python
def apply(func, value):
    return func(value)

print(apply(abs, -15))          # 15
print(apply(str, 42))           # '42'
print(apply(lambda x: x**3, 4)) # 64
```

---

⬅️ Previous: [03-03: Exercises — while Loops](03-03-while-loops-exe.md)
➡️ Next: [05-01: Exercises — Lists](05-01-lists-exe.md)
