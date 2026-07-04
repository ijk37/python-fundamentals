// ============================================================================
//  Python — Fundamentals · Quiz Data
//  data.js       →  TOPICS list, QUIZ_CONFIG, and Chapter 01 questions
//  data-02.js … data-08.js  →  one file per chapter (02–08)
//  data-mixed-1.js … -5.js  →  5 cumulative mixed quizzes
// ============================================================================

const TOPICS = [
  { id: "01", title: "Setup & Environment" },
  { id: "02", title: "Core Language" },
  { id: "03", title: "Control Flow" },
  { id: "04", title: "Functions" },
  { id: "05", title: "Data Structures" },
  { id: "06", title: "Comprehensions & Exceptions" },
  { id: "07", title: "File I/O" },
  { id: "08", title: "Modules & Packages" },
  { id: "mixed-1", title: "Final Mixed Quiz 1" },
  { id: "mixed-2", title: "Final Mixed Quiz 2" },
  { id: "mixed-3", title: "Final Mixed Quiz 3" },
  { id: "mixed-4", title: "Final Mixed Quiz 4" },
  { id: "mixed-5", title: "Final Mixed Quiz 5" },
];

// ── Quiz sizing ─────────────────────────────────────────────────────────────
// Each attempt draws a RANDOM subset of this many questions from the topic
// pool (re-picked on every retry). If a pool is smaller than the configured
// size, the whole pool is used. Override per attempt with a ?n= URL parameter.
const QUIZ_CONFIG = {
  defaultAttempt: 20,        // random questions per attempt for chapter quizzes
  attempt: {                 // per-topic overrides
    "01": 10,                // Chapter 01 draws 10 (smaller ~30-question bank)
    "mixed-1": 50,
    "mixed-2": 50,
    "mixed-3": 50,
    "mixed-4": 50,
    "mixed-5": 50,
  },
};

// How many questions a given topic shows per attempt (capped at pool size).
function attemptSizeFor(topicId, poolLen) {
  const cfg = (QUIZ_CONFIG.attempt && QUIZ_CONFIG.attempt[topicId]) || QUIZ_CONFIG.defaultAttempt;
  return Math.min(cfg, poolLen);
}

const QUESTIONS = {};

// ── Chapter 01 — Setup & Environment ────────────────────────────────────────
QUESTIONS["01"] = [
  {
    q: "What kind of programming language is Python?",
    options: [
      "A low-level assembly language",
      "A high-level, interpreted, general-purpose language",
      "A markup language like HTML",
      "A compiled-only systems language",
    ],
    answer: 1,
    explain: "Python is a high-level, interpreted, general-purpose language. Its readable syntax and huge standard library make it popular for web, data science, automation, and scripting.",
  },
  {
    q: "Why is Python described as 'dynamically typed'?",
    options: [
      "You must declare the type of every variable",
      "Variable types are checked and can change at run time, without explicit type declarations",
      "It can only store numbers",
      "Types are fixed at compile time",
    ],
    answer: 1,
    explain: "In a dynamically typed language you don't declare types; a name simply refers to an object, and it can be reassigned to an object of a different type at run time.",
  },
  {
    q: "Which statement about Python execution is correct?",
    options: [
      "Python source must be compiled to a standalone .exe before running",
      "The Python interpreter reads and executes source code (via bytecode) at run time",
      "Python runs directly as machine code with no interpreter",
      "Python cannot run scripts, only interactive commands",
    ],
    answer: 1,
    explain: "CPython compiles source to bytecode and the interpreter executes that bytecode. You run a program simply by passing the .py file to the interpreter — no separate manual compile step.",
  },
  {
    q: "What does IDE stand for?",
    options: [
      "Integrated Development Environment",
      "Internal Data Engine",
      "Interpreted Debugging Executable",
      "Interface Design Editor",
    ],
    answer: 0,
    explain: "An IDE (Integrated Development Environment) bundles an editor, run/debug tools, and often linting and version-control integration into one application.",
  },
  {
    q: "Which of these is an IDE / code editor commonly used for Python?",
    options: ["Microsoft Excel", "VS Code", "Adobe Photoshop", "Windows Notepad only"],
    answer: 1,
    explain: "VS Code is a popular, free, extensible editor for Python. Other common choices include PyCharm, Jupyter, and online environments like Google Colab and Replit.",
  },
  {
    q: "What is Jupyter Notebook best known for?",
    options: [
      "Compiling C++ programs",
      "Running code in cells mixed with text and visual output, great for data science",
      "Editing images",
      "Managing databases only",
    ],
    answer: 1,
    explain: "Jupyter lets you run code in individual cells and interleave Markdown notes and rich output (tables, plots). It's widely used for data exploration and teaching.",
  },
  {
    q: "Which command typically checks the installed Python version from a terminal?",
    options: ["python --version", "python show version", "get python version", "py.version()"],
    answer: 0,
    explain: "`python --version` (or `python -V`, and on Windows often `py --version`) prints the interpreter version so you can confirm your installation.",
  },
  {
    q: "What is `pip`?",
    options: [
      "A text editor for Python",
      "Python's package installer for adding third-party libraries",
      "The Python interpreter itself",
      "A type of variable",
    ],
    answer: 1,
    explain: "pip is the standard package manager for Python. `pip install <package>` downloads and installs libraries from the Python Package Index (PyPI).",
  },
  {
    q: "Which command installs the 'requests' library with pip?",
    options: ["pip get requests", "pip install requests", "python requests install", "install requests.py"],
    answer: 1,
    explain: "`pip install requests` fetches the package from PyPI and installs it into the active environment.",
  },
  {
    q: "What is the main purpose of a virtual environment (venv)?",
    options: [
      "To make Python run faster",
      "To isolate a project's dependencies from other projects and the system Python",
      "To encrypt your source code",
      "To convert Python to machine code",
    ],
    answer: 1,
    explain: "A virtual environment gives a project its own isolated set of installed packages, so different projects can use different versions without conflicting.",
  },
  {
    q: "Which command creates a virtual environment named 'venv'?",
    options: ["python -m venv venv", "pip venv venv", "python create venv", "venv --new venv"],
    answer: 0,
    explain: "`python -m venv venv` runs the built-in venv module to create an isolated environment in a folder called 'venv'.",
  },
  {
    q: "After creating a venv on Windows, how do you typically activate it?",
    options: [
      "venv\\Scripts\\activate",
      "activate venv now",
      "python venv on",
      "source venv/bin/activate (this is the Windows command)",
    ],
    answer: 0,
    explain: "On Windows you activate with `venv\\Scripts\\activate`. On macOS/Linux it's `source venv/bin/activate`. Once active, `python` and `pip` refer to the environment.",
  },
  {
    q: "What is the conventional file extension for a Python script?",
    options: [".py", ".python", ".pt", ".pyt"],
    answer: 0,
    explain: "Python source files use the `.py` extension. Jupyter notebooks use `.ipynb`.",
  },
  {
    q: "How do you run a script named app.py from the terminal?",
    options: ["run app.py", "python app.py", "app.py run", "execute app"],
    answer: 1,
    explain: "`python app.py` (or `py app.py` on Windows) passes the file to the interpreter, which executes it top to bottom.",
  },
  {
    q: "What does the Python REPL let you do?",
    options: [
      "Only edit files",
      "Type expressions and statements interactively and see results immediately",
      "Compile programs to C",
      "Design graphical user interfaces visually",
    ],
    answer: 1,
    explain: "REPL = Read–Eval–Print Loop. Launched by typing `python`, it evaluates each line you type and prints the result — ideal for quick experiments.",
  },
  {
    q: "Which extension should you install in VS Code for the best Python experience?",
    options: [
      "The official Python extension (by Microsoft)",
      "A Java extension",
      "The C# extension",
      "No extension is possible in VS Code",
    ],
    answer: 0,
    explain: "Microsoft's Python extension adds IntelliSense, linting, debugging, environment selection, and notebook support to VS Code.",
  },
  {
    q: "In VS Code, what does the 'Select Interpreter' command control?",
    options: [
      "The color theme",
      "Which Python installation or virtual environment runs your code",
      "The font size",
      "The keyboard layout",
    ],
    answer: 1,
    explain: "'Python: Select Interpreter' chooses which interpreter/venv VS Code uses to run and debug, so you can point a project at its own environment.",
  },
  {
    q: "What is PyPI?",
    options: [
      "A Python IDE",
      "The Python Package Index — the online repository pip installs packages from",
      "A Python version number",
      "A type of loop",
    ],
    answer: 1,
    explain: "PyPI (the Python Package Index, pypi.org) hosts hundreds of thousands of third-party packages that pip can download and install.",
  },
  {
    q: "Which command lists the packages installed in the current environment?",
    options: ["pip list", "pip all", "python packages", "pip show all"],
    answer: 0,
    explain: "`pip list` prints installed packages and versions. `pip freeze` gives the same in requirements-file format.",
  },
  {
    q: "What is a common purpose of a requirements.txt file?",
    options: [
      "To store your program's output",
      "To record the project's package dependencies so they can be reinstalled with pip",
      "To hold user passwords",
      "To configure the operating system",
    ],
    answer: 1,
    explain: "requirements.txt lists dependencies (often produced by `pip freeze`). `pip install -r requirements.txt` recreates the same environment elsewhere.",
  },
  {
    q: "Why is indentation significant in Python?",
    options: [
      "It is purely cosmetic and ignored",
      "It defines code blocks (bodies of functions, loops, conditionals) instead of braces",
      "It only matters inside strings",
      "It controls the color of the code",
    ],
    answer: 1,
    explain: "Python uses indentation (whitespace) to delimit blocks. Consistent indentation is required — inconsistent indentation raises an IndentationError.",
  },
  {
    q: "Which of the following is NOT a typical strength of Python?",
    options: [
      "Readable, beginner-friendly syntax",
      "A large ecosystem of libraries",
      "The fastest possible raw execution speed for all tasks",
      "Strong support for data science and automation",
    ],
    answer: 2,
    explain: "Python trades some raw speed for readability and productivity. For hot loops people use libraries like NumPy or drop into C — but ease of use and libraries are its strengths.",
  },
  {
    q: "What is CPython?",
    options: [
      "Python written in C — the standard reference implementation of the interpreter",
      "A way to write C inside Python files",
      "A Python-to-C compiler only",
      "An unofficial fork with no relation to Python",
    ],
    answer: 0,
    explain: "CPython is the default and most widely used implementation of Python, written in C. Others include PyPy (JIT), Jython, and IronPython.",
  },
  {
    q: "Which website is the official home for downloading Python?",
    options: ["python.org", "python.com", "getpython.io", "pythonlang.net"],
    answer: 0,
    explain: "python.org is the official site for downloading interpreters and reading the documentation.",
  },
  {
    q: "On Windows, what does checking 'Add Python to PATH' during installation do?",
    options: [
      "Encrypts Python",
      "Lets you run `python` and `pip` from any terminal without the full path",
      "Installs a game",
      "Deletes older Python versions",
    ],
    answer: 1,
    explain: "Adding Python to PATH makes the interpreter and pip available by name in any terminal, rather than needing to type the full install path.",
  },
  {
    q: "What is the difference between a `.py` file and a `.ipynb` file?",
    options: [
      "They are identical",
      "`.py` is a plain script; `.ipynb` is a Jupyter notebook storing cells, code, and output as JSON",
      "`.ipynb` runs faster than `.py`",
      "`.py` cannot contain functions",
    ],
    answer: 1,
    explain: "A `.py` file is plain Python source. A `.ipynb` notebook is a JSON document holding code/Markdown cells plus their saved outputs, run cell by cell in Jupyter.",
  },
  {
    q: "How do you deactivate an active virtual environment?",
    options: ["deactivate", "venv off", "exit venv", "python -m deactivate"],
    answer: 0,
    explain: "Typing `deactivate` in the terminal exits the active virtual environment and returns you to the system/base Python.",
  },
  {
    q: "Which best describes the Python Standard Library?",
    options: [
      "Third-party packages you must install with pip",
      "A large collection of modules bundled with Python (e.g. math, os, json, random)",
      "A single file of built-in functions",
      "Only available in the paid version of Python",
    ],
    answer: 1,
    explain: "The Standard Library ships with Python — modules like math, os, sys, json, random, and datetime are available without installing anything.",
  },
];
