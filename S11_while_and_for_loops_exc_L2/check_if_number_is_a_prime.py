"""
Excercise 11-65
Determine if n is a prime or not

Hint: for determining if a number is a prime, see:
https://en.wikipedia.org/wiki/Prime_number
"""
import sys
sys.path.append("..")
from libs import input_library as il


def trial_division(n: int) -> list[int]:
    """
    https://en.wikipedia.org/wiki/Trial_division

    Gives back all the factors for given positive n > 1
    
    If the resulted list has len() == 1 then n is a prime
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1: a.append(n)
    # Only odd number is possible
    return a


def main() -> None:
    extra_info = [
        "Determine if n is a prime or not",
        "Q = quit",
    ]
    while True:
        user_input = il.get_user_input("for which 'n': ", extra_info)
        # Quiting corner-case
        if user_input.casefold() == 'q':
            break

        if user_input.isdigit():
            int_user_input = int(user_input)
            if int_user_input in {0,1}:
                print(f"{int_user_input} is not a Prime")
                print()
                continue
            elif int_user_input > 1:
                factors_of_n = trial_division(int_user_input)
                if len(factors_of_n) == 1:
                    print(f"{user_input} is a Prime")
                else:
                    print(f"{user_input} is not a Prime")
        else:
            print("Unexpected input, please try again")
        # for readability
        print()


if __name__ == "__main__":
    main()
    