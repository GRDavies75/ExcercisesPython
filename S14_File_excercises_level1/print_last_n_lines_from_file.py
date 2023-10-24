"""
Excercise 14-86
Print the last (user inputted) n lines from a file
if n > max lines print appropiate feedback
"""
import sys
sys.path.append("..")
from libs import input_prompter as ip


def main() -> None:
    FILE_NAME = "basic_file.txt"
    BASIC_ERROR_MSG = "Unexpected Input, try again"
    content = []

    with open(FILE_NAME, encoding='utf-8') as text_file:
        content = text_file.readlines()

    max_lines = len(content)
    TO_BIG_ERROR_MSG = f"The file '{FILE_NAME}' has a maximum of {max_lines} lines"

    extra_information = [
        f"Print last n number of lines from file '{FILE_NAME}'",
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

            # Cornercase(s)
            if n_lines > max_lines:
                print(TO_BIG_ERROR_MSG)
                continue
            elif not n_lines >= 1:
                print(BASIC_ERROR_MSG)
                continue

            last_lines_content = content[(n_lines * -1):]
            for line in last_lines_content:
                print(line, end="")
            # Readability and the last line 'correction'
            print()
        else:
                print(BASIC_ERROR_MSG)


if __name__ == "__main__":
    main()
