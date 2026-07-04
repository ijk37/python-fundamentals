"""
Project 03-03: Multi-Currency Converter
=========================================
Topics: variables, arithmetic, dictionaries, functions, f-strings,
        input validation, while loop
Difficulty: Beginner

Converts amounts between BDT, USD, EUR, GBP, JPY, and INR
using configurable exchange rates stored in a dictionary.
"""

# =============================================================================
# EXCHANGE RATES
# =============================================================================

# All rates are expressed as: 1 unit of the currency → BDT (Bangladeshi Taka)
# This "BDT as base" approach makes converting any pair simple:
#   amount_in_B = amount_in_A * RATES[A]
#   result      = amount_in_B / RATES[B]

RATES_TO_BDT = {
    "BDT": 1.0,       # 1 BDT = 1 BDT (base)
    "USD": 110.0,     # 1 USD = 110 BDT
    "EUR": 120.0,     # 1 EUR = 120 BDT
    "GBP": 140.0,     # 1 GBP = 140 BDT
    "JPY": 0.74,      # 1 JPY = 0.74 BDT
    "INR": 1.32,      # 1 INR = 1.32 BDT
}

# Currency symbols for nicer output
SYMBOLS = {
    "BDT": "৳",
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "INR": "₹",
}

# Number of decimal places to show for each currency
DECIMALS = {
    "BDT": 2,
    "USD": 2,
    "EUR": 2,
    "GBP": 2,
    "JPY": 0,   # Yen is quoted without decimals
    "INR": 2,
}


# =============================================================================
# CONVERSION LOGIC
# =============================================================================

def convert(amount, from_currency, to_currency):
    """
    Convert an amount from one currency to another.

    Strategy:
        1. Convert from_currency → BDT  (multiply by from-rate)
        2. Convert BDT → to_currency    (divide by to-rate)

    Parameters:
        amount        (float): The amount to convert.
        from_currency (str):   Source currency code (e.g. "USD").
        to_currency   (str):   Target currency code (e.g. "BDT").

    Returns:
        float: Converted amount.
    """
    amount_in_bdt = amount * RATES_TO_BDT[from_currency]   # step 1
    result        = amount_in_bdt / RATES_TO_BDT[to_currency]   # step 2
    return result


def format_amount(amount, currency):
    """Return a nicely formatted currency string, e.g. '$1,234.56'."""
    decimals = DECIMALS[currency]
    symbol   = SYMBOLS[currency]
    # f-string format spec: comma separator + fixed decimal places
    return f"{symbol}{amount:,.{decimals}f}"


# =============================================================================
# DISPLAY HELPERS
# =============================================================================

def print_separator(char="─", width=55):
    print(char * width)


def show_rate_table():
    """Print the current exchange rate table relative to 1 USD."""
    print()
    print_separator("═")
    print("  Current Exchange Rates  (base: 1 USD)")
    print_separator("─")
    usd_in_bdt = RATES_TO_BDT["USD"]   # how many BDT per 1 USD
    for code, rate_to_bdt in RATES_TO_BDT.items():
        if code == "USD":
            continue
        # How much of 'code' equals 1 USD?
        units_per_usd = usd_in_bdt / rate_to_bdt
        symbol = SYMBOLS[code]
        decimals = DECIMALS[code]
        print(f"  1 USD = {symbol}{units_per_usd:,.{decimals}f} {code}")
    print_separator("═")
    print()


# =============================================================================
# INPUT HELPERS
# =============================================================================

def get_currency(prompt):
    """Ask for a valid currency code and keep prompting until one is given."""
    codes = list(RATES_TO_BDT.keys())
    print(f"  Available currencies: {', '.join(codes)}")
    while True:
        code = input(prompt).strip().upper()
        if code in RATES_TO_BDT:
            return code
        print(f"  Unknown currency '{code}'. Please try again.\n")


def get_positive_float(prompt):
    """Ask for a positive number; retry on invalid input."""
    while True:
        try:
            value = float(input(prompt).replace(",", ""))  # allow "1,000"
            if value > 0:
                return value
            print("  Amount must be positive.\n")
        except ValueError:
            print("  Please enter a valid number.\n")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print_separator("═")
    print("         Multi-Currency Converter")
    print_separator("═")
    print()

    while True:
        # --- Show menu ---
        print("Options:")
        print("  1. Convert an amount")
        print("  2. Show rate table")
        print("  3. Quit")
        print()

        choice = input("Choose (1 / 2 / 3): ").strip()

        if choice == "1":
            print()
            amount        = get_positive_float("Amount to convert: ")
            from_currency = get_currency("From currency: ")
            to_currency   = get_currency("To currency  : ")

            result = convert(amount, from_currency, to_currency)

            print()
            print_separator("─")
            print(f"  {format_amount(amount, from_currency)} {from_currency}")
            print(f"  =  {format_amount(result, to_currency)} {to_currency}")
            print_separator("─")

            # Also show the reverse rate for context
            rate = RATES_TO_BDT[from_currency] / RATES_TO_BDT[to_currency]
            print(f"  Rate: 1 {from_currency} = {format_amount(rate, to_currency)} {to_currency}")
            print()

        elif choice == "2":
            show_rate_table()

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid option. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
