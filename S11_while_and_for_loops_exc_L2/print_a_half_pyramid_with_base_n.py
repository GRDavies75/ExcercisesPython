"""
Excercise 11-69
Print a half-pyramid with a base (user-inputted) n

eg, n = 5
    *
   **
  ***
 ****
*****

A bit of a misnomer, I don't consider this a 'half-pyramid'

fun fact, use:
WHITESPACE = ' ' (single space)
PATTERN = '* ' (asterisk + a space)
you actually get an real pyramid with base N
"""
import sys
sys.path.append("..")
from libs import input_library as il


def main() -> None:
    PATTERN = "* " # a space for readability
    WHITESPACE = "  " # Double space for readability
    extra_information = [
        "Print a reversed pyramid with a base n wide",
        "[Q = quit]",
        "-------------------------------------"
    ]
    while True:
        user_input = il.get_user_input("For what 'n': ", extra_information)

        # quiting clause
        if user_input == 'q':
            break

        if user_input.isdigit() and int(user_input) >= 1:
            total_base_width = int(user_input)
            for i in range (1, total_base_width + 1):
                white_space_width = total_base_width - i
                line_pattern = (WHITESPACE * white_space_width) + (PATTERN * i)
                print(line_pattern)
        else:
            print("Unexpected input")
        # for readability
        print()


if __name__ == "__main__":
    main()
