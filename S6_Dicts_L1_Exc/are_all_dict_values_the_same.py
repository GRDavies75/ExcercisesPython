"""
Excercise 6-37
Check if all values in a dictionary are one and the same
Print True or False
Exception, with an empty dict, print "Empty"
"""


def main() -> None:
    input_data = [
        {"a": 4, "b": 4, "c":4},
        {"a": 4, "b": 6, "c":4},
        {"a": 4, "b": 6, "c":10},
        {},
    ]

    for entry in input_data:
        # Cornercase
        if not entry:
            print("Empty")
            continue

        values_set = set(entry.values())
        print(len(values_set) == 1)


if __name__ == "__main__":
    main()
