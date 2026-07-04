# 01-05: Writing and Executing Python Code in VS Code

---

## Part 1: Creating / Opening a Python File

### 🔹 Case 1: Create a New File

#### Step 1: Create file in VS Code

File → New File

👉 Select file type: Python (if prompted)

#### Step 2: Write the code

```python
print("Hello, Python World!")
```

#### Step 3: Save the file

File → Save As

✔ Save with .py extension

Example: 01-first-code.py

---

### 🔹 Case 2: Open an Existing File

#### Way 1:

Right Click file → Open with VS Code

#### Way 2:

In VS Code → File → Open File → Select the .py file from its folder

---

## Part 2: Running a Python File

### 🔹 Method 1: Using Terminal

#### Step 1: Open terminal

Terminal → New Terminal

#### Step 2: Go to file directory

```bash
cd <file_directory>
```

Example:

```bash
cd C:\Users\jahid\github-projects\python-fundamentals\02-exercises
```

#### Step 3: Run the file

```bash
python filename.py
```

OR (recommended on Windows):

```bash
py filename.py
```

Example:

```bash
py 01-first-code.py
```

👉 Output:

```
Hello, Python World!
```

![run_python_code](image-1.png)

### 🔹 Method 2: Using Run Button

#### Way 1:

Click the ▶️ Run button (top right)

#### Way 2:

Right Click on the code file → Run Python → Run Python File in Terminal

---

### ⚠️ Important Notes

In VS Code Terminal, Run from correct directory:

```bash
cd <folder_where_file_exists>
```

---

⬅️ Previous: [01-04: Environment Setup](01-04-environment-setup.md)
➡️ Next: [02-01: Basic Syntax](02-01-basic-syntax.md)
