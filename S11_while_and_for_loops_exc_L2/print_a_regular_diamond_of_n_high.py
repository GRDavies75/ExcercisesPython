"""
Excercise 11-72
Print a diamond of * of n-rows
For symmetry sake n can only be odd
"""
import sys
sys.path.append("..")
from libs import input_prompter as ip


def main() -> None:
    PATTERN = "* "
    WHITESPACE = " " # Singular space
    extra_information = [
        "Print a diamond of * of N Rows",
        "[Note: N must be odd, Q = quit]",
        "-------------------------------------"
    ]
    while True:
        user_input = ip.get_user_input("For what 'N': ", extra_information)

        # quiting clause
        if user_input.casefold() == 'q':
            break

        if user_input.isdigit() and int(user_input) % 2 != 0:
            total_rows = int(user_input)
            reversal_row = total_rows // 2 + 1
            pattern_history = []

            for i in range (1, reversal_row + 1):
                pattern = PATTERN * i
                white_space_width = reversal_row - i
                line_pattern = (WHITESPACE * white_space_width) + pattern
                pattern_history.append(line_pattern)
                print(line_pattern)
            for element in reversed(pattern_history[:-1]):
                print(element)
        else:
            print("Unexpected input / no even N")
        # for readability
        print()


if __name__ == "__main__":
    main()
