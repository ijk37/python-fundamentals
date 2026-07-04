"""
Project 03-01: Mad Libs Story Generator
========================================
Topics: variables, input(), f-strings, string methods, type coercion
Difficulty: Beginner

A Mad Libs game where the user supplies words (nouns, verbs, adjectives, etc.)
and the program assembles them into a funny story.
"""

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


def get_word(prompt, min_length=2):
    """
    Ask the user for a single word and keep asking until they provide one
    that is at least min_length characters and contains only letters.

    Parameters:
        prompt (str): The message displayed to the user.
        min_length (int): Minimum acceptable word length.

    Returns:
        str: A validated, title-cased word.
    """
    while True:
        word = input(prompt).strip()  # .strip() removes accidental spaces

        # Validate: must not be empty and must only contain letters
        if len(word) >= min_length and word.isalpha():
            return word.title()  # e.g. "dog" → "Dog"
        else:
            print(
                f"  Please enter a real word (letters only, at least {min_length} chars).\n"
            )


def print_separator(char="=", width=60):
    """Print a decorative separator line."""
    print(char * width)


# =============================================================================
# STORY TEMPLATES
# =============================================================================

# Each template is stored as a function so the filled-in words slot in cleanly.
# The function receives a dictionary of words and returns the finished story.


def story_adventure(words):
    """An adventure story template."""
    return f"""
Once upon a time, a {words['adjective1']} {words['animal']} named {words['name']}
lived in the city of {words['city']}. Every morning, {words['name']} would
{words['verb1']} to the {words['place']} and {words['verb2']} for exactly
{words['number']} minutes. One {words['adjective2']} day, a mysterious
{words['noun']} appeared and everything changed forever.
The {words['animal']} screamed "{words['exclamation']}!" and ran away.
"""


def story_cooking(words):
    """A cooking show story template."""
    return f"""
Welcome back to "{words['adjective1']} Cooking with {words['name']}"!
Today we are making {words['adjective2']} {words['food']} with a twist.
First, you {words['verb1']} the ingredients in a {words['noun']}.
Then, {words['verb2']} everything for {words['number']} seconds.
Finally, serve it to your {words['animal']} and watch them {words['verb3']}.
{words['exclamation']}! Your dish is ready.
"""


# A menu mapping story names to (template function, required word list)
STORIES = {
    "1": (
        "Adventure",
        story_adventure,
        [
            ("adjective1", "an adjective (e.g. brave)"),
            ("animal", "an animal"),
            ("name", "a person's name"),
            ("city", "a city name"),
            ("verb1", "a verb (base form, e.g. run)"),
            ("place", "a place (e.g. park)"),
            ("verb2", "another verb"),
            ("number", "a number (digits only)"),  # special — digits
            ("adjective2", "another adjective"),
            ("noun", "a noun"),
            ("exclamation", "an exclamation (e.g. Wow)"),
        ],
    ),
    "2": (
        "Cooking Show",
        story_cooking,
        [
            ("adjective1", "an adjective"),
            ("name", "a chef's name"),
            ("adjective2", "another adjective"),
            ("food", "a type of food"),
            ("verb1", "a cooking verb (e.g. stir)"),
            ("noun", "a kitchen tool"),
            ("verb2", "another cooking verb"),
            ("number", "a number"),  # special — digits
            ("animal", "an animal"),
            ("verb3", "a reaction verb (e.g. smile)"),
            ("exclamation", "an exclamation"),
        ],
    ),
}


# =============================================================================
# MAIN PROGRAM
# =============================================================================


def main():
    print_separator()
    print("       Welcome to the Mad Libs Story Generator!")
    print_separator()
    print()

    # --- Choose a story ---
    print("Available stories:")
    for key, (title, _, _) in STORIES.items():
        print(f"  {key}. {title}")
    print()

    choice = input("Choose a story number: ").strip()
    if choice not in STORIES:
        print("Invalid choice. Defaulting to Adventure.")
        choice = "1"

    story_title, story_func, word_prompts = STORIES[choice]

    print()
    print_separator("-")
    print(f"  Story: {story_title}")
    print("  Fill in each blank — no peeking at the story!")
    print_separator("-")
    print()

    # --- Collect words from the user ---
    collected = {}  # dictionary to hold all entered words

    for key, description in word_prompts:
        if key == "number":
            # Numbers need different validation
            while True:
                val = input(f"  Enter {description}: ").strip()
                if val.isdigit():
                    collected[key] = val
                    break
                print("  Please enter digits only.\n")
        else:
            collected[key] = get_word(f"  Enter {description}: ")

    # --- Build and display the story ---
    print()
    print_separator()
    print(f"                  YOUR MAD LIBS STORY")
    print_separator()

    finished_story = story_func(collected)
    print(finished_story)

    print_separator()

    # --- Offer to play again ---
    again = input("Play again? (yes / no): ").strip().lower()
    if again in ("yes", "y"):
        print()
        main()  # recursive call to restart
    else:
        print("\nThanks for playing! Goodbye.")


if __name__ == "__main__":
    main()
