"""
Excercise 6-34
Check if a key exists in a dictionary
"""


def main() -> None:
    input_data = [
        ({"a": 4, "b": 6}, "a"),
        ({"a": 4, "b": 6}, "c"),
        ({}, "d"),
    ]

    for a_dict, key_to_find in input_data:
        print(key_to_find in a_dict)


if __name__ == "__main__":
    main()
