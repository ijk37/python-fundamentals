"""
mathutils.statistics
=====================
Descriptive statistics functions implemented from scratch
(without importing the standard statistics module).
"""


def mean(numbers):
    """
    Return the arithmetic mean (average) of a list of numbers.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list.")
    return sum(numbers) / len(numbers)


def median(numbers):
    """
    Return the median (middle value) of a list of numbers.

    For an even-length list, return the average of the two middle values.
    Does NOT modify the original list (uses a sorted copy).
    """
    if not numbers:
        raise ValueError("Cannot calculate median of an empty list.")

    sorted_nums = sorted(numbers)   # sorted() returns a new list
    n           = len(sorted_nums)
    mid         = n // 2

    if n % 2 == 1:
        return sorted_nums[mid]          # odd length: middle element
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2   # even: average of two middle


def mode(numbers):
    """
    Return the most frequently occurring value(s) as a list.
    If all values occur equally, returns all of them.
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of an empty list.")

    # Build a frequency count manually
    freq = {}
    for n in numbers:
        freq[n] = freq.get(n, 0) + 1

    max_count  = max(freq.values())
    modes      = [val for val, count in freq.items() if count == max_count]
    return sorted(modes)


def variance(numbers, population=True):
    """
    Return the variance of a list of numbers.

    Parameters:
        population (bool): True → population variance (÷ n)
                           False → sample variance (÷ n-1)
    """
    if len(numbers) < 2:
        raise ValueError("Need at least 2 numbers for variance.")

    avg    = mean(numbers)
    # Each term: (x - mean)²
    sq_diffs = [(x - avg) ** 2 for x in numbers]
    divisor  = len(numbers) if population else len(numbers) - 1
    return sum(sq_diffs) / divisor


def std_dev(numbers, population=True):
    """Return the standard deviation (square root of variance)."""
    return variance(numbers, population) ** 0.5


if __name__ == "__main__":
    data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
    print("statistics.py self-test:")
    print(f"  Data   : {data}")
    print(f"  Mean   : {mean(data)}")
    print(f"  Median : {median(data)}")
    print(f"  Mode   : {mode(data)}")
    print(f"  Std Dev: {std_dev(data):.4f}")
