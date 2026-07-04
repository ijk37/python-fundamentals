# 03-01: Exercises — Conditional Statements

> **Notes reference:** [03-01: Conditional Statements — if, elif, else](../01-notes/03-01-if-elif-else.md)

---

## Q1: Simple if
Ask the user for a number. Print `"Positive"` if it is greater than 0.

**Solution**
```python
n = float(input("Enter a number: "))
if n > 0:
    print("Positive")
```

---

## Q2: if/else — even or odd
Print whether a given integer is even or odd.

**Solution**
```python
n = int(input("Enter an integer: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Q3: if/elif/else — letter grade
Map a score (0–100) to a letter grade: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, F below 60.

**Solution**
```python
score = int(input("Enter score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")
```

---

## Q4: Nested if — eligibility check
A person can apply for a job if they are 18–60 years old AND have at least 2 years of experience.

**Solution**
```python
age        = int(input("Enter age: "))
experience = int(input("Years of experience: "))

if 18 <= age <= 60:
    if experience >= 2:
        print("Eligible to apply")
    else:
        print("Need more experience")
else:
    print("Age out of range")

# Equivalent using and:
if 18 <= age <= 60 and experience >= 2:
    print("Eligible")
else:
    print("Not eligible")
```

---

## Q5: Ternary expression
Print `"Weekend"` if the day is `"Saturday"` or `"Sunday"`, otherwise `"Weekday"` — in one line.

**Solution**
```python
day    = input("Enter day: ")
status = "Weekend" if day in ("Saturday", "Sunday") else "Weekday"
print(status)
```

---

## Q6: Multiple conditions — season
Given a month number (1–12), print the season: Dec–Feb → Winter, Mar–May → Spring, Jun–Aug → Summer, Sep–Nov → Autumn.

**Solution**
```python
month = int(input("Enter month (1-12): "))
if month in (12, 1, 2):
    season = "Winter"
elif month in (3, 4, 5):
    season = "Spring"
elif month in (6, 7, 8):
    season = "Summer"
elif month in (9, 10, 11):
    season = "Autumn"
else:
    season = "Invalid month"
print(season)
```

---

## Q7: FizzBuzz
Print numbers 1–20. For multiples of 3 print `"Fizz"`, for multiples of 5 print `"Buzz"`, for multiples of both print `"FizzBuzz"`.

**Solution**
```python
for n in range(1, 21):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```

---

## Q8: Shipping cost calculator
Shipping cost depends on weight (kg):
- up to 1 kg → $5
- 1–5 kg → $10
- 5–20 kg → $20
- over 20 kg → $50

**Solution**
```python
weight = float(input("Enter weight in kg: "))
if weight <= 1:
    cost = 5
elif weight <= 5:
    cost = 10
elif weight <= 20:
    cost = 20
else:
    cost = 50
print(f"Shipping cost: ${cost}")
```

---

⬅️ Previous: [02-10: Exercises — Type Conversion](02-10-type-conversion-exe.md)
➡️ Next: [03-02: Exercises — for Loops](03-02-for-loops-exe.md)
