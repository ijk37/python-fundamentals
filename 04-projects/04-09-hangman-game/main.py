"""
Project 03-09: Hangman Game
==============================
Topics: strings, lists, set, while loop, random,
        for loop, string methods, input validation
Difficulty: Beginner

Classic hangman: the player guesses one letter at a time
to reveal a hidden word before running out of lives.
"""

import random   # for randomly picking a word


# =============================================================================
# WORD LISTS (grouped by category)
# =============================================================================

WORD_LISTS = {
    "animals": [
        "elephant", "penguin", "crocodile", "butterfly",
        "giraffe", "dolphin", "leopard", "mongoose",
    ],
    "countries": [
        "bangladesh", "indonesia", "argentina", "portugal",
        "mozambique", "cambodia", "venezuela", "switzerland",
    ],
    "fruits": [
        "jackfruit", "watermelon", "strawberry", "pineapple",
        "pomegranate", "blueberry", "tangerine", "kiwi",
    ],
    "programming": [
        "python", "variable", "function", "algorithm",
        "exception", "iteration", "comprehension", "dictionary",
    ],
}

# Maximum wrong guesses allowed before the player loses
MAX_WRONG = 6


# =============================================================================
# HANGMAN ART
# =============================================================================

# Each stage adds one body part to the gallows.
# Index 0 = no wrong guesses yet, Index 6 = fully drawn (lose).
HANGMAN_STAGES = [
    # 0 wrong
    """
   ------
   |    |
   |
   |
   |
  ---
""",
    # 1 wrong — head
    """
   ------
   |    |
   |    O
   |
   |
  ---
""",
    # 2 wrong — body
    """
   ------
   |    |
   |    O
   |    |
   |
  ---
""",
    # 3 wrong — left arm
    """
   ------
   |    |
   |    O
   |   /|
   |
  ---
""",
    # 4 wrong — both arms
    """
   ------
   |    |
   |    O
   |   /|\\
   |
  ---
""",
    # 5 wrong — left leg
    """
   ------
   |    |
   |    O
   |   /|\\
   |   /
  ---
""",
    # 6 wrong — both legs (game over)
    """
   ------
   |    |
   |    O
   |   /|\\
   |   / \\
  ---
""",
]


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def choose_word(category):
    """Randomly pick a word from the given category."""
    return random.choice(WORD_LISTS[category])


def build_display(secret_word, guessed_letters):
    """
    Return a list that shows correctly guessed letters and
    underscores for letters not yet guessed.

    Example:
        secret_word = "python", guessed_letters = {'p', 'h', 'o'}
        returns: ['p', '_', '_', 'h', 'o', '_']
    """
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return display


def is_won(secret_word, guessed_letters):
    """Return True if every letter in the word has been guessed."""
    # all() returns True if every character is in the guessed set
    return all(letter in guessed_letters for letter in secret_word)


# =============================================================================
# DISPLAY
# =============================================================================

def print_game_state(secret_word, guessed_letters, wrong_guesses):
    """Print the gallows, current word state, and wrong guess list."""
    print(HANGMAN_STAGES[len(wrong_guesses)])

    # Show letters revealed so far (spaced out for readability)
    display = build_display(secret_word, guessed_letters)
    print("  Word : " + "  ".join(display))
    print(f"  Wrong guesses ({len(wrong_guesses)}/{MAX_WRONG}): "
          + "  ".join(sorted(wrong_guesses)) if wrong_guesses else "  No wrong guesses yet.")
    print()


# =============================================================================
# ONE GAME
# =============================================================================

def play_game(category):
    """
    Run a single round of hangman.
    Returns True if the player won, False if they lost.
    """
    secret_word     = choose_word(category)
    guessed_letters = set()   # use a set for fast membership checks
    wrong_guesses   = set()

    print(f"\n  Category: {category.title()}")
    print(f"  The word has {len(secret_word)} letters.\n")

    while len(wrong_guesses) < MAX_WRONG:
        print_game_state(secret_word, guessed_letters, wrong_guesses)

        # Get a valid single alphabetic letter from the player
        guess = input("  Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("  Please enter a single letter.\n")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print(f"  You already guessed '{guess}'.\n")
            continue

        # Evaluate the guess
        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"  ✅ '{guess}' is in the word!")

            if is_won(secret_word, guessed_letters):
                print_game_state(secret_word, guessed_letters, wrong_guesses)
                print(f"  🎉 Correct! The word was '{secret_word}'.")
                return True   # player won
        else:
            wrong_guesses.add(guess)
            remaining = MAX_WRONG - len(wrong_guesses)
            print(f"  ❌ '{guess}' is not in the word. "
                  f"{remaining} guess(es) remaining.")

    # Ran out of lives
    print(HANGMAN_STAGES[MAX_WRONG])
    print(f"  💀 Game over! The word was '{secret_word}'.")
    return False   # player lost


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 45)
    print("           Hangman Game")
    print("=" * 45)

    categories = list(WORD_LISTS.keys())
    wins   = 0
    games  = 0

    while True:
        print("\nOptions:")
        print("  1. Play")
        print("  2. View score")
        print("  3. Quit")
        print()
        choice = input("Choose (1–3): ").strip()

        if choice == "1":
            # Ask for category
            print("\n  Categories:")
            for i, cat in enumerate(categories, 1):
                print(f"    {i}. {cat.title()}")
            print(f"    {len(categories)+1}. Random")
            print()

            cat_choice = input(f"  Choose (1–{len(categories)+1}): ").strip()
            try:
                idx = int(cat_choice) - 1
                if idx == len(categories):
                    category = random.choice(categories)
                elif 0 <= idx < len(categories):
                    category = categories[idx]
                else:
                    print("  Invalid choice, using random.")
                    category = random.choice(categories)
            except ValueError:
                category = random.choice(categories)

            won = play_game(category)
            games += 1
            if won:
                wins += 1

        elif choice == "2":
            if games == 0:
                print("  No games played yet.")
            else:
                print(f"\n  Score: {wins} win(s) / {games} game(s) "
                      f"({100 * wins // games}%)")

        elif choice == "3":
            print("\nThanks for playing!")
            break

        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
