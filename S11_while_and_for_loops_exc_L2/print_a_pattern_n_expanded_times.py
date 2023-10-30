"""
Excercise 11-66
Print a pattern using loops (based on user-input)

eg, give n = 3, expected output
*
**
***

"""
import sys
sys.path.append("..")
from libs import input_library as il


def main() -> None:
    PATTERN = '*'
    extra_information = [
        "Print an expanding pattern on n-lines",
        "[Q = quit]",
        "-------------------------------------"
    ]
    while True:
        user_input = il.get_user_input("For what 'n': ", extra_information)

        # quiting clause
        if user_input == 'q':
            break

        if user_input.isdigit() and int(user_input) >= 1:
            int_user_input = int(user_input)
            for i in range (1, int_user_input + 1):
                print(PATTERN * i)
        else:
            print("Unexpected input")
        # for readability
        print()


if __name__ == "__main__":
    main()
