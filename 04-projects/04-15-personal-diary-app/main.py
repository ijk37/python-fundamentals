"""
Project 03-15: Personal Diary App
====================================
Topics: file I/O, datetime, pathlib, append mode,
        read mode, text file parsing, functions, while loop
Difficulty: Beginner–Intermediate

Saves diary entries to a plain-text file on disk.
Each entry has a timestamp, title, and body. Supports
adding entries, listing all entries, reading a specific
entry, and searching by keyword.
"""

from datetime import datetime
from pathlib  import Path


# =============================================================================
# CONSTANTS
# =============================================================================

DIARY_FILE = Path("diary.txt")   # stored in the same folder as the script

# Separator used between entries in the file
ENTRY_SEPARATOR = "=" * 60 + "\n"

# Date-time format used when saving and parsing entries
DATE_FORMAT = "%Y-%m-%d %H:%M"


# =============================================================================
# FILE OPERATIONS
# =============================================================================

def save_entry(title, body):
    """
    Append a new diary entry to DIARY_FILE.

    Each entry is saved as:
        ============================================================
        DATE: 2025-06-09 14:35
        TITLE: My Entry Title
        ----
        body text here
        ============================================================
    """
    now       = datetime.now().strftime(DATE_FORMAT)
    entry_text = (
        ENTRY_SEPARATOR
        + f"DATE: {now}\n"
        + f"TITLE: {title.strip()}\n"
        + "----\n"
        + body.strip() + "\n"
    )

    # Open in append mode ("a") — creates the file if it doesn't exist
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(entry_text)


def load_entries():
    """
    Read the diary file and return a list of entry dicts.

    Each dict has keys: "date", "title", "body"
    Returns an empty list if the file does not exist.
    """
    if not DIARY_FILE.exists():
        return []

    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by the separator line — gives raw blocks for each entry
    raw_blocks = content.split(ENTRY_SEPARATOR)

    entries = []
    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue   # skip empty blocks

        lines = block.splitlines()
        entry = {"date": "", "title": "", "body": ""}

        # Parse the structured header lines
        body_lines = []
        reading_body = False

        for line in lines:
            if line.startswith("DATE: "):
                entry["date"] = line[6:]        # everything after "DATE: "
            elif line.startswith("TITLE: "):
                entry["title"] = line[7:]       # everything after "TITLE: "
            elif line == "----":
                reading_body = True             # next lines are the body
            elif reading_body:
                body_lines.append(line)

        entry["body"] = "\n".join(body_lines)
        entries.append(entry)

    return entries


def search_entries(keyword):
    """Return entries where the keyword appears in title or body."""
    keyword = keyword.lower()
    return [
        e for e in load_entries()
        if keyword in e["title"].lower() or keyword in e["body"].lower()
    ]


# =============================================================================
# DISPLAY
# =============================================================================

def list_entries():
    """Print a numbered summary of all entries (date + title)."""
    entries = load_entries()
    if not entries:
        print("  No diary entries yet.\n")
        return

    print()
    print(f"  {'#':<4} {'Date':<18} Title")
    print("  " + "─" * 50)
    for i, entry in enumerate(entries, 1):
        print(f"  {i:<4} {entry['date']:<18} {entry['title']}")
    print()
    return entries


def print_entry(entry, number=None):
    """Print the full content of one diary entry."""
    print()
    print("─" * 55)
    if number:
        print(f"  Entry #{number}")
    print(f"  Date : {entry['date']}")
    print(f"  Title: {entry['title']}")
    print("─" * 55)
    print(entry["body"])
    print("─" * 55)
    print()


# =============================================================================
# INPUT HELPERS
# =============================================================================

def get_multiline_input(prompt):
    """
    Let the user type multiple lines.
    Type 'END' on its own line to finish.
    """
    print(prompt)
    print("  (Type 'END' on a new line to finish.)")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 50)
    print("           Personal Diary")
    print("=" * 50)
    print(f"  Diary stored at: {DIARY_FILE.resolve()}")
    print()

    while True:
        print("Options:")
        print("  1. Write new entry")
        print("  2. List all entries")
        print("  3. Read an entry")
        print("  4. Search entries")
        print("  5. Quit")
        print()

        choice = input("Choose (1–5): ").strip()

        # ── 1. WRITE ─────────────────────────────────────────────
        if choice == "1":
            title = input("  Entry title: ").strip()
            if not title:
                print("  Title cannot be empty.\n")
                continue
            body = get_multiline_input("  Write your entry:")
            if not body.strip():
                print("  Entry body cannot be empty.\n")
                continue
            save_entry(title, body)
            print("  ✅ Entry saved.\n")

        # ── 2. LIST ──────────────────────────────────────────────
        elif choice == "2":
            list_entries()

        # ── 3. READ ──────────────────────────────────────────────
        elif choice == "3":
            entries = list_entries()
            if not entries:
                continue

            raw = input("  Enter entry number: ").strip()
            try:
                idx = int(raw) - 1   # convert to 0-based index
                if 0 <= idx < len(entries):
                    print_entry(entries[idx], idx + 1)
                else:
                    print("  Number out of range.\n")
            except ValueError:
                print("  Please enter a valid number.\n")

        # ── 4. SEARCH ────────────────────────────────────────────
        elif choice == "4":
            keyword = input("  Search keyword: ").strip()
            if not keyword:
                continue
            results = search_entries(keyword)
            if results:
                print(f"\n  Found {len(results)} matching entry/entries:\n")
                for i, entry in enumerate(results, 1):
                    print_entry(entry, i)
            else:
                print(f"  No entries found for '{keyword}'.\n")

        # ── 5. QUIT ──────────────────────────────────────────────
        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
