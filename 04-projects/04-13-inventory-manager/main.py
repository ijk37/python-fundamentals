"""
Project 03-13: Inventory Manager
===================================
Topics: dicts, list comprehensions, exception handling,
        functions, sorting, f-strings, while loop
Difficulty: Beginner–Intermediate

Manages a shop's stock: add products, restock,
sell, and check for low-stock alerts. All data is
stored in a nested dictionary.
"""


# =============================================================================
# CONSTANTS
# =============================================================================

LOW_STOCK_THRESHOLD = 10   # items below this quantity trigger a warning


# =============================================================================
# DATA STORE
# =============================================================================

# inventory: {product_name (str): {"qty": int, "price": float, "category": str}}
inventory = {}


# =============================================================================
# OPERATIONS
# =============================================================================

def add_product(name, qty, price, category="General"):
    """
    Add a new product to inventory.
    If the product already exists, raises a ValueError.
    """
    name = name.strip().title()
    if name in inventory:
        raise ValueError(f"'{name}' already exists. Use restock to add quantity.")

    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    if price < 0:
        raise ValueError("Price cannot be negative.")

    inventory[name] = {
        "qty":      qty,
        "price":    round(price, 2),
        "category": category.strip().title(),
    }


def restock(name, amount):
    """
    Add `amount` units to an existing product.
    Raises KeyError if product not found, ValueError if amount <= 0.
    """
    name = name.strip().title()
    if name not in inventory:
        raise KeyError(f"'{name}' not found in inventory.")
    if amount <= 0:
        raise ValueError("Restock amount must be positive.")

    inventory[name]["qty"] += amount


def sell(name, amount):
    """
    Reduce stock by `amount` units when a sale is made.
    Raises KeyError if product not found.
    Raises ValueError if insufficient stock.
    """
    name = name.strip().title()
    if name not in inventory:
        raise KeyError(f"'{name}' not found in inventory.")
    if amount <= 0:
        raise ValueError("Sale amount must be positive.")

    current_qty = inventory[name]["qty"]
    if amount > current_qty:
        raise ValueError(
            f"Insufficient stock: only {current_qty} unit(s) available."
        )

    inventory[name]["qty"] -= amount


def delete_product(name):
    """Remove a product entirely from inventory."""
    name = name.strip().title()
    if name not in inventory:
        raise KeyError(f"'{name}' not found.")
    del inventory[name]


def get_low_stock():
    """Return a list of (name, qty) for products below LOW_STOCK_THRESHOLD."""
    return [
        (name, item["qty"])
        for name, item in inventory.items()
        if item["qty"] < LOW_STOCK_THRESHOLD
    ]


def inventory_value():
    """Return the total value of all stock (qty × price for each product)."""
    return sum(item["qty"] * item["price"] for item in inventory.values())


# =============================================================================
# DISPLAY
# =============================================================================

def list_inventory(sort_by="name"):
    """
    Print the full inventory table.

    sort_by options: "name", "qty", "price", "category"
    """
    if not inventory:
        print("  Inventory is empty.\n")
        return

    # Build a list of (name, dict) pairs, then sort
    key_map = {
        "name":     lambda pair: pair[0].lower(),
        "qty":      lambda pair: pair[1]["qty"],
        "price":    lambda pair: pair[1]["price"],
        "category": lambda pair: pair[1]["category"].lower(),
    }
    key_func = key_map.get(sort_by, key_map["name"])
    items    = sorted(inventory.items(), key=key_func)

    print()
    print(f"  {'Product':<22} {'Qty':>6}  {'Price':>10}  Category")
    print("  " + "─" * 55)

    for name, item in items:
        # Flag low-stock items with a warning symbol
        flag = " ⚠️" if item["qty"] < LOW_STOCK_THRESHOLD else ""
        print(f"  {name:<22} {item['qty']:>6}  "
              f"৳{item['price']:>8,.2f}  {item['category']}{flag}")

    print("  " + "─" * 55)
    print(f"  {len(inventory)} product(s)   "
          f"Total stock value: ৳{inventory_value():,.2f}")
    print()


def show_low_stock():
    """Print products that need restocking."""
    low = get_low_stock()
    if not low:
        print("  ✅ All products are sufficiently stocked.\n")
        return

    print(f"\n  ⚠️  LOW STOCK ALERT ({len(low)} product(s) below {LOW_STOCK_THRESHOLD} units)")
    print("  " + "─" * 35)
    for name, qty in sorted(low, key=lambda x: x[1]):
        print(f"  {name:<22} {qty:>4} unit(s)")
    print()


# =============================================================================
# SEED DATA
# =============================================================================

def _seed():
    """Pre-populate with sample products."""
    add_product("Rice",         500, 70.00,  "Groceries")
    add_product("Cooking Oil",  200, 195.00, "Groceries")
    add_product("Sugar",        150, 85.00,  "Groceries")
    add_product("Salt",           8, 20.00,  "Groceries")   # low stock
    add_product("Bread",         45, 60.00,  "Bakery")
    add_product("Milk",          30, 90.00,  "Dairy")
    add_product("Eggs",           6, 155.00, "Protein")    # low stock
    add_product("Chicken",       80, 280.00, "Protein")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 50)
    print("          Inventory Manager")
    print("=" * 50)

    _seed()

    while True:
        print("\nOptions:")
        print("  1. View inventory")
        print("  2. Add new product")
        print("  3. Restock a product")
        print("  4. Record a sale")
        print("  5. Delete a product")
        print("  6. Low-stock report")
        print("  7. Quit")
        print()

        choice = input("Choose (1–7): ").strip()

        # ── 1. VIEW ──────────────────────────────────────────────
        if choice == "1":
            sort = input("  Sort by (name/qty/price/category) [name]: ").strip().lower()
            list_inventory(sort or "name")

        # ── 2. ADD ───────────────────────────────────────────────
        elif choice == "2":
            try:
                name     = input("  Product name : ").strip()
                qty      = int(input("  Quantity     : "))
                price    = float(input("  Price (৳)    : "))
                category = input("  Category     : ").strip()
                add_product(name, qty, price, category)
                print(f"  ✅ '{name.title()}' added.\n")
            except (ValueError, KeyError) as e:
                print(f"  ❌ {e}\n")

        # ── 3. RESTOCK ───────────────────────────────────────────
        elif choice == "3":
            try:
                name   = input("  Product name : ").strip()
                amount = int(input("  Add quantity : "))
                restock(name, amount)
                print(f"  ✅ Restocked '{name.title()}'.\n")
            except (ValueError, KeyError) as e:
                print(f"  ❌ {e}\n")

        # ── 4. SELL ──────────────────────────────────────────────
        elif choice == "4":
            try:
                name   = input("  Product name : ").strip()
                amount = int(input("  Units sold   : "))
                sell(name, amount)
                remaining = inventory[name.strip().title()]["qty"]
                print(f"  ✅ Sale recorded. Remaining stock: {remaining}.\n")
                if remaining < LOW_STOCK_THRESHOLD:
                    print(f"  ⚠️  Stock is now low!\n")
            except (ValueError, KeyError) as e:
                print(f"  ❌ {e}\n")

        # ── 5. DELETE ────────────────────────────────────────────
        elif choice == "5":
            try:
                name    = input("  Product name : ").strip()
                confirm = input(f"  Delete '{name.title()}'? (yes/no): ").strip().lower()
                if confirm in ("yes", "y"):
                    delete_product(name)
                    print("  ✅ Product deleted.\n")
                else:
                    print("  Cancelled.\n")
            except KeyError as e:
                print(f"  ❌ {e}\n")

        # ── 6. LOW STOCK ─────────────────────────────────────────
        elif choice == "6":
            show_low_stock()

        # ── 7. QUIT ──────────────────────────────────────────────
        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.\n")


if __name__ == "__main__":
    main()
