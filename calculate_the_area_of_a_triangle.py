"""
Excercise 16-96
Calculate the area of a triangle
if the base & height are given
Round down to 2 decimal places (or not and use stringformatting)
The user should input the values (for base and for height)
If either one of them is not a number/float give appropiate feedback
original excercise only used integer values as input
You can provide a float too in my/this version
"""
import sys
sys.path.append("..")
import libs.input_prompter as ip


def sanetize_input_to_numerical_value(input: str) -> int|float|None:
    """
    apparently input is interpreted char by char

    and a . isnt a float so float(input) doesn't work

    return None if input not been able to convert to int or float
    """
    if input.count(".") >= 2:
        return None
    # (Potential) float
    elif input.count(".") == 1:
        parts = input.split(".")
        whole = parts[0]
        fraction = parts[1]

        if whole.isdigit() and fraction.isdigit():
            return int(whole) + float(int(fraction) / 10 ** len(fraction))
        
        return None

    # (Potential) integer 
    if input.isdigit():
        return int(input)
    
    # apparently not a numerical value
    return None


def main() -> None:
    extra_info = [
        "Provide a base and a height",
        "for calculating the area of a triangle",
        "[Q = quit, B > 0.0, H > 0.0]",
    ]
    height = None
    base = None

    while True:
        # For readability
        print()

        user_input = ip.get_user_input("Base: ", extra_info)
        if user_input.casefold() == 'q':
            break
        base = sanetize_input_to_numerical_value(user_input)
        if not base or base <= 0:
            base = None

        user_input = ip.get_user_input("Height: ")
        if user_input.casefold() == 'q':
            break
        height = sanetize_input_to_numerical_value(user_input)
        if not height or height <= 0:
            height = None

        # cornercase
        if (not base or not height):
            print("Incorrect input")
            continue

        area = (base * height) / 2
        print(f"The area of a triangle given base {base} and height {height} is {area:.2f}")


if __name__ == "__main__":
    main()
