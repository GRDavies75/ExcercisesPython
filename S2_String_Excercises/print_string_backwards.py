"""
Excercise S2-3
Print a string backwards
Print it normal when empty
"""


def main() -> None:
    input_data = [
        "Hello",
        "Wo",
        "",
    ]

    for entry in input_data:
        if entry:
            print(entry[::-1])
        else:
            print(entry)


if __name__ == "__main__":
    main()
