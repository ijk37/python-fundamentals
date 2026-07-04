"""
Project 03-10: Caesar Cipher
==============================
Topics: strings, ord(), chr(), functions, for loop,
        modular arithmetic, while loop, input validation
Difficulty: Beginner

The Caesar cipher shifts each letter in a message by a fixed
number of positions in the alphabet. This program can both
encrypt and decrypt any text, and also brute-force all 25
possible shifts to crack an unknown cipher.
"""


# =============================================================================
# CONSTANTS
# =============================================================================

ALPHABET_SIZE = 26   # number of letters (a–z)


# =============================================================================
# CORE CIPHER LOGIC
# =============================================================================

def caesar_encrypt(text, shift):
    """
    Encrypt text using the Caesar cipher.

    Each letter is shifted forward by `shift` positions.
    Non-letter characters (spaces, punctuation, digits) are kept as-is.

    Example:
        caesar_encrypt("Hello!", 3)  →  "Khoor!"
    """
    # Normalise shift to the range [0, 25]
    shift = shift % ALPHABET_SIZE

    result = []
    for char in text:
        if char.isalpha():
            # Work out which 'base' to use: ord('a') or ord('A')
            base = ord('a') if char.islower() else ord('A')

            # Shift the letter and wrap around with modulo
            # ord(char) - base  →  position 0–25 within the alphabet
            shifted = (ord(char) - base + shift) % ALPHABET_SIZE
            result.append(chr(base + shifted))
        else:
            result.append(char)   # leave non-letters unchanged

    return "".join(result)


def caesar_decrypt(text, shift):
    """
    Decrypt text that was encrypted with the Caesar cipher.

    Decrypting is just encrypting with the opposite shift.
    """
    # Shifting by (ALPHABET_SIZE - shift) is equivalent to shifting backwards
    return caesar_encrypt(text, ALPHABET_SIZE - shift)


def brute_force(ciphertext):
    """
    Try all 25 possible shifts and print each result.

    Useful when the original shift is unknown.
    """
    print()
    print("─" * 55)
    print(f"  {'Shift':<8} Decrypted text")
    print("─" * 55)

    for shift in range(1, ALPHABET_SIZE):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"  {shift:<8} {decrypted}")

    print("─" * 55)


# =============================================================================
# HELPER: ASK FOR SHIFT
# =============================================================================

def ask_shift():
    """Prompt for a valid shift (1–25) and return it as an integer."""
    while True:
        raw = input("  Enter shift (1–25): ").strip()
        try:
            shift = int(raw)
            if 1 <= shift <= 25:
                return shift
            else:
                print("  Shift must be between 1 and 25.")
        except ValueError:
            print("  Please enter a whole number.")


# =============================================================================
# DISPLAY
# =============================================================================

def show_result(label, text):
    """Print a labelled result in a box."""
    print()
    print("─" * 55)
    print(f"  {label}")
    print(f"  {text}")
    print("─" * 55)
    print()


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 50)
    print("          Caesar Cipher")
    print("=" * 50)
    print("  A cipher that shifts each letter by a fixed amount.")
    print()

    while True:
        print("Options:")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Brute-force all shifts")
        print("  4. Quit")
        print()

        choice = input("Choose (1–4): ").strip()

        if choice == "1":
            text  = input("  Enter message to encrypt: ")
            shift = ask_shift()
            result = caesar_encrypt(text, shift)
            show_result(f"Encrypted (shift {shift}):", result)

        elif choice == "2":
            text  = input("  Enter message to decrypt: ")
            shift = ask_shift()
            result = caesar_decrypt(text, shift)
            show_result(f"Decrypted (shift {shift}):", result)

        elif choice == "3":
            text = input("  Enter the ciphertext to crack: ")
            brute_force(text)

        elif choice == "4":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
