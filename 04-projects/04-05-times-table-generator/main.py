"""
Project 03-05: Times Table Generator
=======================================
Topics: for loops, nested loops, range(), string formatting,
        input validation, functions, f-strings
Difficulty: Beginner

Prints multiplication tables in different display styles
(grid, list, and quiz mode).
"""


# =============================================================================
# DISPLAY FUNCTIONS
# =============================================================================

def print_separator(char="─", width=60):
    print(char * width)


def table_as_list(number, limit=12):
    """
    Print a single multiplication table in vertical list format.

    Example for number=3, limit=5:
        3 × 1  =  3
        3 × 2  =  6
        ...
    """
    print()
    print_separator("═")
    print(f"  Multiplication Table for {number}  (1 to {limit})")
    print_separator("─")

    for i in range(1, limit + 1):        # i goes from 1 to limit (inclusive)
        product = number * i
        # :<3 means left-align in a field of width 3 — keeps columns neat
        print(f"  {number} × {i:<3} = {product:>5}")

    print_separator("═")


def table_grid(start, end, limit=12):
    """
    Print a grid of multiplication tables from start to end.

    The header row shows the multipliers (1 to limit).
    Each subsequent row shows results for one number (start … end).
    """
    print()
    print_separator("═")
    print(f"  Multiplication Grid  ({start}–{end}  ×  1–{limit})")
    print_separator("─")

    # Header row: blank cell + multiplier labels
    header = "     " + "".join(f"{i:>5}" for i in range(1, limit + 1))
    print(header)
    print_separator("─")

    for row in range(start, end + 1):       # outer loop: each base number
        # Build one row of products
        row_values = "".join(f"{row * col:>5}" for col in range(1, limit + 1))
        print(f"  {row:<3}: {row_values}")

    print_separator("═")


def quiz_mode(number, limit=12):
    """
    Interactive quiz: ask the user to multiply 'number' by random
    values and give instant feedback.
    """
    import random

    print()
    print_separator("═")
    print(f"  Quiz Mode — Table of {number}")
    print(f"  Answer {limit} questions. Type 'quit' to stop.")
    print_separator("─")

    score   = 0    # number of correct answers
    asked   = 0    # total questions asked

    multipliers = list(range(1, limit + 1))
    random.shuffle(multipliers)   # randomise order

    for mult in multipliers:
        asked += 1
        answer_raw = input(f"  {number} × {mult} = ? ").strip()

        if answer_raw.lower() == "quit":
            asked -= 1   # don't count the quit as a question
            break

        try:
            answer  = int(answer_raw)
            correct = number * mult

            if answer == correct:
                print("  ✅ Correct!\n")
                score += 1
            else:
                print(f"  ❌ Wrong. The answer is {correct}.\n")

        except ValueError:
            print(f"  Please enter a whole number. Answer was {number * mult}.\n")

    # --- Score summary ---
    print_separator("─")
    if asked > 0:
        pct = score / asked * 100
        print(f"  Score: {score}/{asked}  ({pct:.0f}%)")
        if pct == 100:
            print("  Perfect score! 🏆")
        elif pct >= 70:
            print("  Well done! Keep practising.")
        else:
            print("  Keep practising — you'll get there!")
    else:
        print("  No questions answered.")
    print_separator("═")


# =============================================================================
# INPUT HELPERS
# =============================================================================

def get_int(prompt, min_val=1, max_val=100):
    """Ask for an integer in the range [min_val, max_val]."""
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val <= value <= max_val:
                return value
            print(f"  Please enter a number between {min_val} and {max_val}.\n")
        except ValueError:
            print("  Please enter a whole number.\n")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 60)
    print("            Times Table Generator")
    print("=" * 60)
    print()

    while True:
        print("Modes:")
        print("  1. Single table  (list format)")
        print("  2. Grid of tables")
        print("  3. Quiz mode")
        print("  4. Quit")
        print()

        choice = input("Choose (1 / 2 / 3 / 4): ").strip()

        if choice == "1":
            n     = get_int("\n  Which table? (1–20): ", 1, 20)
            limit = get_int("  Up to how many? (1–20): ", 1, 20)
            table_as_list(n, limit)

        elif choice == "2":
            start = get_int("\n  Start from table: (1–20): ", 1, 20)
            end   = get_int(f"  End at table (>= {start}): ", start, 20)
            limit = get_int("  Columns up to: (1–20): ", 1, 20)
            table_grid(start, end, limit)

        elif choice == "3":
            n     = get_int("\n  Quiz on which table? (1–20): ", 1, 20)
            limit = get_int("  Number of questions (1–20): ", 1, 20)
            quiz_mode(n, limit)

        elif choice == "4":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")

        print()


if __name__ == "__main__":
    main()
