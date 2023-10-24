"""
Excercise 14-85
Print (user inputted) n lines from a file
if n > max lines print appropiate feedback
"""
import sys
sys.path.append("..")
from libs import input_prompter as ip


def main() -> None:
    BASIC_ERROR_MSG = "Unexpected Input, try again"
    FILE_NAME = "basic_file.txt"
    content = []

    with open(FILE_NAME, encoding='utf-8') as text_file:
        content = text_file.readlines()

    extra_information = [
        f"Print n number of lines from file '{FILE_NAME}'",
        "[N >= 1, Q = quit]",
    ]

    while True:
        # For readability
        print()
        user_input = ip.get_user_input("For which N: ", extra_information)

        # Quiting
        if user_input.casefold() == 'q':
            break
        elif user_input.isdigit() :
            n_lines = int(user_input)
            max_lines = len(content)

            # Cornercase(s)
            if n_lines > max_lines:
                print(f"The file '{FILE_NAME}' has a maximum of {max_lines} lines")
                continue
            elif not n_lines >= 1:
                print(BASIC_ERROR_MSG)
                continue

            for i in range(0, n_lines):
                print(content[i].lstrip(), end="")
        else:
                print(BASIC_ERROR_MSG)


if __name__ == "__main__":
    main()
