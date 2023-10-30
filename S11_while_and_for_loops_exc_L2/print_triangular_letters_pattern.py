"""
Excercise 11-71
Print a triangular letters pattern for N rows

eg, n = 5
A
B B
C C C
D D D D
E E E E E
"""
import sys
sys.path.append("..")
from libs import input_library as il


def main() -> None:
    UNICODE_A = 65
    extra_information = [
        "Print a triangular letters pattern for N rows",
        "[Note: 1 <= N <= 26, Q = quit]",
        "-------------------------------------"
    ]
    while True:
        user_input = il.get_user_input("For what 'N': ", extra_information)

        # quiting clause
        if user_input.casefold() == 'q':
            break

        if user_input.isdigit() and 1 <= int(user_input) <= 26:
            # 26 letters in the western alphabet
            total_rows = int(user_input)

            for i in range (0, total_rows):
                letter = chr(UNICODE_A + i) + " " 
                pattern = letter * (i + 1)
                print(pattern)
        else:
            print("Unexpected input")
        # for readability
        print()


if __name__ == "__main__":
    main()
