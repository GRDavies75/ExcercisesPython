"""
Excercise S02-05
Remove chars at even indices
"""


def main() -> None:
    input_data = [
        "Coding",
        "Pizza",
        "Python",
        "A",
        "",
    ]

    for entry in input_data:
        output = "".join(entry[1::2])
        print(f"Input: {entry} - Output: {output}")


if __name__ == "__main__":
    main()
