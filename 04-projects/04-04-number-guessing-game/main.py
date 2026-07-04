"""
Project 03-04: Number Guessing Game
=====================================
Topics: while loop, if/elif/else, random, int() conversion,
        input validation, functions, break/continue, f-strings
Difficulty: Beginner

The computer picks a secret number; the player has a limited
number of attempts to guess it. Includes a difficulty selector,
a hint system, and a high-score tracker.
"""

import random   # built-in module for generating random numbers


# =============================================================================
# DIFFICULTY SETTINGS
# =============================================================================

# Each difficulty level stores: (number range, max attempts)
DIFFICULTY = {
    "easy":   (1,   50,  10),   # range 1–50,   10 guesses
    "medium": (1,  100,   7),   # range 1–100,   7 guesses
    "hard":   (1,  200,   5),   # range 1–200,   5 guesses
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_difficulty():
    """Ask the player to choose a difficulty level and return its settings."""
    print("Difficulty levels:")
    for name, (low, high, attempts) in DIFFICULTY.items():
        print(f"  {name:<8} — guess a number from {low} to {high}  ({attempts} attempts)")
    print()

    while True:
        choice = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if choice in DIFFICULTY:
            low, high, max_attempts = DIFFICULTY[choice]
            return low, high, max_attempts, choice
        print("  Please type easy, medium, or hard.\n")


def get_guess(low, high):
    """Ask the player for a valid integer guess within [low, high]."""
    while True:
        raw = input(f"Your guess ({low}–{high}): ").strip()
        try:
            guess = int(raw)   # convert string → integer
            if low <= guess <= high:
                return guess
            else:
                print(f"  Out of range! Enter a number between {low} and {high}.\n")
        except ValueError:
            print("  Please enter a whole number.\n")


def calculate_score(attempts_used, max_attempts, diff_name):
    """
    Award bonus points based on remaining attempts and difficulty.

    Formula:
        base_score = (max_attempts - attempts_used + 1) * 100
        multiplier = 1x (easy), 2x (medium), 3x (hard)
    """
    multipliers = {"easy": 1, "medium": 2, "hard": 3}
    remaining   = max_attempts - attempts_used + 1   # +1 so the winning guess still scores
    base        = max(remaining * 100, 0)            # never negative
    return base * multipliers[diff_name]


def hint(guess, secret, low, high, attempts_left):
    """
    Return a descriptive hint about how close the guess is.

    Gives increasingly precise hints as attempts_left decreases.
    """
    diff = abs(guess - secret)
    span = high - low   # total range size

    if diff == 0:
        return "🎉 Correct!"

    direction = "higher" if guess < secret else "lower"

    # Percentage of range the guess is off by
    pct = diff / span

    if pct <= 0.05:
        closeness = "Very hot 🔥"
    elif pct <= 0.15:
        closeness = "Hot 🌡️"
    elif pct <= 0.30:
        closeness = "Warm"
    elif pct <= 0.50:
        closeness = "Cold 🧊"
    else:
        closeness = "Very cold ❄️"

    hint_text = f"{closeness} — go {direction}."

    # Extra hint: tell them if they're in the top or bottom half of the range
    if attempts_left <= 2:
        midpoint = (low + high) // 2
        half = "upper half" if secret > midpoint else "lower half"
        hint_text += f" (The number is in the {half}.)"

    return hint_text


# =============================================================================
# MAIN GAME LOOP
# =============================================================================

def play_round(high_scores):
    """
    Run one full round of the game.

    Parameters:
        high_scores (dict): Shared score table to update if the player wins.
    """
    # --- Setup ---
    low, high, max_attempts, diff_name = get_difficulty()
    secret = random.randint(low, high)   # pick a random secret number

    print()
    print(f"  A number between {low} and {high} has been chosen.")
    print(f"  You have {max_attempts} attempts. Good luck!\n")

    attempts_used = 0
    won           = False

    # --- Guessing loop ---
    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        print(f"  Attempts remaining: {remaining}")

        guess         = get_guess(low, high)
        attempts_used += 1

        if guess == secret:
            won = True
            break
        else:
            attempts_left = max_attempts - attempts_used
            print(f"  {hint(guess, secret, low, high, attempts_left)}\n")

    # --- Outcome ---
    print()
    if won:
        score = calculate_score(attempts_used, max_attempts, diff_name)
        print(f"  ✅ Correct! The number was {secret}.")
        print(f"  You guessed it in {attempts_used} attempt(s). Score: {score}")

        # Update high score for this difficulty
        if score > high_scores.get(diff_name, 0):
            high_scores[diff_name] = score
            print(f"  🏆 New high score for {diff_name}!")
    else:
        print(f"  ❌ Out of attempts! The secret number was {secret}.")

    # --- Show current high scores ---
    print()
    print("  High scores:")
    for d in ("easy", "medium", "hard"):
        s = high_scores.get(d, 0)
        print(f"    {d:<8}: {s}")


def main():
    print("=" * 50)
    print("        Number Guessing Game")
    print("=" * 50)
    print()

    high_scores = {}   # stores best score per difficulty this session

    while True:
        play_round(high_scores)
        print()
        again = input("Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
