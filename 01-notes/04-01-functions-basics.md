# 04-01: Functions — Basics

A **function** is a named, reusable block of code. Functions avoid code repetition, break complex problems into smaller pieces, and make programs easier to read and maintain.

---

## Defining a Function

```python
def function_name(parameters):
    """Optional docstring"""
    # function body
    return value    # optional
```

### Minimal example

```python
def greet():
    print("Hello, World!")

greet()   # call the function
# Hello, World!
```

---

## Functions with Parameters

Parameters are inputs to the function:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice!
greet("Bob")      # Hello, Bob!
```

### Multiple parameters

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)     # 8

def describe(name, age, city):
    print(f"{name} is {age} years old from {city}")

describe("Alice", 30, "New York")
```

---

## The `return` Statement

`return` sends a value back to the caller and **exits the function**:

```python
def square(n):
    return n ** 2

x = square(7)
print(x)    # 49

# Return ends the function — code after return is unreachable
def abs_value(n):
    if n < 0:
        return -n     # function ends here for negative n
    return n          # function ends here for positive n
```

### Functions without `return` return `None`

```python
def say_hi():
    print("Hi!")

result = say_hi()   # Hi!
print(result)       # None
```

### Returning multiple values

Python can return multiple values as a **tuple**:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 8, 2, 9, 4])
print(lo, hi)    # 1 9

def divide_with_remainder(a, b):
    quotient  = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"{17} ÷ {5} = {q} remainder {r}")   # 17 ÷ 5 = 3 remainder 2
```

---

## Default Parameter Values

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")             # Hello, Alice!
greet("Bob", "Hi")         # Hi, Bob!
greet("Charlie", "Hey")    # Hey, Charlie!
```

**Rule:** Parameters with defaults must come **after** parameters without defaults.

```python
# Correct
def power(base, exponent=2):
    return base ** exponent

# Wrong — SyntaxError
def power(base=10, exponent):   # default before non-default!
    return base ** exponent
```

---

## Keyword Arguments

When calling a function, arguments can be named — this makes order unimportant and code more readable:

```python
def describe_person(name, age, job):
    print(f"{name}, age {age}, works as {job}")

# Positional
describe_person("Alice", 30, "engineer")

# Keyword (any order)
describe_person(job="teacher", name="Bob", age=25)

# Mixed: positional first, then keyword
describe_person("Charlie", job="doctor", age=40)
```

---

## Docstrings

A function is documented with a docstring — a triple-quoted string placed right after `def`:

```python
def circle_area(radius):
    """
    Calculate the area of a circle.

    Parameters:
        radius (float): Radius of the circle (must be >= 0)

    Returns:
        float: Area of the circle
    """
    import math
    return math.pi * radius ** 2

# Access the docstring
help(circle_area)
print(circle_area.__doc__)
```

---

## Variable Scope

### Local variables

Variables created inside a function are **local** — they only exist within that function:

```python
def calculate():
    x = 10      # local to calculate()
    print(x)

calculate()     # 10
print(x)        # NameError: name 'x' is not defined
```

### Global variables

Variables defined outside functions are **global** — accessible from anywhere:

```python
name = "Python"    # global

def show_name():
    print(name)    # can read global

show_name()    # Python
```

### Modifying globals — `global` keyword

```python
count = 0    # global

def increment():
    global count       # declare intent to modify global
    count += 1

increment()
increment()
increment()
print(count)   # 3
```

**Tip:** Avoid modifying globals — use parameters and return values instead. It makes code more predictable.

---

## Functions Calling Other Functions

```python
def circle_area(r):
    import math
    return math.pi * r ** 2

def cylinder_volume(r, h):
    base = circle_area(r)   # reuse!
    return base * h

print(cylinder_volume(3, 10))   # ~282.74

def min_of_2(a, b):
    return a if a < b else b

def min_of_3(a, b, c):
    return min_of_2(min_of_2(a, b), c)   # reuse!

print(min_of_3(5, 2, 8))   # 2
```

---

## Functions as Values

In Python, functions are **first-class objects** — they can be assigned to variables, passed to other functions, and returned:

```python
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

# Assign to variable
f = square
print(f(5))    # 25

# Pass as argument
def apply(func, value):
    return func(value)

print(apply(square, 4))   # 16
print(apply(cube, 3))     # 27
```

---

## Lambda Functions (Anonymous Functions)

A `lambda` is a small, one-expression function:

```python
# Syntax: lambda parameters: expression

square = lambda n: n ** 2
print(square(5))    # 25

add = lambda a, b: a + b
print(add(3, 7))    # 10

# Common use: as argument to sorted(), map(), filter()
words = ["banana", "apple", "cherry", "date"]
sorted_by_length = sorted(words, key=lambda w: len(w))
print(sorted_by_length)   # ['date', 'apple', 'banana', 'cherry']

numbers = [1, -2, 3, -4, 5]
positives = list(filter(lambda n: n > 0, numbers))
print(positives)   # [1, 3, 5]

doubled = list(map(lambda n: n * 2, numbers))
print(doubled)   # [2, -4, 6, -8, 10]
```

---

## `*args` — Variable Number of Positional Arguments

Accept any number of positional arguments:

```python
def sum_all(*args):
    total = 0
    for n in args:
        total += n
    return total

print(sum_all(1, 2, 3))          # 6
print(sum_all(1, 2, 3, 4, 5))    # 15
print(sum_all())                  # 0
```

---

## `**kwargs` — Variable Number of Keyword Arguments

Accept any number of keyword arguments:

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=30, job="Engineer")
# name: Alice
# age: 30
# job: Engineer
```

### Combining all argument types

```python
def mixed(required, default=10, *args, **kwargs):
    print("required:", required)
    print("default:", default)
    print("extra args:", args)
    print("extra kwargs:", kwargs)

mixed(1, 2, 3, 4, key="value", x=99)
# required: 1
# default: 2
# extra args: (3, 4)
# extra kwargs: {'key': 'value', 'x': 99}
```

---

## When to Write a Function

A function is appropriate in these situations:
1. Repeating the same code more than once
2. Writing a block of code that does one clear thing
3. Needing to test or reuse a piece of logic

```python
# Without functions — repetitive
print(80, "F is", 5/9*(80-32), "C")
print(65, "F is", 5/9*(65-32), "C")
print(32, "F is", 5/9*(32-32), "C")

# With a function — clean and reusable
def f_to_c(f):
    return 5/9 * (f - 32)

for temp in [80, 65, 32]:
    print(f"{temp}°F = {f_to_c(temp):.1f}°C")
```

---

## Quick Summary

| Concept | Syntax |
|---------|--------|
| Define function | `def name(params):` |
| Return value | `return value` |
| Default parameter | `def f(x, y=10):` |
| Keyword argument | `f(y=5, x=3)` |
| Variable positional | `def f(*args):` |
| Variable keyword | `def f(**kwargs):` |
| Lambda | `lambda x: x**2` |
| Docstring | `"""Description"""` |

---

## Practice Problems

```python
# 1. Temperature conversion with both directions
def convert_temp(value, from_unit):
    if from_unit == "C":
        return value * 9/5 + 32, "F"
    elif from_unit == "F":
        return (value - 32) * 5/9, "C"

result, unit = convert_temp(100, "C")
print(f"{result:.1f}°{unit}")   # 212.0°F

# 2. Factorial
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))   # 120

# 3. Is palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))       # True
print(is_palindrome("A man a plan a canal Panama"))  # True

# 4. Statistics
def stats(numbers):
    n = len(numbers)
    total = sum(numbers)
    mean = total / n
    sorted_nums = sorted(numbers)
    median = sorted_nums[n//2] if n % 2 else (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    return {"mean": mean, "median": median, "min": min(numbers), "max": max(numbers)}

data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
for key, val in stats(data).items():
    print(f"{key}: {val}")
```

---

> **Exercises:** [04-01: Exercises — Functions](../02-exercises/04-01-functions-basics-exe.md)

---

⬅️ Previous: [03-03: while Loops](03-03-while-loops.md)
➡️ Next: [05-01: Lists — The Complete Guide](05-01-lists.md)
