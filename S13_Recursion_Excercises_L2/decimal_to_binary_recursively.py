"""
Excercise 13-82
Convert a decimal number to binary using recursion
Note: [without the use of functions like bin() or int(n, 2)]
Note: [you may use log2]
"""
from math import log2


def dc2bin(decimal: int) -> str:
    """
    convert the given decimal to a binary string representation
    """

    # Base step
    if decimal <= 1:
        return str(decimal)
    
    # recursion steps
    max_power_of_2_decimal = int(log2(decimal))
    remainder = decimal - 2 ** max_power_of_2_decimal
    max_power_of_2_remainder = int(log2(remainder)) if remainder > 0 else 0

    # like a range, not including the max_power_of_2_remainder, hence the - 1
    return str(10 ** (max_power_of_2_decimal - max_power_of_2_remainder - 1)) + dc2bin(remainder)


def main() -> None:
    input_data = [
        0,
        5,
        34,
        567,
    ]

    for entry in input_data:
        print(dc2bin(entry))


if __name__ == "__main__":
    main()
