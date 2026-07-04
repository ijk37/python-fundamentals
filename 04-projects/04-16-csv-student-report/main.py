"""
Project 03-16: CSV Student Report
====================================
Topics: csv module, DictReader, DictWriter, filtering,
        sorting, functions, pathlib, type conversion
Difficulty: Intermediate

Reads student scores from a CSV file, calculates averages
and grades, filters by grade, and saves a summary report
to a new CSV file.
"""

import csv
from pathlib import Path


# =============================================================================
# CONSTANTS
# =============================================================================

INPUT_FILE  = Path("students.csv")
OUTPUT_FILE = Path("student_report.csv")

# Grade scale: (minimum score, letter grade, GPA points)
GRADE_SCALE = [
    (90, "A+", 4.0),
    (85, "A",  4.0),
    (80, "A-", 3.7),
    (75, "B+", 3.3),
    (70, "B",  3.0),
    (65, "B-", 2.7),
    (60, "C+", 2.3),
    (55, "C",  2.0),
    (50, "D",  1.0),
    (0,  "F",  0.0),
]

PASS_SCORE = 50   # below this → fail


# =============================================================================
# GRADE HELPERS
# =============================================================================

def score_to_grade(average):
    """Return (letter_grade, gpa) for the given average score."""
    for minimum, letter, gpa in GRADE_SCALE:
        if average >= minimum:
            return letter, gpa
    return "F", 0.0


# =============================================================================
# SAMPLE DATA CREATION
# =============================================================================

def create_sample_csv():
    """
    Write a sample students.csv file if it does not already exist.
    This function exists so the project works without needing an external file.
    """
    if INPUT_FILE.exists():
        return   # don't overwrite if the file is already there

    sample_rows = [
        ["Name",       "Math", "English", "Science", "History", "ICT"],
        ["Rahim",        88,      72,        90,        81,       85],
        ["Karim",        55,      60,        50,        45,       70],
        ["Nasrin",       92,      88,        95,        91,       93],
        ["Arif",         70,      65,        68,        72,       75],
        ["Salma",        40,      38,        45,        50,       42],
        ["Tanvir",       80,      77,        82,        79,       85],
        ["Riya",         95,      92,        98,        94,       97],
        ["Hasan",        62,      58,        66,        60,       64],
    ]

    with open(INPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(sample_rows)

    print(f"  Created sample file: {INPUT_FILE}")


# =============================================================================
# READING AND PROCESSING
# =============================================================================

def read_students(filepath=INPUT_FILE):
    """
    Read students.csv and return a list of student dicts.

    Each dict has:
        name, scores (list of float), average, grade, gpa, status
    """
    students = []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # DictReader uses the first row as header → each row is a dict

        for row in reader:
            name = row["Name"]

            # Subject columns: everything except "Name"
            subject_names = [col for col in row if col != "Name"]

            # Convert string scores to floats; skip blank cells
            scores = []
            for subj in subject_names:
                try:
                    scores.append(float(row[subj]))
                except (ValueError, KeyError):
                    pass   # ignore missing or non-numeric values

            if not scores:
                continue   # skip rows with no scores

            average      = sum(scores) / len(scores)
            letter, gpa  = score_to_grade(average)
            status       = "PASS" if average >= PASS_SCORE else "FAIL"

            students.append({
                "name":    name,
                "scores":  scores,
                "average": round(average, 1),
                "grade":   letter,
                "gpa":     gpa,
                "status":  status,
            })

    return students


# =============================================================================
# FILTERING AND SORTING
# =============================================================================

def filter_by_grade(students, grade):
    """Return only students with the specified letter grade."""
    return [s for s in students if s["grade"] == grade.upper()]


def filter_passing(students):
    """Return only passing students."""
    return [s for s in students if s["status"] == "PASS"]


def sort_students(students, by="average", descending=True):
    """Sort students by 'average', 'name', 'gpa', or 'grade'."""
    if by == "name":
        return sorted(students, key=lambda s: s["name"].lower(),
                      reverse=not descending)
    else:
        return sorted(students, key=lambda s: s[by], reverse=descending)


# =============================================================================
# SAVING REPORT
# =============================================================================

def save_report(students, filepath=OUTPUT_FILE):
    """
    Write a summary CSV with: Name, Average, Grade, GPA, Status.
    Uses csv.DictWriter for clean column headers.
    """
    fieldnames = ["Name", "Average", "Grade", "GPA", "Status"]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()   # writes the header row

        for s in students:
            writer.writerow({
                "Name":    s["name"],
                "Average": s["average"],
                "Grade":   s["grade"],
                "GPA":     s["gpa"],
                "Status":  s["status"],
            })

    print(f"  ✅ Report saved to {filepath}")


# =============================================================================
# DISPLAY
# =============================================================================

def print_report(students, title="Student Report"):
    """Print all students in a formatted table."""
    if not students:
        print("  No students to display.\n")
        return

    print()
    print(f"  {title}")
    print(f"  {'Name':<15} {'Avg':>6}  {'Grade':<6}  {'GPA':>5}  Status")
    print("  " + "─" * 48)

    for s in students:
        status_icon = "✅" if s["status"] == "PASS" else "❌"
        print(f"  {s['name']:<15} {s['average']:>6.1f}  {s['grade']:<6}  "
              f"{s['gpa']:>5.1f}  {status_icon} {s['status']}")

    print("  " + "─" * 48)
    avg_of_class = sum(s["average"] for s in students) / len(students)
    passes       = sum(1 for s in students if s["status"] == "PASS")
    print(f"  Total: {len(students)} students  |  "
          f"Class avg: {avg_of_class:.1f}  |  "
          f"Pass rate: {passes}/{len(students)}")
    print()


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 50)
    print("       CSV Student Report Generator")
    print("=" * 50)

    create_sample_csv()

    try:
        students = read_students()
    except FileNotFoundError:
        print(f"  ❌ Cannot find {INPUT_FILE}. Please create it first.")
        return

    while True:
        print("\nOptions:")
        print("  1. Show all students (sorted by average)")
        print("  2. Show only passing students")
        print("  3. Filter by grade (e.g. A+, B)")
        print("  4. Sort by name")
        print("  5. Save report CSV")
        print("  6. Quit")
        print()

        choice = input("Choose (1–6): ").strip()

        if choice == "1":
            print_report(sort_students(students), "All Students — Sorted by Average")

        elif choice == "2":
            passing = filter_passing(students)
            print_report(sort_students(passing), "Passing Students")

        elif choice == "3":
            grade   = input("  Enter grade (e.g. A+, B, C): ").strip()
            filtered = filter_by_grade(students, grade)
            print_report(filtered, f"Students with grade {grade.upper()}")

        elif choice == "4":
            print_report(sort_students(students, by="name"), "Students — A to Z")

        elif choice == "5":
            save_report(sort_students(students))

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
