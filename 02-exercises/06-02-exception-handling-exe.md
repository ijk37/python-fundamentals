# 06-02: Exercises — Exception Handling

> **Notes reference:** [06-02: Exception Handling](../01-notes/06-02-exception-handling.md)

---

## Q1: Basic try/except
Wrap a division that could fail. Catch the `ZeroDivisionError` and print a friendly message.

**Solution**
```python
try:
    result = 100 / int(input("Enter divisor: "))
    print(f"Result: {result:.2f}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid integer.")
```

---

## Q2: Multiple except clauses
Handle three different error types when converting user input.

**Solution**
```python
raw = input("Enter a number: ")
try:
    n = int(raw)
    print(100 / n)
except ValueError:
    print(f"'{raw}' is not a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Q3: else clause
The `else` block runs only when no exception occurred. Use it to print a success message.

**Solution**
```python
try:
    n = int(input("Enter a positive integer: "))
    result = 1000 / n
except ValueError:
    print("Not a valid integer.")
except ZeroDivisionError:
    print("Must be non-zero.")
else:
    print(f"1000 / {n} = {result:.4f}")   # only runs if no exception
```

---

## Q4: finally clause
Show that `finally` always executes, regardless of whether an exception occurred.

**Solution**
```python
def read_data(filename):
    f = None
    try:
        f = open(filename, "r")
        content = f.read()
        print(content[:100])
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    finally:
        if f:
            f.close()
        print("Cleanup complete.")   # always runs

read_data("missing.txt")
```

---

## Q5: raise — validate input
Write a function `set_age(age)` that raises a `ValueError` if age is not between 0 and 120.

**Solution**
```python
def set_age(age):
    if not 0 <= age <= 120:
        raise ValueError(f"Age {age} is out of range (0–120).")
    return age

try:
    set_age(150)
except ValueError as e:
    print(e)   # Age 150 is out of range (0–120).
```

---

## Q6: Custom exception
Create a custom `InsufficientFundsError` for a simple bank account.

**Solution**
```python
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount  = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    balance = withdraw(500, 750)
except InsufficientFundsError as e:
    print(e)
```

---

## Q7: Re-raise an exception
Catch an exception, log it, then re-raise it so the caller also handles it.

**Solution**
```python
def parse_number(s):
    try:
        return int(s)
    except ValueError as e:
        print(f"[LOG] Failed to parse: '{s}' — {e}")
        raise   # re-raise the same exception

try:
    parse_number("abc")
except ValueError:
    print("Handled at caller level.")
```

---

## Q8: try/except in a loop — robust input
Keep asking the user for a valid integer between 1 and 10 until they provide one.

**Solution**
```python
while True:
    try:
        n = int(input("Enter a number (1–10): "))
        if 1 <= n <= 10:
            print(f"Got it: {n}")
            break
        else:
            print("Out of range, try again.")
    except ValueError:
        print("Not a valid integer, try again.")
```

---

⬅️ Previous: [06-01: Exercises — Comprehensions](06-01-comprehensions-exe.md)
➡️ Next: [07-01: Exercises — File I/O](07-01-file-io-exe.md)
