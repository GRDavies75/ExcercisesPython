"""
Excercise S02-07
Remove nth character from a string
Print intact string if n > len(s) or empty string
"""


def main() -> None:
    input_data = [
        ("Hello", 1),
        ("World", 3),
        ("Dog", 15),
        ("", 2),
    ]

    for string, index in input_data:
        if not string or index >= len(string):
            print(f"Input: '{string}' - Output: '{string}'")
        else:
            output = string[:index] + string[index+1:]
            print(f"Input: '{string}' - Output: '{output}'")


if __name__ == "__main__":
    main()
