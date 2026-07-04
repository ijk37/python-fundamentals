# 08-03: Python Ecosystem — Common Libraries Overview

Python's strength comes not just from the language itself but from its massive ecosystem of libraries. This note gives a high-level map of the most important ones — what they do, when to use them, and how to install them.

---

## Standard Library — No Installation Needed

These ship with every Python installation:

| Module | Purpose | Key Features |
|--------|---------|-------------|
| `os` | OS interface | Files, dirs, env vars, process |
| `sys` | Python runtime | argv, path, exit, version |
| `pathlib` | File paths | OO path handling |
| `math` | Math functions | sqrt, log, trig, constants |
| `random` | Random numbers | randint, choice, shuffle |
| `datetime` | Dates and times | date, time, datetime, timedelta |
| `time` | Timing | sleep, perf_counter |
| `re` | Regular expressions | Pattern matching in strings |
| `json` | JSON I/O | load, dump, loads, dumps |
| `csv` | CSV I/O | reader, writer, DictReader |
| `collections` | Specialized containers | Counter, defaultdict, deque, namedtuple |
| `itertools` | Iterator tools | chain, combinations, product |
| `functools` | Function tools | reduce, partial, lru_cache |
| `typing` | Type hints | List, Dict, Optional, Union |
| `abc` | Abstract classes | ABC, abstractmethod |
| `copy` | Copy objects | copy (shallow), deepcopy |
| `io` | I/O streams | StringIO, BytesIO |
| `urllib` | HTTP requests | urlopen |
| `hashlib` | Cryptographic hashing | md5, sha256 |
| `argparse` | CLI argument parsing | ArgumentParser |
| `logging` | Application logging | basicConfig, getLogger |
| `unittest` | Testing | TestCase, assertEqual |
| `threading` | Multi-threading | Thread, Lock |
| `multiprocessing` | Multi-processing | Process, Pool |
| `subprocess` | Run shell commands | run, Popen |
| `sqlite3` | SQLite database | connect, cursor, execute |
| `zipfile` | ZIP archives | ZipFile, extract |
| `shutil` | High-level file ops | copy, move, rmtree |
| `tempfile` | Temporary files | TemporaryFile, mkdtemp |
| `pickle` | Python object serialization | dump, load |
| `struct` | Binary data | pack, unpack |

---

## Data Science and Machine Learning

### NumPy — Numerical Computing

```python
pip install numpy
import numpy as np
```

- N-dimensional array (`ndarray`)
- Vectorized math — fast element-wise operations
- Linear algebra, statistics, Fourier transforms
- Foundation for almost all scientific Python

**Use when:** Any numeric computation with arrays, linear algebra.

---

### Pandas — Data Manipulation

```python
pip install pandas
import pandas as pd
```

- `DataFrame` — labeled 2D table (like Excel or SQL)
- `Series` — labeled 1D array
- Read/write CSV, Excel, SQL, JSON
- Filtering, grouping, merging, reshaping data
- Time series analysis

**Use when:** Loading, cleaning, exploring, and transforming tabular data.

```python
df = pd.read_csv("data.csv")
df.head()
df.groupby("city")["score"].mean()
```

---

### Matplotlib — Visualization

```python
pip install matplotlib
import matplotlib.pyplot as plt
```

- Line, bar, scatter, histogram, pie, heatmap charts
- Full control over every visual element
- Save to PNG, PDF, SVG

**Use when:** Creating any kind of plot or chart.

```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("My Chart")
plt.show()
```

---

### Seaborn — Statistical Visualization

```python
pip install seaborn
import seaborn as sns
```

- Built on Matplotlib — higher-level, beautiful defaults
- Statistical plots: box, violin, pair plots, heatmaps
- Works directly with Pandas DataFrames

**Use when:** Attractive statistical charts are needed with minimal code.

```python
sns.boxplot(data=df, x="city", y="score")
```

---

### Scikit-learn — Machine Learning

```python
pip install scikit-learn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
```

- Classification, regression, clustering, dimensionality reduction
- Preprocessing, pipelines, cross-validation
- Consistent `.fit()` / `.predict()` API
- Great for classical ML (not deep learning)

**Use when:** Training ML models, preprocessing data, evaluating models.

---

### TensorFlow and PyTorch — Deep Learning

```python
pip install tensorflow     # Google's framework
pip install torch          # Meta's framework (PyTorch)
```

- Neural networks, GPU acceleration
- TensorFlow: production-oriented, TensorFlow Serving
- PyTorch: research-friendly, dynamic graphs, more Pythonic
- Both support CNNs, RNNs, Transformers

**Use when:** Deep learning — image recognition, NLP, generative models.

---

### SciPy — Scientific Computing

```python
pip install scipy
import scipy
```

- Optimization, integration, interpolation
- Signal processing, statistics
- Linear algebra beyond NumPy
- Built on top of NumPy

**Use when:** Advanced scientific and engineering computations.

---

## Web Development

### Flask — Micro Web Framework

```python
pip install flask
from flask import Flask, request, jsonify
```

- Lightweight, minimal setup
- Build REST APIs, simple web apps
- Easy to learn, no boilerplate

```python
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"
```

---

### FastAPI — Modern API Framework

```python
pip install fastapi uvicorn
```

- Auto-generates API docs (Swagger UI)
- Type-based validation with Pydantic
- Async support (`async/await`)
- Best performance among Python web frameworks

---

### Django — Full-Stack Web Framework

```python
pip install django
```

- "Batteries included" — ORM, auth, admin, templates
- Large applications, content sites
- Mature ecosystem

---

### Requests — HTTP Client

```python
pip install requests
import requests
```

- Make HTTP requests to APIs and websites
- Handles headers, cookies, sessions, auth
- Much easier than urllib

```python
response = requests.get("https://api.example.com/data")
data = response.json()
```

---

## Database

| Library | DB | Use |
|---------|----|----|
| `sqlite3` (built-in) | SQLite | Lightweight local DB |
| `psycopg2` | PostgreSQL | pip install psycopg2 |
| `mysql-connector` | MySQL | pip install mysql-connector-python |
| `SQLAlchemy` | Any SQL DB | ORM + raw SQL, pip install sqlalchemy |
| `pymongo` | MongoDB | pip install pymongo |
| `redis-py` | Redis | pip install redis |

---

## File Handling

| Library | Purpose |
|---------|---------|
| `csv` (built-in) | CSV files |
| `json` (built-in) | JSON files |
| `openpyxl` | Excel `.xlsx` read/write |
| `xlrd` | Excel `.xls` read |
| `pypdf` | PDF read/merge/split |
| `reportlab` | Create PDFs |
| `pdfplumber` | Extract text/tables from PDF |
| `python-docx` | Word `.docx` files |
| `Pillow (PIL)` | Image processing |
| `zipfile` (built-in) | ZIP archives |

---

## Automation and Scripting

| Library | Purpose |
|---------|---------|
| `subprocess` (built-in) | Run shell commands |
| `schedule` | Cron-like task scheduling |
| `pyautogui` | Mouse/keyboard automation |
| `selenium` | Browser automation |
| `playwright` | Modern browser automation |
| `beautifulsoup4` | HTML/XML parsing (web scraping) |
| `scrapy` | Web scraping framework |
| `paramiko` | SSH connections |
| `watchdog` | Watch file system changes |

---

## Utilities

| Library | Purpose |
|---------|---------|
| `tqdm` | Progress bars |
| `rich` | Beautiful terminal output |
| `click` | CLI application framework |
| `pydantic` | Data validation with type hints |
| `arrow` | Friendly datetime handling |
| `dotenv` | Load `.env` environment variables |
| `loguru` | Better logging |
| `pytest` | Testing framework |
| `black` | Code formatter |
| `mypy` | Static type checker |

---

## Quick Install Reference

```bash
# Data science stack
pip install numpy pandas matplotlib seaborn scikit-learn

# Web development
pip install flask fastapi uvicorn requests

# Database
pip install sqlalchemy psycopg2

# File handling
pip install openpyxl pypdf reportlab python-docx Pillow

# Utilities
pip install tqdm rich click pydantic python-dotenv loguru pytest

# Deep learning (choose one)
pip install tensorflow
pip install torch torchvision

# Install everything at once from a file
pip install -r requirements.txt
```

---

## Which Libraries to Learn First

```
Step 1 — Core data science (this course's focus)
  numpy → pandas → matplotlib → seaborn

Step 2 — Machine learning
  scikit-learn → (tensorflow OR pytorch)

Step 3 — Web/API
  requests → flask OR fastapi

Step 4 — Based on the domain:
  Data engineering  → sqlalchemy, airflow
  Web scraping      → beautifulsoup4, selenium
  Automation        → pyautogui, subprocess
  CLI tools         → click, rich
  Finance           → yfinance, zipline
  NLP               → nltk, spacy, transformers (HuggingFace)
  Computer vision   → opencv-python, Pillow
```

---

## Checking Installed Packages

```python
import pkg_resources

# List all installed packages
for pkg in sorted(pkg_resources.working_set, key=lambda x: x.key):
    print(f"{pkg.key}=={pkg.version}")

# Check if a specific package is installed
try:
    import numpy
    print(f"numpy {numpy.__version__} is installed")
except ImportError:
    print("numpy is NOT installed — run: pip install numpy")
```

---

⬅️ Previous: [08-02: Module Structure — `__name__` and `__main__`](08-02-module-structure.md)
📚 [Notes Index](README.md)
