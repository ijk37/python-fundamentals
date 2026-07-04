# 01-03: Python Platforms and IDEs

Python can be written and run in many different environments. The right choice depends on the intended workflow — scripting, data science, web development, or quick experimentation.

---

## IDLE — Python's Built-in Editor

**IDLE** (Integrated Development and Learning Environment) ships with every Python installation. It is minimal but requires zero setup.

### Launching IDLE

- **Windows:** Search "IDLE" in Start menu, or run `python -m idlelib` in terminal
- **Mac/Linux:** Run `idle3` in terminal

### Two Modes

| Mode | Description |
|------|-------------|
| **Shell** | Interactive REPL — type and run one line at a time |
| **Editor** | Write and save `.py` files, run with `F5` |

### IDLE Shell (interactive)

```python
>>> 2 + 2
4
>>> name = "Alice"
>>> print(f"Hello, {name}!")
Hello, Alice!
```

### IDLE Editor

1. `File → New File` (or `Ctrl+N`)
2. Write the code
3. `File → Save` (`Ctrl+S`)
4. `Run → Run Module` (`F5`)

### Pros and Cons

| Pros | Cons |
|------|------|
| Comes with Python — no install needed | Very limited features |
| Good for absolute beginners | No extensions/plugins |
| Syntax highlighting | No debugger integration |
| Lightweight | Not used professionally |

**Best for:** Complete beginners running their first Python scripts.

---

## VS Code — Recommended General-Purpose IDE

**Visual Studio Code** is a free, lightweight editor by Microsoft with powerful Python support via extensions. (Covered in detail in notes 01-02 and 01-03.)

### Key Features

- Python extension by Microsoft (IntelliSense, linting, debugging)
- Integrated terminal
- Git integration
- Jupyter notebook support
- Remote development (SSH, containers)
- Huge extension marketplace

```
Extensions to install:
- Python (by Microsoft)       — core support
- Pylance                     — fast type checking
- Jupyter                     — notebook support
- GitLens                     — enhanced git
- Black Formatter / autopep8  — auto-formatting
```

**Best for:** General Python development, scripts, web apps, automation.

---

## PyCharm — Professional Python IDE

**PyCharm** by JetBrains is a full-featured Python IDE. It comes in two editions:

| Edition | Cost | Use Case |
|---------|------|----------|
| **Community** | Free | General Python, scripts |
| **Professional** | Paid (free for students) | Web (Django/Flask), databases, remote dev |

### Key Features

- Deep code intelligence (refactoring, navigation, auto-import)
- Built-in debugger with breakpoints
- Database tools (Professional)
- Django/Flask/FastAPI support (Professional)
- Virtual environment management
- Code inspections and quick-fixes

### Getting Started

1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Open/create a project
3. PyCharm auto-detects or allows configuration of a Python interpreter
4. Run with `Shift+F10`, debug with `Shift+F9`

**Best for:** Large Python projects, professional development teams, Django/Flask web development.

---

## Anaconda — Python for Data Science

**Anaconda** is a Python distribution bundled with 250+ data science packages and tools. It installs Python + NumPy + Pandas + Matplotlib + Jupyter and more in one click.

### What Anaconda Includes

- Python interpreter
- `conda` — package and environment manager
- **Jupyter Notebook** and **JupyterLab**
- Spyder IDE
- Navigator (graphical launcher)
- Pre-installed: NumPy, Pandas, Matplotlib, Scikit-learn, SciPy, etc.

### Install

Download from [anaconda.com](https://www.anaconda.com/) — choose the version matching the OS.

### conda vs pip

| | `pip` | `conda` |
|--|-------|---------|
| Package source | PyPI | Anaconda repository |
| Environment management | `venv` | `conda env` |
| Binary packages | Sometimes problematic | Pre-compiled, reliable |
| Non-Python deps | No | Yes (C libraries, etc.) |

### conda Environments

```bash
# Create a new environment
conda create -n myenv python=3.11

# Activate it
conda activate myenv

# Install packages
conda install numpy pandas matplotlib

# List environments
conda env list

# Deactivate
conda deactivate

# Export environment
conda env export > environment.yml

# Re-create from file
conda env create -f environment.yml
```

**Best for:** Data science, machine learning, scientific computing. Especially good on Windows where binary packages are hard to compile.

---

## Spyder — Scientific Python IDE

**Spyder** comes bundled with Anaconda. It is designed for data science workflows and resembles MATLAB's interface.

### Key Features

- **Variable Explorer** — inspect arrays, dataframes visually
- **IPython console** — interactive with inline plots
- **Editor** with cell-based execution (`# %%` to define cells)
- Debugger and profiler
- Help pane showing docstrings

```python
# In Spyder, use # %% to create "cells"
# %% Section 1
import numpy as np
x = np.linspace(0, 10, 100)

# %% Section 2
import matplotlib.pyplot as plt
plt.plot(x, np.sin(x))
plt.show()
```

Run only a cell with `Ctrl+Enter`, or run the entire file with `F5`.

**Best for:** Scientific computing and data analysis; users coming from MATLAB.

---

## Jupyter Notebook

**Jupyter Notebook** is a browser-based interactive environment that mixes code, output, text (Markdown), equations (LaTeX), and visualizations in a single `.ipynb` file.

### Starting Jupyter

```bash
# After installing (pip or conda)
pip install notebook
jupyter notebook

# Opens browser at http://localhost:8888
```

### Notebook Structure

A notebook is made of **cells**:

| Cell type | Content |
|-----------|---------|
| **Code** | Python code — run with `Shift+Enter` |
| **Markdown** | Text, headings, equations, images |
| **Raw** | Plain text (not rendered) |

### Key Shortcuts

| Shortcut | Action |
|----------|--------|
| `Shift+Enter` | Run cell and move to next |
| `Ctrl+Enter` | Run cell, stay |
| `A` (command mode) | Insert cell above |
| `B` (command mode) | Insert cell below |
| `DD` (command mode) | Delete cell |
| `M` | Change to Markdown |
| `Y` | Change to Code |
| `Esc` | Enter command mode |
| `Enter` | Enter edit mode |

### Magic Commands

```python
# Time a single expression
%timeit sum(range(1000))

# Time a block
%%timeit
total = 0
for i in range(1000):
    total += i

# Run a shell command
!pip install numpy
!ls

# Show matplotlib plots inline
%matplotlib inline

# Load external file into cell
%load script.py

# Run an external file
%run script.py

# Display all variables
%whos
```

### Pros and Cons

| Pros | Cons |
|------|------|
| Great for exploration and storytelling | Not ideal for large production code |
| Inline visualizations | No traditional debugging |
| Share as HTML/PDF | Execution order can cause confusion |
| Reproducible analysis reports | Version control (git) is awkward |

**Best for:** Data analysis, machine learning experiments, teaching, sharing results.

---

## JupyterLab — Next-Gen Jupyter

**JupyterLab** is the modern successor to Jupyter Notebook. Same `.ipynb` format but with a richer interface.

```bash
pip install jupyterlab
jupyter lab
```

### Additional Features over Notebook

- Multiple tabs (notebooks, terminals, editors)
- Drag-and-drop cells
- File browser sidebar
- Extension system
- Better table-of-contents support

**Best for:** Same as Jupyter but with a more complete IDE feel.

---

## Google Colab — Jupyter in the Cloud

**Google Colaboratory** (Colab) runs Jupyter notebooks entirely in the browser with no local setup, backed by Google's servers.

### Access

Go to [colab.research.google.com](https://colab.research.google.com) — free with a Google account.

### Key Features

- **Free GPU/TPU access** — critical for deep learning
- Stored in Google Drive as `.ipynb`
- Pre-installed: TensorFlow, PyTorch, Pandas, Matplotlib, etc.
- Share like a Google Doc
- Mount Google Drive to access files

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Access your files
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/data.csv')

# Install packages
!pip install some-package

# Check GPU availability
import tensorflow as tf
print("GPU:", tf.config.list_physical_devices('GPU'))

# Use magic commands (same as Jupyter)
%matplotlib inline
```

### Colab-Specific Widgets

```python
# File upload
from google.colab import files
uploaded = files.upload()

# File download
files.download('output.csv')
```

### Free vs. Colab Pro

| Feature | Free | Colab Pro |
|---------|------|-----------|
| GPU | T4 (limited) | A100/V100 |
| Session timeout | ~12 hours | Longer |
| RAM | ~12 GB | ~25 GB |
| Background execution | No | Yes |

**Best for:** Deep learning, sharing notebooks publicly, working without local setup, accessing free GPUs.

---

## Kaggle Kernels — Data Science Notebooks

**Kaggle** (owned by Google) offers free Jupyter-like notebooks (called "Kernels" or "Notebooks") with:

- Free GPU and TPU
- Direct access to Kaggle datasets
- Public notebook sharing and competitions

Access at [kaggle.com/code](https://www.kaggle.com/code)

---

## Replit — Browser-Based Coding

**Replit** is an online IDE that runs in the browser — no installation needed.

- [replit.com](https://replit.com)
- Supports 50+ languages including Python
- Collaborative real-time editing
- Hosts web apps directly
- Good for sharing runnable code snippets

---

## AI-Integrated Development Platforms

Modern development increasingly integrates AI directly into the coding workflow:

### GitHub Copilot

- AI pair programmer integrated into VS Code, JetBrains, Neovim
- Autocompletes entire functions based on comments or context
- `Tab` to accept suggestions, `Alt+[` / `Alt+]` to cycle alternatives
- [github.com/features/copilot](https://github.com/features/copilot)

```python
# Just write a comment — Copilot generates the function
# Function to calculate the nth Fibonacci number
def fibonacci(n):
    # Copilot suggests the full body here
```

### Cursor — AI-Native Code Editor

- VS Code fork with deep AI integration
- **Inline editing:** Select code → `Ctrl+K` → describe change in English
- **Chat:** Ask questions about the codebase
- **Agent mode:** Multi-file edits with one instruction
- [cursor.com](https://cursor.com)

### Claude Code (by Anthropic)

- Terminal-based AI coding agent
- Can read, write, and execute code across an entire project
- Understands full codebase context
- Run: `claude` in the terminal
- [claude.ai/code](https://claude.ai/code)

### Windsurf (by Codeium)

- AI-native IDE based on VS Code
- "Cascade" agent for multi-step coding tasks
- Free tier available
- [codeium.com/windsurf](https://codeium.com/windsurf)

### Amazon CodeWhisperer / Q Developer

- AWS's AI code assistant
- Deep integration with AWS services
- Free tier for individual developers

### JetBrains AI Assistant

- Built into all JetBrains IDEs (PyCharm, IntelliJ, etc.)
- Code completion, explanation, refactoring, test generation
- Subscription required

---

## Platform Comparison Summary

| Platform | Type | Best For | Cost |
|----------|------|----------|------|
| **IDLE** | Desktop IDE | Absolute beginners | Free |
| **VS Code** | Desktop IDE | All-purpose development | Free |
| **PyCharm** | Desktop IDE | Professional Python projects | Free/Paid |
| **Spyder** | Desktop IDE | Scientific/data analysis | Free |
| **Anaconda** | Distribution + tools | Data science environment setup | Free/Paid |
| **Jupyter Notebook** | Browser (local) | Exploratory analysis, teaching | Free |
| **JupyterLab** | Browser (local) | Same as Jupyter, richer UI | Free |
| **Google Colab** | Cloud | Free GPU, sharing, no setup | Free/Paid |
| **Kaggle** | Cloud | Data competitions, datasets | Free |
| **Replit** | Cloud | Quick experiments, sharing | Free/Paid |
| **Cursor** | Desktop IDE | AI-assisted development | Free/Paid |
| **GitHub Copilot** | Extension | AI autocomplete in any IDE | Paid |
| **Claude Code** | Terminal agent | Full-project AI coding | Usage-based |

---

## Choosing the Right Tool

```
Just starting out?
└── IDLE (zero setup) OR VS Code (best long-term)

Data science / machine learning?
└── Anaconda + Jupyter Lab / Google Colab (for GPU)

Professional Python development?
└── VS Code + Python extension  OR  PyCharm Community

Want AI assistance?
└── Cursor (free, AI-native) or VS Code + GitHub Copilot

No local install / quick share?
└── Google Colab or Replit

Scientific computing (MATLAB-like)?
└── Spyder (comes with Anaconda)
```

---

⬅️ Previous: [01-02: IDE](01-02-IDE.md)
➡️ Next: [01-04: Environment Setup](01-04-environment-setup.md)
