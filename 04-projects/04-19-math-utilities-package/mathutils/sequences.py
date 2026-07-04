"""
mathutils.sequences
====================
Number-theory and sequence functions.
"""


def factorial(n):
    """
    Return n! (n factorial) iteratively.
    factorial(0) = 1 by definition.
    Raises ValueError for negative input.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):   # 1 × 2 × 3 × ... × n
        result *= i
    return result


def fibonacci(n):
    """
    Return the first n Fibonacci numbers as a list.
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        # Each term = sum of the two preceding terms
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence


def is_prime(n):
    """
    Return True if n is a prime number.

    A prime is divisible only by 1 and itself.
    Uses trial division up to √n for efficiency.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors from 3 up to √n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False   # found a divisor → not prime
        i += 2             # skip even numbers

    return True


def prime_factors(n):
    """
    Return a list of prime factors of n (with repetition).
    Example: prime_factors(12) → [2, 2, 3]
    """
    if n < 2:
        return []

    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor           # divide out this factor
        divisor += 1

    if n > 1:
        factors.append(n)   # n itself is prime

    return factors


if __name__ == "__main__":
    print("sequences.py self-test:")
    print(f"  factorial(10)     = {factorial(10)}")
    print(f"  fibonacci(10)     = {fibonacci(10)}")
    print(f"  is_prime(17)      = {is_prime(17)}")
    print(f"  prime_factors(60) = {prime_factors(60)}")
