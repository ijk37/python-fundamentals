# 06-02: Exception Handling

An **exception** is a runtime error that disrupts the normal flow of a program. Exception handling allows errors to be detected and responded to gracefully instead of crashing.

---

## What Are Exceptions?

```python
# These all raise exceptions
print(10 / 0)          # ZeroDivisionError
print(int("hello"))    # ValueError
print([1,2][5])        # IndexError
print("hi" + 5)        # TypeError
print(undefined_var)   # NameError
print(open("nope.txt"))  # FileNotFoundError
```

Without handling, these crash the program with a **traceback**.

---

## Common Built-in Exceptions

| Exception | When it occurs |
|-----------|----------------|
| `ZeroDivisionError` | Division or modulo by zero |
| `ValueError` | Wrong value (right type) — e.g., `int("hello")` |
| `TypeError` | Wrong type — e.g., `"hi" + 5` |
| `IndexError` | List/string index out of range |
| `KeyError` | Dict key not found |
| `AttributeError` | Attribute not found on object |
| `NameError` | Variable not defined |
| `FileNotFoundError` | File doesn't exist |
| `PermissionError` | No permission to read/write file |
| `OverflowError` | Number too large for float |
| `RecursionError` | Stack too deep |
| `StopIteration` | Iterator exhausted |
| `ImportError` | Module not found |
| `OSError` | OS-level error |

---

## Basic `try ... except`

```python
try:
    # code that might raise an exception
    result = 10 / 0
except:
    # runs if any exception occurs
    print("Something went wrong")
```

Better — catch the specific exception:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## Catching Multiple Exceptions

```python
# Multiple except clauses
try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(result)
except ValueError:
    print("That's not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catch multiple in one clause
try:
    data = [1, 2, 3]
    print(data[int(input("Index: "))])
except (ValueError, IndexError) as e:
    print(f"Error: {e}")
```

---

## The `as` Clause — Accessing the Exception Object

```python
try:
    x = int("not a number")
except ValueError as e:
    print(f"ValueError caught: {e}")
    # ValueError caught: invalid literal for int() with base 10: 'not a number'

try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print(f"Key {e} not found in dictionary")
```

---

## `else` Clause — Runs When No Exception

```python
try:
    n = int(input("Enter a number: "))
    result = 10 / n
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    # runs ONLY if no exception occurred
    print(f"10 / {n} = {result}")
```

---

## `finally` Clause — Always Runs

The `finally` block runs **whether or not** an exception occurred — perfect for cleanup:

```python
try:
    f = open("data.txt")
    data = f.read()
    result = int(data)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("File doesn't contain a valid number")
finally:
    # This ALWAYS runs — for cleanup
    print("Execution complete")
    # If file was opened, close it

# Better approach — with statement handles this automatically
with open("data.txt") as f:
    data = f.read()
```

### `finally` with return

```python
def read_file(path):
    try:
        f = open(path)
        return f.read()
    except FileNotFoundError:
        return None
    finally:
        print("Attempted to read:", path)   # always prints
```

---

## Full try/except/else/finally Structure

```python
try:
    # dangerous code
    pass
except SpecificError as e:
    # handle specific error
    pass
except (AnotherError, YetAnother) as e:
    # handle multiple errors
    pass
except Exception as e:
    # catch any remaining exception
    pass
else:
    # runs if NO exception occurred
    pass
finally:
    # ALWAYS runs (cleanup)
    pass
```

---

## Catching All Exceptions

```python
# Catch any exception (use sparingly — can hide bugs)
try:
    risky_code()
except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")

# Even broader — catches SystemExit, KeyboardInterrupt too
try:
    risky_code()
except BaseException as e:
    print(f"Critical error: {e}")
```

**Best practice:** Always catch the most specific exception first. Avoid bare `except:` in production code.

---

## Re-raising Exceptions

```python
def process(value):
    try:
        result = int(value)
    except ValueError:
        print(f"Log: Invalid input '{value}'")
        raise    # re-raise the same exception

try:
    process("abc")
except ValueError as e:
    print(f"Failed to process: {e}")
```

### Raise a different exception

```python
def validate_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age is unrealistically large")
        return age
    except TypeError:
        raise ValueError(f"Expected a number, got {type(age).__name__}")
```

---

## Raising Exceptions Manually

```python
# raise ExceptionType("message")

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b

def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be int, not {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of valid range [0, 150]")
    return age
```

---

## Custom Exceptions

Custom exception classes can be created for domain-specific errors:

```python
class AppError(Exception):
    """Base class for application errors"""
    pass

class ValidationError(AppError):
    """Raised when input validation fails"""
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"Validation failed for '{field}': {message}")

class DatabaseError(AppError):
    """Raised when database operation fails"""
    pass

# Usage
def save_user(name, age):
    if not name.strip():
        raise ValidationError("name", "cannot be empty")
    if age < 0:
        raise ValidationError("age", "must be non-negative")
    print(f"Saved: {name}, {age}")

try:
    save_user("", 25)
except ValidationError as e:
    print(f"Error: {e}")
    print(f"Problem field: {e.field}")
except AppError as e:
    print(f"Application error: {e}")
```

---

## Input Validation Pattern

A robust pattern for validating user input:

```python
def get_integer(prompt, min_val=None, max_val=None):
    """Get valid integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")

age = get_integer("Enter your age: ", min_val=0, max_val=120)
print(f"Your age is: {age}")
```

---

## Exception Hierarchy

Python exceptions form a hierarchy. Catching a parent class catches all its children:

```python
# Exception hierarchy (simplified)
# BaseException
#   SystemExit
#   KeyboardInterrupt
#   Exception
#     ValueError
#     TypeError
#     OSError
#       FileNotFoundError
#       PermissionError
#     LookupError
#       IndexError
#       KeyError
#     ArithmeticError
#       ZeroDivisionError
#       OverflowError

# Catching OSError catches FileNotFoundError too
try:
    f = open("missing.txt")
except OSError as e:
    print(type(e).__name__, e)   # FileNotFoundError ...
```

---

## Context Managers (`with` statement)

The `with` statement provides automatic exception-safe cleanup:

```python
# Without with — risk of forgetting close()
f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()

# With with — automatic, cleaner
with open("data.txt") as f:
    data = f.read()
# f is automatically closed here, even if an exception occurs
```

---

## Quick Summary

| Clause | Purpose |
|--------|---------|
| `try:` | Wrap risky code |
| `except ExcType:` | Handle specific exception |
| `except (A, B):` | Handle multiple exceptions |
| `except ExcType as e:` | Access exception object |
| `else:` | Run if no exception |
| `finally:` | Always run (cleanup) |
| `raise ExcType(msg)` | Raise an exception |
| `raise` | Re-raise current exception |

---

## Practice Problems

```python
# 1. Safe division function
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError as e:
        raise TypeError(f"Both arguments must be numbers: {e}")

print(safe_divide(10, 3))    # 3.333...
print(safe_divide(10, 0))    # None
print(safe_divide(10, "2"))  # TypeError

# 2. Safe file reader
def read_file_safe(path):
    try:
        with open(path, "rt", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return ""
    except PermissionError:
        print(f"Permission denied: {path}")
        return ""
    except UnicodeDecodeError:
        print(f"Encoding error in: {path}")
        return ""

# 3. Safe JSON parser
import json
def parse_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON at line {e.lineno}: {e.msg}")
        return None

print(parse_json('{"a": 1}'))         # {'a': 1}
print(parse_json('{invalid json}'))   # None

# 4. Retry decorator
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator
```

---

> **Exercises:** [06-02: Exercises — Exception Handling](../02-exercises/06-02-exception-handling-exe.md)

---

⬅️ Previous: [06-01: Comprehensions — list, set, dict](06-01-comprehensions.md)
➡️ Next: [07-01: File I/O — Reading and Writing Files](07-01-file-io.md)
