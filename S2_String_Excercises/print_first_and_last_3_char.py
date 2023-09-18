"""
Excercise S2-4
Given a string print out the first 3 and last 3 characters as 1 string
Print an empty string when len(s) < 6

Later it is changed to first and last X chars
"""


def main() -> None:
    input_data = [
        "Blue",
        "Wonderful",
        "Amazing",
    ]

    # If you repeat specific values it's best to make it a variable
    # For easier changes to the code, instead of 3 positions, now only 1
    CHARS_TO_SNIP = 3

    for entry in input_data:
        if len(entry) < CHARS_TO_SNIP*2:
            print("")
        else:
            first_X_char = entry[:CHARS_TO_SNIP]
            last_X_char = entry[-CHARS_TO_SNIP:]
            print(first_X_char + last_X_char)


if __name__ == "__main__":
    main()
