# 02-04: Operators

Operators are symbols or keywords used to perform operations on values and variables.

```python
a = 10
b = 5
print(a + b)   # 15
```

Here, `+` is an operator.

---

## Types of Operators in Python

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators

---

### 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning             | Example       | Result |
|----------|---------------------|---------------|--------|
| `+`      | Addition            | `5 + 2`       | `7`    |
| `-`      | Subtraction         | `5 - 2`       | `3`    |
| `*`      | Multiplication      | `5 * 2`       | `10`   |
| `/`      | Division            | `5 / 2`       | `2.5`  |
| `//`     | Floor Division      | `5 // 2`      | `2`    |
| `%`      | Modulus (remainder) | `5 % 2`       | `1`    |
| `**`     | Exponent (power)    | `5 ** 2`      | `25`   |

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

### 2. Assignment Operators

Used to assign values to variables.

| Operator | Example    | Equivalent to  |
|----------|------------|----------------|
| `=`      | `x = 5`    | assign 5 to x  |
| `+=`     | `x += 3`   | `x = x + 3`    |
| `-=`     | `x -= 3`   | `x = x - 3`    |
| `*=`     | `x *= 3`   | `x = x * 3`    |
| `/=`     | `x /= 3`   | `x = x / 3`    |
| `//=`    | `x //= 3`  | `x = x // 3`   |
| `%=`     | `x %= 3`   | `x = x % 3`    |
| `**=`    | `x **= 3`  | `x = x ** 3`   |

```python
x = 10
x += 5
print(x)   # 15

x *= 2
print(x)   # 30

x -= 4
print(x)   # 26
```

---

### 3. Comparison Operators

Compare two values and return `True` or `False`.

| Operator | Meaning                  | Example      | Result  |
|----------|--------------------------|--------------|---------|
| `==`     | Equal to                 | `5 == 5`     | `True`  |
| `!=`     | Not equal to             | `5 != 3`     | `True`  |
| `>`      | Greater than             | `5 > 3`      | `True`  |
| `<`      | Less than                | `5 < 3`      | `False` |
| `>=`     | Greater than or equal to | `5 >= 5`     | `True`  |
| `<=`     | Less than or equal to    | `5 <= 2`     | `False` |

```python
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a > b)    # False
print(a <= 10)  # True
print(b >= 15)  # True
```

---

### 4. Logical Operators

Combine multiple conditions.

| Operator | Meaning                            | Example            | Result  |
|----------|------------------------------------|--------------------|---------|
| `and`    | `True` if **both** are `True`      | `5 > 3 and 2 < 4`  | `True`  |
| `or`     | `True` if **at least one** is `True` | `5 > 3 or 2 > 4` | `True`  |
| `not`    | Reverses the result                | `not(5 > 3)`       | `False` |

```python
a = 10
b = 5

print(a > 5 and b < 10)   # True  — both conditions true
print(a < 5 or b < 10)    # True  — second condition true
print(not(a > 5))         # False — reverses True
```

---

### 5. Bitwise Operators

Operate on the binary (bit-level) representation of integers.

| Operator | Meaning      | Example    | Result |
|----------|--------------|------------|--------|
| `&`      | AND          | `5 & 3`    | `1`    |
| `\|`     | OR           | `5 \| 3`   | `7`    |
| `^`      | XOR          | `5 ^ 3`    | `6`    |
| `~`      | NOT          | `~5`       | `-6`   |
| `<<`     | Left shift   | `5 << 1`   | `10`   |
| `>>`     | Right shift  | `5 >> 1`   | `2`    |

```python
a = 5   # binary: 0101
b = 3   # binary: 0011

print(a & b)   # 1   (0001)
print(a | b)   # 7   (0111)
print(a ^ b)   # 6   (0110)
print(a << 1)  # 10  (1010)
print(a >> 1)  # 2   (0010)
```

<details>
<summary>💡 How does binary work? (click to expand)</summary>

Every integer is stored in memory as a sequence of bits (0s and 1s). Bitwise operators manipulate those bits directly.

**Example: `5 & 3`**

```
5  →  0 1 0 1
3  →  0 0 1 1
        -------
&  →  0 0 0 1  =  1
```

`&` (AND) keeps a bit only if **both** sides have a `1`.

**Example: `5 | 3`**

```
5  →  0 1 0 1
3  →  0 0 1 1
        -------
|  →  0 1 1 1  =  7
```

`|` (OR) keeps a bit if **either** side has a `1`.

**Example: `5 ^ 3`**

```
5  →  0 1 0 1
3  →  0 0 1 1
        -------
^  →  0 1 1 0  =  6
```

`^` (XOR) keeps a bit only if the two sides **differ**.

**Shift operators** move all bits left or right:

```python
5 << 1   # 0101 → 1010 = 10  (multiply by 2)
5 >> 1   # 0101 → 0010 = 2   (divide by 2)
```

> Bitwise operators are rarely needed in everyday Python. They appear in low-level programming, networking (IP masks), flags, and performance-critical code.

</details>

---

### 6. Membership Operators

Check whether a value exists in a sequence (list, tuple, string, etc.).

| Operator | Meaning              | Example          | Result |
|----------|----------------------|------------------|--------|
| `in`     | Value exists         | `2 in [1,2,3]`   | `True` |
| `not in` | Value does not exist | `7 not in [1,2]` | `True` |

```python
nums = [1, 2, 3, 4]

print(2 in nums)       # True
print(7 in nums)       # False
print(7 not in nums)   # True

text = "python"
print("py" in text)        # True
print("java" not in text)  # True
```

---

### 7. Identity Operators

Check whether two variables refer to the **same object in memory** (not just equal values).

| Operator | Meaning         |
|----------|-----------------|
| `is`     | Same object     |
| `is not` | Not same object |

```python
a = [1, 2, 3]
b = a            # b points to the same object as a
c = [1, 2, 3]   # c is a separate object with same values

print(a is b)    # True  — same object
print(a is c)    # False — different objects, same values
print(a == c)    # True  — values are equal
```

> **Key distinction:** `==` checks whether values are equal. `is` checks whether they are the same object in memory.

---

## Operator Precedence

Precedence determines which operator is evaluated first in an expression.

```python
print(2 + 3 * 4)   # 14, not 20
```

Python evaluates `3 * 4` first because `*` has higher precedence than `+`.

### Precedence Table (highest → lowest)

| Priority | Operators                                          |
|----------|----------------------------------------------------|
| Highest  | `()` — parentheses                                 |
|          | `**` — exponent                                    |
|          | `+x`, `-x`, `~x` — unary                          |
|          | `*`, `/`, `//`, `%`                                |
|          | `+`, `-`                                           |
|          | `<<`, `>>`                                         |
|          | `&`                                                |
|          | `^`                                                |
|          | `\|`                                               |
|          | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `not in`  |
|          | `not`                                              |
|          | `and`                                              |
| Lowest   | `or`                                               |

---

## Associativity

When two operators have the **same precedence**, associativity decides the evaluation order.

### Left-to-right (most operators)

```python
print(10 - 3 - 2)   # (10 - 3) - 2 = 5
print(20 / 5 * 2)   # (20 / 5) * 2 = 8.0
```

### Right-to-left (`**` only)

```python
print(2 ** 3 ** 2)   # 2 ** (3 ** 2) = 2 ** 9 = 512
```

---

## Comparison Chaining

Python allows chaining comparisons naturally:

```python
x = 5
print(1 < x < 10)    # True  — equivalent to: 1 < x and x < 10
print(10 > 5 > 2)    # True
print(10 > 5 < 2)    # False
```

---

## Common Beginner Mistakes

### Mistake 1: `=` vs `==`

```python
x = 5    # assignment — stores the value
x == 5   # comparison — returns True or False
```

### Mistake 2: `is` vs `==`

```python
a = [1, 2]
b = [1, 2]

print(a == b)   # True  — same values
print(a is b)   # False — different objects in memory
```

### Mistake 3: Forgetting precedence

```python
print(2 + 3 * 4)     # 14  (not 20)
print((2 + 3) * 4)   # 20  — use parentheses to be explicit
```

---

## Worked Examples

```python
a = 10
b = 3
c = 2

print(a + b * c)           # 16   — b*c first, then +a
print((a + b) * c)         # 26   — parentheses override precedence
print(a > b and b > c)     # True
print(a == 10 or b == 5)   # True
print(not(a < b))          # True
print(2 ** 3 ** 2)         # 512  — right-to-left: 2**(3**2)
```

---

## Key Takeaways

| Concept | Summary |
|---------|---------|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` for math |
| Assignment | `=`, `+=`, `-=`, `*=`, etc. to assign/update |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` — return `True`/`False` |
| Logical | `and`, `or`, `not` — combine conditions |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` — bit-level ops |
| Membership | `in`, `not in` — check presence in a sequence |
| Identity | `is`, `is not` — check if same object in memory |
| Precedence | `**` > `*/%` > `+-` > comparisons > `not` > `and` > `or` |
| Associativity | Most left-to-right; `**` is right-to-left |

---

> **Exercises:** [02-04: Exercises — Operators](../02-exercises/02-04-operators-exe.md)

---

⬅️ Previous: [02-03: Input and Output](02-03-input-output.md)
➡️ Next: [02-05: Number Types — int and float](02-05-number-types-int-float.md)
