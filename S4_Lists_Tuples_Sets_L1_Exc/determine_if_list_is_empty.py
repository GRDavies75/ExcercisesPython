"""
Excercise 4-20
Determine if a list is empty
Print Empty or Not Empty respectively
"""


def main() -> None:
    input_data = [
        [],
        [4],
        [4, 5, 6, 7],
    ]

    for entry in input_data:
        if entry:
            print("Not Empty")
        else:
            print("Empty")


if __name__ == "__main__":
    main()
