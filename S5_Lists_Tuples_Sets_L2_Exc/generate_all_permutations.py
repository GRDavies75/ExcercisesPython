"""
Excercise 5-33
Generate all permutations of a list
"""
from itertools import permutations


def main() -> None:
    input_data = [
        [1, 2, 3],
    ]

    for entry in input_data:
        permutaties = permutations(entry)

        print(*permutaties, sep="\n")


if __name__ == "__main__":
    main()
