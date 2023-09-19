"""
Excercise 4-19
Print the smallest and largest values of a list
Largest first, smallest second
Assume the lists are numerical lists
With an empty list None is expected
"""


def main() -> None:
    input_data = [
        [3, 4, 5, 6],
        [-1, -2, -3, -4],
        [0, 0, 0, 0],
        [],
    ]

    for entry in input_data:
        if entry:
            print(max(entry), min(entry))
        else:
            print(None)


if __name__ == "__main__":
    main()
