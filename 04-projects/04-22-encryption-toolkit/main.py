"""
Project 03-30: Encryption Toolkit
====================================
Topics: Caesar cipher, Vigenère cipher, ord()/chr(),
        modular arithmetic, string methods, functions
Difficulty: Intermediate

Implements three classical text encryption techniques:
1. Caesar cipher    — single-shift substitution
2. Vigenère cipher  — multi-key poly-alphabetic substitution
3. ROT13            — fixed 13-shift (self-reversing)

Also includes a frequency analysis tool for cracking ciphers.
"""

import string
from collections import Counter


# =============================================================================
# CONSTANTS
# =============================================================================

ALPHABET_SIZE = 26
ALPHABET_LOWER = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase


# =============================================================================
# CAESAR CIPHER
# =============================================================================

def caesar(text, shift, decrypt=False):
    """
    Encrypt or decrypt using Caesar cipher.

    Parameters:
        text    (str):  Input text (any characters)
        shift   (int):  Number of positions to shift (1–25)
        decrypt (bool): If True, shift backwards instead

    How it works:
        1. For each letter, find its 0-based position (ord(c) - ord('a'))
        2. Add or subtract the shift
        3. Wrap around using modulo 26
        4. Convert back to a character with chr()
    """
    if decrypt:
        shift = -shift   # decrypting = encrypting with negative shift

    result = []
    for char in text:
        if char.isalpha():
            base    = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % ALPHABET_SIZE
            result.append(chr(base + shifted))
        else:
            result.append(char)   # non-letters pass through unchanged

    return "".join(result)


# =============================================================================
# ROT13
# =============================================================================

def rot13(text):
    """
    ROT13 is a special Caesar cipher with shift=13.
    It's self-reversing: applying it twice gives the original.
    """
    return caesar(text, 13)


# =============================================================================
# VIGENÈRE CIPHER
# =============================================================================

def vigenere(text, key, decrypt=False):
    """
    Vigenère cipher: each letter uses a different shift based on the key.

    The key is repeated to match the length of the message.
    Example: key="KEY", message="HELLO"
        H → shifted by K(10) = R
        E → shifted by E(4)  = I
        L → shifted by Y(24) = J
        L → shifted by K(10) = V (key wraps: position 3 → key[3 % 3] = K)
        O → shifted by E(4)  = S

    Parameters:
        text    (str):  Input text
        key     (str):  Encryption key (letters only)
        decrypt (bool): If True, reverse shifts

    The key position only advances for alphabetic characters.
    """
    key        = key.lower()
    key_len    = len(key)
    key_index  = 0   # tracks position in key (advances only on letters)
    result     = []

    for char in text:
        if char.isalpha():
            # Determine the shift from the current key character
            key_shift = ord(key[key_index % key_len]) - ord('a')
            if decrypt:
                key_shift = -key_shift

            base    = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + key_shift) % ALPHABET_SIZE
            result.append(chr(base + shifted))
            key_index += 1   # advance key only for letters
        else:
            result.append(char)

    return "".join(result)


# =============================================================================
# FREQUENCY ANALYSIS (CIPHER CRACKING TOOL)
# =============================================================================

def frequency_analysis(ciphertext, top_n=5):
    """
    Analyse letter frequencies in the ciphertext.

    In English, 'e' is the most common letter (~12.7%).
    If we find the most common letter in the cipher, the shift
    is likely (cipher_letter - 'e') mod 26.

    Returns:
        list of (letter, count, percentage) tuples for top_n letters
    """
    letters = [c.lower() for c in ciphertext if c.isalpha()]
    if not letters:
        return []

    freq   = Counter(letters)
    total  = len(letters)
    result = [(letter, count, 100 * count / total)
              for letter, count in freq.most_common(top_n)]
    return result


def guess_caesar_shift(ciphertext):
    """
    Guess the most likely Caesar shift by assuming the most common
    ciphertext letter corresponds to 'e' (most common English letter).
    Returns a list of (probable_shift, decrypted_preview) tuples.
    """
    letters = [c.lower() for c in ciphertext if c.isalpha()]
    if not letters:
        return []

    freq = Counter(letters)
    most_common_letter = freq.most_common(1)[0][0]

    # If 'e' was shifted to `most_common_letter`, shift = (cipher_pos - e_pos) mod 26
    probable_shift = (ord(most_common_letter) - ord('e')) % ALPHABET_SIZE

    # Also check ±1 around the probable shift
    guesses = []
    for s in [probable_shift, (probable_shift + 1) % 26, (probable_shift - 1) % 26]:
        decrypted = caesar(ciphertext, s, decrypt=True)
        guesses.append((s, decrypted[:50]))   # show first 50 chars

    return guesses


# =============================================================================
# DISPLAY
# =============================================================================

def show_result(label, text):
    print()
    print("─" * 55)
    print(f"  {label}")
    # Wrap long text for readability
    for i in range(0, len(text), 70):
        print(f"  {text[i:i+70]}")
    print("─" * 55)
    print()


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 55)
    print("           Encryption Toolkit")
    print("=" * 55)
    print("  Classical cipher implementations in pure Python.")
    print()

    while True:
        print("Options:")
        print("  1. Caesar cipher — encrypt")
        print("  2. Caesar cipher — decrypt")
        print("  3. ROT13")
        print("  4. Vigenère cipher — encrypt")
        print("  5. Vigenère cipher — decrypt")
        print("  6. Frequency analysis")
        print("  7. Guess Caesar shift (crack)")
        print("  8. Quit")
        print()

        choice = input("Choose (1–8): ").strip()

        if choice in ("1", "2"):
            text = input("  Text: ")
            try:
                shift = int(input("  Shift (1–25): "))
            except ValueError:
                shift = 3
            result = caesar(text, shift, decrypt=(choice == "2"))
            label  = "Encrypted" if choice == "1" else "Decrypted"
            show_result(f"{label} (shift={shift}):", result)

        elif choice == "3":
            text   = input("  Text: ")
            result = rot13(text)
            show_result("ROT13:", result)
            print("  (Apply ROT13 again to reverse it.)")

        elif choice in ("4", "5"):
            text = input("  Text: ")
            key  = input("  Key (letters only): ").strip()
            if not key.isalpha():
                print("  Key must contain only letters.\n")
                continue
            result = vigenere(text, key, decrypt=(choice == "5"))
            label  = "Encrypted" if choice == "4" else "Decrypted"
            show_result(f"Vigenère {label} (key='{key}'):", result)

        elif choice == "6":
            text = input("  Ciphertext: ")
            freq = frequency_analysis(text)
            if freq:
                print(f"\n  Letter Frequencies:")
                for letter, count, pct in freq:
                    bar = "█" * int(pct / 2)
                    print(f"  '{letter}': {count:>4} ({pct:>5.1f}%)  {bar}")
            else:
                print("  No letters found.\n")

        elif choice == "7":
            text   = input("  Ciphertext to crack: ")
            guesses = guess_caesar_shift(text)
            print(f"\n  Most likely shifts:")
            for shift, preview in guesses:
                print(f"  Shift {shift:>2}: {preview}")
            print()

        elif choice == "8":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
