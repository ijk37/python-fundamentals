// ── Chapter 01 — Setup & Environment · expansion pool ───────────────────────
QUESTIONS["01"].push(
  {
    q: "What does `pip freeze` output?",
    options: [
      "The Python version",
      "Installed packages with exact versions, in requirements-file format",
      "A frozen (compiled) executable",
      "The list of virtual environments",
    ],
    answer: 1,
    explain: "pip freeze prints installed packages as name==version lines, ideal for redirecting into requirements.txt.",
  },
  {
    q: "What is the __pycache__ folder with .pyc files?",
    options: [
      "Your source backups",
      "Cached compiled bytecode Python generates to speed up imports",
      "Temporary internet files",
      "The virtual environment",
    ],
    answer: 1,
    explain: "Python caches compiled bytecode (.pyc) in __pycache__ so re-importing unchanged modules is faster. It's safe to delete.",
  },
  {
    q: "On Windows, what is the `py` launcher used for?",
    options: [
      "Compiling Python to C",
      "Selecting and launching an installed Python version (e.g. py -3.12)",
      "Editing files",
      "Uninstalling Python",
    ],
    answer: 1,
    explain: "The Windows `py` launcher finds installed interpreters and lets you pick a version, e.g. `py -3.12 script.py`.",
  },
  {
    q: "What does `pip uninstall requests` do?",
    options: [
      "Reinstalls requests",
      "Removes the requests package from the current environment",
      "Updates requests",
      "Lists requests' files",
    ],
    answer: 1,
    explain: "pip uninstall removes an installed package from the active environment.",
  },
  {
    q: "What does running `python -m module` do?",
    options: [
      "Opens a file called module",
      "Runs a module as a script using its package path (e.g. python -m venv, python -m pip)",
      "Imports without running",
      "Creates a module",
    ],
    answer: 1,
    explain: "The -m flag runs a library module as a script, resolving it on sys.path — used for venv, pip, http.server, and more.",
  }
);
