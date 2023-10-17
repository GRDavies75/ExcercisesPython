"""
Excercise 12-75
calculate factorial n using recursion
"""


def factorial(n: int) -> int|None:
    """
    Return the factorial of non-negative n (negative n -> None)

    n in {0, 1} -> 1
    """
    # Cornercase
    if n < 0:
        return None
    
    # Base case
    if n in {0, 1}:
        return 1

    # oterhwise down the rabbit hole we go
    return n * factorial(n-1)


def main() -> None:
    input_data = [
        0,
        1,
        5,
        -3,
        8,
        25,
    ]

    for entry in input_data:
        print(factorial(entry))


if __name__ == "__main__":
    main()
