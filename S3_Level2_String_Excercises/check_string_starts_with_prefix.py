"""
Excercise 3-12
Check if a given string starts with a certain prefix
Case-sensitive
False when len(prefix) > len(string)
"""


def main() -> None:
    input_data = [
        ("Hello", "He"),
        ("Coding", "Con"),
        ("Nora", "Circum"),
    ]

    for s, prefix in input_data:
        # My solution
        #------------
        # output = None
        # if len(prefix) > len(s):
        #     output = False
        # else:
        #     output = s.startswith(prefix)
        #
        # The whole if / else block is unnessesary
        # the string.startswith() method does all the error handling
        output = s.startswith(prefix)

        print(f"Input: '{s}'/'{prefix}' - Output: {output}")


if __name__ == "__main__":
    main()
