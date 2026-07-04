"""
Project 03-11: Text Statistics Analyzer
==========================================
Topics: strings, Counter, dicts, comprehensions,
        str methods, sorted(), for loop, functions
Difficulty: Beginner–Intermediate

Takes a block of text (from the user or a file) and
produces a detailed statistics report: word count,
sentence count, character frequencies, top words,
average word length, and more.
"""

import string
from collections import Counter


# =============================================================================
# CONSTANTS
# =============================================================================

TOP_N_WORDS  = 10   # number of most-frequent words to display
TOP_N_CHARS  = 8    # number of most-frequent letters to display
STOP_WORDS   = {
    # Common English words that don't add meaning to word-frequency analysis
    "the", "a", "an", "and", "or", "but", "in", "on", "at",
    "to", "for", "of", "with", "is", "are", "was", "were",
    "it", "this", "that", "be", "by", "as", "i", "you",
    "he", "she", "we", "they", "not", "so", "if", "from",
}


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def clean_word(word):
    """
    Remove punctuation from both ends of a word and lowercase it.
    Example: '"Hello,"' → 'hello'
    """
    return word.strip(string.punctuation).lower()


def count_sentences(text):
    """
    Count sentences by counting sentence-ending punctuation: . ! ?
    This is a simple approximation (not perfect for abbreviations).
    """
    return sum(1 for char in text if char in ".!?")


def analyse_text(text):
    """
    Analyse the text and return a dict of statistics.

    Returns:
        dict with keys: char_count, letter_count, word_count,
                        sentence_count, avg_word_len,
                        word_freq (Counter), letter_freq (Counter)
    """
    # ── Character stats ──────────────────────────────────────────
    char_count   = len(text)
    letter_count = sum(1 for c in text if c.isalpha())
    digit_count  = sum(1 for c in text if c.isdigit())
    space_count  = text.count(" ")

    # ── Word stats ───────────────────────────────────────────────
    raw_words  = text.split()
    # clean_word strips punctuation; filter out empty strings
    words      = [clean_word(w) for w in raw_words if clean_word(w)]
    word_count = len(words)

    # ── Sentence stats ───────────────────────────────────────────
    sentence_count = count_sentences(text) or 1   # avoid division by zero

    # ── Average word length ──────────────────────────────────────
    if words:
        avg_word_len = sum(len(w) for w in words) / len(words)
    else:
        avg_word_len = 0

    # ── Word frequency (exclude common stop words) ───────────────
    meaningful_words = [w for w in words if w not in STOP_WORDS]
    word_freq        = Counter(meaningful_words)

    # ── Letter frequency (alphabetic only, lowercase) ────────────
    letters    = [c.lower() for c in text if c.isalpha()]
    letter_freq = Counter(letters)

    # ── Longest and shortest words ───────────────────────────────
    unique_words = list(set(words))
    longest  = max(unique_words, key=len) if unique_words else ""
    shortest = min(unique_words, key=len) if unique_words else ""

    return {
        "char_count":     char_count,
        "letter_count":   letter_count,
        "digit_count":    digit_count,
        "space_count":    space_count,
        "word_count":     word_count,
        "sentence_count": sentence_count,
        "avg_word_len":   avg_word_len,
        "word_freq":      word_freq,
        "letter_freq":    letter_freq,
        "longest_word":   longest,
        "shortest_word":  shortest,
    }


# =============================================================================
# DISPLAY FUNCTIONS
# =============================================================================

def print_overview(stats):
    """Print the overview / summary section of the report."""
    print()
    print("═" * 50)
    print("  TEXT STATISTICS REPORT")
    print("═" * 50)
    print(f"  Total characters  : {stats['char_count']:,}")
    print(f"  Letters           : {stats['letter_count']:,}")
    print(f"  Digits            : {stats['digit_count']:,}")
    print(f"  Spaces            : {stats['space_count']:,}")
    print(f"  Words             : {stats['word_count']:,}")
    print(f"  Sentences         : {stats['sentence_count']:,}")
    print(f"  Words per sentence: {stats['word_count']/stats['sentence_count']:.1f}")
    print(f"  Avg word length   : {stats['avg_word_len']:.1f} letters")
    print(f"  Longest word      : {stats['longest_word']}")
    print(f"  Shortest word     : {stats['shortest_word']}")


def print_top_words(word_freq, n=TOP_N_WORDS):
    """Print the top-N most frequent (meaningful) words with a bar chart."""
    print()
    print("─" * 50)
    print(f"  TOP {n} WORDS (stop words excluded)")
    print("─" * 50)

    top_words = word_freq.most_common(n)
    if not top_words:
        print("  No meaningful words found.")
        return

    max_count = top_words[0][1]   # the highest frequency

    for word, count in top_words:
        # Scale bar to 20 characters max
        bar_len = int(count / max_count * 20)
        bar     = "█" * bar_len
        print(f"  {word:<18} {count:>4}  {bar}")


def print_letter_freq(letter_freq, n=TOP_N_CHARS):
    """Print the top-N most frequent letters with a mini bar chart."""
    print()
    print("─" * 50)
    print(f"  TOP {n} LETTERS")
    print("─" * 50)

    top_letters = letter_freq.most_common(n)
    if not top_letters:
        print("  No letters found.")
        return

    max_count = top_letters[0][1]

    for letter, count in top_letters:
        bar_len = int(count / max_count * 20)
        bar     = "█" * bar_len
        print(f"  '{letter}'  {count:>5}  {bar}")

    print()


# =============================================================================
# INPUT: TEXT FROM USER OR FILE
# =============================================================================

def get_text_from_user():
    """Prompt user to type or paste a block of text."""
    print("  Enter/paste your text. Type 'END' on a new line when done.")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def get_text_from_file():
    """Ask for a file path and read its contents."""
    while True:
        path = input("  File path: ").strip().strip('"')
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"  File not found: {path}")
        except OSError as e:
            print(f"  Error reading file: {e}")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 50)
    print("       Text Statistics Analyzer")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Analyse typed/pasted text")
        print("  2. Analyse a text file")
        print("  3. Quit")
        print()

        choice = input("Choose (1–3): ").strip()

        if choice == "1":
            text = get_text_from_user()
        elif choice == "2":
            text = get_text_from_file()
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("  Invalid choice.")
            continue

        if not text.strip():
            print("  No text provided.\n")
            continue

        stats = analyse_text(text)
        print_overview(stats)
        print_top_words(stats["word_freq"])
        print_letter_freq(stats["letter_freq"])


if __name__ == "__main__":
    main()
