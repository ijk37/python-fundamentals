"""
Project 03-17: JSON Expense Tracker
======================================
Topics: json module, datetime, CRUD operations,
        pathlib, functions, while loop, dicts, lists
Difficulty: Intermediate

Records daily expenses to a JSON file. Each expense has
an ID, date, category, description, and amount. Supports
adding, listing, filtering by category or date, deleting,
and a monthly summary report.
"""

import json
from datetime import datetime, date
from pathlib  import Path


# =============================================================================
# CONSTANTS
# =============================================================================

DATA_FILE = Path("expenses.json")

CATEGORIES = [
    "Food", "Transport", "Utilities", "Health",
    "Education", "Shopping", "Entertainment", "Other",
]

DATE_FORMAT = "%Y-%m-%d"


# =============================================================================
# JSON FILE HELPERS
# =============================================================================

def load_expenses():
    """
    Load expenses from JSON file.
    Returns a list of expense dicts.
    Returns an empty list if the file does not exist.
    """
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)   # json.load reads from a file object
    except json.JSONDecodeError:
        print("  ⚠️  Expense file is corrupted. Starting fresh.")
        return []


def save_expenses(expenses):
    """Save the expenses list to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        # indent=2 makes the JSON human-readable
        json.dump(expenses, f, indent=2, ensure_ascii=False)


def next_id(expenses):
    """Return the next auto-increment ID (max existing + 1)."""
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1


# =============================================================================
# CRUD OPERATIONS
# =============================================================================

def add_expense(category, description, amount, expense_date=None):
    """
    Add a new expense entry.

    Parameters:
        category    (str):   One of CATEGORIES
        description (str):   Short description
        amount      (float): Amount in BDT
        expense_date (str):  Optional "YYYY-MM-DD"; defaults to today
    """
    expenses = load_expenses()

    # Use today's date if none provided
    if expense_date is None:
        expense_date = date.today().strftime(DATE_FORMAT)

    new_expense = {
        "id":          next_id(expenses),
        "date":        expense_date,
        "category":    category.title(),
        "description": description.strip(),
        "amount":      round(float(amount), 2),
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    return new_expense


def delete_expense(expense_id):
    """
    Delete an expense by ID.
    Returns True if deleted, False if not found.
    """
    expenses = load_expenses()
    original_count = len(expenses)

    # Keep all expenses EXCEPT the one to delete
    expenses = [e for e in expenses if e["id"] != expense_id]

    if len(expenses) == original_count:
        return False   # nothing was removed

    save_expenses(expenses)
    return True


# =============================================================================
# FILTERING AND REPORTING
# =============================================================================

def filter_by_category(expenses, category):
    """Return expenses matching the given category (case-insensitive)."""
    cat = category.lower()
    return [e for e in expenses if e["category"].lower() == cat]


def filter_by_month(expenses, year, month):
    """Return expenses in the given year-month."""
    prefix = f"{year}-{month:02d}"
    return [e for e in expenses if e["date"].startswith(prefix)]


def monthly_summary(expenses, year, month):
    """
    Build a monthly summary: total per category and grand total.
    Returns a dict: {category: total_amount}
    """
    monthly = filter_by_month(expenses, year, month)

    # Accumulate totals per category using a regular dict
    summary = {}
    for e in monthly:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    return summary, sum(e["amount"] for e in monthly)


# =============================================================================
# DISPLAY
# =============================================================================

def print_expenses(expenses, title="Expenses"):
    """Print a formatted table of expenses."""
    if not expenses:
        print("  No expenses found.\n")
        return

    print()
    print(f"  {title}")
    print(f"  {'ID':<5} {'Date':<12} {'Category':<14} {'Description':<22} {'Amount':>10}")
    print("  " + "─" * 67)

    for e in expenses:
        print(f"  {e['id']:<5} {e['date']:<12} {e['category']:<14} "
              f"{e['description']:<22} ৳{e['amount']:>8,.2f}")

    total = sum(e["amount"] for e in expenses)
    print("  " + "─" * 67)
    print(f"  {'TOTAL':>55} ৳{total:>8,.2f}")
    print()


def print_monthly_summary(year, month):
    """Print a category breakdown for a given month."""
    expenses = load_expenses()
    summary, grand_total = monthly_summary(expenses, year, month)

    month_name = datetime(year, month, 1).strftime("%B %Y")
    print()
    print(f"  Monthly Summary — {month_name}")
    print("  " + "─" * 35)

    if not summary:
        print("  No expenses this month.\n")
        return

    # Sort by amount (highest first)
    for cat, total in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        bar_len = int(total / grand_total * 20)
        bar     = "█" * bar_len
        print(f"  {cat:<14} ৳{total:>8,.2f}  {bar}")

    print("  " + "─" * 35)
    print(f"  {'TOTAL':<14} ৳{grand_total:>8,.2f}")
    print()


# =============================================================================
# SEED SAMPLE DATA
# =============================================================================

def _seed():
    """Add sample expenses if the file is empty."""
    if DATA_FILE.exists():
        return

    samples = [
        ("Food",          "Lunch at restaurant",   350,  "2025-06-01"),
        ("Transport",     "Rickshaw to office",     60,  "2025-06-01"),
        ("Food",          "Groceries",             850,  "2025-06-02"),
        ("Utilities",     "Mobile recharge",       200,  "2025-06-03"),
        ("Education",     "Book purchase",         550,  "2025-06-05"),
        ("Food",          "Dinner",                280,  "2025-06-07"),
        ("Entertainment", "Movie ticket",          250,  "2025-06-08"),
        ("Health",        "Medicine",              180,  "2025-06-09"),
    ]

    for cat, desc, amt, dt in samples:
        add_expense(cat, desc, amt, dt)

    print("  ✅ Sample expenses loaded.")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 55)
    print("            JSON Expense Tracker")
    print("=" * 55)
    print(f"  Data file: {DATA_FILE.resolve()}")

    _seed()

    while True:
        print("\nOptions:")
        print("  1. View all expenses")
        print("  2. Add an expense")
        print("  3. Delete an expense")
        print("  4. Filter by category")
        print("  5. Monthly summary")
        print("  6. Quit")
        print()

        choice = input("Choose (1–6): ").strip()

        # ── 1. VIEW ALL ──────────────────────────────────────────
        if choice == "1":
            expenses = load_expenses()
            print_expenses(expenses, "All Expenses")

        # ── 2. ADD ───────────────────────────────────────────────
        elif choice == "2":
            print("  Categories: " + ", ".join(CATEGORIES))
            cat  = input("  Category   : ").strip().title()
            if cat not in CATEGORIES:
                print(f"  Unknown category. Using 'Other'.")
                cat = "Other"
            desc   = input("  Description: ").strip()
            raw_amt = input("  Amount (৳) : ").strip()
            try:
                amount = float(raw_amt)
            except ValueError:
                print("  Invalid amount.\n")
                continue
            raw_date = input("  Date (YYYY-MM-DD, Enter for today): ").strip()
            expense  = add_expense(cat, desc, amount, raw_date or None)
            print(f"  ✅ Expense #{expense['id']} saved.\n")

        # ── 3. DELETE ────────────────────────────────────────────
        elif choice == "3":
            raw = input("  Expense ID to delete: ").strip()
            try:
                eid = int(raw)
                if delete_expense(eid):
                    print(f"  ✅ Expense #{eid} deleted.\n")
                else:
                    print(f"  ❌ No expense with ID {eid}.\n")
            except ValueError:
                print("  Please enter a number.\n")

        # ── 4. FILTER BY CATEGORY ────────────────────────────────
        elif choice == "4":
            print("  Categories: " + ", ".join(CATEGORIES))
            cat      = input("  Category: ").strip()
            expenses = load_expenses()
            filtered = filter_by_category(expenses, cat)
            print_expenses(filtered, f"Expenses — {cat.title()}")

        # ── 5. MONTHLY SUMMARY ───────────────────────────────────
        elif choice == "5":
            today = date.today()
            raw_y = input(f"  Year  [{today.year}]: ").strip()
            raw_m = input(f"  Month [{today.month:02d}]: ").strip()
            try:
                year  = int(raw_y) if raw_y else today.year
                month = int(raw_m) if raw_m else today.month
                if not (1 <= month <= 12):
                    raise ValueError("Month must be 1–12.")
                print_monthly_summary(year, month)
            except ValueError as e:
                print(f"  ❌ {e}\n")

        # ── 6. QUIT ──────────────────────────────────────────────
        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
