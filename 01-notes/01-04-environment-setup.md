# 01-04: Environment Setup

---

## Install Python 3

### Option 1: Manual

Step 1: Go to official Python website: https://www.python.org/downloads/

Step 2: Download the latest version of Python 

![install-python](image.png)

👉 Download:
- Python 3.x.x (recommended)

Or,

- Python Install Manager (optional)

Step 3: Install Python

IMPORTANT:
✔ Check "Add Python to PATH" before clicking Install

---

### Option 2: In PowerShell (Windows) / Terminal

Step 1: Search available Python versions

```bash
winget search Python
```

Step 2: Install using exact version from search result

```bash
winget install Python.Python.<version found in Step 1>
```

---

### ✅ Verify Installation (in PowerShell/Terminal)

```bash
python --version
```

If not working:

```bash
py --version
```

---

### 📚 Install Libraries (in PowerShell/Terminal)

General command:

```bash
pip install <library_name>
```

Examples:

```bash
pip install numpy        # numerical computing
pip install pandas       # data analysis and handling
pip install matplotlib   # data visualization
```

Optional (for Reinforcement Learning):

```bash
pip install gymnasium    # RL environments (e.g., CartPole)
```

---

### 💻 Install VS Code

Step 1: Download: https://code.visualstudio.com/

Step 2: Install

During installation:

✔ Add to PATH

✔ Add "Open with Code"

---

### 🔌 Install Python Extension in VS Code

Open VS Code → Extensions → Search: Python

Install: Python (by Microsoft)

NOTE: Python extension does NOT install Python

---

⬅️ Previous: [01-03: Python Platforms and IDEs](01-03-python-platforms-and-ides.md)
➡️ Next: [01-05: Writing and Executing Python Code in VS Code](01-05-write-execute-python-code-in-vscode.md)
