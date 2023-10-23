"""
Excercise 13-81
Print a pattern recursively
"""
import sys
sys.path.append("..")
import libs.input_prompter as ip


def produce_pattern(string: str) -> str:
    """
    ... recursively
    """
    if len(string) <= 1:
        return string + "\n"
    else:
        return string + "\n" + produce_pattern(string[:-1])


def main() -> None:
    extra_information = [
        "Print * n times",
        "[Q = quit]",
    ]
    while True:
        length_pattern = ip.get_user_input("For what N: ", extra_information)
        if length_pattern.casefold() == 'q':
            return # breaking out of main
        elif length_pattern.isdigit():
            line_pattern = "*" * int(length_pattern)
            print(produce_pattern(line_pattern), end='')
        else:
            print("Unexpected input")
        
        # For readability
        print()


if __name__ == "__main__":
    main()
