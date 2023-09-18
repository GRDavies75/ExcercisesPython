"""
Excercise S03-09
Given a string, print a version where
the commas are replaced by dots
"""


def main() -> None:
    input_data = [
        "Hello, World!",
        "3,456,344",
    ]

    for entry in input_data:
        output = entry.replace(",", ".")
        print(f"Input: '{entry}' - Output: '{output}'")


if __name__ == "__main__":
    main()
