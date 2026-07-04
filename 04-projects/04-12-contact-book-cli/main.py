"""
Project 03-12: Contact Book CLI
=================================
Topics: dicts, lists, CRUD operations, while loop,
        functions, f-strings, input validation, sorting
Difficulty: Beginner–Intermediate

An in-memory contact book. Supports adding, viewing,
searching, editing, and deleting contacts. All data is
stored in a dictionary keyed by a numeric ID.
"""


# =============================================================================
# DATA STORE
# =============================================================================

# contacts is a dict: { id (int) : {name, phone, email, notes} }
contacts     = {}
next_id      = 1   # auto-incrementing ID counter


# =============================================================================
# CRUD OPERATIONS
# =============================================================================

def add_contact(name, phone, email="", notes=""):
    """
    Add a new contact and return the assigned ID.

    Parameters:
        name  (str): Full name (required)
        phone (str): Phone number (required)
        email (str): Optional email address
        notes (str): Optional free-text notes
    """
    global next_id   # modify the module-level counter

    contacts[next_id] = {
        "name":  name.strip(),
        "phone": phone.strip(),
        "email": email.strip(),
        "notes": notes.strip(),
    }
    assigned_id = next_id
    next_id += 1
    return assigned_id


def get_contact(contact_id):
    """Return the contact dict for the given ID, or None if not found."""
    return contacts.get(contact_id)   # dict.get() returns None if key missing


def update_contact(contact_id, **fields):
    """
    Update one or more fields of an existing contact.

    Usage:
        update_contact(3, phone="01711-123456", email="new@mail.com")

    **fields uses keyword arguments to let the caller specify
    only the fields they want to change.
    """
    contact = contacts.get(contact_id)
    if contact is None:
        return False   # contact not found

    for field, value in fields.items():
        if field in contact and value.strip():
            contact[field] = value.strip()

    return True   # success


def delete_contact(contact_id):
    """Delete a contact by ID. Returns True if deleted, False if not found."""
    if contact_id in contacts:
        del contacts[contact_id]
        return True
    return False


def search_contacts(query):
    """
    Search for contacts whose name, phone, or email contains the query.
    The search is case-insensitive.
    Returns a list of (id, contact_dict) tuples.
    """
    query  = query.lower()
    results = []

    for cid, contact in contacts.items():
        # Check if the query appears in any searchable field
        if (query in contact["name"].lower()
                or query in contact["phone"]
                or query in contact["email"].lower()):
            results.append((cid, contact))

    return results


# =============================================================================
# DISPLAY HELPERS
# =============================================================================

def print_contact(cid, contact):
    """Print a single contact in a readable format."""
    print(f"  ID    : {cid}")
    print(f"  Name  : {contact['name']}")
    print(f"  Phone : {contact['phone']}")
    if contact["email"]:
        print(f"  Email : {contact['email']}")
    if contact["notes"]:
        print(f"  Notes : {contact['notes']}")
    print()


def list_contacts():
    """Print all contacts sorted alphabetically by name."""
    if not contacts:
        print("  No contacts saved yet.\n")
        return

    # Sort by the 'name' field of each contact dict
    sorted_contacts = sorted(contacts.items(), key=lambda pair: pair[1]["name"].lower())

    print()
    print(f"  {'ID':<5} {'Name':<22} {'Phone':<16} Email")
    print("  " + "─" * 60)

    for cid, contact in sorted_contacts:
        print(f"  {cid:<5} {contact['name']:<22} "
              f"{contact['phone']:<16} {contact['email']}")
    print()


# =============================================================================
# INPUT HELPERS
# =============================================================================

def ask_contact_id(prompt="  Contact ID: "):
    """Ask for a numeric contact ID. Returns the int or None on error."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print("  Please enter a number.\n")
        return None


def input_non_empty(prompt, field_name="Value"):
    """Keep prompting until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"  {field_name} cannot be empty.")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def _seed_sample_data():
    """Add a few sample contacts so the program starts with data."""
    add_contact("Rahim Uddin",    "01711-001122", "rahim@mail.com",   "Childhood friend")
    add_contact("Karim Ahmed",    "01812-334455", "karim@office.com", "Work colleague")
    add_contact("Nasrin Begum",   "01919-667788", "",                 "Neighbour")
    add_contact("Arif Hossain",   "01611-998877", "arif@study.edu",  "Study group")


def main():
    print("=" * 50)
    print("          Contact Book")
    print("=" * 50)

    _seed_sample_data()   # pre-populate with sample contacts

    while True:
        print("\nOptions:")
        print("  1. List all contacts")
        print("  2. Add a contact")
        print("  3. View a contact")
        print("  4. Edit a contact")
        print("  5. Delete a contact")
        print("  6. Search contacts")
        print("  7. Quit")
        print()

        choice = input("Choose (1–7): ").strip()

        # ── 1. LIST ──────────────────────────────────────────────
        if choice == "1":
            list_contacts()

        # ── 2. ADD ───────────────────────────────────────────────
        elif choice == "2":
            name  = input_non_empty("  Name  : ", "Name")
            phone = input_non_empty("  Phone : ", "Phone")
            email = input("  Email (optional): ").strip()
            notes = input("  Notes (optional): ").strip()
            cid   = add_contact(name, phone, email, notes)
            print(f"  ✅ Contact saved with ID {cid}.\n")

        # ── 3. VIEW ──────────────────────────────────────────────
        elif choice == "3":
            cid = ask_contact_id()
            if cid is not None:
                c = get_contact(cid)
                if c:
                    print()
                    print_contact(cid, c)
                else:
                    print(f"  No contact with ID {cid}.\n")

        # ── 4. EDIT ──────────────────────────────────────────────
        elif choice == "4":
            cid = ask_contact_id()
            if cid is None:
                continue
            c = get_contact(cid)
            if not c:
                print(f"  No contact with ID {cid}.\n")
                continue

            print(f"  Editing '{c['name']}'. Press Enter to keep current value.")
            name  = input(f"  Name  [{c['name']}]: ").strip() or c["name"]
            phone = input(f"  Phone [{c['phone']}]: ").strip() or c["phone"]
            email = input(f"  Email [{c['email']}]: ").strip()
            notes = input(f"  Notes [{c['notes']}]: ").strip()

            update_contact(cid, name=name, phone=phone,
                           email=email or c["email"],
                           notes=notes or c["notes"])
            print("  ✅ Contact updated.\n")

        # ── 5. DELETE ────────────────────────────────────────────
        elif choice == "5":
            cid = ask_contact_id()
            if cid is None:
                continue
            c = get_contact(cid)
            if not c:
                print(f"  No contact with ID {cid}.\n")
                continue

            confirm = input(f"  Delete '{c['name']}'? (yes/no): ").strip().lower()
            if confirm in ("yes", "y"):
                delete_contact(cid)
                print("  ✅ Contact deleted.\n")
            else:
                print("  Cancelled.\n")

        # ── 6. SEARCH ────────────────────────────────────────────
        elif choice == "6":
            query   = input("  Search query: ").strip()
            results = search_contacts(query)

            if results:
                print(f"\n  Found {len(results)} result(s):\n")
                for cid, c in results:
                    print_contact(cid, c)
            else:
                print(f"  No contacts matching '{query}'.\n")

        # ── 7. QUIT ──────────────────────────────────────────────
        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
