"""
Excercise 10-61
Print a multiplication table
"""


def main() -> None:
    input_data = [
        3,
        7
    ]

    for entry in input_data:
        print(f"The multiplication table of {entry}:")
        print("-------------------------------------")
        for multiplier in range(1, 11):
            print(f"{multiplier:2} x {entry:3} = {(multiplier * entry):4}")
        print()


if __name__ == "__main__":
    main()
