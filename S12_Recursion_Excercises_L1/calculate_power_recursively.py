"""
Excercise 12-77
Calculate the power of given (base) a & (exponent) b
Remember: a**b for given b = 0 -> 1
Assume a & b are whole numbers
"""


def calculate_power(base: int, exponent: int) -> int:
    """
    ...using recursion

    only whole positive numbers are expected for base & exponent
    """
    # Base case(s)
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    
    # Recursion it is
    return base * calculate_power(base, exponent - 1)


def main() -> None:
    input_data = [
        (2, 0),
        (3, 1),
        (2, 3),
        (5, 2),
    ]

    for entry in input_data:
        base, exponent = entry
        print(calculate_power(base, exponent))


if __name__ == "__main__":
    main()
