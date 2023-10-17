"""
Excercise 12-76
Calculate the sum of the digits of non-negative n
using recursion
"""


def sum_of_digits(n: int) -> int|None:
    """
    for given non-negative n (negative n -> None)
    """
    # Cornercase
    if n < 0:
        return None
    
    # Base case
    if n < 10:
        return n
    
    # Otherwise recursion
    return n % 10 + sum_of_digits(n // 10)


def main() -> None:
    input_data = [
        2,
        23,
        10,
        100,
        -100, # cornercase testing
        111,
        1234,
    ]

    for entry in input_data:
        print(sum_of_digits(entry))


if __name__ == "__main__":
    main()
