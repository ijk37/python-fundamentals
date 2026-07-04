"""
Project 03-31: Full Expense Tracker
======================================
Topics: file I/O, JSON, CSV, datetime, functions,
        exception handling, pathlib, while loop
Difficulty: Intermediate–Advanced

A comprehensive expense tracker that ties together many
Python skills from throughout the course:
  - JSON for persistent storage
  - CSV for exporting reports
  - datetime for timestamps and monthly filtering
  - pathlib for file management
  - Exception handling for robust input
  - Functions and modules for clean code

Features:
  - Add/edit/delete expenses
  - Category and monthly filtering
  - Budget tracking per category
  - Export to CSV
  - Summary statistics
"""

import json
import csv
from datetime import datetime, date
from pathlib  import Path


# =============================================================================
# CONSTANTS / CONFIGURATION
# =============================================================================

DATA_FILE    = Path("expense_tracker.json")
EXPORT_FILE  = Path("expenses_export.csv")
DATE_FORMAT  = "%Y-%m-%d"

CATEGORIES = [
    "Food", "Transport", "Utilities", "Health",
    "Education", "Shopping", "Entertainment", "Savings", "Other",
]

# Monthly budget limits per category (BDT)
DEFAULT_BUDGETS = {
    "Food":          5000,
    "Transport":     2000,
    "Utilities":     3000,
    "Health":        2000,
    "Education":     3000,
    "Shopping":      4000,
    "Entertainment": 2000,
    "Savings":       5000,
    "Other":         2000,
}


# =============================================================================
# DATA MODEL
# =============================================================================

def empty_store():
    """Return the default data store structure."""
    return {
        "expenses": [],
        "budgets":  dict(DEFAULT_BUDGETS),
        "next_id":  1,
    }


def load_store():
    """Load the JSON data store from disk, or return a fresh one."""
    if not DATA_FILE.exists():
        return empty_store()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, KeyError):
        print("  ⚠️  Data file corrupted — starting fresh.")
        return empty_store()


def save_store(store):
    """Save the data store to disk as pretty JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(store, f, indent=2, ensure_ascii=False)


# =============================================================================
# EXPENSE CRUD
# =============================================================================

def add_expense(store, category, description, amount, expense_date=None):
    """Add a new expense to the store."""
    if expense_date is None:
        expense_date = date.today().strftime(DATE_FORMAT)

    expense = {
        "id":          store["next_id"],
        "date":        expense_date,
        "category":    category.title(),
        "description": description.strip(),
        "amount":      round(float(amount), 2),
    }
    store["expenses"].append(expense)
    store["next_id"] += 1
    save_store(store)
    return expense


def delete_expense(store, expense_id):
    """Delete an expense by ID. Returns True if found and deleted."""
    original = len(store["expenses"])
    store["expenses"] = [e for e in store["expenses"] if e["id"] != expense_id]
    if len(store["expenses"]) < original:
        save_store(store)
        return True
    return False


def update_expense(store, expense_id, **kwargs):
    """Update fields of an existing expense."""
    for expense in store["expenses"]:
        if expense["id"] == expense_id:
            for key, val in kwargs.items():
                if key in expense and val:
                    expense[key] = val
            save_store(store)
            return True
    return False


# =============================================================================
# FILTERING
# =============================================================================

def filter_by_month(expenses, year, month):
    """Return expenses for a specific year-month."""
    prefix = f"{year}-{month:02d}"
    return [e for e in expenses if e["date"].startswith(prefix)]


def filter_by_category(expenses, category):
    """Return expenses matching a category."""
    return [e for e in expenses if e["category"].lower() == category.lower()]


# =============================================================================
# BUDGET TRACKING
# =============================================================================

def budget_report(store, year, month):
    """
    Compare spending vs budget for each category in a given month.
    Returns a list of (category, spent, budget, status) tuples.
    """
    monthly = filter_by_month(store["expenses"], year, month)
    report  = []

    for cat in CATEGORIES:
        spent  = sum(e["amount"] for e in monthly if e["category"] == cat)
        budget = store["budgets"].get(cat, 0)
        if budget > 0:
            pct    = spent / budget * 100
            status = "✅ OK" if pct <= 80 else ("⚠️ Warning" if pct <= 100 else "❌ Over")
        else:
            pct    = 0
            status = "—"
        report.append((cat, spent, budget, pct, status))

    return report


# =============================================================================
# CSV EXPORT
# =============================================================================

def export_csv(expenses, filepath=EXPORT_FILE):
    """Export the expense list to a CSV file."""
    fieldnames = ["ID", "Date", "Category", "Description", "Amount"]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for e in sorted(expenses, key=lambda x: x["date"]):
            writer.writerow({
                "ID":          e["id"],
                "Date":        e["date"],
                "Category":    e["category"],
                "Description": e["description"],
                "Amount":      e["amount"],
            })
    return len(expenses)


# =============================================================================
# DISPLAY
# =============================================================================

def print_expenses(expenses, title="Expenses"):
    """Print a formatted table of expenses."""
    if not expenses:
        print("  No expenses found.\n")
        return

    total = sum(e["amount"] for e in expenses)
    print()
    print(f"  {title}  ({len(expenses)} entries)")
    print(f"  {'ID':<5} {'Date':<12} {'Category':<14} {'Amount':>10}  Description")
    print("  " + "─" * 65)
    for e in sorted(expenses, key=lambda x: x["date"]):
        print(f"  {e['id']:<5} {e['date']:<12} {e['category']:<14} "
              f"৳{e['amount']:>8,.0f}  {e['description']}")
    print("  " + "─" * 65)
    print(f"  {'TOTAL':>32} ৳{total:>8,.0f}")
    print()


def print_budget_report(report, year, month):
    """Print the budget vs. spending comparison."""
    month_name = datetime(year, month, 1).strftime("%B %Y")
    print(f"\n  Budget Report — {month_name}")
    print(f"  {'Category':<16} {'Spent':>9}  {'Budget':>9}  {'%':>6}  Status")
    print("  " + "─" * 58)

    total_spent  = 0
    total_budget = 0

    for cat, spent, budget, pct, status in report:
        if spent > 0 or budget > 0:
            print(f"  {cat:<16} ৳{spent:>7,.0f}  ৳{budget:>7,.0f}  "
                  f"{pct:>5.0f}%  {status}")
            total_spent  += spent
            total_budget += budget

    print("  " + "─" * 58)
    total_pct = 100 * total_spent / total_budget if total_budget > 0 else 0
    print(f"  {'TOTAL':<16} ৳{total_spent:>7,.0f}  ৳{total_budget:>7,.0f}  "
          f"{total_pct:>5.0f}%")
    print()


def print_summary(store):
    """Print overall statistics."""
    expenses = store["expenses"]
    if not expenses:
        print("  No expenses recorded.\n")
        return

    total  = sum(e["amount"] for e in expenses)
    by_cat = {}
    for e in expenses:
        by_cat[e["category"]] = by_cat.get(e["category"], 0) + e["amount"]

    print(f"\n  All-time Summary")
    print(f"  Total expenses : {len(expenses)}")
    print(f"  Total spent    : ৳{total:,.0f}")
    print(f"  Avg per expense: ৳{total/len(expenses):,.0f}")
    print()
    print(f"  By category:")
    for cat, amt in sorted(by_cat.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * int(amt / total * 20)
        print(f"  {cat:<16} ৳{amt:>8,.0f}  {bar}")
    print()


# =============================================================================
# SEED DATA
# =============================================================================

def _seed(store):
    """Add sample data on first run."""
    if store["expenses"]:
        return   # already has data

    samples = [
        ("Food",    "Lunch",          350,  "2025-06-01"),
        ("Transport","Rickshaw",        60,  "2025-06-01"),
        ("Food",    "Groceries",      1200,  "2025-06-02"),
        ("Utilities","Phone bill",     600,  "2025-06-03"),
        ("Education","Python book",    550,  "2025-06-05"),
        ("Food",    "Dinner out",      450,  "2025-06-07"),
        ("Entertainment","Movie",      250,  "2025-06-08"),
        ("Health",  "Medicine",       180,  "2025-06-09"),
        ("Shopping","New shirt",       800,  "2025-06-10"),
        ("Food",    "Breakfast",       120,  "2025-06-11"),
    ]
    for cat, desc, amt, dt in samples:
        add_expense(store, cat, desc, amt, dt)
    print("  ✅ Sample data loaded.")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 55)
    print("          Full Expense Tracker")
    print("=" * 55)
    print(f"  Data file: {DATA_FILE.resolve()}")

    store = load_store()
    _seed(store)

    while True:
        print("\nOptions:")
        print("  1. View all expenses")
        print("  2. Add an expense")
        print("  3. Delete an expense")
        print("  4. Filter by category")
        print("  5. Filter by month")
        print("  6. Budget report")
        print("  7. Overall summary")
        print("  8. Export to CSV")
        print("  9. Quit")
        print()

        choice = input("Choose (1–9): ").strip()

        # ── 1. VIEW ALL ──────────────────────────────────────────
        if choice == "1":
            print_expenses(store["expenses"])

        # ── 2. ADD ───────────────────────────────────────────────
        elif choice == "2":
            print("  Categories: " + ", ".join(CATEGORIES))
            cat  = input("  Category   : ").strip().title()
            if cat not in CATEGORIES:
                cat = "Other"
            desc = input("  Description: ").strip()
            try:
                amt = float(input("  Amount (৳) : "))
            except ValueError:
                print("  Invalid amount.\n")
                continue
            raw_date = input("  Date (YYYY-MM-DD, Enter=today): ").strip()
            e = add_expense(store, cat, desc, amt, raw_date or None)
            print(f"  ✅ Saved (ID #{e['id']}).\n")

        # ── 3. DELETE ────────────────────────────────────────────
        elif choice == "3":
            try:
                eid = int(input("  ID to delete: "))
                if delete_expense(store, eid):
                    print(f"  ✅ Deleted #{eid}.\n")
                else:
                    print(f"  ❌ ID #{eid} not found.\n")
            except ValueError:
                print("  Enter a number.\n")

        # ── 4. FILTER BY CATEGORY ────────────────────────────────
        elif choice == "4":
            cat  = input("  Category: ").strip()
            data = filter_by_category(store["expenses"], cat)
            print_expenses(data, f"Category: {cat.title()}")

        # ── 5. FILTER BY MONTH ───────────────────────────────────
        elif choice == "5":
            today = date.today()
            try:
                y = int(input(f"  Year  [{today.year}]: ").strip() or today.year)
                m = int(input(f"  Month [{today.month}]  : ").strip() or today.month)
                data = filter_by_month(store["expenses"], y, m)
                month_name = datetime(y, m, 1).strftime("%B %Y")
                print_expenses(data, month_name)
            except (ValueError, OverflowError):
                print("  Invalid date.\n")

        # ── 6. BUDGET REPORT ─────────────────────────────────────
        elif choice == "6":
            today = date.today()
            try:
                y = int(input(f"  Year  [{today.year}]: ").strip() or today.year)
                m = int(input(f"  Month [{today.month}]  : ").strip() or today.month)
                report = budget_report(store, y, m)
                print_budget_report(report, y, m)
            except ValueError:
                print("  Invalid input.\n")

        # ── 7. SUMMARY ───────────────────────────────────────────
        elif choice == "7":
            print_summary(store)

        # ── 8. EXPORT ────────────────────────────────────────────
        elif choice == "8":
            count = export_csv(store["expenses"])
            print(f"  ✅ Exported {count} expenses to {EXPORT_FILE}\n")

        # ── 9. QUIT ──────────────────────────────────────────────
        elif choice == "9":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
