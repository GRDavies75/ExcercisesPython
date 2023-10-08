"""
Excercise 7-44
A dict containing key-value pairs (string: list)
Mutate the the list in ascending order
(Not replace with a sorted copy)
"""


def main() -> None:
    input_data = [
        {
            "a": [4, 3, 2],
            "b": [5, 3, 7],
            "c": [1, 9, 10],
            "d": [3, 4, 1],
        },
    ]

    for entry in input_data:
        for key in entry:
            entry[key].sort()

    print(entry)


if __name__ == "__main__":
    main()
