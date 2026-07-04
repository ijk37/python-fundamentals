"""
Project 03-07: Password Strength Checker & Generator
======================================================
Topics: string methods, any(), all(), functions, list comprehensions,
        secrets/random module, f-strings, input validation
Difficulty: Beginner–Intermediate

Analyses a password against multiple criteria, gives a strength
score with colour-coded feedback, and can generate a strong password.
"""

import secrets   # cryptographically secure random — better than random for passwords
import string    # provides string.ascii_letters, string.digits, string.punctuation


# =============================================================================
# STRENGTH CRITERIA
# =============================================================================

# Each criterion is stored as a (label, check_function, points) tuple.
# check_function takes the password string and returns True/False.

CRITERIA = [
    ("At least 8 characters",        lambda p: len(p) >= 8,                         1),
    ("At least 12 characters",       lambda p: len(p) >= 12,                        1),
    ("Contains lowercase letter",    lambda p: any(c.islower() for c in p),         1),
    ("Contains uppercase letter",    lambda p: any(c.isupper() for c in p),         1),
    ("Contains a digit",             lambda p: any(c.isdigit() for c in p),         1),
    ("Contains a special character", lambda p: any(c in string.punctuation for c in p), 2),
    ("No repeated characters (3×+)", lambda p: not _has_repeats(p),                 1),
    ("No common patterns",           lambda p: not _has_common_pattern(p),          2),
]

# Common weak patterns to flag
COMMON_PATTERNS = [
    "password", "123456", "qwerty", "abc", "111", "000",
    "pass", "admin", "login", "welcome", "letmein", "dhaka",
]


# =============================================================================
# HELPER CHECKS
# =============================================================================

def _has_repeats(password, max_run=3):
    """
    Return True if any character appears 3 or more times in a row.
    Example: "aaabcd" → True, "aababc" → False
    """
    count = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count >= max_run:
                return True   # found a long run
        else:
            count = 1   # reset counter on a different character
    return False


def _has_common_pattern(password):
    """Return True if the password contains a known weak pattern."""
    lower_pw = password.lower()
    return any(pattern in lower_pw for pattern in COMMON_PATTERNS)


# =============================================================================
# ANALYSIS
# =============================================================================

def analyse_password(password):
    """
    Check the password against all criteria and return a results dict.

    Returns:
        dict with keys:
            'passed'  (list of (label, points) for met criteria)
            'failed'  (list of label strings for unmet criteria)
            'score'   (int: total points earned)
            'max'     (int: maximum possible points)
            'level'   (str: 'Weak', 'Fair', 'Good', 'Strong', 'Excellent')
    """
    passed = []
    failed = []
    score  = 0
    max_score = sum(pts for _, _, pts in CRITERIA)

    for label, check, pts in CRITERIA:
        if check(password):
            passed.append((label, pts))
            score += pts
        else:
            failed.append(label)

    # Determine strength level
    pct = score / max_score
    if pct < 0.30:
        level = "Weak      ❌"
    elif pct < 0.50:
        level = "Fair      🟠"
    elif pct < 0.70:
        level = "Good      🟡"
    elif pct < 0.90:
        level = "Strong    🟢"
    else:
        level = "Excellent 🏆"

    return {
        "passed":    passed,
        "failed":    failed,
        "score":     score,
        "max":       max_score,
        "level":     level,
    }


def display_analysis(password, result):
    """Print a detailed analysis report."""
    # Mask the middle of the password for display: "pass****ord"
    if len(password) > 4:
        masked = password[:2] + "*" * (len(password) - 4) + password[-2:]
    else:
        masked = "*" * len(password)

    print()
    print("═" * 52)
    print(f"  Password  : {masked}  (length: {len(password)})")
    print(f"  Strength  : {result['level']}")
    print(f"  Score     : {result['score']} / {result['max']}")
    print("─" * 52)

    # Show each criterion as pass or fail
    for label, pts in result["passed"]:
        print(f"  ✅  {label}  (+{pts})")
    for label in result["failed"]:
        print(f"  ❌  {label}")

    print("═" * 52)


# =============================================================================
# PASSWORD GENERATOR
# =============================================================================

def generate_password(length=16, use_special=True):
    """
    Generate a cryptographically secure random password.

    Strategy:
        1. Pick at least one character from each required category.
        2. Fill the rest randomly from all allowed characters.
        3. Shuffle to remove any predictable ordering.

    Parameters:
        length      (int):  Desired password length.
        use_special (bool): Whether to include punctuation.

    Returns:
        str: The generated password.
    """
    # Build the character pool
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if use_special:
        # Use a subset of punctuation that avoids confusing characters
        safe_punct = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        pool += safe_punct

    # Guarantee at least one character from each required type
    required = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    if use_special:
        required.append(secrets.choice(safe_punct))

    # Fill the remaining positions
    remaining_length = max(length - len(required), 0)
    rest = [secrets.choice(pool) for _ in range(remaining_length)]

    # Combine and shuffle to avoid predictable category ordering
    all_chars = required + rest
    # secrets.SystemRandom is safer than random.shuffle for passwords
    shuffled  = list(all_chars)
    for i in range(len(shuffled) - 1, 0, -1):
        j = secrets.randbelow(i + 1)   # Fisher-Yates shuffle
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    return "".join(shuffled)


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 52)
    print("    Password Strength Checker & Generator")
    print("=" * 52)
    print()

    while True:
        print("Options:")
        print("  1. Check a password")
        print("  2. Generate a strong password")
        print("  3. Quit")
        print()

        choice = input("Choose (1 / 2 / 3): ").strip()

        if choice == "1":
            password = input("\n  Enter the password to check: ")
            if not password:
                print("  No password entered.\n")
                continue
            result = analyse_password(password)
            display_analysis(password, result)

        elif choice == "2":
            try:
                length = int(input("\n  Password length (8–64): ").strip())
                length = max(8, min(64, length))   # clamp to [8, 64]
            except ValueError:
                length = 16   # default

            spec_yn = input("  Include special characters? (yes/no): ").strip().lower()
            use_special = spec_yn in ("yes", "y")

            pw      = generate_password(length, use_special)
            result  = analyse_password(pw)

            print(f"\n  Generated: {pw}")
            display_analysis(pw, result)

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid option.\n")

        print()


if __name__ == "__main__":
    main()
