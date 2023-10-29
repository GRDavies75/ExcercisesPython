"""
Excercise 16-95
Calculate the area of a cirkel if the diameter is given
Rounddown to 2 decimal places (or don't and stringformat it to 2 decimal places)
Note: Radius is halve the diameter and area calculation is:
Pi * R^2
"""
from math import pi


def main() -> None:
    input_data = [
        0,
        10,
        14,
    ]

    for entry in input_data:
        area = pi * (entry / 2) ** 2
        print(f"The area of a circle with diameter {entry} is {area:.2f}") 


if __name__ == "__main__":
    main()
