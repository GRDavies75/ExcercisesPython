"""
Excercise 11-70
Print a Floyd's Triangle of (user-inputted) n rows
https://en.wikipedia.org/wiki/Floyd%27s_triangle
"""
import sys
sys.path.append("..")
from libs import input_prompter as ip


def main() -> None:
    WHITESPACE = " " 
    extra_information = [
        "Print a Floyd's Trangle of N rows",
        "[Note: 1 <= N <= 13, Q = quit]",
        "-------------------------------------"
    ]
    while True:
        user_input = ip.get_user_input("For what 'N': ", extra_information)

        # quiting clause
        if user_input == 'q':
            break

        if user_input.isdigit() and 1 <= int(user_input) <= 13:
            # 13 rows produces a maximum of 2 digit numbers
            total_rows = int(user_input)
            counter = 1

            for i in range (1, total_rows + 1):
                tmp_list = []
                while len(tmp_list) < i:
                    tmp_list.append(f"{counter:2}")
                    counter += 1
                pattern = " ".join(tmp_list)
                white_space_width = total_rows - i
                line_pattern = (WHITESPACE * white_space_width) + pattern
                print(line_pattern)
        else:
            print("Unexpected input")
        # for readability
        print()


if __name__ == "__main__":
    main()
