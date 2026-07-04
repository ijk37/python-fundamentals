# 03-03: Exercises — while Loops

> **Notes reference:** [03-03: while Loops](../01-notes/03-03-while-loops.md)

---

## Q1: Basic while loop
Print the numbers 1 through 8 using a while loop.

**Solution**
```python
i = 1
while i <= 8:
    print(i)
    i += 1
```

---

## Q2: Sum until threshold
Add positive integers starting from 1 until the running total exceeds 50. Print the total and the last number added.

**Solution**
```python
total = 0
n     = 1
while total <= 50:
    total += n
    n     += 1
print(f"Total: {total}, last number added: {n - 1}")
# Total: 55, last number added: 10
```

---

## Q3: Validated input
Keep asking the user for an age until they enter a valid integer between 1 and 120.

**Solution**
```python
age = -1
while not (1 <= age <= 120):
    try:
        age = int(input("Enter your age (1-120): "))
    except ValueError:
        print("Please enter a valid integer.")
print(f"Age recorded: {age}")
```

---

## Q4: break — find first divisor
Find the smallest divisor of 91 greater than 1.

**Solution**
```python
n = 91
i = 2
while i <= n:
    if n % i == 0:
        print(f"Smallest divisor of {n}: {i}")
        break
    i += 1
# Smallest divisor of 91: 7
```

---

## Q5: continue — skip negatives
Given `data = [3, -1, 7, -4, 0, 5, -2, 8]`, print only the positive values using a while loop.

**Solution**
```python
data = [3, -1, 7, -4, 0, 5, -2, 8]
i    = 0
while i < len(data):
    if data[i] <= 0:
        i += 1
        continue
    print(data[i])
    i += 1
# 3 7 5 8
```

---

## Q6: while/else
Check whether a number is prime using a while loop with an `else` clause.

**Solution**
```python
n = int(input("Enter a number: "))
i = 2
while i * i <= n:
    if n % i == 0:
        print(f"{n} is NOT prime (divisible by {i})")
        break
    i += 1
else:
    print(f"{n} is prime")
```

---

## Q7: Do-while simulation
Ask the user to enter a password. Keep asking until they enter `"secure123"`. Print how many attempts it took.

**Solution**
```python
attempts = 0
while True:
    password = input("Enter password: ")
    attempts += 1
    if password == "secure123":
        print(f"Access granted after {attempts} attempt(s).")
        break
    print("Wrong password, try again.")
```

---

## Q8: for vs while — when to choose
Rewrite the following `for` loop as a `while` loop:

```python
for i in range(0, 20, 3):
    print(i)
```

**Solution**
```python
i = 0
while i < 20:
    print(i)
    i += 3
```

The `for` loop is preferred when the number of iterations is known. The `while` loop is preferred when iteration depends on a condition that changes unpredictably.

---

⬅️ Previous: [03-02: Exercises — for Loops](03-02-for-loops-exe.md)
➡️ Next: [04-01: Exercises — Functions](04-01-functions-basics-exe.md)
