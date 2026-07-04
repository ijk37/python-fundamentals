"""
Project 03-18: File Organizer
================================
Topics: pathlib, shutil, glob/rglob, dicts,
        functions, while loop, os.path
Difficulty: Intermediate

Scans a directory and moves files into category
sub-folders based on their extensions.
Example: .jpg/.png → Images/, .pdf/.docx → Documents/
"""

import shutil
from pathlib import Path


# =============================================================================
# EXTENSION → CATEGORY MAPPING
# =============================================================================

# Each category name maps to a list of lowercase file extensions.
CATEGORY_MAP = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
    "Videos":     [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Audio":      [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Documents":  [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Archives":   [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Code":       [".py", ".js", ".ts", ".html", ".css", ".json",
                   ".xml", ".java", ".cpp", ".c", ".h", ".sh"],
    "Executables": [".exe", ".msi", ".dmg", ".deb", ".rpm", ".apk"],
    "Fonts":      [".ttf", ".otf", ".woff", ".woff2"],
    "Data":       [".sql", ".db", ".sqlite"],
}


def extension_to_category(ext):
    """
    Return the category name for a file extension.
    Extension should be lowercase, e.g. '.jpg'.
    Returns 'Others' if no matching category found.
    """
    for category, extensions in CATEGORY_MAP.items():
        if ext in extensions:
            return category
    return "Others"


# =============================================================================
# ANALYSIS (DRY RUN)
# =============================================================================

def analyse_directory(target_dir):
    """
    Scan a directory and report what would be moved — without actually moving.

    Returns:
        dict: { category: [Path, ...] }
    """
    target_path = Path(target_dir)
    if not target_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {target_dir}")

    plan = {}   # category → list of file Paths

    # glob("*") gets all items in the top-level directory (not recursive)
    for item in target_path.glob("*"):
        if item.is_file():
            ext      = item.suffix.lower()
            category = extension_to_category(ext)
            plan.setdefault(category, []).append(item)

    return plan


def print_plan(plan, target_dir):
    """Display the organisation plan (dry run output)."""
    total_files = sum(len(files) for files in plan.values())

    print()
    print(f"  Files found in '{target_dir}': {total_files}")
    print(f"  {'Category':<18} {'Count':>6}  Files (first 3 shown)")
    print("  " + "─" * 55)

    for category in sorted(plan.keys()):
        files   = plan[category]
        samples = [f.name for f in files[:3]]   # show at most 3 filenames
        if len(files) > 3:
            samples.append(f"... +{len(files)-3} more")
        print(f"  {category:<18} {len(files):>6}  {', '.join(samples)}")

    print()


# =============================================================================
# ORGANISING (ACTUAL MOVE)
# =============================================================================

def organise_directory(target_dir, dry_run=False):
    """
    Move files in target_dir into category sub-folders.

    Parameters:
        target_dir (str or Path): Directory to organise
        dry_run    (bool):        If True, only print — don't move

    Returns:
        dict: { category: count_moved }
    """
    plan    = analyse_directory(target_dir)
    moved   = {}
    target  = Path(target_dir)

    for category, files in plan.items():
        dest_folder = target / category   # e.g.  /path/Images/

        for file_path in files:
            if dry_run:
                print(f"  [DRY RUN] {file_path.name}  →  {category}/")
                continue

            # Create the destination folder if it doesn't exist
            dest_folder.mkdir(exist_ok=True)

            dest_path = dest_folder / file_path.name

            # Handle name conflicts: add _1, _2, ... suffix
            counter = 1
            while dest_path.exists():
                stem     = file_path.stem
                suffix   = file_path.suffix
                dest_path = dest_folder / f"{stem}_{counter}{suffix}"
                counter += 1

            shutil.move(str(file_path), str(dest_path))
            moved[category] = moved.get(category, 0) + 1

    return moved


# =============================================================================
# UNDO (FLATTEN)
# =============================================================================

def flatten_directory(target_dir):
    """
    Move all files from sub-folders back to target_dir (undo organise).
    Only touches the category folders listed in CATEGORY_MAP + "Others".
    """
    target       = Path(target_dir)
    known_cats   = list(CATEGORY_MAP.keys()) + ["Others"]
    moved_back   = 0

    for cat in known_cats:
        cat_folder = target / cat
        if not cat_folder.is_dir():
            continue   # skip if this category folder doesn't exist

        for file_path in cat_folder.iterdir():
            if file_path.is_file():
                dest = target / file_path.name
                # Avoid overwriting files already at the top level
                if dest.exists():
                    dest = target / f"{file_path.stem}_restored{file_path.suffix}"
                shutil.move(str(file_path), str(dest))
                moved_back += 1

        # Remove the folder if now empty
        if not any(cat_folder.iterdir()):
            cat_folder.rmdir()

    return moved_back


# =============================================================================
# DEMO FOLDER CREATOR
# =============================================================================

def create_demo_folder():
    """
    Create a temporary demo folder with dummy files
    so the user can test the organiser immediately.
    """
    demo = Path("demo_folder")
    demo.mkdir(exist_ok=True)

    dummy_files = [
        "photo1.jpg", "photo2.png", "banner.svg",
        "report.pdf", "notes.txt", "essay.docx",
        "data.csv", "budget.xlsx",
        "song.mp3", "podcast.wav",
        "video.mp4", "clip.avi",
        "archive.zip", "backup.tar",
        "script.py", "index.html", "styles.css",
        "setup.exe",
    ]

    for name in dummy_files:
        (demo / name).touch()   # creates empty files

    print(f"  ✅ Demo folder created at: {demo.resolve()}")
    print(f"     Contains {len(dummy_files)} dummy files.")
    return str(demo)


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 55)
    print("            File Organizer")
    print("=" * 55)
    print("  Sorts files into sub-folders by type.")
    print()

    while True:
        print("Options:")
        print("  1. Create a demo folder to try")
        print("  2. Analyse a directory (dry run)")
        print("  3. Organise a directory (move files)")
        print("  4. Undo organise (flatten sub-folders)")
        print("  5. Quit")
        print()

        choice = input("Choose (1–5): ").strip()

        if choice == "1":
            path = create_demo_folder()
            print(f"  Now choose option 2 or 3 with path: {path}\n")

        elif choice in ("2", "3"):
            target = input("  Directory path: ").strip().strip('"')
            try:
                plan = analyse_directory(target)
                print_plan(plan, target)

                if choice == "3":
                    confirm = input("  Proceed with moving files? (yes/no): ").strip().lower()
                    if confirm in ("yes", "y"):
                        moved = organise_directory(target)
                        total_moved = sum(moved.values())
                        print(f"\n  ✅ Moved {total_moved} file(s):")
                        for cat, count in sorted(moved.items()):
                            print(f"     {cat}: {count} file(s)")
                        print()
                    else:
                        print("  Cancelled.\n")

            except NotADirectoryError as e:
                print(f"  ❌ {e}\n")

        elif choice == "4":
            target = input("  Directory path to flatten: ").strip().strip('"')
            try:
                count = flatten_directory(target)
                print(f"  ✅ Moved {count} file(s) back to root.\n")
            except Exception as e:
                print(f"  ❌ Error: {e}\n")

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
