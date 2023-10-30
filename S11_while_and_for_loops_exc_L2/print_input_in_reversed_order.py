"""
Excercise 11-67 (and in hindsight apparently 11-68)
Print a given input in reverse order

Well, originally the excercise mentions print digits in reversed order
But nothing is done with the fact we are handling digits (and input is str anyways
or mentioning of cornercases and such)
Hence, the little alteration on my part

UPDATE: 2 solutions are shown:
one containing str(int(n)[::-1])
another some algorithm using modulo and integer divsion (hence the number part)

UPDATE 2: Guess what excercise 11-68 was all about...
In the spirit that it is more about thinking/approaching problems in a certain way
I consider this a case of all is well (for 11-67 )
"""
import sys
sys.path.append("..")
from libs import input_library as il


def main() -> None:
    while True:
        user_input = il.get_user_input("Give any input [Exception: 'Q' = quit]")

        # quiting handling
        if user_input.casefold() == 'q':
            break

        for char in reversed(user_input):
            print(char, end="")
        # for readability
        print()


if __name__ == "__main__":
    main()
