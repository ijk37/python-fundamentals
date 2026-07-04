"""
Project 03-29: Number System Explorer
========================================
Topics: number bases (binary/octal/hex), bin()/oct()/hex(),
        int(x, base), math module, bitwise operators
Difficulty: Beginner–Intermediate

Converts numbers between base-2, base-8, base-10, and base-16.
Also demonstrates bitwise operations and the math module.
"""

import math


# =============================================================================
# CONVERSION FUNCTIONS
# =============================================================================

def to_all_bases(decimal_num):
    """
    Convert a decimal integer to binary, octal, and hexadecimal.

    Built-in functions:
        bin(n) → "0b1010"   (prefix 0b)
        oct(n) → "0o12"     (prefix 0o)
        hex(n) → "0xa"      (prefix 0x)

    [2:] strips the prefix to get just the digits.
    """
    if not isinstance(decimal_num, int) or decimal_num < 0:
        raise ValueError("Input must be a non-negative integer.")

    return {
        "decimal": decimal_num,
        "binary":  bin(decimal_num)[2:],   # strips "0b"
        "octal":   oct(decimal_num)[2:],   # strips "0o"
        "hex":     hex(decimal_num)[2:].upper(),  # strips "0x", uppercase
    }


def from_binary(binary_str):
    """Convert a binary string to decimal. Example: '1010' → 10"""
    return int(binary_str, 2)   # int(string, base) converts any base string


def from_octal(octal_str):
    """Convert an octal string to decimal. Example: '12' → 10"""
    return int(octal_str, 8)


def from_hex(hex_str):
    """Convert a hex string to decimal. Example: 'A' or 'a' → 10"""
    return int(hex_str, 16)


def manual_binary_convert(n):
    """
    Convert n to binary MANUALLY (without bin()) to show the algorithm.
    Repeatedly divide by 2, collect remainders, then reverse.
    """
    if n == 0:
        return "0"

    remainders = []
    temp = n
    while temp > 0:
        remainders.append(temp % 2)   # remainder is 0 or 1
        temp = temp // 2              # integer division

    # Remainders collected LSB→MSB; reverse to get MSB→LSB
    return "".join(str(r) for r in reversed(remainders))


# =============================================================================
# BITWISE OPERATIONS
# =============================================================================

def show_bitwise(a, b):
    """Demonstrate Python's bitwise operators on two integers."""
    print(f"\n  a = {a:>5}  =  {bin(a)[2:]:>10} (binary)")
    print(f"  b = {b:>5}  =  {bin(b)[2:]:>10} (binary)")
    print()
    print(f"  a & b  (AND) = {a & b:>5}  =  {bin(a & b)[2:]:>10}")
    print(f"  a | b  (OR)  = {a | b:>5}  =  {bin(a | b)[2:]:>10}")
    print(f"  a ^ b  (XOR) = {a ^ b:>5}  =  {bin(a ^ b)[2:]:>10}")
    print(f"  ~a     (NOT) = {~a:>5}  (flips all bits)")
    print(f"  a << 1 (left shift)  = {a << 1:>5}  (×2 each shift)")
    print(f"  a >> 1 (right shift) = {a >> 1:>5}  (÷2 each shift)")


# =============================================================================
# MATH MODULE DEMOS
# =============================================================================

def show_math_functions(n):
    """Show useful math module functions for a given number."""
    print(f"\n  math functions for n = {n}:")
    print(f"  math.sqrt({n})       = {math.sqrt(n):.6f}")
    print(f"  math.floor({n:.2f})    = {math.floor(n)}")
    print(f"  math.ceil({n:.2f})     = {math.ceil(n)}")
    print(f"  math.log2({n})       = {math.log2(n):.4f}")
    print(f"  math.log10({n})      = {math.log10(n):.4f}")
    print(f"  math.factorial({min(int(n), 15)}) = {math.factorial(min(int(n), 15)):,}")
    print(f"  math.gcd(24, 36)     = {math.gcd(24, 36)}")
    print(f"  math.lcm(4, 6)       = {math.lcm(4, 6)}")
    print(f"  math.pi              = {math.pi:.10f}")
    print(f"  math.e               = {math.e:.10f}")


# =============================================================================
# DISPLAY
# =============================================================================

def print_conversion_table(start=0, end=20):
    """Print a reference table: decimal ↔ binary ↔ octal ↔ hex."""
    print()
    print(f"  {'Dec':>5}  {'Binary':<12}  {'Octal':<8}  Hex")
    print("  " + "─" * 38)
    for n in range(start, end + 1):
        conversions = to_all_bases(n)
        print(f"  {conversions['decimal']:>5}  {conversions['binary']:<12}  "
              f"{conversions['octal']:<8}  {conversions['hex']}")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("=" * 50)
    print("       Number System Explorer")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Convert decimal → binary/octal/hex")
        print("  2. Convert binary/octal/hex → decimal")
        print("  3. Manual binary conversion (show algorithm)")
        print("  4. Bitwise operators demo")
        print("  5. Math module functions")
        print("  6. Reference conversion table (0–20)")
        print("  7. Quit")
        print()

        choice = input("Choose (1–7): ").strip()

        if choice == "1":
            try:
                n = int(input("  Enter a decimal integer: "))
                if n < 0:
                    print("  Please use a non-negative number.\n")
                    continue
                result = to_all_bases(n)
                print(f"\n  Decimal  : {result['decimal']}")
                print(f"  Binary   : {result['binary']}")
                print(f"  Octal    : {result['octal']}")
                print(f"  Hex      : {result['hex']}")
            except ValueError:
                print("  Please enter a valid integer.\n")

        elif choice == "2":
            base = input("  Source base (bin/oct/hex): ").strip().lower()
            val  = input("  Enter value: ").strip()
            try:
                if base == "bin":
                    print(f"  Decimal: {from_binary(val)}")
                elif base == "oct":
                    print(f"  Decimal: {from_octal(val)}")
                elif base == "hex":
                    print(f"  Decimal: {from_hex(val)}")
                else:
                    print("  Unknown base. Enter: bin, oct, or hex.")
            except ValueError:
                print(f"  '{val}' is not a valid {base} number.\n")

        elif choice == "3":
            try:
                n = int(input("  Enter a decimal integer: "))
                manual  = manual_binary_convert(n)
                builtin = bin(n)[2:]
                print(f"  Manual  : {manual}")
                print(f"  Built-in: {builtin}")
                print(f"  Match: {manual == builtin}")
            except ValueError:
                print("  Please enter a valid integer.\n")

        elif choice == "4":
            try:
                a = int(input("  Enter integer a: "))
                b = int(input("  Enter integer b: "))
                show_bitwise(a, b)
            except ValueError:
                print("  Please enter valid integers.\n")

        elif choice == "5":
            try:
                n = float(input("  Enter a number: "))
                if n <= 0:
                    print("  Please enter a positive number.\n")
                    continue
                show_math_functions(n)
            except ValueError:
                print("  Please enter a valid number.\n")

        elif choice == "6":
            print_conversion_table()

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
