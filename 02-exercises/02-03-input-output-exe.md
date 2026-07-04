# 02-03: Exercises — Input and Output

> **Notes reference:** [02-03: Input and Output](../01-notes/02-03-input-output.md)

---

## Q1: Read and greet
Ask the user for their name and print: `Hello, <name>! Welcome to Python.`

**Solution**
```python
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python.")
```

---

## Q2: Sum of two numbers
Ask the user for two integers and print their sum.

**Solution**
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
```

---

## Q3: Area of a rectangle
Ask the user for width and height (floats), then print the area formatted to 2 decimal places.

**Solution**
```python
width  = float(input("Enter width: "))
height = float(input("Enter height: "))
area   = width * height
print(f"Area = {area:.2f}")
```

---

## Q4: print() with sep and end
Print `"Dhaka"`, `"Berlin"`, `"Tokyo"` separated by `" → "`, and end the line with `" ✓\n"`.

**Solution**
```python
print("Dhaka", "Berlin", "Tokyo", sep=" → ", end=" ✓\n")
# Output: Dhaka → Berlin → Tokyo ✓
```

---

## Q5: Input always returns a string
What is the data type of `x` after `x = input("Enter: ")`? Show what happens if the user types `42` and the code does `x + 1`.

**Solution**
```python
x = input("Enter: ")   # user types 42
print(type(x))         # <class 'str'>  — NOT int!

# x + 1 raises TypeError: can only concatenate str (not "int") to str
# Fix:
x = int(input("Enter: "))
print(x + 1)           # 43
```

---

## Q6: Multiple inputs in one line
Ask the user to enter three numbers on one line (space-separated) and print their product.

**Solution**
```python
a, b, c = map(int, input("Enter three numbers: ").split())
print("Product =", a * b * c)
# Example input: 2 3 5 → Product = 30
```

---

## Q7: Formatted receipt
Given these values (hardcoded), print a formatted 3-row receipt with columns aligned:

| Item     | Price  |
|----------|--------|
| Rice     |  85.00 |
| Oil      | 150.00 |
| Bread    |  45.50 |

**Solution**
```python
print(f"{'Item':<10} {'Price':>8}")
print("-" * 20)
print(f"{'Rice':<10} {85.00:>8.2f}")
print(f"{'Oil':<10} {150.00:>8.2f}")
print(f"{'Bread':<10} {45.50:>8.2f}")
```

---

## Q8: BDT to USD converter
Ask the user for an amount in BDT, convert it to USD (use rate = 110), and print the result with 2 decimal places.

**Solution**
```python
RATE = 110.0
bdt = float(input("Enter amount in BDT: "))
usd = bdt / RATE
print(f"{bdt:.2f} BDT = {usd:.2f} USD")
```

---

⬅️ Previous: [02-02: Exercises — Variables and Data Types](02-02-variables-and-datatypes-exe.md)
➡️ Next: [02-04: Exercises — Operators](02-04-operators-exe.md)
