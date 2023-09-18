"""
Excercise 3-15
Count the number of repeated chars in a string
Extra requirements:
Print the count of distinct repeated characters
And on a next line display all the relevant chars separated by a space
This also must be done in alphabetical order
Corner case:
With no repeated characters print 0 and None (on next line)
"""


def main() -> None:
    input_data = [
        "Hello",
        "Corporation",
        "Python",
    ]

    for entry in input_data:
        char_set = set()
        repeated_char_set = set()
        for char in entry:
            if char in char_set:
                repeated_char_set.add(char)
            else:
                char_set.add(char)
        print(f"Input: '{entry}'")
        print(f"No. of repeated chars: {len(repeated_char_set)}")
        print(f"Repeated chars: {' '.join(sorted(repeated_char_set)) if repeated_char_set else None}")
        

if __name__ == "__main__":
    main()
