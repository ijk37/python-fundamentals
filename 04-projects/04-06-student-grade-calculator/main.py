"""
Project 03-06: Student Grade Calculator
==========================================
Topics: lists, tuples, dicts, functions, if/elif, for loop,
        accumulation pattern, f-strings, input validation
Difficulty: Beginner–Intermediate

Accepts multiple subjects and marks for one or more students,
calculates averages and letter grades, and prints a report card.
"""


# =============================================================================
# GRADING SCALE
# =============================================================================

# List of (minimum_score, letter_grade, gpa_points) tuples.
# Checked top-down; the first condition that matches is used.
GRADE_SCALE = [
    (90, "A+", 4.0),
    (85, "A",  4.0),
    (80, "A-", 3.7),
    (75, "B+", 3.3),
    (70, "B",  3.0),
    (65, "B-", 2.7),
    (60, "C+", 2.3),
    (55, "C",  2.0),
    (50, "C-", 1.7),
    (45, "D",  1.0),
    ( 0, "F",  0.0),
]


# =============================================================================
# CORE FUNCTIONS
# =============================================================================

def score_to_grade(score):
    """
    Convert a numeric score to a (letter_grade, gpa_points) tuple.

    Works by iterating GRADE_SCALE top-down and returning the first
    row where score >= minimum.
    """
    for minimum, letter, gpa in GRADE_SCALE:
        if score >= minimum:
            return letter, gpa
    # Safety fallback (should never reach here because 0 is in scale)
    return "F", 0.0


def average(scores):
    """
    Calculate the arithmetic mean of a list of numbers.

    Returns 0 if the list is empty to avoid ZeroDivisionError.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def build_student(name, subjects, scores):
    """
    Create a student record as a dictionary.

    Parameters:
        name     (str):   Student's name.
        subjects (list):  List of subject names.
        scores   (list):  List of corresponding numeric scores.

    Returns:
        dict: Student record with computed grades.
    """
    # Combine subjects and scores into a list of (subject, score, letter, gpa)
    results = []
    for subject, score in zip(subjects, scores):
        letter, gpa = score_to_grade(score)
        results.append((subject, score, letter, gpa))

    avg_score  = average(scores)
    avg_letter, avg_gpa = score_to_grade(avg_score)

    return {
        "name":       name,
        "results":    results,       # list of tuples
        "average":    avg_score,
        "grade":      avg_letter,
        "gpa":        avg_gpa,
        "passed":     avg_score >= 50,
    }


# =============================================================================
# DISPLAY
# =============================================================================

def print_report_card(student):
    """Print a formatted report card for one student."""
    width = 52
    print()
    print("═" * width)
    print(f"  REPORT CARD — {student['name'].upper()}")
    print("─" * width)

    # Table header
    print(f"  {'Subject':<20} {'Score':>6}  {'Grade':>5}  {'GPA':>4}")
    print("─" * width)

    # One row per subject
    for subject, score, letter, gpa in student["results"]:
        # Highlight failing subjects with an asterisk
        flag = " *" if score < 50 else "  "
        print(f"  {subject:<20} {score:>6.1f}  {letter:>5}  {gpa:>4.1f}{flag}")

    print("─" * width)

    # Summary row
    status = "PASS ✅" if student["passed"] else "FAIL ❌"
    print(f"  {'AVERAGE':<20} {student['average']:>6.1f}  "
          f"{student['grade']:>5}  {student['gpa']:>4.1f}  {status}")
    print("═" * width)

    if not student["passed"]:
        print("  * Subject(s) marked with * are below 50.")
    print()


def print_class_summary(students):
    """Print a summary table comparing all students."""
    print()
    print("═" * 55)
    print("  CLASS SUMMARY")
    print("─" * 55)
    print(f"  {'Name':<20} {'Avg':>5}  {'Grade':>5}  {'GPA':>4}  {'Status':>6}")
    print("─" * 55)

    for s in sorted(students, key=lambda x: x["average"], reverse=True):
        status = "Pass" if s["passed"] else "Fail"
        print(f"  {s['name']:<20} {s['average']:>5.1f}  "
              f"{s['grade']:>5}  {s['gpa']:>4.1f}  {status:>6}")

    # Class statistics
    all_avgs    = [s["average"] for s in students]
    class_avg   = average(all_avgs)
    pass_count  = sum(1 for s in students if s["passed"])
    print("─" * 55)
    print(f"  Class average: {class_avg:.1f}   "
          f"Pass rate: {pass_count}/{len(students)}")
    print("═" * 55)


# =============================================================================
# INPUT HELPERS
# =============================================================================

def get_subjects():
    """Ask the user to enter subject names until they type 'done'."""
    subjects = []
    print("  Enter subject names one by one. Type 'done' when finished.")
    while True:
        name = input(f"  Subject {len(subjects)+1}: ").strip().title()
        if name.lower() == "done":
            if len(subjects) == 0:
                print("  Please enter at least one subject.\n")
                continue
            break
        if name:
            subjects.append(name)
    return subjects


def get_scores(subjects):
    """Ask for a score for each subject. Returns a list of floats."""
    scores = []
    for subject in subjects:
        while True:
            try:
                score = float(input(f"  {subject} score (0–100): "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                print("  Score must be between 0 and 100.\n")
            except ValueError:
                print("  Please enter a number.\n")
    return scores


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 52)
    print("        Student Grade Calculator")
    print("=" * 52)
    print()

    # --- Get subjects once (same for all students) ---
    print("Step 1: Enter the subjects for this class.")
    subjects = get_subjects()

    students = []   # list that will hold all student records

    # --- Add students in a loop ---
    while True:
        print()
        print(f"Step 2: Enter a student's name (or 'done' to finish).")
        name = input("  Student name: ").strip().title()

        if name.lower() == "done":
            if not students:
                print("  Please enter at least one student.\n")
                continue
            break

        if not name:
            continue

        print(f"\n  Enter scores for {name}:")
        scores  = get_scores(subjects)
        student = build_student(name, subjects, scores)
        students.append(student)
        print_report_card(student)

    # --- Class summary ---
    if len(students) > 1:
        print_class_summary(students)
    else:
        print("(Only one student — no class summary.)")


if __name__ == "__main__":
    main()
