"""
Excercise 6-36
Merge 2 dictionaries,
for existing keys: values are overwritten by dict2.value (== normal behaviour)
"""


def main() -> None:
    input_data = [
        ({"a": 1, "b": 2, "c": 3}, {"c": 4, "d": 6, "e": 8}),
    ]

    for first_dict, second_dict in input_data:
        merged_dict = first_dict | second_dict

        print(merged_dict)


if __name__ == "__main__":
    main()
