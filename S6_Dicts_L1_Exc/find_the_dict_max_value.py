"""
Excercise 6-38
Find the maximum value in a dict
Assume all values are numerical
Print None if dict is empty
"""


def main() -> None:
    input_data = [
        {"a": 4, "b": 3, "c":7},
        {"a": 4, "b": 6},
        {"a": 4, "b": 4},
        {},
    ]

    for entry in input_data:
        # Cornercase
        if not entry:
            print(None)
            continue

        print(max(entry.values()))


if __name__ == "__main__":
    main()
