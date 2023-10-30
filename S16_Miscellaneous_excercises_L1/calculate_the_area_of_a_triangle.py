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
import libs.input_library as il


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

        user_input = il.get_user_input("Base: ", extra_info)
        if user_input.casefold() == 'q':
            break
        base = il.sanetize_input_to_numerical_value(user_input)
        if not base or base <= 0:
            base = None

        user_input = il.get_user_input("Height: ")
        if user_input.casefold() == 'q':
            break
        height = il.sanetize_input_to_numerical_value(user_input)
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
