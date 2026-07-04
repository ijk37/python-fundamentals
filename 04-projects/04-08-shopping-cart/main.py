"""
Project 03-08: Shopping Cart System
======================================
Topics: lists, dictionaries, functions, for/while loops,
        f-strings, type conversion, sorting, comprehensions
Difficulty: Beginner–Intermediate

A command-line shopping cart that lets you browse a product
catalogue, add/remove items, apply discount codes, and
generate a receipt.
"""


# =============================================================================
# PRODUCT CATALOGUE
# =============================================================================

# Each product is a dictionary with id, name, price (BDT), and category.
CATALOGUE = [
    {"id": 1,  "name": "Rice (5 kg)",         "price":  350, "category": "Groceries"},
    {"id": 2,  "name": "Cooking Oil (1 L)",   "price":  195, "category": "Groceries"},
    {"id": 3,  "name": "Lentils (1 kg)",      "price":  145, "category": "Groceries"},
    {"id": 4,  "name": "Milk (1 L)",          "price":   90, "category": "Dairy"},
    {"id": 5,  "name": "Yoghurt (500 g)",     "price":   75, "category": "Dairy"},
    {"id": 6,  "name": "Bread (loaf)",        "price":   60, "category": "Bakery"},
    {"id": 7,  "name": "Eggs (dozen)",        "price":  155, "category": "Protein"},
    {"id": 8,  "name": "Chicken (1 kg)",      "price":  280, "category": "Protein"},
    {"id": 9,  "name": "Tomatoes (1 kg)",     "price":   80, "category": "Vegetables"},
    {"id": 10, "name": "Potatoes (1 kg)",     "price":   55, "category": "Vegetables"},
    {"id": 11, "name": "Bottled Water (2 L)", "price":   45, "category": "Drinks"},
    {"id": 12, "name": "Orange Juice (1 L)",  "price":  110, "category": "Drinks"},
]

# Discount codes: code → discount percentage
DISCOUNT_CODES = {
    "WELCOME10": 10,   # 10% off
    "SAVE20":    20,   # 20% off
    "STUDENT5":   5,   # 5% off
}

TAX_RATE = 0.05   # 5% VAT


# =============================================================================
# CART OPERATIONS
# =============================================================================

def find_product(product_id):
    """Find and return the product dict with the given id, or None."""
    for product in CATALOGUE:
        if product["id"] == product_id:
            return product
    return None   # not found


def add_to_cart(cart, product_id, quantity):
    """
    Add a quantity of a product to the cart.

    The cart is a list of dicts:
        [{"product": {...}, "quantity": int}, ...]

    If the product is already in the cart, its quantity is increased.
    """
    product = find_product(product_id)
    if product is None:
        print(f"  Product ID {product_id} not found.\n")
        return

    # Check if this product is already in the cart
    for item in cart:
        if item["product"]["id"] == product_id:
            item["quantity"] += quantity
            print(f"  Updated: {product['name']} × {item['quantity']}")
            return

    # Product not yet in cart — add a new entry
    cart.append({"product": product, "quantity": quantity})
    print(f"  Added: {product['name']} × {quantity}  "
          f"(৳{product['price']:,.0f} each)")


def remove_from_cart(cart, product_id):
    """Remove a product entirely from the cart by product id."""
    for i, item in enumerate(cart):
        if item["product"]["id"] == product_id:
            removed = cart.pop(i)   # remove and return the item
            print(f"  Removed: {removed['product']['name']}")
            return
    print(f"  Product ID {product_id} is not in the cart.\n")


def cart_total(cart):
    """Calculate and return the subtotal (before tax and discount)."""
    total = 0
    for item in cart:
        # price × quantity for each line
        total += item["product"]["price"] * item["quantity"]
    return total


# =============================================================================
# DISPLAY
# =============================================================================

def show_catalogue(filter_category=None):
    """Print the product catalogue, optionally filtered by category."""
    # Get unique categories
    categories = sorted(set(p["category"] for p in CATALOGUE))

    # If filtering, check the category exists
    if filter_category and filter_category not in categories:
        print(f"  Unknown category '{filter_category}'.")
        filter_category = None

    print()
    print("─" * 55)
    print(f"  {'ID':<4} {'Product':<25} {'Price':>8}  Category")
    print("─" * 55)

    for product in CATALOGUE:
        if filter_category and product["category"] != filter_category:
            continue   # skip products not in the requested category
        print(f"  {product['id']:<4} {product['name']:<25} "
              f"৳{product['price']:>6,}  {product['category']}")

    print("─" * 55)
    print(f"  Categories: {', '.join(categories)}")
    print()


def show_cart(cart):
    """Print the current cart contents."""
    if not cart:
        print("  Your cart is empty.\n")
        return

    print()
    print("─" * 52)
    print(f"  {'Product':<25} {'Qty':>4}  {'Unit':>8}  {'Line':>9}")
    print("─" * 52)

    for item in cart:
        p        = item["product"]
        qty      = item["quantity"]
        line_tot = p["price"] * qty
        print(f"  {p['name']:<25} {qty:>4}  ৳{p['price']:>6,}  ৳{line_tot:>7,}")

    print("─" * 52)
    print(f"  Subtotal: ৳{cart_total(cart):,}")
    print()


def print_receipt(cart, discount_pct=0, discount_code=""):
    """Print the final receipt with tax and discount applied."""
    subtotal     = cart_total(cart)
    discount_amt = subtotal * (discount_pct / 100)
    after_disc   = subtotal - discount_amt
    tax_amt      = after_disc * TAX_RATE
    total        = after_disc + tax_amt

    print()
    print("═" * 50)
    print("              RECEIPT")
    print("═" * 50)

    for item in cart:
        p    = item["product"]
        line = p["price"] * item["quantity"]
        print(f"  {p['name']:<28} ৳{line:>7,}")

    print("─" * 50)
    print(f"  {'Subtotal':<30} ৳{subtotal:>7,}")

    if discount_pct > 0:
        print(f"  {'Discount (' + discount_code + ') -' + str(discount_pct) + '%':<30} "
              f"-৳{discount_amt:>6,.1f}")

    print(f"  {'VAT (' + str(int(TAX_RATE*100)) + '%)':<30} ৳{tax_amt:>7,.1f}")
    print("─" * 50)
    print(f"  {'TOTAL':<30} ৳{total:>7,.1f}")
    print("═" * 50)
    print()


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 50)
    print("          Shopping Cart")
    print("=" * 50)

    cart         = []    # starts empty
    discount_pct = 0
    discount_code = ""

    while True:
        print("\nOptions:")
        print("  1. Browse catalogue")
        print("  2. Add item to cart")
        print("  3. Remove item from cart")
        print("  4. View cart")
        print("  5. Apply discount code")
        print("  6. Checkout (print receipt)")
        print("  7. Quit")
        print()

        choice = input("Choose (1–7): ").strip()

        if choice == "1":
            cat = input("  Filter by category (or press Enter for all): ").strip().title()
            show_catalogue(cat or None)

        elif choice == "2":
            try:
                pid = int(input("  Product ID: "))
                qty = int(input("  Quantity  : "))
                if qty <= 0:
                    print("  Quantity must be at least 1.")
                else:
                    add_to_cart(cart, pid, qty)
            except ValueError:
                print("  Please enter whole numbers.\n")

        elif choice == "3":
            try:
                pid = int(input("  Product ID to remove: "))
                remove_from_cart(cart, pid)
            except ValueError:
                print("  Please enter a whole number.\n")

        elif choice == "4":
            show_cart(cart)

        elif choice == "5":
            code = input("  Enter discount code: ").strip().upper()
            if code in DISCOUNT_CODES:
                discount_pct  = DISCOUNT_CODES[code]
                discount_code = code
                print(f"  Code applied: {discount_pct}% off! ✅")
            else:
                print("  Invalid discount code. ❌")

        elif choice == "6":
            if not cart:
                print("  Cart is empty — nothing to checkout.")
            else:
                print_receipt(cart, discount_pct, discount_code)
                confirm = input("  Confirm order? (yes / no): ").strip().lower()
                if confirm in ("yes", "y"):
                    print("  Order placed! Thank you for shopping. 🛒")
                    cart          = []   # clear cart after purchase
                    discount_pct  = 0
                    discount_code = ""
                else:
                    print("  Order cancelled. Cart kept.")

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
