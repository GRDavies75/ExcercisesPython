"""
Excercise 5-31
Make a frequency dict based on a list
keys are case sensitive (A != a)
"""


def main() -> None:
    input_data = [
        ["a","a","b","c","a","b"],
        [1, 2, 3, 4, 3, 2, 1, 2],
        # case sensitive example
        ["a","A","b","c","a","b"],
    ]

    for entry in input_data:
        output_dict = {}
        for elem in entry:
            output_dict[elem] = output_dict.get(elem, 0) + 1

        print(output_dict)


if __name__ == "__main__":
    main()
