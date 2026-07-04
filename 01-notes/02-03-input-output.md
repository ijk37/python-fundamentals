# 02-03: Input and Output

---

## input() Function

input() is used to take input from the user through the keyboard.

- It pauses the program and waits for user input
- Whatever the user types is returned as a string (str)
- Optional message (prompt) can be shown to guide the user

✅ Syntax

```python
input("message to user")
```

✅ Example

```python
name = input("Enter your name: ")
print("Hello", name)
```

👉 Sample run:

```
Enter your name: Imran
Hello Imran
```

💡 Explanation
- The program displays → Enter your name:
- The user types → Imran
- name stores "Imran" (string)
- print() displays the result

⚠️ Important Note

```python
age = input("Enter age: ")
```

- Even if the user enters 25, Python stores it as: "25"   # string, not integer

### 📌 Taking Multiple Inputs

🔹 Simple Way

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
```

👉 Sample run:

```
Enter first number: 10
Enter second number: 20
Sum = 30
```

🔹 Multiple Inputs in One Line

```python
a, b = map(int, input("Enter two numbers: ").split())

print("Sum =", a + b)
```

👉 Sample run:

```
Enter two numbers: 10 20
Sum = 30
```

---

## Type Conversion (Casting)

### 🔹 Why Type Conversion is Needed?

Since input() returns a string, mathematical operations will fail without conversion.

❌ Example (Error)

```python
num = input("Enter a number: ")
print(num + 5)
```

👉 Error because:
- "num" is string
- 5 is integer

```
TypeError: can only concatenate str (not "int") to str
```

✅ Correct Approach

```python
num = int(input("Enter a number: "))
print(num + 5)
```

👉 Sample run:

```
Enter a number: 10
15
```

### 🔹 Common Conversion Functions

| Function | Description            | Example                  |
|----------|------------------------|--------------------------|
| `int()`  | Converts to integer    | `int("10") → 10`         |
| `float()`| Converts to decimal    | `float("3.5") → 3.5`     |
| `str()`  | Converts to string     | `str(100) → "100"`       |

🔹 Float Example

```python
price = float(input("Enter price: "))
print(price * 2)
```

👉 Sample run:

```
Enter price: 49.5
99.0
```

🔹 String Conversion Example

```python
num = 50
text = str(num)
print("Value is " + text)
```

👉 Output:

```
Value is 50
```

---

## print() Function

print() is used to display output on the screen

- It can print text, numbers, variables, and expressions
- It automatically converts values to string when displaying

✅ Basic Usage

```python
print("Hello World")
print(10)
print("Age:", 25)
```

👉 Output:

```
Hello World
10
Age: 25
```

🔹 Printing Multiple Values

```python
name = "Imran"
age = 25

print("Name:", name, "Age:", age)
```

👉 Output:

```
Name: Imran Age: 25
```

### ⚙️ Important Parameters of print()

#### 🔹 1. sep (Separator)

Defines how multiple values are separated

```python
print("A", "B", "C", sep="-")
```

👉 Output:

```
A-B-C
```

#### 🔹 2. end (Ending Character)

Controls what is printed at the end

```python
print("Hello", end=" ")
print("World")
```

👉 Output:

```
Hello World
```

🔹 Default Behavior

```python
print("Hello")
print("World")
```

👉 Output:

```
Hello
World
```

👉 **Because default end = "\n" (new line)**

---

### 📌 Output Formatting

Formatting helps display output in a clear and readable way

#### 🔹 Method 1: Using Comma ,

```python
name = "Imran"
age = 25

print("Name:", name, "Age:", age)
```

👉 Output:

```
Name: Imran Age: 25
```

👉 Simple and beginner-friendly

#### 🔹 Method 2: Using + (Concatenation)

```python
name = "Imran"
print("Hello " + name)
```

👉 Output:

```
Hello Imran
```

⚠️ **Only works with strings**

```python
print("Age: " + str(25))   # must convert number to string
```

👉 Output:

```
Age: 25
```

#### 🔹 Method 3: format() Method

```python
name = "Imran"
age = 25

print("My name is {} and I am {} years old".format(name, age))
```

👉 Output:

```
My name is Imran and I am 25 years old
```

#### 🔹 Method 4: f-Strings (Best ⭐)

Introduced in Python 3.6

```python
name = "Imran"
age = 25

print(f"My name is {name} and I am {age} years old")
```

👉 Output:

```
My name is Imran and I am 25 years old
```

f-strings are powerful, because:
- Clean and readable
- Can include variables + expressions

```python
a = 10
b = 5

print(f"Sum = {a + b}")
```

👉 Output:

```
Sum = 15
```

---

### Formatting Numbers using f-Strings

#### 🔹 Basic Syntax

```python
f"{value:format_specifier}"
```

#### 🔹 1.1 Decimal Precision

Example:

```python
pi = 3.1415926535

print(f"{pi:.2f}")
```

👉 Output:

```
3.14
```

💡 Explanation

.2f → 2 decimal places

f → float

Examples

```python
num = 5

print(f"{num:.2f}")
```

👉 Output:

```
5.00
```

#### 🔹 1.2 Width & Alignment

```python
num = 25

print('*****')
print(f"{num:5}")
```

👉 Output:

```
*****
   25
```

##### Alignment Types

```python
print('*****')
print(f"{25:<5}")  # Left
print(f"{25:>5}")  # Right
print(f"{25:^5}")  # Center
print('*****')
```

👉 Output:

```
*****
25   
   25
 25  
*****
```

#### 🔹 1.3 Zero Padding

```python
num = 7

print(f"{num:05}")
```

👉 Output:

```
00007
```

### 🔹 1.4 Comma Separator

```python
num = 1000000

print(f"{num:,}")
```

👉 Output:

```
1,000,000
```

### 🔹 1.5 Percentage Formatting

```python
value = 0.85

print(f"{value:.2%}")
```

👉 Output:

```
85.00%
```

### 🔹 1.6 Scientific Notation

```python
num = 123456

print(f"{num:.2e}")
```

👉 Output:

```
1.23e+05
```

### 🔹 1.7 Combining Everything

```python
num = 12345.6789

print(f"{num:,.2f}")
```

👉 Output:

```
12,345.68
```

---

## Combined Example (Real Use)

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(f"\n--- User Information ---")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Height : {height:.2f}")
print(f"In 5 years, age will be {age + 5}")
```

👉 Sample run:

```
Enter your name: Imran
Enter your age: 25
Enter your height: 5.9

--- User Information ---
Name   : Imran
Age    : 25
Height : 5.90
In 5 years, age will be 30
```

---

## Quick Summary
- input() → takes input (always string)
- print() → displays output
- sep → controls separator
- end → controls line ending
- int(), float(), str() → type conversion
- f-strings → best for formatting

---

## Practice Problems

```python
# Problem 1
name = input("Enter name: ")
print(f"Welcome {name}")

# Problem 2
num = int(input("Enter a number: "))
print(f"Square = {num * num}")

# Problem 3
a, b = map(int, input("Enter two numbers: ").split())
print(f"Sum = {a + b}, Difference = {a - b}")
```

👉 Sample run:

```
Enter name: Imran
Welcome Imran
Enter a number: 6
Square = 36
Enter two numbers: 10 4
Sum = 14, Difference = 6
```

---
---

> **Exercises:** [02-03: Exercises — Input and Output](../02-exercises/02-03-input-output-exe.md)

---

⬅️ Previous: [02-02: Variables and Data Types](02-02-variables-and-datatypes.md)
➡️ Next: [02-04: Operators](02-04-operators.md)
