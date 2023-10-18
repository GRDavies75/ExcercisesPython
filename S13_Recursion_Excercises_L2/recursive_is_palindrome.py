"""
Excercise 13-79
Determine if a string is a palindrome (case-insensitive)
The recursive way
"""


def is_palindrome(string: str) -> bool:
    length_string = len(string)
    last_letter_index = length_string - 1
    # Base case(s)
    if not string or length_string == 1:
        return True
    elif string[0].casefold() != string[last_letter_index].casefold():
        return False
    
    # recursion steps
    return is_palindrome(string[1:last_letter_index])

# Forgot about the -1 index, so my initial check for len <= 1 was appropiate
# And the var last_letter_index is not necessary and could be replaced by -1
# (no errors because the inital len <= 1 catches that situation)


def main() -> None:
    input_data = [
        "Hello",
        "Anna",
        "",
        "World",
    ]

    for entry in input_data:
        print(is_palindrome(entry))


if __name__ == "__main__":
    main()
