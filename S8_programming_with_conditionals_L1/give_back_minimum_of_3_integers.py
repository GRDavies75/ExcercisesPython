"""
Excercise 8-49 
Give back the minimum of 3 integers

This is almost the same as the last one (max of 3)
When working with conditionals, maybe the min or max 
should have been a conditional argument?
"""


def main() -> None:
    input_data = [
        (1, 2, 3),
        (7, 2, 15),
        (3, 3, 3),
    ]

    for entry in input_data:
        print(f"{min(entry)}")


if __name__ == "__main__":
    main()
