"""
Project 03-20: Quiz Game (JSON-backed)
=========================================
Topics: JSON file, random, score tracking, functions,
        while loop, dicts, lists, time module
Difficulty: Intermediate

Loads multiple-choice questions from a JSON file.
Supports category selection, timed questions, high-score
tracking, and per-question explanations.
"""

import json
import random
import time
from pathlib import Path


# =============================================================================
# CONSTANTS
# =============================================================================

QUESTIONS_FILE = Path("questions.json")
SCORES_FILE    = Path("high_scores.json")
PASS_SCORE_PCT = 60   # score % needed to "pass"


# =============================================================================
# SAMPLE QUESTIONS DATA
# =============================================================================

SAMPLE_QUESTIONS = [
    {
        "id": 1, "category": "Python Basics",
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B",
        "explanation": "'def' is Python's keyword for defining a function."
    },
    {
        "id": 2, "category": "Python Basics",
        "question": "What is the output of: print(type(3.14))?",
        "options": ["A. int", "B. str", "C. float", "D. double"],
        "answer": "C",
        "explanation": "3.14 is a floating-point number, so type() returns <class 'float'>."
    },
    {
        "id": 3, "category": "Python Basics",
        "question": "Which of these creates an empty list?",
        "options": ["A. list = {}", "B. list = ()", "C. list = []", "D. list = <>"],
        "answer": "C",
        "explanation": "Square brackets [] create a list. {} is a dict/set, () is a tuple."
    },
    {
        "id": 4, "category": "Data Structures",
        "question": "What method removes and returns the last item from a list?",
        "options": ["A. remove()", "B. delete()", "C. pop()", "D. discard()"],
        "answer": "C",
        "explanation": "list.pop() removes and returns the last item. pop(i) removes index i."
    },
    {
        "id": 5, "category": "Data Structures",
        "question": "Which data structure uses key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D",
        "explanation": "A dictionary (dict) stores key-value pairs: {'key': 'value'}."
    },
    {
        "id": 6, "category": "Data Structures",
        "question": "Which collection type is immutable (cannot be changed)?",
        "options": ["A. List", "B. Set", "C. Dict", "D. Tuple"],
        "answer": "D",
        "explanation": "Tuples are immutable: once created, their items cannot be changed."
    },
    {
        "id": 7, "category": "Control Flow",
        "question": "What does the 'break' statement do inside a loop?",
        "options": [
            "A. Skips the current iteration",
            "B. Exits the loop immediately",
            "C. Restarts the loop",
            "D. Pauses the program"
        ],
        "answer": "B",
        "explanation": "'break' exits the nearest enclosing loop immediately."
    },
    {
        "id": 8, "category": "Control Flow",
        "question": "What does 'continue' do inside a loop?",
        "options": [
            "A. Exits the loop",
            "B. Restarts the entire program",
            "C. Skips to the next iteration",
            "D. None of the above"
        ],
        "answer": "C",
        "explanation": "'continue' skips the rest of the current loop body and goes to the next iteration."
    },
    {
        "id": 9, "category": "Functions",
        "question": "What does *args allow in a function definition?",
        "options": [
            "A. Arbitrary keyword arguments",
            "B. Arbitrary positional arguments",
            "C. Default argument values",
            "D. Only one argument"
        ],
        "answer": "B",
        "explanation": "*args collects extra positional arguments into a tuple."
    },
    {
        "id": 10, "category": "Functions",
        "question": "What is a lambda function?",
        "options": [
            "A. A function defined with the 'lambda' module",
            "B. A multi-line anonymous function",
            "C. A single-expression anonymous function",
            "D. A function that returns None"
        ],
        "answer": "C",
        "explanation": "lambda is an anonymous (unnamed) function limited to a single expression."
    },
    {
        "id": 11, "category": "File I/O",
        "question": "Which mode opens a file for appending without overwriting?",
        "options": ["A. 'r'", "B. 'w'", "C. 'a'", "D. 'x'"],
        "answer": "C",
        "explanation": "'a' mode appends to the end of the file; 'w' overwrites it."
    },
    {
        "id": 12, "category": "File I/O",
        "question": "Which module provides an object-oriented path API?",
        "options": ["A. os", "B. sys", "C. shutil", "D. pathlib"],
        "answer": "D",
        "explanation": "pathlib.Path provides an OOP interface to file-system paths."
    },
]


# =============================================================================
# FILE OPERATIONS
# =============================================================================

def create_questions_file():
    """Write the sample questions to the JSON file if it doesn't exist."""
    if not QUESTIONS_FILE.exists():
        with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(SAMPLE_QUESTIONS, f, indent=2, ensure_ascii=False)
        print(f"  Created: {QUESTIONS_FILE}")


def load_questions():
    """Load questions from the JSON file and return as a list."""
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_scores():
    """Load high scores dict from file, or return empty dict."""
    if not SCORES_FILE.exists():
        return {}
    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_scores(scores):
    """Save the high scores dict to file."""
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2)


def update_high_score(name, score, total):
    """
    Update the high score for a player name.
    Only saves if the new score is better than the stored one.
    """
    scores      = load_scores()
    pct         = round(100 * score / total, 1)
    current     = scores.get(name, {}).get("pct", 0)

    if pct > current:
        scores[name] = {"score": score, "total": total, "pct": pct}
        save_scores(scores)
        return True   # new high score

    return False


# =============================================================================
# QUIZ LOGIC
# =============================================================================

def filter_by_category(questions, category):
    """Return only questions matching the given category."""
    cat = category.lower()
    return [q for q in questions if q["category"].lower() == cat]


def ask_question(q, number, total, timed=False):
    """
    Display a question and collect the answer.

    Parameters:
        q      (dict): Question dict
        number (int):  Question number (1-based)
        total  (int):  Total questions in this quiz
        timed  (bool): Whether to show elapsed time

    Returns:
        (bool, float): (is_correct, seconds_taken)
    """
    print()
    print(f"  Question {number}/{total} — {q['category']}")
    print(f"  {q['question']}")
    print()
    for option in q["options"]:
        print(f"    {option}")
    print()

    start = time.time()
    answer = input("  Your answer (A/B/C/D): ").strip().upper()
    elapsed = time.time() - start

    is_correct = (answer == q["answer"])

    if is_correct:
        print(f"  ✅ Correct!")
    else:
        print(f"  ❌ Wrong. The answer was: {q['answer']}")

    print(f"  💡 {q['explanation']}")

    if timed:
        print(f"  ⏱  Time: {elapsed:.1f}s")

    return is_correct, elapsed


def run_quiz(questions, player_name, timed=False):
    """
    Run the quiz and return the final score.

    Parameters:
        questions   (list): Questions to ask
        player_name (str):  Player's name for high score
        timed       (bool): Whether to track time

    Returns:
        (int, int): (score, total)
    """
    random.shuffle(questions)   # randomise order each time
    score       = 0
    total_time  = 0

    for i, q in enumerate(questions, 1):
        correct, elapsed = ask_question(q, i, len(questions), timed)
        if correct:
            score += 1
        total_time += elapsed

    # ── Final result ─────────────────────────────────────────────
    pct    = round(100 * score / len(questions))
    status = "PASS ✅" if pct >= PASS_SCORE_PCT else "FAIL ❌"

    print()
    print("═" * 45)
    print(f"  Quiz complete, {player_name}!")
    print(f"  Score : {score} / {len(questions)} ({pct}%)  {status}")
    if timed:
        print(f"  Total time: {total_time:.1f}s  |  "
              f"Avg: {total_time/len(questions):.1f}s per question")
    print("═" * 45)

    new_high = update_high_score(player_name, score, len(questions))
    if new_high:
        print("  🏆 New high score!")

    return score, len(questions)


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 50)
    print("            Python Quiz Game")
    print("=" * 50)

    create_questions_file()
    all_questions = load_questions()

    # Get unique categories
    categories = sorted(set(q["category"] for q in all_questions))

    player_name = input("\n  Enter your name: ").strip() or "Player"

    while True:
        print("\nOptions:")
        print("  1. Start quiz (all categories)")
        print("  2. Quiz by category")
        print("  3. Quick quiz (5 random questions)")
        print("  4. Timed quiz")
        print("  5. View high scores")
        print("  6. Quit")
        print()

        choice = input("Choose (1–6): ").strip()

        if choice == "1":
            run_quiz(list(all_questions), player_name)

        elif choice == "2":
            print("\n  Categories:")
            for i, cat in enumerate(categories, 1):
                print(f"    {i}. {cat}")
            try:
                idx = int(input("  Choose category number: ").strip()) - 1
                cat = categories[idx]
            except (ValueError, IndexError):
                print("  Invalid choice.\n")
                continue
            filtered = filter_by_category(all_questions, cat)
            if not filtered:
                print("  No questions in that category.\n")
            else:
                run_quiz(filtered, player_name)

        elif choice == "3":
            subset = random.sample(all_questions, min(5, len(all_questions)))
            run_quiz(subset, player_name)

        elif choice == "4":
            run_quiz(list(all_questions), player_name, timed=True)

        elif choice == "5":
            scores = load_scores()
            if not scores:
                print("  No high scores yet.\n")
            else:
                print()
                print(f"  {'Name':<20} {'Score':<10} {'%':>6}")
                print("  " + "─" * 38)
                # Sort by percentage descending
                for name, data in sorted(scores.items(),
                                          key=lambda x: x[1]["pct"], reverse=True):
                    print(f"  {name:<20} {data['score']}/{data['total']:<6} "
                          f"{data['pct']:>5}%")
                print()

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
