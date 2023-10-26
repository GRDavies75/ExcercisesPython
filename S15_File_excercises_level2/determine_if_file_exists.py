"""
Excercise 15-92
Determine if a file exists
"""
from os import path


def main() -> None:
    input_data = [
        "famous_quotes.txt",
        "famous_books.txt",
    ]

    for entry in input_data:
        if path.isfile(entry):
            print(f"The file '{entry}' exists")
        else:
            print(f"The file '{entry}' does not exist")


if __name__ == "__main__":
    main()
