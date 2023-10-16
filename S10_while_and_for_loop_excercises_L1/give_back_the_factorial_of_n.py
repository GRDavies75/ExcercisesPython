"""
Excercise 10-63
Give back the factorial of (user inputted) n
"""
import sys
sys.path.append("..")
from libs import input_handler as ih


def give_factorial(n: int) -> int|None:
    """
    Give back the factorial for any n >= 0 
    
    None for any other n
    """
    result = None
    if n == 0:
        return 1
    elif n > 0:
        result = 1
        for i in range(1, n + 1):
            result *= i

    return result


def main() -> None:
    extra_info = [
        "Calculate the factorial for n", 
        "Q = quit",
    ]
    while True:
        user_input = ih.get_user_input("for which 'n': ", extra_info)
        # Quiting corner-case
        if user_input.casefold() == 'q':
            break

        if user_input.isdigit():
            print(f"Factorial of {user_input} is: {give_factorial(int(user_input))}")
            print()
        else:
            print("Unexpected input, please try again")
            print()


if __name__ == "__main__":
    main()
