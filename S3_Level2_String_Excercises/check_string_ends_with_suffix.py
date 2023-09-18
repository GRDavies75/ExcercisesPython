"""
Excercise 3-13
Check if a given string ends with a certain suffix
Case-sensitive
False when len(suffix) > len(string)
"""


def main() -> None:
    input_data = [
        ("Hello", "ello"),
        ("Coding", "eng"),
        ("Nora", "rowing"),
    ]

    for s, suffix in input_data:
        output = s.endswith(suffix)

        print(f"Input: '{s}'/'{suffix}' - Output: {output}")


if __name__ == "__main__":
    main()
