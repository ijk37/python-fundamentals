"""
Project 03-14: Safe Math Calculator
======================================
Topics: exception handling, raise, custom exceptions,
        try/except/else/finally, functions, while loop
Difficulty: Beginner–Intermediate

A calculator that uses custom exception classes to handle
every possible error cleanly: division by zero, invalid
input, overflow, and unsupported operations.
"""

import math


# =============================================================================
# CUSTOM EXCEPTION CLASSES
# =============================================================================

class CalculatorError(Exception):
    """Base class for all calculator-related errors."""
    pass   # inherits __init__ and __str__ from Exception


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide (or mod) by zero."""
    def __init__(self, dividend):
        self.dividend = dividend
        super().__init__(f"Cannot divide {dividend} by zero.")


class InvalidInputError(CalculatorError):
    """Raised when a non-numeric value is entered."""
    def __init__(self, value):
        super().__init__(f"'{value}' is not a valid number.")


class NegativeSquareRootError(CalculatorError):
    """Raised when taking the square root of a negative number."""
    def __init__(self, value):
        super().__init__(f"Cannot take square root of negative number ({value}).")


class UnsupportedOperationError(CalculatorError):
    """Raised when an unknown operation code is entered."""
    def __init__(self, op):
        super().__init__(f"Unknown operation: '{op}'. Check the menu.")


# =============================================================================
# CALCULATION FUNCTIONS
# =============================================================================

def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a × b."""
    return a * b


def divide(a, b):
    """
    Return a / b.
    Raises DivisionByZeroError if b == 0.
    """
    if b == 0:
        raise DivisionByZeroError(a)
    return a / b


def floor_divide(a, b):
    """
    Return a // b (integer division).
    Raises DivisionByZeroError if b == 0.
    """
    if b == 0:
        raise DivisionByZeroError(a)
    return a // b


def modulo(a, b):
    """
    Return a % b (remainder).
    Raises DivisionByZeroError if b == 0.
    """
    if b == 0:
        raise DivisionByZeroError(a)
    return a % b


def power(a, b):
    """Return a raised to the power b."""
    return a ** b


def square_root(a):
    """
    Return the square root of a.
    Raises NegativeSquareRootError if a < 0.
    """
    if a < 0:
        raise NegativeSquareRootError(a)
    return math.sqrt(a)


# =============================================================================
# INPUT HELPERS
# =============================================================================

def parse_number(raw):
    """
    Convert a string to float.
    Raises InvalidInputError (our custom exception) on failure.
    """
    try:
        return float(raw)
    except ValueError:
        raise InvalidInputError(raw)


def ask_number(prompt):
    """Keep prompting until the user enters a valid number."""
    while True:
        raw = input(prompt).strip()
        try:
            return parse_number(raw)
        except InvalidInputError as e:
            print(f"  ❌ {e}")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

OPERATIONS = {
    "1": ("Add",            "+"),
    "2": ("Subtract",       "-"),
    "3": ("Multiply",       "×"),
    "4": ("Divide",         "÷"),
    "5": ("Floor Divide",   "//"),
    "6": ("Modulo",         "%"),
    "7": ("Power",          "^"),
    "8": ("Square Root",    "√ (one number)"),
}


def calculate(op, a, b=None):
    """
    Dispatch to the right calculation function based on op code.
    Raises UnsupportedOperationError for unknown op codes.
    """
    if   op == "1": return add(a, b)
    elif op == "2": return subtract(a, b)
    elif op == "3": return multiply(a, b)
    elif op == "4": return divide(a, b)
    elif op == "5": return floor_divide(a, b)
    elif op == "6": return modulo(a, b)
    elif op == "7": return power(a, b)
    elif op == "8": return square_root(a)
    else:
        raise UnsupportedOperationError(op)


def main():
    print("=" * 50)
    print("        Safe Math Calculator")
    print("=" * 50)
    print("  All errors are handled with custom exceptions.")
    print()

    history = []   # store (expression, result) pairs

    while True:
        print("Operations:")
        for code, (name, symbol) in OPERATIONS.items():
            print(f"  {code}. {name} ({symbol})")
        print("  h. View history")
        print("  q. Quit")
        print()

        op = input("Choose: ").strip().lower()

        if op == "q":
            print("\nGoodbye!")
            break

        if op == "h":
            if not history:
                print("  No calculations yet.\n")
            else:
                print()
                for expr, res in history:
                    print(f"  {expr} = {res}")
                print()
            continue

        if op not in OPERATIONS:
            print(f"  ❌ Unknown option '{op}'.\n")
            continue

        # ── Get operands ─────────────────────────────────────────
        try:
            a = ask_number("  First number : ")

            # Square root only needs one number
            if op == "8":
                b      = None
                expr   = f"√{a}"
            else:
                b    = ask_number("  Second number: ")
                _, sym = OPERATIONS[op]
                expr  = f"{a} {sym} {b}"

            # ── Perform calculation ───────────────────────────────
            # The else clause runs only if no exception was raised
            try:
                result = calculate(op, a, b)
            except DivisionByZeroError as e:
                print(f"\n  ❌ Math Error: {e}\n")
            except NegativeSquareRootError as e:
                print(f"\n  ❌ Math Error: {e}\n")
            else:
                # Format: show int if result has no fractional part
                display = int(result) if isinstance(result, float) and result.is_integer() else result
                print(f"\n  ✅ {expr} = {display}\n")
                history.append((expr, display))

        except KeyboardInterrupt:
            print("\n  Cancelled.\n")

        finally:
            # The finally block ALWAYS runs — great place for cleanup messages
            pass   # nothing to clean up here, but the block shows the pattern


if __name__ == "__main__":
    main()
