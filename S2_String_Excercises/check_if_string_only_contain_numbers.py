"""
Excercise S02-06
Check if a given string contains only numbers
"""


def main() -> None:
    input_data = [
        "Hello",
        "4567",
        "Hello59",
        "",
    ]

    for entry in input_data:
        outcome = entry.isdigit()
        print(f"Input: '{entry}' - Output: {outcome}")


if __name__ == "__main__":
    main()
