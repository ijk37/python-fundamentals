"""
Project 03-02: BMI Calculator & Health Advisor
===============================================
Topics: variables, arithmetic operators, type conversion, if/elif/else,
        f-strings, functions, input validation
Difficulty: Beginner

Calculates Body Mass Index (BMI) from weight and height,
then advises on the health category with personalised messages.
"""

# =============================================================================
# CONSTANTS
# =============================================================================

# BMI boundary values as named constants (avoids "magic numbers" in code)
BMI_UNDERWEIGHT  = 18.5
BMI_NORMAL_HIGH  = 25.0
BMI_OVERWEIGHT   = 30.0

# Conversion factors
KG_PER_LB   = 0.453592    # 1 pound = 0.453592 kg
M_PER_INCH  = 0.0254      # 1 inch  = 0.0254 metres
CM_PER_M    = 100.0


# =============================================================================
# INPUT HELPERS
# =============================================================================

def get_positive_float(prompt):
    """
    Ask the user for a positive number and keep asking until they provide one.

    Returns:
        float: A validated positive number.
    """
    while True:
        try:
            value = float(input(prompt))   # float() can raise ValueError
            if value > 0:
                return value
            else:
                print("  Value must be greater than zero. Try again.\n")
        except ValueError:
            # User typed something that cannot be converted to a float
            print("  Please enter a valid number (e.g. 70 or 1.75). Try again.\n")


def get_unit_choice(prompt, valid_options):
    """
    Ask the user to pick from a set of valid options (case-insensitive).

    Returns:
        str: The chosen option in lower case.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        print(f"  Please choose one of: {', '.join(valid_options)}\n")


# =============================================================================
# CORE CALCULATION
# =============================================================================

def calculate_bmi(weight_kg, height_m):
    """
    Compute BMI using the standard formula.

    BMI = weight (kg) / height (m) squared

    Parameters:
        weight_kg (float): Weight in kilograms.
        height_m  (float): Height in metres.

    Returns:
        float: Rounded BMI value (1 decimal place).
    """
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def bmi_category(bmi):
    """
    Return a (category string, advice string) tuple based on BMI value.

    WHO classification:
        < 18.5  → Underweight
        18.5–25 → Normal weight
        25–30   → Overweight
        >= 30   → Obese
    """
    if bmi < BMI_UNDERWEIGHT:
        category = "Underweight"
        advice   = ("Consider eating more nutrient-dense meals. "
                    "Consult a nutritionist for a personalised plan.")
    elif bmi < BMI_NORMAL_HIGH:
        category = "Normal weight"
        advice   = ("Great work! Maintain your current lifestyle — "
                    "balanced diet and regular exercise.")
    elif bmi < BMI_OVERWEIGHT:
        category = "Overweight"
        advice   = ("Some lifestyle adjustments may help. "
                    "Focus on whole foods and regular physical activity.")
    else:
        category = "Obese"
        advice   = ("It is advisable to consult a healthcare professional "
                    "for a structured weight-management programme.")

    return category, advice


def healthy_weight_range(height_m):
    """
    Return the healthy weight range (in kg) for a given height.

    A Normal BMI is 18.5–25.0, so:
        min_weight = 18.5 * height_m²
        max_weight = 25.0 * height_m²
    """
    min_weight = round(BMI_UNDERWEIGHT * (height_m ** 2), 1)
    max_weight = round(BMI_NORMAL_HIGH * (height_m ** 2), 1)
    return min_weight, max_weight


# =============================================================================
# DISPLAY
# =============================================================================

def print_separator(char="─", width=55):
    print(char * width)


def display_results(name, weight_kg, height_m, bmi, category, advice):
    """Print a formatted results card."""
    min_w, max_w = healthy_weight_range(height_m)

    print()
    print_separator("═")
    print(f"  BMI Report for {name}")
    print_separator("═")
    print(f"  Weight   : {weight_kg:.1f} kg  ({weight_kg / KG_PER_LB:.1f} lbs)")
    print(f"  Height   : {height_m:.2f} m  ({height_m * CM_PER_M:.0f} cm)")
    print(f"  BMI      : {bmi}")
    print(f"  Category : {category}")
    print_separator("─")
    print(f"  Advice   : {advice}")
    print_separator("─")
    print(f"  Healthy weight range for your height:")
    print(f"    {min_w} kg – {max_w} kg")
    print_separator("═")
    print()


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print_separator("═")
    print("       BMI Calculator & Health Advisor")
    print_separator("═")
    print()

    # --- Collect name ---
    name = input("Your name: ").strip().title() or "User"

    # --- Choose unit system ---
    print("\nUnit system:")
    print("  1. Metric  (kg and metres)")
    print("  2. Imperial (lbs and inches)")
    unit = get_unit_choice("Choose (metric / imperial): ", ["metric", "imperial", "1", "2"])

    print()

    if unit in ("metric", "1"):
        # --- Metric input ---
        weight_kg = get_positive_float("Weight (kg): ")
        height_m  = get_positive_float("Height (m, e.g. 1.75): ")

    else:
        # --- Imperial input — convert to metric ---
        weight_lbs = get_positive_float("Weight (lbs): ")
        height_in  = get_positive_float("Height (inches, e.g. 68): ")

        weight_kg  = weight_lbs * KG_PER_LB           # convert to kg
        height_m   = height_in  * M_PER_INCH          # convert to metres
        print(f"\n  Converted: {weight_kg:.1f} kg, {height_m:.2f} m")

    # --- Calculate ---
    bmi              = calculate_bmi(weight_kg, height_m)
    category, advice = bmi_category(bmi)

    # --- Display results ---
    display_results(name, weight_kg, height_m, bmi, category, advice)

    # --- Option to calculate again ---
    again = input("Calculate another? (yes / no): ").strip().lower()
    if again in ("yes", "y"):
        print()
        main()
    else:
        print("Stay healthy!")


if __name__ == "__main__":
    main()
