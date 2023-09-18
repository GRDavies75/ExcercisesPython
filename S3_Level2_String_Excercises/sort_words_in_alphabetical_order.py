"""
Excercise 3-16
Convert a string so that the words are sorted alphabeticly (lowercaseed)
Keep the spaces
Assume only letters and spaces
"""


def main() -> None:
    input_data = [
        "Hello World",
        "Wonderful World",
    ]

    for entry in input_data:
        output = ""
        lc_entry = entry.casefold()
        words_list = lc_entry.split(" ")
        for word in words_list:
            output += "".join(sorted(word)) + " "

        output = output.rstrip()
        print(f"Input: '{entry}' - Output: '{output}'")


if __name__ == "__main__":
    main()
