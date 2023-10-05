"""
Excercise 7-42
Print the maximum value sum of values in a dictionary
Assume values are lists or tuples
"""


def main() -> None:
    input_data = [
        {
            "a": [1, 2, 3],
            "b": [4, 0, -4],
            "c": [3, 5, 9],
            "d": [45, 12, 100],
        },
    ]

    for entry in input_data:
        max_value = None
        for list_of_values in entry.values():
            sum_of_values = sum(list_of_values)
            if not max_value or sum_of_values > max_value:
                max_value = sum_of_values
        
        print(sum_of_values)


if __name__ == "__main__":
    main()
