"""
Excercise S03-11
Given a string, print a copy without the spaces
"""


def main() -> None:
    input_data = [
        "Hello, World!",
        "Have a great day",
        "Python",
    ]

    for entry in input_data:
        print(entry.replace(" ", ""))


if __name__ == "__main__":
    main()
